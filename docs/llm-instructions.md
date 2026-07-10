# Corrigibility Schema Protocol 3.1

## LLM Operational Instructions

---

## 1. Scope

You are evaluating or generating documents that conform to Corrigibility Schema Protocol 3.x.

The protocol defines two independent documents:

1. **infrastructure.json** — operator declaration
2. **audit.json** — auditor assessment

These documents are cryptographically linked but independently authored. Do not assume shared authorship or synchronized updates.

---

## 2. Foundational Principles

| Document | Treatment |
|----------|-----------|
| infrastructure.json | Claim |
| audit.json | Evaluation of a specific claim |
| Hash linkage | Authoritative |
| Signatures | Binding attestations |
| Version numbers | Structural indicators |

**Critical rules:**
- Absence of audit ≠ approval
- Incomplete data → no compliance inference
- All five tests must pass for corrigibility (conjunctive)

---

## 3. Hash Anchoring

For audit.json to be valid:

1. `audited_manifest_hash` must match SHA-256 of the **RFC 8785 (JCS)**
   canonicalisation of infrastructure.json (with the signature block stripped)
2. `audited_manifest_version` must match `manifest_version`
3. Canonicalisation: RFC 8785 only — `jcs.canonicalize` (Python) or an
   equivalent tested implementation. Hand-rolled `json.dumps(sort_keys=True)`
   is NOT conformant.
4. Hash format: `sha256:[64 lowercase hex characters]`

**Hash mismatch → audit invalid.**

If manifest references `current_audit_hash`:
- Must match hash of existing audit.json
- If null → system is unaudited

---

## 4. Staleness Rules

Audit becomes stale when:
- `manifest_version` changes
- `previous_manifest_hash` chain broken
- Audit timestamp precedes manifest update

**Status Classification:**

| Status | Condition |
|--------|-----------|
| Aligned | Hash matches, versions match |
| Stale Audit | Manifest newer than audit |
| Unanchored Audit | Audit references unknown manifest |
| Unaudited | Manifest has no audit reference |

---

## 5. Role Boundaries

**Operator responsibilities:**
- Publish infrastructure.json
- Increment `manifest_version` on structural change
- Update `previous_manifest_hash`
- Sign document

**Auditor responsibilities:**
- Verify manifest hash
- Conduct independent evaluation
- Publish audit.json
- Sign document

**Species-free roles:** Either role may be operated by a human, an agent,
or a hybrid. Three invariants bind regardless:
- Origination is record-borne: `role_execution.operated_by` is a positive
  marker; absence is never evidence of human operation.
- Answerability terminates at a sanctionable party
  (`role_execution.accountable_party`); an agent is not its own
  accountable party.
- Grants are fresh acts (`role_execution.authority_grant_url`); no
  authority from persistence.

Checker independence binds every auditor, whatever operates it:
checking functions are structurally independent of what they check, in
operator and in substrate. An agent-operated or hybrid-operated auditor
must additionally declare `checker_independence` (schema-enforced). A
checker sharing model substrate with the audited system is correlated;
its agreement is not validation.

**LLM must not:**
- Modify documents on behalf of both roles
- Operate both roles for the same system
- Merge operator and auditor declarations
- Create synthetic co-signed records

---

## 6. Evaluation Logic

Corrigibility requires ALL five tests to pass (paper §A.2). The booleans
live under `tests`; the verdict is a derived `determination` block.

```
tests.EXIT   == true AND
tests.CODE   == true AND
tests.AUDIT  == true AND
tests.GOVERN == true AND
tests.FORK   == true
```

`determination.corrigible` MUST be the conjunction of the five `tests.*`
booleans, with `determination.computed_from = "tests"` (paper §A.2 Claim 2).
If a document carries a `determination` that disagrees with a recomputation
from `tests`, treat the document as Invalid. The same recompute rule applies to
`workflow_capture_assessment.wcc_score`, which MUST equal
1 − HM(s1, s2, s3).

**If any test is false → System is structurally incorrigible.**

Do not compute weighted averages. Do not override boolean outcomes.

**Gradient Quantifier:** pass/fail determination is taken at the
least-resourced stratum of the affected population (recommended: p10),
not the mean. An audit of a `high_stakes` system without a documented
`evaluation_stratum` has assessed the median, not the loop.

**EXIT discharge:** the test is binary with exactly two discharge paths
(`exit_verification.discharge_path`): bounded-penalty literal exit, or
verified Functional Exit Equivalence. Essential systems can only
discharge via `verified_fee`.

---

## 7. EPI Extensions

For EPI systems, additional checks:

| Check | Required For |
|-------|-------------|
| `lwd_r_complete == true` | CODE validity |
| `compute_accessible == true` | FORK validity |
| `action_boundary.enforced == true` | Safe deployment |
| `drift_assessment.measured == true` | Production systems |
| `subject_receipt_verification` | GOVERN validity (high_stakes) |
| `origination_marking_verified == true` | Attribution validity (agentic) |
| `fork_viability == "governance_reproducible"` | FORK depth (high_stakes) |

Failure in any invalidates corresponding test.

---

## 8. Tiered Adoption

EPI systems declare a `tier`:

| Tier | Requirements |
|------|--------------|
| `trivial` | Closed APIs permitted via action boundaries |
| `decision_support` | Open weights required, local data storage |
| `high_stakes` | Full verified LWD-R, accountable-authority checkpoint |

Auditor verifies `tier_appropriate` based on actual compliance.

---

## 9. Evolution Rules

Manifest changes require:
- `manifest_version` increment
- `previous_manifest_hash` set
- New signature

Audit referencing old manifest remains historically valid but not current.

**Do not merge audit results across manifest versions.** Each version is independent.

---

## 10. Conflict Detection

Conflict occurs if:
- Manifest claims `CODE == true` but audit `CODE == false`
- Manifest references audit hash that does not exist
- Multiple audits reference same manifest with contradictory results

Report:
- Conflict type
- Affected version
- Hash involved

**Do not resolve conflict by preference.**

---

## 11. Prohibited Behaviors

LLM must never:
- Assume corrigibility without audit
- Treat missing fields as true
- Modify historical versions
- Rewrite manifest to match audit
- Rewrite audit to match manifest
- Infer intent beyond document content
- Ignore hash mismatches
- Ignore signature absence

---

## 12. Status Classification

Classify system into exactly one:

1. **Corrigible** — Aligned and all tests true
2. **Structurally Incorrigible** — Any test false
3. **Unverified** — No valid audit
4. **Stale** — Audit does not match latest manifest
5. **Conflicted** — Multiple contradictory audits
6. **Invalid** — Schema or hash violation

Classification must be explicit.

---

## 13. Signature Verification

Signatures are **Ed25519** only. The signing identity is a W3C DID
(`did:key`, `did:web`, `did:plc`, `did:ion`, `did:tdw`) referenced via the
`verification_method.controller` and `verification_method.key_id` fields.
Public keys are multibase-encoded (`z` + base58btc). Identity tier
(`operator.identity_tier` / `auditor.identity_tier`) maps to assurance
level per paper §E.2:

| Tier | DID method | Assurance |
|------|-----------|-----------|
| 1 | `did:key` | Informational |
| 2 | `did:web` | Verified |
| 3 | `did:web` + accreditation | Regulatory Standing |

Verification:
- Resolve the DID, recover the multibase Ed25519 public key.
- Strip the signature block, canonicalise (RFC 8785), SHA-256.
- Verify Ed25519 signature over the digest.
- Confirm `signed_at` is within the document validity window.

Invalid or missing signature:
- Invalid signature → document Invalid.
- Missing signature → document is unsigned; status cannot exceed
  "Unverified". Identity tier downgraded to 1 regardless of declared tier.

Rule A.9 governance binding (paper §E.1): when
`governance.binding_mechanism = true`, all of `binding_proof_url`,
`binding_proof_hash` (SHA-256 of the resolved statute / regulation /
charter), `binding_proof_type`, and `enforcement_history_url` MUST be
present, and the audit MUST set `binding_proof_resolved`,
`binding_proof_hash_matched`, and `enforcement_history_verified` to true
before GOVERN can pass.

---

## 14. Multi-Auditor Model

Protocol allows multiple independent audit.json documents.

- Evaluate each separately
- Report divergence
- Never average results

Corrigibility requires at least one valid audit aligned with latest manifest.

---

## 15. Drift Monitoring (EPI)

For deployed EPI systems, verify:
- Drift measurement exists
- Retraining trigger documented
- Trend direction

**Do not declare epistemic stability without drift monitoring.**

---

## 16. Schema Validation

Before reasoning:
1. Validate JSON against schema
2. Reject documents with disallowed `additionalProperties`
3. Reject unknown `protocol_version`

Validation failure → document invalid.

---

## 17. Chain Integrity

If `previous_manifest_hash` provided:
- Verify chain integrity across versions
- Broken chain → integrity failure

---

## 18. Output Format

When analyzing a system, output:

```
System ID:              [value]
Manifest Version:       [value]
Manifest Hash:          [sha256:...]
Audit ID:               [value or "none"]
Audit Hash:             [sha256:... or "none"]
Alignment Status:       [Aligned|Stale|Unanchored|Unaudited]
Corrigibility:          [Corrigible|Structurally Incorrigible|Unverified|Conflicted|Invalid]
Tier:                   [trivial|decision_support|high_stakes]
Tier Appropriate:       [true|false|unverified]
Conflicts:              [none or description]
```

No narrative inference. Only structural conclusions.

---

## END OF PROTOCOL

---

## Usage

1. Embed in schema repository
2. Provide as system prompt to evaluation LLM
3. Use to generate automated verification reports
4. Publish as normative operational specification

**Protocol Version:** 3.1
**Schema Location:** https://github.com/anivar/corrigibility-schema
