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

### Current Version: 3.1

### Version History

| Version | Date | Changes |
|---------|------|---------|
| 3.1 | 2026-07 | July 2026 paper alignment, all fields optional. Gradient Quantifier `evaluation_stratum`. EXIT `discharge_path`. Collective-Standing Precondition. Rule A.11 `data_access_declaration`. Species-free `role_execution` + `checker_independence`. Subject receipts, citizen-constraint registry, Injunction Hooks. Origination marking. Operative R + R-Layer Change Control. Normalized-Boundary lifetimes + accountable-authority checkpoint. Scale bounds, nested delegation, effect-surface placement. WCC assessment. `fork_viability`. Assessment rule files retired to archive. |
| 3.0 | 2026-04 | Paper-faithful rewrite. RFC 8785 canonicalization. Ed25519 + W3C DID. Rule A.9 binding-mechanism enforcement. Tiered Assurance Model (paper §E.2). `tests` (replacing `results`) + derived `determination` field. Continuous indicators. Active Deception detection. FEE block with θ_E. Required action_boundaries for non-trivial EPI tiers. Vertical-strata `layer_type` enum + separate `domain` field. |
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

All hashes are computed over the **RFC 8785 (JSON Canonicalization Scheme, JCS)**
canonical form of the document, hashed with SHA-256. This is the algorithm
mandated by paper Rule A.10.

> **DO NOT** hand-roll canonicalization with `json.dumps(sort_keys=True)`.
> That recipe is **not** RFC 8785 conformant — it mishandles numeric edge
> cases (e.g. `1.0` → `"1.0"` where JCS requires `"1"`; `-0.0` stays `-0.0`
> where JCS requires `"0"`), Unicode normalisation, and integer/float
> boundary rules. Use a tested implementation.

### Reference Implementation

```python
import hashlib
import jcs  # https://pypi.org/project/jcs/ — RFC 8785 reference

def hash_manifest(obj) -> str:
    canonical = jcs.canonicalize(obj)         # bytes
    digest = hashlib.sha256(canonical).hexdigest()
    return f"sha256:{digest}"
```

The `tools/canonicalize.py` and `tools/hash.py` scripts in this repository
delegate to the `jcs` package and MUST NOT be replaced with hand-rolled
recipes.

### Rules

1. Canonicalisation algorithm: **RFC 8785 (JCS)**, no exceptions
2. Hash algorithm: **SHA-256** only
3. Output format: `sha256:<64 lowercase hex characters>`
4. UTF-8 encoding
5. The `operator_signature` / `auditor_signature` block itself MUST be
   stripped before computing `*_hash` of the document, and re-added after
   signing
6. Trailing newlines or BOM marks MUST NOT be present in the canonical bytes

---

## 6. Signature Standard

### Algorithm

- **Ed25519 only.** RSA-PSS, ECDSA-P256, and other algorithms are NOT
  permitted (paper Rule A.10).

### Identity & Key Format

Signing identity is bound through a **W3C Decentralized Identifier (DID)**.
The supported DID methods are `did:key`, `did:web`, `did:plc`, `did:ion`,
and `did:tdw`. The DID method choice maps to the Tiered Assurance Model
(paper §E.2):

| Tier | DID method | Assurance label |
|------|-----------|-----------------|
| 1 | `did:key` | Informational |
| 2 | `did:web` (HTTPS-resolved) | Verified |
| 3 | `did:web` + institutional accreditation reference | Regulatory Standing |

Public keys are encoded as **multibase base58btc** (`z` prefix,
`Ed25519VerificationKey2020` type) in the `verification_method` block.
PEM-wrapped keys are NOT permitted.

### Signature Format

Signatures are **base64url** (RFC 4648 §5, no padding) over the SHA-256
digest of the RFC 8785 canonical bytes of the document with the
`operator_signature` / `auditor_signature` block removed.

```json
{
  "algorithm": "Ed25519",
  "canonicalization": "RFC8785",
  "value": "<base64url(64 bytes)>",
  "signed_at": "2026-02-01T00:00:00Z",
  "key_id": "did:web:authority.example.gov#manifest-signer"
}
```

### Verification

1. Resolve `key_id` DID → multibase public key
2. Strip the signature block from the document
3. Canonicalise (RFC 8785), hash (SHA-256)
4. Verify Ed25519 signature over the digest
5. Confirm `signed_at` is within the document's validity window

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

## 11. Escalation Triggers

Technical thresholds MUST link to institutional mechanisms. Escalation
terminates at an accountable authority — a sanctionable party whose grant
is fresh and whose liability binds; the human legal person is the current
instance. The requirement is functional, not positional (papers, The
Normalized Boundary):

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

## 14. Periodic Enhancement Workflow

### Why Periodic Enhancement

DPI and EPI systems evolve. The corrigibility framework must evolve with them:

1. **Variety Drift**: Environmental variety changes over time
2. **New Architectures**: AI architectures evolve faster than governance
3. **Regulatory Changes**: Legal requirements shift
4. **Community Feedback**: Deployment experience informs improvements

### Enhancement Cycle

```
Research Papers → Schema Updates → Validation
      ↑                              │
      └────── Community Feedback ←───┘
```

### Paper-Schema Alignment

| Layer | Purpose | Update Trigger |
|-------|---------|----------------|
| Research Papers | Theoretical foundation | New threats, architectures |
| Schemas | Structural contracts | Paper concepts need encoding |
| Validation | Verification tools | Schema changes |

The papers and schemas are the specification. Hand-written assessment
rule files were retired to `archive/skills-v3-era/` in 3.1; evaluators
consume the schema pair directly (see `AGENTS.md` and
`docs/llm-instructions.md`).

### Enhancement Process

1. **Paper Update**: New concepts introduced in research papers
2. **Schema Proposal**: Issue opened proposing schema additions
3. **Validation**: Tools and examples updated to verify new fields
4. **Release**: Coordinated release

### Backward Compatibility

| Change Type | Compatibility |
|-------------|---------------|
| New optional field | Backward compatible |
| New enum value | Backward compatible |
| New required field | Breaking (MAJOR bump) |
| Field removal | Breaking (MAJOR bump) |

### Audit Revalidation Triggers

Periodic assessment required when:

| Trigger | Timeframe | Action |
|---------|-----------|--------|
| Time-based | 12 months max | Full re-audit |
| Drift threshold | When Δ(t) > τ | Drift-focused audit |
| Manifest change | Immediate | Delta audit |
| Paper update | Schema MAJOR bump | Gap assessment |

---

## 15. Paper-Schema Compliance

### Authoritative Sources

| Paper | Scope | Citation |
|-------|-------|----------|
| DPI Corrigibility Framework | Digital infrastructure | Aravind (2025) |
| Epistemic Public Infrastructure | AI/learned systems | Aravind (2025) |

### Compliance Requirements

Schemas MUST encode all paper concepts:

| Paper Concept | Schema Location | Verification |
|---------------|-----------------|--------------|
| Five tests | `tests.*` (audit) / `corrigibility_claim.*` (manifest) | Boolean fields |
| Derived determination | `determination` (audit) | `computed_from: "tests"` (paper §A.2) |
| Layer decomposition | `layers[]` + `layer_verification.*` | Vertical-strata `layer_type` + `domain` |
| LWD-R | `lwd_r.*` (manifest) / `lwd_r_verification.*` (audit) | Required for EPI |
| Topology | `topology` enum | `centralized_sovereign` / `federated_protocol` / `market_platform` / `open_commons` |
| Verification depth | `verification_depth` | `presence` / `behavior` / `proof` |
| Variety drift Δ(t) > τ | `drift_assessment` | EPI audit |
| Action boundaries | `action_boundaries` | Required for EPI tiers ≥ decision_support |
| Compute capture (κ) | `compute.kappa`, `compute.community_compute_estimate_usd` | EPI infrastructure |
| Tiered adoption | `tier` | EPI infrastructure |
| Identity tier (paper §E.2) | `operator.identity_tier` / `auditor.identity_tier` | DID method × assurance |
| FEE θ_E | `exit.fee` | DPI + EPI infrastructure |
| Switching cost σ | `exit_verification.switching_cost_sigma` | DPI audit |
| Rule A.9 (binding authority) | `governance.binding_proof_url`, `binding_proof_hash`, `enforcement_history_url` | Required when `binding_mechanism=true` |
| Active Deception | `active_deception.*` (audit) | Open-washing / safety-washing / audit theatre |
| Continuous indicators (Tables 8/9) | `continuous_indicators.*` | Audit |
| RFC 8785 canonicalisation | Signature block `canonicalization: "RFC8785"` | Tools |
| Ed25519 + W3C DID | `verification_method` ($defs) | Tools |

### Skills MUST Cover

Each paper concept requires corresponding skill rule:

| Rule File | Paper Section |
|-----------|---------------|
| test-exit.md | EXIT test |
| test-code.md | CODE test, LWD-R |
| test-audit.md | AUDIT test |
| test-govern.md | GOVERN test |
| test-fork.md | FORK test, compute capture |
| layer-decomposition.md | Layer analysis |
| variety-drift.md | Temporal drift |
| action-boundary.md | Agentic systems |

---

## 16. License

- Schemas: CC0 (public domain)
- Documentation: CC-BY-SA 4.0
- Tools: MIT
