#!/usr/bin/env python3
"""
Rename CYOA page files from ID-based names (1-2-1.md) to sequential page numbers (23.md)
and update all internal links to match.

Usage:
    python rename-pages.py <output-dir> <mapping-file>

Arguments:
    output-dir: Directory containing the .md page files
    mapping-file: TSV file with old_filename<tab>new_filename per line

Example mapping.tsv:
    1.md	1.md
    1-1.md	17.md
    1-2-A.md	8.md
"""

import sys
import os
import re
from pathlib import Path


def load_mapping(mapping_file: str) -> dict[str, str]:
    """Load the old->new filename mapping from a TSV file."""
    mapping = {}
    with open(mapping_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split('\t')
            if len(parts) >= 2:
                old_name, new_name = parts[0], parts[1]
                mapping[old_name] = new_name
    return mapping


def rename_files(output_dir: Path, mapping: dict[str, str]) -> None:
    """Rename files using a two-pass approach to avoid conflicts."""
    # Pass 1: Rename to temporary names
    for old_name in mapping:
        old_path = output_dir / old_name
        if old_path.exists():
            tmp_path = output_dir / f"{old_name}.tmp"
            old_path.rename(tmp_path)

    # Pass 2: Rename from temporary to final names
    for old_name, new_name in mapping.items():
        tmp_path = output_dir / f"{old_name}.tmp"
        new_path = output_dir / new_name
        if tmp_path.exists():
            tmp_path.rename(new_path)


def update_links(output_dir: Path, mapping: dict[str, str]) -> None:
    """Update all [page X](./X.md) links in all markdown files."""
    # Build regex pattern to match all old filenames
    # Link format: [page 1-2-1](./1-2-1.md) -> [page 23](./23.md)

    def replace_link(match: re.Match) -> str:
        old_filename = match.group(1)
        if old_filename in mapping:
            new_filename = mapping[old_filename]
            old_page = old_filename.removesuffix('.md')
            new_page = new_filename.removesuffix('.md')
            return f"[page {new_page}](./{new_filename})"
        return match.group(0)  # No change if not in mapping

    # Pattern matches [page ANYTHING](./FILENAME.md)
    link_pattern = re.compile(r'\[page [^\]]+\]\(\./([^)]+\.md)\)')

    for md_file in output_dir.glob('*.md'):
        content = md_file.read_text()
        new_content = link_pattern.sub(replace_link, content)
        if new_content != content:
            md_file.write_text(new_content)


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <output-dir> <mapping-file>", file=sys.stderr)
        sys.exit(1)

    output_dir = Path(sys.argv[1])
    mapping_file = sys.argv[2]

    if not output_dir.is_dir():
        print(f"Error: {output_dir} is not a directory", file=sys.stderr)
        sys.exit(1)

    if not os.path.isfile(mapping_file):
        print(f"Error: {mapping_file} does not exist", file=sys.stderr)
        sys.exit(1)

    mapping = load_mapping(mapping_file)
    print(f"Loaded {len(mapping)} file mappings")

    rename_files(output_dir, mapping)
    print("Files renamed")

    update_links(output_dir, mapping)
    print("Links updated")

    print("Done!")


if __name__ == '__main__':
    main()
