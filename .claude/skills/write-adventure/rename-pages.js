#!/usr/bin/env node
/**
 * Rename CYOA page files from ID-based names (1-2-1.md) to sequential page numbers (23.md)
 * and update all internal links to match.
 *
 * Usage:
 *   node rename-pages.js <output-dir> <mapping-file>
 *
 * Arguments:
 *   output-dir: Directory containing the .md page files
 *   mapping-file: TSV file with old_filename<tab>new_filename per line
 *
 * Example mapping.tsv:
 *   1.md	1.md
 *   1-1.md	17.md
 *   1-2-A.md	8.md
 */

import { readFile, writeFile, rename, readdir, stat } from 'node:fs/promises';
import { join, resolve } from 'node:path';

const loadMapping = async (mappingFile) => {
  const content = await readFile(mappingFile, 'utf-8');
  const mapping = new Map();

  for (const line of content.split('\n')) {
    const trimmed = line.trim();
    if (!trimmed) continue;

    const [oldName, newName] = trimmed.split('\t');
    if (oldName && newName) {
      mapping.set(oldName, newName);
    }
  }

  return mapping;
};

const renameFiles = async (outputDir, mapping) => {
  // Pass 1: Rename to temporary names
  for (const oldName of mapping.keys()) {
    const oldPath = join(outputDir, oldName);
    const tmpPath = join(outputDir, `${oldName}.tmp`);

    try {
      await rename(oldPath, tmpPath);
    } catch {
      // File might not exist, skip
    }
  }

  // Pass 2: Rename from temporary to final names
  for (const [oldName, newName] of mapping) {
    const tmpPath = join(outputDir, `${oldName}.tmp`);
    const newPath = join(outputDir, newName);

    try {
      await rename(tmpPath, newPath);
    } catch {
      // Temp file might not exist, skip
    }
  }
};

const updateLinks = async (outputDir, mapping) => {
  // Pattern matches [page ANYTHING](./FILENAME.md)
  const linkPattern = /\[page [^\]]+\]\(\.\/([^)]+\.md)\)/g;

  const replaceLink = (match, oldFilename) => {
    if (mapping.has(oldFilename)) {
      const newFilename = mapping.get(oldFilename);
      const newPage = newFilename.replace('.md', '');
      return `[page ${newPage}](./${newFilename})`;
    }
    return match;
  };

  const files = await readdir(outputDir);
  const mdFiles = files.filter((f) => f.endsWith('.md'));

  await Promise.all(
    mdFiles.map(async (file) => {
      const filePath = join(outputDir, file);
      const content = await readFile(filePath, 'utf-8');
      const newContent = content.replaceAll(linkPattern, replaceLink);

      if (newContent !== content) {
        await writeFile(filePath, newContent);
      }
    })
  );
};

const main = async () => {
  const [, , outputDirArg, mappingFileArg] = process.argv;

  if (!outputDirArg || !mappingFileArg) {
    console.error(`Usage: node rename-pages.js <output-dir> <mapping-file>`);
    process.exit(1);
  }

  const outputDir = resolve(outputDirArg);
  const mappingFile = resolve(mappingFileArg);

  try {
    const stats = await stat(outputDir);
    if (!stats.isDirectory()) {
      console.error(`Error: ${outputDir} is not a directory`);
      process.exit(1);
    }
  } catch {
    console.error(`Error: ${outputDir} does not exist`);
    process.exit(1);
  }

  try {
    await stat(mappingFile);
  } catch {
    console.error(`Error: ${mappingFile} does not exist`);
    process.exit(1);
  }

  const mapping = await loadMapping(mappingFile);
  console.log(`Loaded ${mapping.size} file mappings`);

  await renameFiles(outputDir, mapping);
  console.log('Files renamed');

  await updateLinks(outputDir, mapping);
  console.log('Links updated');

  console.log('Done!');
};

main();
