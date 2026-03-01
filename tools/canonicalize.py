#!/usr/bin/env python3
"""
Canonicalize JSON for hashing.

Usage:
    python canonicalize.py <input.json> [output.json]

If output not specified, prints to stdout.
"""

import json
import sys


def canonicalize(obj):
    """
    Canonicalize JSON object for deterministic hashing.

    Rules:
    - Sort keys lexicographically (recursive)
    - No whitespace between elements
    - UTF-8 encoding
    - No trailing newline
    """
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=False)


def main():
    if len(sys.argv) < 2:
        print("Usage: python canonicalize.py <input.json> [output.json]", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    with open(input_file, 'r', encoding='utf-8') as f:
        obj = json.load(f)

    canonical = canonicalize(obj)

    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(canonical)
        print(f"Canonical JSON written to {output_file}")
    else:
        print(canonical)


if __name__ == '__main__':
    main()
