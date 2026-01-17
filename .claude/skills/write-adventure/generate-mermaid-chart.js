#!/usr/bin/env node
/**
 * Generate Mermaid structure diagram for a CYOA book.
 *
 * Usage: node generate-mermaid-chart.js <input-dir> <output-dir>
 *
 * Reads:
 *   - <input-dir>/outline.json (for ending types)
 *   - <output-dir>/mapping.tsv (for page structure)
 *
 * Writes:
 *   - <output-dir>/structure.mmd
 */

import { readFile, writeFile, stat } from 'node:fs/promises';
import { join, resolve, dirname, basename } from 'node:path';

const parseTitle = async (summaryPath) => {
  try {
    const content = await readFile(summaryPath, 'utf-8');
    const match = content.match(/^Title:\s*(.+)$/m);
    return match?.[1]?.trim() ?? null;
  } catch {
    return null;
  }
};

const ENDING_EMOJIS = {
  DEATH: '💀',
  GOOD: '🏆',
  NEUTRAL: '😐',
  BAD: '😰',
};

const parseOutlineEndings = async (outlinePath) => {
  try {
    const content = await readFile(outlinePath, 'utf-8');
    const outline = JSON.parse(content);
    const endings = new Map();

    const traverse = (node) => {
      const nodeId = node.id ?? '';
      if (node.end !== undefined) {
        endings.set(nodeId, node.end);
      }
      if (node.choices) {
        Object.values(node.choices).forEach(traverse);
      }
    };

    traverse(outline);
    return endings;
  } catch {
    return new Map();
  }
};

const loadMapping = async (mappingPath) => {
  const content = await readFile(mappingPath, 'utf-8');
  const mapping = new Map();

  for (const line of content.split('\n')) {
    const parts = line.trim().split('\t');
    if (parts.length === 2) {
      const nodeId = parts[0].replace('.md', '');
      const pageNum = parts[1].replace('.md', '');
      mapping.set(nodeId, pageNum);
    }
  }

  return mapping;
};

const buildEdges = (mapping) => {
  const edges = [];
  const nodeIds = new Set(mapping.keys());

  // Group by base (without letter suffix)
  const baseToParts = new Map();

  for (const nodeId of nodeIds) {
    const parts = nodeId.split('-');
    const lastPart = parts.at(-1);

    if (['A', 'B', 'C', 'D', 'E'].includes(lastPart)) {
      const base = parts.slice(0, -1).join('-');
      if (!baseToParts.has(base)) baseToParts.set(base, []);
      baseToParts.get(base).push([lastPart, nodeId]);
    } else {
      if (!baseToParts.has(nodeId)) baseToParts.set(nodeId, []);
      baseToParts.get(nodeId).push(['', nodeId]);
    }
  }

  const letterOrder = ([letter]) => (letter === '' ? 0 : letter.charCodeAt(0));

  // Edges within nodes (base -> A -> B -> C)
  for (const parts of baseToParts.values()) {
    parts.sort((a, b) => letterOrder(a) - letterOrder(b));
    for (let i = 0; i < parts.length - 1; i++) {
      edges.push([mapping.get(parts[i][1]), mapping.get(parts[i + 1][1])]);
    }
  }

  // Edges between parent and children
  for (const [base, parts] of baseToParts) {
    parts.sort((a, b) => letterOrder(a) - letterOrder(b));
    const lastPage = mapping.get(parts.at(-1)[1]);

    const prefix = `${base}-`;
    for (const otherBase of baseToParts.keys()) {
      if (otherBase.startsWith(prefix)) {
        const suffix = otherBase.slice(prefix.length);
        if (!suffix.includes('-') && /^\d+$/.test(suffix)) {
          const childParts = baseToParts.get(otherBase);
          childParts.sort((a, b) => letterOrder(a) - letterOrder(b));
          const firstPage = mapping.get(childParts[0][1]);
          edges.push([lastPage, firstPage]);
        }
      }
    }
  }

  return edges;
};

const findReachable = (start, edges) => {
  const edgeMap = new Map();
  for (const [src, dst] of edges) {
    if (!edgeMap.has(src)) edgeMap.set(src, []);
    edgeMap.get(src).push(dst);
  }

  const reachable = new Set();
  const queue = [start];

  while (queue.length > 0) {
    const node = queue.shift();
    if (reachable.has(node)) continue;
    reachable.add(node);
    for (const next of edgeMap.get(node) ?? []) {
      if (!reachable.has(next)) queue.push(next);
    }
  }

  return reachable;
};

const generateMermaid = (bookName, pages, edges, endings, endingTypes, transitions) => {
  const reachable = findReachable('1', edges);
  const orphaned = new Set([...pages].filter((p) => !reachable.has(p)));

  const incoming = new Map();
  for (const [src, dst] of edges) {
    if (!incoming.has(dst)) incoming.set(dst, new Set());
    incoming.get(dst).add(src);
  }
  const convergent = new Set(
    [...incoming.entries()].filter(([, srcs]) => srcs.size >= 3).map(([p]) => p)
  );

  const lines = ['---', `title: ${bookName}`, '---', 'flowchart TD'];

  const sortedPages = [...pages].sort((a, b) => Number(a) - Number(b));

  for (const page of sortedPages) {
    if (orphaned.has(page)) {
      lines.push(`    ${page}[${page} - ORPHAN]:::orphan`);
    } else if (convergent.has(page) && endings.has(page)) {
      const etype = endingTypes.get(page) ?? '';
      const emoji = ENDING_EMOJIS[etype] ?? '';
      const label = emoji ? `END ${emoji}` : 'END';
      lines.push(`    ${page}[${page} - ${label} x${incoming.get(page).size}]:::convergent_end`);
    } else if (convergent.has(page)) {
      lines.push(`    ${page}[${page} x${incoming.get(page).size}]:::convergent`);
    } else if (endings.has(page)) {
      const etype = endingTypes.get(page) ?? '';
      const emoji = ENDING_EMOJIS[etype] ?? '';
      const label = emoji ? `END ${emoji}` : 'END';
      const cls = { DEATH: 'death', GOOD: 'good', BAD: 'bad', NEUTRAL: 'neutral' }[etype] ?? 'ending';
      lines.push(`    ${page}[${page} - ${label}]:::${cls}`);
    } else if (transitions.has(page)) {
      lines.push(`    ${page}[${page}]:::transition`);
    } else {
      lines.push(`    ${page}((${page}))`);
    }
  }

  const sortedEdges = [...edges].sort((a, b) => Number(a[0]) - Number(b[0]) || Number(a[1]) - Number(b[1]));
  for (const [src, dst] of sortedEdges) {
    lines.push(`    ${src} --> ${dst}`);
  }

  lines.push('');
  lines.push('    classDef ending fill:#ff6b6b,stroke:#c92a2a,color:#fff');
  lines.push('    classDef death fill:#495057,stroke:#212529,color:#fff');
  lines.push('    classDef good fill:#51cf66,stroke:#2f9e44,color:#fff');
  lines.push('    classDef bad fill:#ff0000,stroke:#cc0000,color:#fff');
  lines.push('    classDef neutral fill:#74c0fc,stroke:#339af0,color:#fff');
  lines.push('    classDef orphan fill:#ffd43b,stroke:#fab005,color:#000');
  lines.push('    classDef convergent fill:#9775fa,stroke:#7048e8,color:#fff');
  lines.push('    classDef convergent_end fill:#e599f7,stroke:#be4bdb,color:#000');
  lines.push('    classDef transition fill:#dee2e6,stroke:#adb5bd,color:#000');
  lines.push('');
  lines.push(`    %% ${pages.size} pages, ${edges.length} edges, ${endings.size} endings, ${orphaned.size} orphaned, ${convergent.size} convergent`);

  return lines.join('\n');
};

const main = async () => {
  const [, , inputDirArg, outputDirArg] = process.argv;

  if (!inputDirArg || !outputDirArg) {
    console.log(`Usage: node generate-mermaid-chart.js <input-dir> <output-dir>`);
    process.exit(1);
  }

  const inputDir = resolve(inputDirArg);
  const outputDir = resolve(outputDirArg);

  const outlinePath = join(inputDir, 'outline.json');
  const summaryPath = join(inputDir, 'summary.yaml');
  const mappingPath = join(outputDir, 'mapping.tsv');

  try {
    await stat(mappingPath);
  } catch {
    console.error(`Error: ${mappingPath} not found`);
    process.exit(1);
  }

  // Load data
  const mapping = await loadMapping(mappingPath);
  const outlineEndings = await parseOutlineEndings(outlinePath);

  // Build structure
  const pages = new Set(mapping.values());
  const edges = buildEdges(mapping);

  // Find endings (pages with no outgoing edges)
  const sources = new Set(edges.map(([src]) => src));
  const endings = new Set([...pages].filter((p) => !sources.has(p)));

  // Map node IDs to page numbers for ending types
  // The ending type in the outline is on the base node (e.g., 1-2)
  // but the actual ending page might be a letter-suffix (e.g., 1-2-B)
  // Always find the LAST page in the chain (highest letter suffix, or base if none)
  const endingTypes = new Map();
  for (const [nodeId, etype] of outlineEndings) {
    // Look for letter-suffix versions first (highest to lowest)
    const suffixes = ['E', 'D', 'C', 'B', 'A'];
    let found = false;
    for (const suffix of suffixes) {
      const suffixedId = `${nodeId}-${suffix}`;
      if (mapping.has(suffixedId)) {
        endingTypes.set(mapping.get(suffixedId), etype);
        found = true;
        break;
      }
    }
    // Fall back to base node if no suffixes
    if (!found && mapping.has(nodeId)) {
      endingTypes.set(mapping.get(nodeId), etype);
    }
  }

  // Find transition pages (letter suffix nodes)
  const transitions = new Set(
    [...mapping.entries()]
      .filter(([nodeId]) => ['A', 'B', 'C', 'D', 'E'].includes(nodeId.split('-').at(-1)))
      .map(([, pageNum]) => pageNum)
  );

  // Generate and write
  const bookName = await parseTitle(summaryPath) ?? basename(dirname(outputDir));
  const mermaid = generateMermaid(bookName, pages, edges, endings, endingTypes, transitions);

  const outputPath = join(outputDir, 'structure.mmd');
  await writeFile(outputPath, mermaid + '\n');

  console.log(`Generated ${outputPath}: ${pages.size} pages, ${edges.length} edges, ${endings.size} endings`);
};

main();
