# Changelog

All notable changes to the Corrigibility Schema Protocol.

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
