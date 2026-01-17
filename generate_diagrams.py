#!/usr/bin/env python3
"""Parse CYOA books and generate Mermaid diagrams for branching structure."""

import re
import os
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path("/Users/dev/Sites/can-claude-code-write-a-good-choose-your-own-adventure-book")


def parse_single_file_book(filepath):
    """Parse a book that's a single file with sections (number-1 format)."""
    with open(filepath, 'r') as f:
        content = f.read()

    # Find all sections
    section_pattern = r'### Section (\d+)'
    sections = re.findall(section_pattern, content)

    # Find all links: → Go to Section N
    edges = []
    current_section = None
    for line in content.split('\n'):
        section_match = re.search(r'### Section (\d+)', line)
        if section_match:
            current_section = section_match.group(1)

        link_match = re.search(r'→ Go to Section (\d+)', line)
        if link_match and current_section:
            target = link_match.group(1)
            edges.append((current_section, target))

    return set(sections), edges


def parse_multi_file_book(output_dir):
    """Parse a book with multiple .md files (number-2,3,4,5 format)."""
    pages = set()
    edges = []

    for md_file in output_dir.glob('*.md'):
        page_num = md_file.stem
        if not page_num.isdigit():
            continue
        pages.add(page_num)

        with open(md_file, 'r') as f:
            content = f.read()

        # Find links: [page N](./N.md) or [page N](N.md)
        link_pattern = r'\[page (\d+)\]\(\./?\d+\.md\)'
        targets = re.findall(link_pattern, content)
        for target in targets:
            edges.append((page_num, target))

    return pages, edges


def find_endings(pages, edges):
    """Find pages that have no outgoing edges (endings)."""
    sources = set(src for src, _ in edges)
    return pages - sources


def find_reachable(start, edges):
    """Find all pages reachable from start using BFS."""
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
        for neighbor in edge_map[node]:
            if neighbor not in reachable:
                queue.append(neighbor)
    return reachable


def generate_mermaid(book_name, pages, edges, endings):
    """Generate Mermaid flowchart."""

    # Find orphaned pages (not reachable from page 1)
    reachable = find_reachable('1', edges)
    orphaned = pages - reachable

    # Count incoming edges per destination (for showing convergent nodes)
    incoming_count = defaultdict(int)
    incoming_sources = defaultdict(set)
    for src, dst in edges:
        incoming_count[dst] += 1
        incoming_sources[dst].add(src)

    # Pages with 3+ incoming edges from different sources are "convergent"
    convergent = {page for page, sources in incoming_sources.items() if len(sources) >= 3}

    lines = [
        f"---",
        f"title: {book_name}",
        f"---",
        f"flowchart TD"
    ]

    # Define all nodes with appropriate styling
    for page in sorted(pages, key=lambda x: int(x)):
        if page in orphaned:
            lines.append(f"    {page}[{page} - ORPHAN]:::orphan")
        elif page in convergent and page in endings:
            lines.append(f"    {page}[{page} - END x{len(incoming_sources[page])}]:::convergent_end")
        elif page in convergent:
            lines.append(f"    {page}[{page} x{len(incoming_sources[page])}]:::convergent")
        elif page in endings:
            lines.append(f"    {page}[{page} - END]:::ending")
        else:
            # Regular node - just the number
            lines.append(f"    {page}(({page}))")

    # Add edges (keep ALL edges including duplicates to show the problem)
    for src, dst in sorted(edges, key=lambda x: (int(x[0]), int(x[1]))):
        lines.append(f"    {src} --> {dst}")

    # Add styling
    lines.append("")
    lines.append("    classDef ending fill:#ff6b6b,stroke:#c92a2a,color:#fff")
    lines.append("    classDef orphan fill:#ffd43b,stroke:#fab005,color:#000")
    lines.append("    classDef convergent fill:#9775fa,stroke:#7048e8,color:#fff")
    lines.append("    classDef convergent_end fill:#e599f7,stroke:#be4bdb,color:#000")

    # Add summary as comment
    lines.append("")
    lines.append(f"    %% {len(pages)} pages, {len(edges)} edges, {len(endings)} endings, {len(orphaned)} orphaned, {len(convergent)} convergent")

    return '\n'.join(lines)


def main():
    results = {}

    # Parse number-1 (single file)
    book1_path = BASE_DIR / "number-1" / "output" / "allegedly-fixed.md"
    if book1_path.exists():
        pages, edges = parse_single_file_book(book1_path)
        endings = find_endings(pages, edges)
        results['number-1'] = (pages, edges, endings)
        print(f"Number 1: {len(pages)} pages, {len(edges)} edges, {len(endings)} endings")

    # Parse number-2,3,4,5 (multi-file)
    for num in [2, 3, 4, 5]:
        output_dir = BASE_DIR / f"number-{num}" / "output"
        if output_dir.exists():
            pages, edges = parse_multi_file_book(output_dir)
            endings = find_endings(pages, edges)
            results[f'number-{num}'] = (pages, edges, endings)
            print(f"Number {num}: {len(pages)} pages, {len(edges)} edges, {len(endings)} endings")

    # Generate Mermaid files
    for book_name, (pages, edges, endings) in results.items():
        mermaid = generate_mermaid(book_name, pages, edges, endings)
        output_path = BASE_DIR / f"{book_name}" / "output" / "structure.mmd"
        with open(output_path, 'w') as f:
            f.write(mermaid)
        print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
