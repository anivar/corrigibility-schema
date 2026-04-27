# Changelog

All notable changes to the Corrigibility Schema Protocol.

## [3.0] - 2026-04

Paper-faithful rewrite. Every schema field is now anchored to a specific
section of the published Corrigibility / EPI papers. Previous v2.x schemas
are preserved under `archive/v2/`.

### Breaking Changes

- **Audit field rename**: `results.*` → `tests.*` (paper §A.2). The five
  test booleans live under `tests`; the new derived `determination` block
  carries the corrigibility verdict and MUST recompute mechanically from
  `tests` (paper §A.2 Claim 2).
- **Canonicalization**: Required canonical form is now **RFC 8785 (JCS)**
  via the `jcs` Python package. The previous `json.dumps(sort_keys=True,
  separators=...)` recipe is NOT RFC 8785 conformant and is removed from
  PROTOCOL.md.
- **Signatures**: `operator_signature` / `auditor_signature` are now
  structured objects (`algorithm`, `canonicalization`, `value`,
  `signed_at`, `key_id`) instead of bare base64 strings. **Ed25519 only**;
  RSA-PSS removed. Public keys are multibase-encoded under
  `verification_method` (W3C DID-based) — PEM strings under `public_key`
  removed.
- **Tiered Assurance Model** (paper §E.2): `operator.identity_tier` and
  `auditor.identity_tier` are required integer enums `1|2|3`, mapped to
  `did:key` / `did:web` / institutional-accreditation respectively.
- **Topology enum** (paper §6.6): `topology` is required on infrastructure
  manifests and constrained to
  `centralized_sovereign | federated_protocol | market_platform | open_commons`.
- **`verification_tier` → `verification_depth`** in audit schemas (the term
  "tier" is now reserved for §E.2 identity tiers).
- **DPI `code` block** required: `source_available`, `license_open`,
  `build_reproducible`, `public_loc_pct` are now first-class fields on DPI
  infrastructure (previously these were collapsed into per-layer flags).
- **EPI action_boundaries**: required when `tier ∈ {decision_support,
  high_stakes}` and must include `executed_outside_llm_context: true` and
  `termination_criteria_explicit: true` (paper §6.7.3).
- **Layer typing split**: `layer_type` is now a vertical-strata enum
  (DPI: `protocol|implementation|operations|data|presentation`; EPI:
  `inference|orchestration|retrieval|training|evaluation|action|presentation`).
  Substantive purpose moves to a new `domain` field
  (`identity|payments|credentials|consent|data|...`).

### Added

- **Rule A.9 enforcement** (paper §E.1): when
  `governance.binding_mechanism = true`, `binding_proof_url`,
  `binding_proof_hash` (sha256 of the statute / charter / regulation),
  `binding_proof_type`, and `enforcement_history_url` are required (JSON
  Schema `if/then`). Audits add `binding_proof_resolved`,
  `binding_proof_hash_matched`, `enforcement_history_verified` flags.
- **FEE block** (paper §6.7.2 + B.7): `exit.fee` with `theta_E ∈ [0.8, 1.0]`,
  `baseline_signal_strength`, `alt_signal_strength`, and an enum of FEE
  design responses (paper §6.7.3): `protected_alternatives`,
  `multi_issuer_mandate`, `credential_acceptance_diversity`,
  `binding_multi_stakeholder_charter`, `funded_fallback_operations`,
  `federated_implementation`.
- **Switching cost σ** (paper §B.8): `exit_verification.switching_cost_sigma`
  on DPI audit.
- **Continuous indicators** (paper Tables 8/9): full
  `continuous_indicators` block on audits — penalty ratios, code visibility
  fraction, MTTD, override rate, throughput, fork cost ratio, and so on.
- **Active Deception detection** (paper §6.4.2): audit-side
  `active_deception` block with `open_washing_detected`,
  `safety_washing_detected`, `audit_theatre_detected`, `evidence_url`.
- **Compute capture** (companion paper): `compute.kappa`,
  `compute.community_compute_estimate_usd`, audit-side
  `kappa_used` and `training_cost_to_community_ratio`.
- **`previous_audit_hash`** on audits — chains audits the same way
  `previous_manifest_hash` chains manifests.
- **Cross-schema `$ref`**: EPI schemas reference DPI's `verification_method`
  and `signature` `$defs` via URN `$id`s. `tools/validate.py` now uses
  `referencing.Registry` so cross-schema references resolve.

### Removed

- Hand-rolled `json.dumps`-based canonicalisation recipe in PROTOCOL.md §5.
- RSA-PSS signature option.
- Bare base64 `auditor_signature` / `operator_signature` strings.
- PEM `public_key` strings on `operator` / `auditor` (replaced by
  `verification_method` + multibase).
- `results` (renamed to `tests`).

### Tools

- `tools/canonicalize.py` — replaced with a thin wrapper over the `jcs`
  PyPI package; CLI emits raw RFC 8785 bytes.
- `tools/hash.py` — uses `jcs.canonicalize` then `hashlib.sha256`.
- `tools/validate.py` — Draft 2020-12 + cross-schema `Registry`; auto-detects
  family/kind from document shape.

### Examples

All four examples rewritten to v3.0:

- `examples/dpi/infrastructure.example.json` — federated identity passing all
  five tests, FEE mechanisms, `did:web` operator at identity tier 2.
- `examples/dpi/audit.example.json` — Aadhaar-shaped system failing
  EXIT/CODE/GOVERN/FORK; demonstrates Rule A.9 violations and active
  deception detection.
- `examples/epi/infrastructure.example.json` — high-stakes welfare AI
  passing all five tests with full LWD-R, action_boundaries enforced,
  κ = 0.05.
- `examples/epi/audit.example.json` — same system; FORK fails because
  training cost-to-community ratio sits above the feasibility floor.

### Migration

v2.x manifests and audits are not directly upgradable. See
`archive/v2/` for the previous schemas. To migrate:

1. Rename `results` → `tests` on all audits.
2. Add a `determination` block computed from `tests`.
3. Replace `public_key` PEM strings with a `verification_method` block
   (DID + multibase) and add `identity_tier`.
4. Replace bare base64 signature strings with the structured signature
   object (`algorithm: "Ed25519"`, `canonicalization: "RFC8785"`, etc.).
5. Add `topology` to all infrastructure manifests.
6. Move per-layer `layer_type` substantive labels (e.g., `identity`) into
   a new `domain` field; pick a vertical-strata `layer_type`.
7. If `governance.binding_mechanism = true`, add `binding_proof_url`,
   `binding_proof_hash`, `binding_proof_type`, and
   `enforcement_history_url`.
8. Recompute all hashes with `tools/hash.py` (RFC 8785 / `jcs`).

## [2.0.1] - 2025-03

### Added

- **Fork verification fields** — legally_permitted, artifacts_available, constructed_barriers for DPI
- **Training forkability** — inference_forkable vs training_forkable distinction for EPI
- **Compute capture assessment** — C_train > κ × C_accessible verification fields
- **Revalidation structure** — monitoring_frequency, drift_threshold, next_revalidation_due
- **Fork verification in audit** — reproduction_attempted, reproduction_successful

### Skill Rules Added

- `layer-decomposition.md` — propagation rule, weakest-layer principle
- `variety-drift.md` — temporal drift, revalidation thresholds
- `action-boundary.md` — GDoS, deterministic envelope, agentic systems

### Protocol Updates

- Section 14: Periodic Enhancement Workflow
- Section 15: Paper-Schema Compliance requirements

## [2.0] - 2025-02

### Added

- **DPI and EPI schema separation** — distinct schemas for traditional DPI and AI-based EPI
- **LWD-R structure** — Logic, Weights, Data, Representation transparency for EPI
- **Tiered adoption** — trivial, decision_support, high_stakes classification
- **Verification tiers** — presence, behavior, proof depth levels
- **Audit validity period** — 12-month expiration with valid_until field
- **Contestation mechanism** — operator can dispute audit findings
- **Revocation support** — auditors can revoke issued audits
- **Observatory model** — delegated verification for shared components
- **Human escalation triggers** — link technical thresholds to institutional mechanisms
- **Governance verification** — distinguish grievance channels from binding governance
- **Action boundaries** — deterministic envelope specification for EPI
- **Drift monitoring** — variety drift assessment with retraining triggers
- **Swapability metrics** — zero-cost swap time for FORK test
- **Workflow filtering** — RAG-level EXIT mechanism for EPI
- **Chain integrity** — previous_manifest_hash for version chain verification
- **LLM instructions** — machine reasoning protocol for automated evaluation

### Changed

- `$id` now uses URN format (`urn:corrigibility:...`) instead of domain
- Version in `protocol_version` field, not filename
- Hash format standardized to `sha256:[64 hex chars]`

## [1.0] - 2024 (Internal)

### Added

- Basic five-test structure (EXIT, CODE, AUDIT, GOVERN, FORK)
- Simple operator/auditor separation
- Boolean results only

---

## Versioning Policy

- **MAJOR** (2.x → 3.x): Breaking schema changes
- **MINOR** (2.0 → 2.1): New optional fields, enum additions
- **Patch**: Documentation only, no schema changes
