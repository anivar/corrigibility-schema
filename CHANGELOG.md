# Changelog

All notable changes to the Corrigibility Schema Protocol.

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
