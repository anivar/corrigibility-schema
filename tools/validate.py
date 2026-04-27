#!/usr/bin/env python3
"""
Validate JSON document against the Corrigibility Schema (Protocol 3.x).

Loads all four schemas (DPI/EPI × infrastructure/audit) into a Registry
keyed by their `$id` URNs so cross-schema `$ref`s resolve.

Usage:
    python validate.py <document.json> [--schema <schema.json>]
"""

import argparse
import json
import sys
from pathlib import Path

try:
    import jsonschema
    from jsonschema import Draft202012Validator
    from referencing import Registry, Resource
    from referencing.jsonschema import DRAFT202012
except ImportError:
    print(
        "Error: jsonschema >=4.18 + referencing required.\n"
        "Install with: pip install 'jsonschema[format]>=4.18'",
        file=sys.stderr,
    )
    sys.exit(1)


SCHEMA_DIR = Path(__file__).parent.parent / "schema"


def load_registry() -> Registry:
    resources = []
    for sub in ("dpi", "epi"):
        for kind in ("infrastructure", "audit"):
            path = SCHEMA_DIR / sub / f"{kind}.json"
            with open(path, "r", encoding="utf-8") as f:
                schema = json.load(f)
            resources.append((schema["$id"], Resource(contents=schema, specification=DRAFT202012)))
    return Registry().with_resources(resources)


def detect_schema_id(doc: dict) -> str:
    is_audit = "auditor" in doc or "audit_id" in doc
    is_epi = "lwd_r" in doc or "lwd_r_verification" in doc or "tier" in doc and isinstance(doc.get("tier"), str)
    family = "epi" if is_epi else "dpi"
    kind = "audit" if is_audit else "infrastructure"
    return f"urn:corrigibility:{family}/{kind}.json"


def validate_document(doc_path: Path, schema_path: Path | None) -> bool:
    with open(doc_path, "r", encoding="utf-8") as f:
        doc = json.load(f)

    registry = load_registry()

    if schema_path is not None:
        with open(schema_path, "r", encoding="utf-8") as f:
            schema = json.load(f)
        schema_id = schema["$id"]
    else:
        schema_id = detect_schema_id(doc)
        schema = registry.contents(schema_id)
        print(f"Auto-detected schema: {schema_id}")

    validator = Draft202012Validator(schema, registry=registry)
    errors = sorted(validator.iter_errors(doc), key=lambda e: list(e.absolute_path))
    if not errors:
        print(f"OK Valid: {doc_path}")
        return True

    print(f"FAIL Invalid: {doc_path}")
    for e in errors:
        path = " -> ".join(str(p) for p in e.absolute_path) or "(root)"
        print(f"  [{path}] {e.message}")
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate against Corrigibility Schema 3.x")
    parser.add_argument("document", help="JSON document to validate")
    parser.add_argument("--schema", "-s", help="Schema file (auto-detected if not specified)")
    args = parser.parse_args()

    schema_path = Path(args.schema) if args.schema else None
    success = validate_document(Path(args.document), schema_path)
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
