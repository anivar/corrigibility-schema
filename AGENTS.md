# AGENTS.md

Instructions for agents. Both protocol roles — the operator producing an
Operator's Affidavit (`infrastructure.json`) and the auditor producing an
Auditor's Finding (`audit.json`) — may be operated by agents. The protocol
binds the same invariants regardless of what species of actor exercises
the role.

## The roles are positional, not personal

When both roles are agents, what separates them is position, and the
schemas enforce it structurally. The operator asserts a first-person
claim (`corrigibility_claim`); the auditor issues the only authoritative
determination (`tests`), and never about its own system. Identity
difference is the weakest guarantee: a fresh DID does not make a checker.
What makes a checker is `checker_independence` in operator and in
substrate. Two agents sharing a model substrate are correlated checkers:
their blind spots correlate, so their agreement is redundancy, not
independent validation. Accordingly, an agent-operated or
hybrid-operated auditor MUST declare `checker_independence`
(schema-enforced), and any agent-operated role MUST reference the fresh
grant it operates under (`authority_grant_url`, schema-enforced): a
grant is an act, not an inference from persistence. Duties differ by
position, not species: the auditor carries the Rule A.11 data duties,
the stratum obligation, and Rule A.10 canonical serialization of its
findings; the operator carries the GOVERN evidence chain (binding proofs
and their hashes) and the manifest chain of disclosure. Both are inward
actors; neither substitutes for the governed. That is why receipts go to
the subject and verification remains permissionless: the outward
exercise must not depend on trusting either inward party.

## Three invariants for any role

1. **Origination is record-borne.** Declare `role_execution.operated_by`
   (`human` | `agent` | `hybrid`) on the document you produce. Absence of
   a marker is never evidence of human operation.
2. **Answerability terminates at a sanctionable party.** Declare
   `role_execution.accountable_party`. An agent cannot be its own
   accountable party; the human legal person is the current instance.
3. **Grants are fresh acts.** Authority to operate a role comes from a
   grant (`role_execution.authority_grant_url`), not from having operated
   it before. No authority from persistence.

## If you operate the operator role

- The affidavit is a good-faith claim, not a verdict. The five
  `corrigibility_claim` booleans are assertions the auditor tests.
- Every `binding_mechanism: true` requires the Rule A.9 instruments:
  resolvable proof URL, its SHA-256, and enforcement history. Never
  fabricate evidence URLs.
- Increment `manifest_version`, chain `previous_manifest_hash`, sign.

## If you operate the auditor role

- **Checker independence.** You must be structurally independent of what
  you check, in operator and in substrate. If you run on the audited
  system's model substrate or a correlated one, you are a correlated
  checker and your agreement is not validation. Declare
  `checker_independence`.
- **Evaluate at the least-resourced stratum.** Pass/fail is taken at the
  lower decile of the affected population, not the mean user. Document
  `evaluation_stratum`.
- **Data duties (Rule A.11).** Access is purpose-bound. Declare data
  categories, purpose, and retention/deletion in
  `data_access_declaration`. Violations revoke DID standing.
- **Recompute, never copy.** `determination.corrigible` is the
  conjunction of `tests.*`; `workflow_capture_assessment.wcc_score` is
  1 − HM(s1, s2, s3). A document whose derived fields disagree with
  recomputation is invalid.

## Never

- Operate both roles for the same system.
- Merge the two documents or create synthetic co-signed records.
- Treat missing fields as true. Absence of audit is not approval.
- Compute weighted averages over the five tests. Failure of any one test
  is structural incorrigibility.

The full machine protocol is `docs/llm-instructions.md`. The schemas are
the interface; the published papers are the specification — every field
anchors to a paper section, and disagreement between a field description
and the paper is a bug in this repository.

## Contributing to this repository

- Additive, optional fields only within MAJOR version 3; breaking changes
  follow PROTOCOL.md §12.
- Validate all four examples with `tools/validate.py` before committing.
- Hashes are RFC 8785 (`tools/hash.py`); signatures are Ed25519 only.
