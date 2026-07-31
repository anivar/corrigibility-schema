# Changelog

All notable changes to the Corrigibility Schema Protocol.

## [3.2] - 2026-07

The two holes the July papers left in 3.1, found by a systematic audit of
every Definition/Principle/Condition/Proposition in both papers against the
schema fields. All new fields are optional (MINOR); 3.0 and 3.1 documents
remain valid. This closes the 3.x line's paper alignment; structural repair
of the accumulated surface is planned as 4.0 and will not be additive.

### Added

- **Data Capture** (companion paper Definition 5.2, D_required > κ_D ·
  D_accessible): `data` block on `schema/epi/infrastructure.json` — corpus
  reproducibility, κ_D, required-to-accessible ratio, auditable-substitute
  flag, and the §5.2 upstream-dependency taxonomy (synthetic data from
  proprietary models, distilled closed-API outputs, proprietary evaluation
  sets, undisclosed RLHF traces/preference data, unavailable reward models,
  undisclosed tokenizer/filter rules). `fork.data_capture_status` mirrors
  the compute axis; the Joint Forkability Condition requires evading both.
- **`data_verification`** on `schema/epi/audit.json`, mirroring
  `compute_verification`, plus `DATA` in the findings test enum. A FORK
  assessment can now record the failure axis the paper says compute-only
  analyses miss.
- **Temporal Stability upper bound** (paper Principle 6.1): the
  accountable-authority checkpoint's `correction_within_window` (lower
  bound, harm accumulation) gains `correction_upper_bound_enforced` (upper
  bound, manipulation prevention), so the condition is representable as the
  two-sided inequality the paper states rather than one boolean.

## [3.1] - 2026-07

Alignment with the July 2026 revision of both papers. All new fields are
optional (MINOR); existing 3.0 documents remain valid.

### Added

- **`fork_viability`** in `schema/epi/audit.json` (artifact_reproducible /
  governance_reproducible / not_reproducible), per the EPI paper's
  governance-reproducible FORK standard; required in practice for
  high_stakes tier audits.
- **Gradient Quantifier**: `evaluation_stratum` on both audits — the
  stratum at which minimum performance was measured, how it was
  identified, and the quantile used (recommended p10). New `STRATUM`
  finding class.
- **EXIT discharge path**: `discharge_path` (literal_exit | verified_fee)
  on both manifests' `exit` and both audits' `exit_verification`; EPI adds
  `regeneration_resistant` / `regeneration_resistant_verified` (purge alone
  is not the test).
- **Collective-Standing Precondition** (Ostrom Principle 7):
  `governance.collective_standing` on manifests;
  `collective_standing_verified` + `collective_standing_constraint` on
  audits.
- **Rule A.11 Auditor Data Duties**: `auditor.data_access_declaration` —
  data categories, purpose, privacy budget, retention/deletion.
- **Species-free role execution**: shared `role_execution` $def
  (operated_by human|agent|hybrid, accountable_party, authority_grant_url)
  on operator and auditor; `checker_independence` $def on auditors
  (independence in operator and in substrate).
- **Subject Receipt Requirement**: `subject_receipts` block on the EPI
  manifest; `subject_receipt_verification` on the EPI audit. New `RECEIPT`
  finding class.
- **Citizen-side GOVERN**: `citizen_constraint_registry` and
  `injunction_hooks` on EPI governance, with audit-side
  `citizen_constraint_registry_verified` and `injunction_hook_tested`.
- **Origination marking**: `origination_marking` block on the EPI manifest
  (positive signed markers; absence is never human; markers only narrow
  authority) and `origination_marking_verified` on the EPI audit. New
  `ORIGINATION` finding class.
- **Machine-verifiable legitimacy (a)–(d)**:
  `machine_verifiable_legitimacy` block on the EPI manifest (authority
  credentials, revocation propagation, tamper-evident traces,
  incident-triggered mitigation); audit-side
  `legitimacy_requirements_verified`.
- **Dual Exercise of the Tests**: outward-instrument fields —
  `code.decision_rule_legible` on both manifests (the operative rule in a
  subject's case is identifiable and stated), DPI-side `subject_receipts`
  and `subject_receipt_verification` (decision notice, subject-verifiable
  record), and `decision_rule_legibility_verified` on the DPI audit.
- **Operative R**: `lwd_r.representation.operative_r` — deployment
  variables enumerated (quantization, pruning, routing, output
  filtering), published probe set, declared tolerance ε and sample size
  n; audit-side `operative_r_reproduced`.
- **R-Layer Change Control**: `lwd_r.representation.change_control`
  (materiality threshold, notice window, suspensive effect, versioned
  schema diffs); audit-side `r_change_control_verified`.
- **Normalized Boundary**: `specification_lifetime_days`,
  `renewal_requires_fresh_grant`, and `accountable_authority_checkpoint`
  (scope per_decision|per_class|boundary; grant fresh, liability binds,
  correction within window) on EPI action_boundaries, with audit-side
  `specification_lifetime_verified` and `accountable_authority_verified`.
- **Scale as a Governed Variable**: `scale_bounds` (fan-out, action-rate,
  blast-radius) on EPI action_boundaries; `scale_bounds_verified` on the
  audit. New `SCALE` finding class.
- **Untyped Action Channels / Nested Delegation**: `enforcement_placement`
  (action_proposal | effect_surface | hybrid) and `nested_delegation`
  (max depth, attenuation, cross-depth audit reconstruction, EXIT
  propagation) on EPI action_boundaries, with audit-side
  `enforcement_placement_verified` and `nested_delegation_verified`.
- **Exception Handling at the Margin**: `explicit_exception_pathways`,
  `guaranteed_fallbacks`, `fallback_spec_url` on EPI action_boundaries;
  `exception_pathways_verified` on the audit.
- **WCC assessment**: `workflow_capture_assessment` on the EPI audit
  (field names per the EPI paper appendix) — sovereignty scores s1
  (workflow reproducibility), s2 (ontological substitutability), s3
  (model portability) in (0,1], with derived `wcc_score = 1 − HM(s1,s2,s3)`
  under the same mechanical-recompute rule as `determination`.
- **Governance-reproducible FORK, manifest side**:
  `fork.governance_artifacts` on the EPI manifest (eval suites, red-team
  scenarios, failure registry, sanitized incident logs, harness docs) —
  what the audit's `fork_viability` verifies against.
- **EPI `layer_verification`**: per-layer audit results over the EPI
  strata, closing the weakest-link gap (T_system = AND over layers);
  nested delegation carries the depth axis.
- **`AGENTS.md`**: instructions for agents operating either protocol role.

### Changed

- Assessment rule files retired to `archive/skills-v3-era/`. Frontier
  evaluators no longer need hand-written rule prompts; the durable machine
  interface is the schema pair itself (the operator's affidavit and the
  auditor's finding). The papers and schemas are the specification.
- `high_stakes` tier language updated from positional human-in-loop to the
  functional accountable-authority checkpoint (papers, The Normalized
  Boundary).
- Stale `skills/…` pointers and numbered float/definition citations in
  schema descriptions replaced with named paper anchors, which survive
  renumbering across paper revisions.
- Examples updated to 3.1: agent-operated manifest and hybrid-operated
  audit with checker independence, stratum documentation, receipts,
  injunction hooks, scale bounds, and a fully-open model exemplar
  (OLMo 2) consistent with the papers' training-forkability finding.
- Positional invariants enforced structurally (same day as the fields
  they tighten, before any external documents exist): agent- or
  hybrid-operated roles require `authority_grant_url` (a grant is an act,
  not an inference from persistence); agent- or hybrid-operated auditors
  require `checker_independence`, whose two axes (operator, substrate)
  are required within the block. Papers state checker independence
  universally; the schema enforces the declaration structurally where
  operation is agentic, and docs/llm-instructions.md states the universal
  duty for all auditors.

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
