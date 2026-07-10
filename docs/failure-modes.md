# Failure Modes and the Fields That Catch Them

Common operator evasion patterns, the corrigibility tests they degrade,
what the papers require, and the schema fields that carry the requirement.
For auditors and automated evaluators; read with `docs/llm-instructions.md`
and `AGENTS.md`. Every mapping below is stated in the papers; this table
only indexes them against the protocol surface.

Determination reminders: pass/fail is taken at the least-resourced stratum
(`evaluation_stratum`), a test discharged only inward has been verified for
the operator, not the governed, and failure of any one test is structural
incorrigibility.

| Evasion pattern | Tests degraded | What the papers require | Schema fields |
|---|---|---|---|
| **DID-washing**: decentralized identifiers, centralized credential and reliance layers | FORK, GOVERN | Layer decomposition; the weakest layer binds; acceptance diversity prevents reliance-layer lock-in | `layers[]`, `layer_verification`, `exit.fee.mechanisms` (`multi_issuer_mandate`, `credential_acceptance_diversity`) |
| **Open weights, closed training**: inference weights released, data/pipeline/RL artifacts withheld | FORK, CODE | Training forkability, full provenance, joint forkability of compute and data | `lwd_r.data`, `compute.training_code_available`, `compute.data_manifest_available`, `fork.training_forkable`, audit `fork_verification`, `workflow_capture_assessment` |
| **Model-judging-model**: agent panels presented as governance | GOVERN | Stochastic redundancy is not validation; deterministic checks outside the shared substrate | `action_boundaries.mechanism`, `action_boundaries.executed_outside_llm_context`, auditor `checker_independence` |
| **Paper fallbacks** (the Bole evasion): statutory fallback guaranteed in law, inaccessible at the margin | EXIT | FEE verified by operative availability at the least-resourced stratum, evidenced by invocation records | `exit.fee` (incl. `funded_fallback_operations`), `exit.discharge_path`, audit `exit_verification.fee_satisfied` + `evaluation_stratum` |
| **Residue regeneration**: opt-out honored in session, authority regenerated from persistent memory | EXIT | Purge alone is not the test; resumption requires a fresh grant; nothing inferable from what persists | `exit.regeneration_resistant`, `renewal_requires_fresh_grant`, audit `exit_verification.regeneration_resistant_verified` |
| **Aggregate error masking**: healthy mean hides margin failure and intermediary capture | AUDIT | Distributions across strata, determination at the lower decile, per-node variance in the audit surface | `evaluation_stratum` (`distributions_reported`), `continuous_indicators`, `STRATUM` finding class |
| **Ontological drift**: operative R shifts faster than the community can contest it | CODE, GOVERN | Operative-R disclosure with enumerated deployment variables; R-layer change control with notice and suspensive effect | `lwd_r.representation.operative_r`, `lwd_r.representation.change_control`, audit `operative_r_reproduced`, `r_change_control_verified` |
| **Grievance without standing**: individual complaint channels, collective aggregation foreclosed | GOVERN | Collective-Standing Precondition: the right to organize, legally protected and historically exercised at the stratum | `governance.collective_standing`, audit `collective_standing_verified` + `collective_standing_constraint` |
| **Inward-only boundary**: validator enforces operator policy, logs to operator storage | GOVERN, AUDIT | The outward exercise: constraints the operator did not author, decisions verifiable from outside | `governance.citizen_constraint_registry`, `governance.injunction_hooks`, `subject_receipts`, audit `subject_receipt_verification` |
| **Governance denial of service**: fan-out and action rate outrun correction | GOVERN | Scale as a governed variable: fan-out, rate, and blast-radius bounds as first-class GOVERN instruments | `action_boundaries.scale_bounds`, `termination_criteria_explicit`, audit `gdos_mitigation_verified`, `scale_bounds_verified` |
| **Origination laundering**: agent operation of human-gated ceremonies passes as human | AUDIT, GOVERN | Origination is record-borne; absence of a marker is never evidence of human operation | `origination_marking`, `machine_verifiable_legitimacy`, audit `origination_marking_verified`, `ORIGINATION` finding class |
| **Open-washing** (general form): peripheral openness substituted for structural accountability | CODE | Visibility on the critical execution path, deterministic builds, deception detection | `code.public_loc_pct`, `code.build_reproducible`, audit `active_deception` |
