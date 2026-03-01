# Corrigibility Schema Protocol

## Governance & Development

---

## 1. Document Classification

### Public (This Repository)

| Artifact | Purpose |
|----------|---------|
| Schema definitions | Structural contracts |
| LLM instructions | Machine reasoning rules |
| Validation tools | Generic verification |
| Fictional examples | Adoption guidance |
| Versioning rules | Protocol evolution |

### Not In This Repository

| Artifact | Reason | Where It Lives |
|----------|--------|----------------|
| Real audit findings | May expose vulnerabilities | Auditor's secure systems |
| Private keys | Security | Operator/auditor key management |
| System-specific analysis | Sensitivity | Separate analysis repos |
| Draft schema proposals | Process | Issues/PRs until merged |

---

## 2. Versioning

### Semantic Versioning for Protocol

```
MAJOR.MINOR
```

| Change Type | Version Impact | Example |
|-------------|----------------|---------|
| Breaking schema change | MAJOR bump | Required field added |
| New optional field | MINOR bump | New optional `findings` array |
| Documentation only | No bump | README update |

### Current Version: 2.0

### Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.0 | 2025-02 | Initial public protocol. LWD-R structure. Tiered adoption. |
| 1.x | Internal | Pre-publication iterations |

---

## 3. Schema Evolution Rules

### Adding Fields

1. New fields MUST be optional unless MAJOR version bump
2. New fields MUST have `description` in schema
3. New fields MUST be documented in CHANGELOG

### Removing Fields

1. Fields cannot be removed without MAJOR version bump
2. Deprecated fields MUST remain for 2 MAJOR versions
3. Deprecation MUST be announced in CHANGELOG

### Changing Field Types

1. Type changes require MAJOR version bump
2. Enum additions are MINOR (backward compatible)
3. Enum removals are MAJOR (breaking)

---

## 4. Contribution Process

### For Schema Changes

1. Open issue describing change rationale
2. Draft PR with schema modification
3. Include example documents showing change
4. Update validation tools if needed
5. Two maintainer approvals required for MAJOR changes

### For Documentation

1. Direct PR acceptable
2. One maintainer approval sufficient

### For Tools

1. PR with tests
2. Must not break existing validation
3. One maintainer approval

---

## 5. Hash Canonicalization Standard

All hashes computed over canonical JSON:

```python
import json
import hashlib

def canonicalize(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'))

def hash_manifest(obj):
    canonical = canonicalize(obj)
    digest = hashlib.sha256(canonical.encode('utf-8')).hexdigest()
    return f"sha256:{digest}"
```

### Rules

1. Sort keys lexicographically (recursive)
2. No whitespace between elements
3. UTF-8 encoding
4. No trailing newline
5. Hash algorithm: SHA-256 only (Protocol 2.x)

---

## 6. Signature Standard

### Algorithm

- Ed25519 (preferred)
- RSA-PSS with SHA-256 (acceptable)

### Format

```
base64(sign(canonical_json, private_key))
```

### Public Key Format

PEM-encoded, stored in `public_key` field.

---

## 7. Publication Locations

### Operator Manifest

```
https://{domain}/.well-known/corrigibility/infrastructure.json
```

### Audit (if published by operator)

```
https://{domain}/.well-known/corrigibility/audit.json
```

### Audit (if published by auditor)

```
https://{auditor-domain}/audits/{system_id}/{audit_id}.json
```

---

## 8. Audit Validity

### Expiration

Audits are valid for **12 months** from `timestamp` unless:
- Manifest version changes (immediate staleness)
- Auditor revokes (explicit invalidation)

### Revocation

Auditor may publish revocation:

```json
{
  "audit_id": "...",
  "revoked_at": "2025-06-01T00:00:00Z",
  "reason": "Material change in system behavior"
}
```

---

## 9. Contestation Process

### Operator Contest

If operator disputes audit results:

1. File contestation with audit body
2. `contestation` field added to audit:

```json
"contestation": {
  "contested": true,
  "filed_at": "2025-03-01T00:00:00Z",
  "status": "pending",
  "resolution": null
}
```

3. Resolution updates `status` to `upheld` or `overturned`

### Public Disclosure

Contested audits MUST remain published with contestation status visible.

---

## 10. Observatory Model

For jurisdictions lacking audit capacity:

### Delegated Verification

Centralized bodies (UN, DPG Alliance, regional consortia) may:
1. Audit common models/components
2. Publish certified profiles
3. Local operators reference certification

```json
"delegated_verification": {
  "observatory": "DPG Alliance EPI Observatory",
  "component": "meta-llama/Llama-3-70B",
  "certified_profile_hash": "sha256:...",
  "certification_date": "2025-01-15",
  "certification_url": "https://..."
}
```

### Scope Limits

Delegated verification covers component only, not deployment context.
Local audit still required for:
- Data handling
- Action boundaries
- Governance structures

---

## 11. Human Escalation Triggers

Technical thresholds MUST link to institutional mechanisms:

```json
"escalation": {
  "oversight_body": "Digital Rights Ombudsman",
  "oversight_url": "https://...",
  "triggers": [
    {
      "condition": "any_test_false",
      "action": "mandatory_review"
    },
    {
      "condition": "drift_score > 0.3",
      "action": "citizen_jury_notification"
    },
    {
      "condition": "high_stakes_tier",
      "action": "judicial_review_available"
    }
  ],
  "liability_framework_url": "https://..."
}
```

---

## 12. Breaking Changes Checklist

Before any MAJOR version:

- [ ] 6-month deprecation notice
- [ ] Migration guide published
- [ ] Validation tools updated
- [ ] Example documents updated
- [ ] LLM instructions updated
- [ ] Downstream users notified

---

## 13. Maintainers

Protocol maintained by:
- [To be determined by community]

### Decision Process

- MINOR changes: Maintainer consensus
- MAJOR changes: Public comment period (30 days) + maintainer consensus

---

## 14. License

- Schemas: CC0 (public domain)
- Documentation: CC-BY-SA 4.0
- Tools: MIT
