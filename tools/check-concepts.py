#!/usr/bin/env python3
"""
Concept-inventory gate.

Verifies that every paper concept in docs/concept-map.json still has its
declared home: schema field paths resolve, docs entries match, tool files
exist. Run before and after any schema change; a refactor that orphans a
concept fails here instead of shipping silently.

Also reports (without failing) top-level schema properties no concept
claims — the drift detector: fields nothing in the papers asks for are
candidates for deletion, not preservation.

Usage:
    python tools/check-concepts.py [--strict-coverage]
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCHEMAS = {
    "dpi/infrastructure": ROOT / "schema/dpi/infrastructure.json",
    "dpi/audit": ROOT / "schema/dpi/audit.json",
    "epi/infrastructure": ROOT / "schema/epi/infrastructure.json",
    "epi/audit": ROOT / "schema/epi/audit.json",
}


def _deref(node: dict, all_schemas: dict) -> dict:
    """Follow a $ref to its target (urn cross-file or #/$defs local-in-common)."""
    ref = node.get("$ref")
    if not ref:
        return node
    if ref.startswith("urn:"):
        base, _, frag = ref.partition("#")
        target = next((s for s in all_schemas.values() if s.get("$id") == base), None)
        if target is None:
            return node
    else:
        _, _, frag = ref.partition("#")
        target = node.get("$_root", {})
    for part in [p for p in frag.split("/") if p]:
        target = target.get(part, {})
    return target


def visible_properties(node: dict, all_schemas: dict, root: dict) -> dict:
    """Properties visible at a node: its own, its $ref target's, and its
    allOf branches' — the composition surface the 4.0 schemas use."""
    node = dict(node)
    node.setdefault("$_root", root)
    out: dict = {}
    target = _deref(node, all_schemas)
    if target is not node:
        t = dict(target)
        t["$_root"] = next((s for s in all_schemas.values() if target in _walk_containers(s)), root)
        out.update(visible_properties(t, all_schemas, t.get("$_root", root)))
    for branch in node.get("allOf", []):
        b = dict(branch)
        b["$_root"] = root
        out.update(visible_properties(b, all_schemas, root))
    out.update(node.get("properties", {}))
    if "items" in node:
        out.update(node["items"].get("properties", {}))
    return out


def _walk_containers(schema):
    stack = [schema]
    while stack:
        cur = stack.pop()
        yield cur
        if isinstance(cur, dict):
            stack.extend(v for v in cur.values() if isinstance(v, (dict, list)))
        elif isinstance(cur, list):
            stack.extend(v for v in cur if isinstance(v, (dict, list)))


def make_resolver(all_schemas: dict):
    def resolve(schema: dict, path: str) -> bool:
        node = schema
        for key in path.split("/"):
            props = visible_properties(node, all_schemas, schema)
            if key not in props:
                return False
            node = props[key]
        return True
    return resolve


def main() -> int:
    strict = "--strict-coverage" in sys.argv
    cmap = json.loads((ROOT / "docs/concept-map.json").read_text())
    schemas = {k: json.loads(p.read_text()) for k, p in SCHEMAS.items()}
    schemas["common"] = json.loads((ROOT / "schema/common.json").read_text())
    resolve = make_resolver(schemas)

    failures: list[str] = []
    claimed: dict[str, set[str]] = {k: set() for k in SCHEMAS}

    for c in cmap["concepts"]:
        name = c["concept"]
        for h in c["homes"]:
            kind = h["type"]
            if kind == "field":
                sid, path = h["schema"], h["path"]
                if sid not in schemas:
                    failures.append(f"{name}: unknown schema '{sid}'")
                elif not resolve(schemas[sid], path):
                    failures.append(f"{name}: field home missing — {sid}:{path}")
                else:
                    claimed[sid].add(path.split("/")[0])
            elif kind == "docs":
                f = ROOT / h["file"]
                if not f.exists():
                    failures.append(f"{name}: docs home missing — {h['file']}")
                elif h.get("match") and h["match"].lower() not in f.read_text().lower():
                    failures.append(f"{name}: docs home {h['file']} no longer mentions '{h['match']}'")
            elif kind == "tool":
                if not (ROOT / h["file"]).exists():
                    failures.append(f"{name}: tool home missing — {h['file']}")
            elif kind == "derivation":
                for inp in h.get("inputs", []):
                    sid, path = inp.split(":", 1)
                    if not resolve(schemas[sid], path):
                        failures.append(f"{name}: derivation input missing — {inp}")
            elif kind == "gap":
                pass  # tracked deliberately; nothing to verify yet
            else:
                failures.append(f"{name}: unknown home type '{kind}'")

    # Drift report: top-level properties no concept claims.
    unclaimed_total = 0
    print("— unclaimed top-level properties (candidates for deletion, not preservation):")
    for sid, schema in schemas.items():
        if sid == "common":
            continue
        top = set(schema.get("properties", {}))
        envelope = {
            "protocol_version", "system_id", "manifest_version", "audit_id",
            "timestamp", "valid_until", "previous_manifest_hash",
            "previous_audit_hash", "audited_manifest_version",
            "audited_manifest_hash", "current_audit_hash", "operator",
            "auditor", "operator_signature", "auditor_signature",
            "verification_method", "revocation", "contestation",
            "corrigibility_claim", "tests", "escalation",
            "delegated_verification",
        }
        unclaimed = sorted(top - claimed[sid] - envelope)
        unclaimed_total += len(unclaimed)
        if unclaimed:
            print(f"  {sid}: {', '.join(unclaimed)}")

    if failures:
        print(f"\nconcept gate: {len(failures)} FAILURES")
        for f in failures:
            print(f"  ✗ {f}")
        return 1
    n = len(cmap["concepts"])
    print(f"\nconcept gate: all {n} concepts have their homes")
    if strict and unclaimed_total:
        print(f"strict coverage: {unclaimed_total} unclaimed top-level properties")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
