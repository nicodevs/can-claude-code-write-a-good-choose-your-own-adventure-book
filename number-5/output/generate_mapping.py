#!/usr/bin/env python3
import os
import random

# List all .md files
output_dir = "/Users/dev/Sites/can-claude-code-write-a-good-choose-your-own-adventure-book/talk/output"
files = [f for f in os.listdir(output_dir) if f.endswith('.md') and f != 'mapping.tsv']
files.sort()

# Identify root and ending pages
root_file = None
if '1.md' in files:
    root_file = '1.md'
elif '1-A.md' in files:
    root_file = '1-A.md'

ending_files = [
    '1-1-1-1-1-1-1-1-1-1-1-1-1.md',
    '1-1-1-1-1-1-1-1-1-1-1-1-2.md',
    '1-1-1-1-1-1-1-1-1-1-1-2.md',
    '1-1-1-1-1-1-1-1-1-1-2.md',
    '1-1-1-1-1-1-1-1-1-2.md',
    '1-1-1-1-1-1-1-1-2.md',
    '1-1-1-1-1-1-1-2.md',
    '1-1-1-1-1-1-2-1.md',
    '1-1-1-1-1-1-2-2.md',
    '1-1-1-1-1-2.md',
    '1-1-1-1-2.md',
    '1-1-1-2-1.md',
    '1-1-1-2-2.md',
    '1-1-2-1-1.md',
    '1-1-2-1-2.md',
    '1-1-2-2.md',
    '1-2-B.md'
]

# All other files
other_files = [f for f in files if f != root_file and f not in ending_files]

# Create number pool
total_files = len(files)
numbers = list(range(1, total_files + 1))

# Assign page 1 to root
mapping = {}
mapping[root_file] = 1
numbers.remove(1)

# Reserve numbers 10+ for endings
ending_numbers = [n for n in numbers if n >= 10]
other_numbers = [n for n in numbers if n < 10]

# Shuffle
random.shuffle(ending_numbers)
random.shuffle(other_numbers)

# Assign to endings
for f in ending_files:
    if ending_numbers:
        mapping[f] = ending_numbers.pop(0)
    else:
        # Fallback if we run out
        mapping[f] = numbers.pop(0)

# Assign to other pages
all_remaining = other_numbers + ending_numbers
random.shuffle(all_remaining)
for f in other_files:
    mapping[f] = all_remaining.pop(0)

# Write mapping file
with open(os.path.join(output_dir, 'mapping.tsv'), 'w') as out:
    for old_file in sorted(mapping.keys()):
        new_file = f"{mapping[old_file]}.md"
        out.write(f"{old_file}\t{new_file}\n")

print(f"Generated mapping for {len(mapping)} files")
