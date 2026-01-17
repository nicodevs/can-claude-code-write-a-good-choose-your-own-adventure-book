#!/usr/bin/env python3
"""Generate Mermaid structure diagram for a CYOA book.

Usage: python3 generate-structure.py <input-dir> <output-dir>

Reads:
  - <input-dir>/outline.json (for ending types)
  - <output-dir>/mapping.tsv (for page structure)

Writes:
  - <output-dir>/structure.mmd
"""

import sys
import json
from pathlib import Path
from collections import defaultdict

ENDING_EMOJIS = {
    "DEATH": "💀",
    "GOOD": "🏆",
    "NEUTRAL": "😐",
    "BAD": "😰",
}


def parse_outline_endings(outline_path):
    """Extract ending types from outline.json: {node_id: ending_type}."""
    if not outline_path.exists():
        return {}

    with open(outline_path, 'r') as f:
        outline = json.load(f)

    endings = {}

    def traverse(node):
        node_id = node.get("id", "")
        if "end" in node:
            endings[node_id] = node["end"]
        if "choices" in node:
            for child in node["choices"].values():
                traverse(child)

    traverse(outline)
    return endings


def load_mapping(mapping_path):
    """Load mapping.tsv: {node_id: page_number}."""
    mapping = {}
    with open(mapping_path, 'r') as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) == 2:
                node_id = parts[0].replace('.md', '')
                page_num = parts[1].replace('.md', '')
                mapping[node_id] = page_num
    return mapping


def build_edges(mapping):
    """Build edges from node ID structure."""
    edges = []
    node_ids = set(mapping.keys())

    # Group by base (without letter suffix)
    base_to_parts = defaultdict(list)
    for node_id in node_ids:
        parts = node_id.split('-')
        last_part = parts[-1]
        if last_part in ('A', 'B', 'C', 'D', 'E'):
            base = '-'.join(parts[:-1])
            base_to_parts[base].append((last_part, node_id))
        else:
            base_to_parts[node_id].append(('', node_id))

    def letter_order(x):
        return 0 if x[0] == '' else ord(x[0])

    # Edges within nodes (base -> A -> B -> C)
    for parts in base_to_parts.values():
        parts.sort(key=letter_order)
        for i in range(len(parts) - 1):
            edges.append((mapping[parts[i][1]], mapping[parts[i + 1][1]]))

    # Edges between parent and children
    for base, parts in base_to_parts.items():
        parts.sort(key=letter_order)
        last_page = mapping[parts[-1][1]]

        prefix = base + "-"
        for other_base in base_to_parts.keys():
            if other_base.startswith(prefix):
                suffix = other_base[len(prefix):]
                if '-' not in suffix and suffix.isdigit():
                    child_parts = base_to_parts[other_base]
                    child_parts.sort(key=letter_order)
                    first_page = mapping[child_parts[0][1]]
                    edges.append((last_page, first_page))

    return edges


def find_reachable(start, edges):
    """BFS to find all reachable pages from start."""
    edge_map = defaultdict(list)
    for src, dst in edges:
        edge_map[src].append(dst)

    reachable = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node in reachable:
            continue
        reachable.add(node)
        queue.extend(n for n in edge_map[node] if n not in reachable)
    return reachable


def generate_mermaid(book_name, pages, edges, endings, ending_types, transitions):
    """Generate Mermaid flowchart."""
    reachable = find_reachable('1', edges)
    orphaned = pages - reachable

    incoming = defaultdict(set)
    for src, dst in edges:
        incoming[dst].add(src)
    convergent = {p for p, srcs in incoming.items() if len(srcs) >= 3}

    lines = [
        "---",
        f"title: {book_name}",
        "---",
        "flowchart TD"
    ]

    for page in sorted(pages, key=int):
        if page in orphaned:
            lines.append(f"    {page}[{page} - ORPHAN]:::orphan")
        elif page in convergent and page in endings:
            etype = ending_types.get(page, "")
            emoji = ENDING_EMOJIS.get(etype, "")
            label = f"END {emoji}" if emoji else "END"
            lines.append(f"    {page}[{page} - {label} x{len(incoming[page])}]:::convergent_end")
        elif page in convergent:
            lines.append(f"    {page}[{page} x{len(incoming[page])}]:::convergent")
        elif page in endings:
            etype = ending_types.get(page, "")
            emoji = ENDING_EMOJIS.get(etype, "")
            label = f"END {emoji}" if emoji else "END"
            cls = {"DEATH": "death", "GOOD": "good", "BAD": "bad", "NEUTRAL": "neutral"}.get(etype, "ending")
            lines.append(f"    {page}[{page} - {label}]:::{cls}")
        elif page in transitions:
            lines.append(f"    {page}[{page}]:::transition")
        else:
            lines.append(f"    {page}(({page}))")

    for src, dst in sorted(edges, key=lambda x: (int(x[0]), int(x[1]))):
        lines.append(f"    {src} --> {dst}")

    lines.append("")
    lines.append("    classDef ending fill:#ff6b6b,stroke:#c92a2a,color:#fff")
    lines.append("    classDef death fill:#495057,stroke:#212529,color:#fff")
    lines.append("    classDef good fill:#51cf66,stroke:#2f9e44,color:#fff")
    lines.append("    classDef bad fill:#ff8787,stroke:#fa5252,color:#fff")
    lines.append("    classDef neutral fill:#74c0fc,stroke:#339af0,color:#fff")
    lines.append("    classDef orphan fill:#ffd43b,stroke:#fab005,color:#000")
    lines.append("    classDef convergent fill:#9775fa,stroke:#7048e8,color:#fff")
    lines.append("    classDef convergent_end fill:#e599f7,stroke:#be4bdb,color:#000")
    lines.append("    classDef transition fill:#dee2e6,stroke:#adb5bd,color:#000")
    lines.append("")
    lines.append(f"    %% {len(pages)} pages, {len(edges)} edges, {len(endings)} endings, {len(orphaned)} orphaned, {len(convergent)} convergent")

    return '\n'.join(lines)


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input-dir> <output-dir>")
        sys.exit(1)

    input_dir = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])

    outline_path = input_dir / "outline.json"
    mapping_path = output_dir / "mapping.tsv"

    if not mapping_path.exists():
        print(f"Error: {mapping_path} not found")
        sys.exit(1)

    # Load data
    mapping = load_mapping(mapping_path)
    outline_endings = parse_outline_endings(outline_path)

    # Build structure
    pages = set(mapping.values())
    edges = build_edges(mapping)

    # Find endings (pages with no outgoing edges)
    sources = {src for src, _ in edges}
    endings = pages - sources

    # Map node IDs to page numbers for ending types
    ending_types = {}
    for node_id, etype in outline_endings.items():
        if node_id in mapping:
            ending_types[mapping[node_id]] = etype

    # Find transition pages (letter suffix nodes)
    transitions = {mapping[nid] for nid in mapping if nid.split('-')[-1] in ('A', 'B', 'C', 'D', 'E')}

    # Generate and write
    book_name = output_dir.parent.name
    mermaid = generate_mermaid(book_name, pages, edges, endings, ending_types, transitions)

    output_path = output_dir / "structure.mmd"
    with open(output_path, 'w') as f:
        f.write(mermaid)

    print(f"Generated {output_path}: {len(pages)} pages, {len(edges)} edges, {len(endings)} endings")


if __name__ == "__main__":
    main()
