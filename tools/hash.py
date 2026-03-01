#!/usr/bin/env python3
"""
Generate SHA-256 hash of canonical JSON.

Usage:
    python hash.py <input.json>

Output format: sha256:<64 hex characters>
"""

import json
import hashlib
import sys


def canonicalize(obj):
    """Canonicalize JSON for deterministic hashing."""
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=False)


def hash_json(obj):
    """Generate SHA-256 hash of canonical JSON."""
    canonical = canonicalize(obj)
    digest = hashlib.sha256(canonical.encode('utf-8')).hexdigest()
    return f"sha256:{digest}"


def main():
    if len(sys.argv) < 2:
        print("Usage: python hash.py <input.json>", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, 'r', encoding='utf-8') as f:
        obj = json.load(f)

    print(hash_json(obj))


if __name__ == '__main__':
    main()
