#!/usr/bin/env python3
"""
Generate SHA-256 hash of RFC 8785 canonical JSON (paper Rule A.10).

Usage:
    python hash.py <input.json>

Output format: sha256:<64 hex characters>
"""

import hashlib
import json
import sys

try:
    import jcs
except ImportError:
    print(
        "Error: 'jcs' package required for RFC 8785 canonicalization.\n"
        "Install with: pip install jcs",
        file=sys.stderr,
    )
    sys.exit(1)


def hash_json(obj) -> str:
    canonical = jcs.canonicalize(obj)
    digest = hashlib.sha256(canonical).hexdigest()
    return f"sha256:{digest}"


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python hash.py <input.json>", file=sys.stderr)
        return 1

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        obj = json.load(f)

    print(hash_json(obj))
    return 0


if __name__ == "__main__":
    sys.exit(main())
