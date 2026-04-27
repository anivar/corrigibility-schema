#!/usr/bin/env python3
"""
Canonicalize JSON for hashing per RFC 8785 (JSON Canonicalization Scheme).

Paper Rule A.10 mandates RFC 8785 for auditor manifests. RFC 8785 differs
from naive `json.dumps(..., sort_keys=True, separators=(',', ':'))` in:

    - Numbers: ECMAScript Number-to-String semantics. `1.0` → `"1"`,
      `1e21` → `"1e+21"`, `-0` → `"0"`, etc. Plain Python `json.dumps(1.0)`
      emits `"1.0"` and so produces hashes that disagree with every
      conformant RFC 8785 implementation.
    - Strings: explicit escape table for control characters; surrogate pair
      handling matches the JCS spec.
    - Encoding: UTF-8, no BOM, no trailing newline.

Usage:
    python canonicalize.py <input.json> [output.json]
"""

import json
import sys

try:
    import jcs  # noqa: F401  (pip install jcs)
except ImportError:
    print(
        "Error: 'jcs' package required for RFC 8785 canonicalization.\n"
        "Install with: pip install jcs",
        file=sys.stderr,
    )
    sys.exit(1)


def canonicalize(obj) -> bytes:
    """Return the RFC 8785 canonical JSON serialization (UTF-8 bytes)."""
    return jcs.canonicalize(obj)


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python canonicalize.py <input.json> [output.json]", file=sys.stderr)
        return 1

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    with open(input_file, "r", encoding="utf-8") as f:
        obj = json.load(f)

    canonical = canonicalize(obj)

    if output_file:
        with open(output_file, "wb") as f:
            f.write(canonical)
        print(f"Canonical JSON written to {output_file}")
    else:
        sys.stdout.buffer.write(canonical)
        sys.stdout.buffer.write(b"\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
