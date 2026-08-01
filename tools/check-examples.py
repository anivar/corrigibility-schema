#!/usr/bin/env python3
"""
Validate every shipped example against its schema, and the four schemas
against JSON Schema 2020-12 itself. CI entry point; validate.py remains the
single-document tool.
"""

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012

ROOT = Path(__file__).resolve().parent.parent
COMMON = "schema/common.json"
PAIRS = [
    ("examples/dpi/infrastructure.example.json", "schema/dpi/infrastructure.json"),
    ("examples/dpi/audit.example.json", "schema/dpi/audit.json"),
    ("examples/epi/infrastructure.example.json", "schema/epi/infrastructure.json"),
    ("examples/epi/audit.example.json", "schema/epi/audit.json"),
]


def main() -> int:
    schemas = {}
    for sc in [COMMON] + [sc for _, sc in PAIRS]:
        s = json.loads((ROOT / sc).read_text())
        Draft202012Validator.check_schema(s)
        schemas[sc] = s
    registry = Registry().with_resources(
        [(s.get("$id", sc), Resource(contents=s, specification=DRAFT202012)) for sc, s in schemas.items()]
    )
    failures = 0
    for ex, sc in PAIRS:
        validator = Draft202012Validator(schemas[sc], registry=registry)
        errors = list(validator.iter_errors(json.loads((ROOT / ex).read_text())))
        if errors:
            failures += len(errors)
            print(f"✗ {ex}: {len(errors)} error(s); first: {errors[0].message[:140]}")
        else:
            print(f"✓ {ex}")
    print("schemas: all valid 2020-12")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
