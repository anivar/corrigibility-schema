#!/usr/bin/env python3
"""
Validate JSON document against Corrigibility Schema.

Usage:
    python validate.py <document.json> [--schema <schema.json>]

If schema not specified, auto-detects based on document content.
"""

import json
import sys
import argparse
from pathlib import Path

try:
    import jsonschema
    from jsonschema import validate, ValidationError
except ImportError:
    print("Error: jsonschema package required. Install with: pip install jsonschema", file=sys.stderr)
    sys.exit(1)


SCHEMA_DIR = Path(__file__).parent.parent / 'schema'


def detect_schema(doc):
    """Auto-detect which schema to use based on document content."""
    protocol = doc.get('protocol_version', '')

    # Check if it's an audit or infrastructure
    if 'auditor' in doc or 'audit_id' in doc:
        doc_type = 'audit'
    else:
        doc_type = 'infrastructure'

    # Check if it's EPI or DPI
    if 'lwd_r' in doc or 'lwd_r_verification' in doc:
        system_type = 'epi'
    else:
        system_type = 'dpi'

    return SCHEMA_DIR / system_type / f'{doc_type}.json'


def validate_document(doc_path, schema_path=None):
    """Validate document against schema."""
    with open(doc_path, 'r', encoding='utf-8') as f:
        doc = json.load(f)

    if schema_path is None:
        schema_path = detect_schema(doc)
        print(f"Auto-detected schema: {schema_path}")

    with open(schema_path, 'r', encoding='utf-8') as f:
        schema = json.load(f)

    try:
        validate(instance=doc, schema=schema)
        print(f"✓ Valid: {doc_path}")
        return True
    except ValidationError as e:
        print(f"✗ Invalid: {doc_path}")
        print(f"  Error: {e.message}")
        print(f"  Path: {' → '.join(str(p) for p in e.absolute_path)}")
        return False


def main():
    parser = argparse.ArgumentParser(description='Validate against Corrigibility Schema')
    parser.add_argument('document', help='JSON document to validate')
    parser.add_argument('--schema', '-s', help='Schema file (auto-detected if not specified)')
    args = parser.parse_args()

    schema_path = Path(args.schema) if args.schema else None
    success = validate_document(args.document, schema_path)
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
