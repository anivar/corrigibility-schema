#!/usr/bin/env python3
"""
Regenerate the four shipped examples with real cryptography.

Keys are TEST KEYS derived from fixed public seeds so regeneration is
deterministic — they prove the signature pipeline, not anyone's identity.
Signatures are Ed25519 over the RFC 8785 canonicalization of the document
with its signature field removed; hashes are sha256 over the RFC 8785 bytes
of the complete signed document (Rule A.10).

Run:  uv run --with jcs --with cryptography python tools/gen-examples.py
"""

import base64
import hashlib
import json
from pathlib import Path

import jcs
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

ROOT = Path(__file__).resolve().parent.parent

OPERATOR_SEED = hashlib.sha256(b"corrigibility-protocol test operator key v4 - NOT A REAL IDENTITY").digest()
AUDITOR_SEED = hashlib.sha256(b"corrigibility-protocol test auditor key v4 - NOT A REAL IDENTITY").digest()

B58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


def b58encode(b: bytes) -> str:
    n = int.from_bytes(b, "big")
    out = ""
    while n:
        n, r = divmod(n, 58)
        out = B58[r] + out
    pad = len(b) - len(b.lstrip(b"\x00"))
    return "1" * pad + out


def keypair(seed: bytes):
    sk = Ed25519PrivateKey.from_private_bytes(seed)
    pub = sk.public_key().public_bytes_raw()
    multibase = "z" + b58encode(b"\xed\x01" + pub)
    return sk, multibase


def sign(doc: dict, sk: Ed25519PrivateKey, field: str, signed_at: str) -> dict:
    unsigned = {k: v for k, v in doc.items() if k != field}
    sig = sk.sign(jcs.canonicalize(unsigned))
    doc[field] = {
        "value": base64.urlsafe_b64encode(sig).decode().rstrip("="),
        "signed_at": signed_at,
    }
    return doc


def sha(doc: dict) -> str:
    return "sha256:" + hashlib.sha256(jcs.canonicalize(doc)).hexdigest()


def write(path: str, doc: dict) -> None:
    p = ROOT / path
    p.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {path}")


op_sk, op_pub = keypair(OPERATOR_SEED)
au_sk, au_pub = keypair(AUDITOR_SEED)

OPERATOR = {
    "entity": "Exemplar Registry Cooperative (fictional)",
    "jurisdiction": "IN",
    "identity_tier": 2,
    "verification_method": {
        "controller": "did:web:registry.example.org",
        "public_key_multibase": op_pub,
    },
    "contact_url": "https://registry.example.org/contact",
}
AUDITOR = {
    "entity": "Independent Assessments Collective (fictional)",
    "jurisdiction": "BR",
    "identity_tier": 2,
    "verification_method": {
        "controller": "did:web:audits.example.net",
        "public_key_multibase": au_pub,
    },
    "data_access_declaration": {
        "data_categories": ["published artifacts", "public endpoints"],
        "purpose": "Corrigibility assessment against Protocol 4.0",
        "individual_level_records": False,
        "retention_and_deletion": "No individual-level records obtained; working notes deleted at publication.",
    },
}

# ---- DPI: an open-commons registry that genuinely passes -------------------
dpi_manifest = {
    "protocol_version": "4.0",
    "system_id": "exemplar-civic-registry",
    "manifest_version": "1.0.0",
    "previous_manifest_hash": None,
    "timestamp": "2026-08-01T00:00:00Z",
    "operator": OPERATOR,
    "topology": "open_commons",
    "layers": [
        {"layer_id": "protocol", "layer_type": "protocol", "domain": "registry", "introduced_at": "2021-03-01", "spec_open": True, "implementation_open": True},
        {"layer_id": "service", "layer_type": "implementation", "domain": "registry", "introduced_at": "2021-06-01", "spec_open": True, "implementation_open": True},
    ],
    "code": {
        "source_available": True,
        "source_repository_url": "https://git.example.org/registry",
        "license_open": True,
        "license_id": "AGPL-3.0-only",
        "build_reproducible": True,
        "build_proof_url": "https://git.example.org/registry/releases/1.0.0/repro.txt",
        "decision_rule_legible": True,
    },
    "audit_surface": {
        "production_probeable": True,
        "logs_accessible": True,
        "third_party_testing_permitted": True,
        "error_rates_publishable": True,
        "test_rights_url": "https://registry.example.org/audit-rights",
    },
    "subject_receipts": {
        "issued": True,
        "inclusion_proof": True,
        "delivery_channel_independent": True,
        "machine_readable": True,
        "format_spec_url": "https://registry.example.org/receipts",
    },
    "exit": {
        "legal_barrier": False,
        "alternative_exists": True,
        "penalty_ratio": 1.0,
        "data_portability": True,
        "deletion_available": True,
        "discharge_path": "literal_exit",
        "exit_procedure_url": "https://registry.example.org/leave",
    },
    "governance": {
        "grievance_channel": True,
        "binding_mechanism": True,
        "binding_proof_url": "https://registry.example.org/charter-v3.pdf",
        "binding_proof_hash": "sha256:" + hashlib.sha256(b"exemplar charter v3 (fictional instrument bytes)").hexdigest(),
        "binding_proof_type": "charter",
        "enforcement_history_url": "https://registry.example.org/governance/rulings",
        "representation_body": "Member Assembly",
        "representation_charter_url": "https://registry.example.org/charter-v3.pdf",
        "collective_standing": {
            "legally_protected": True,
            "historically_exercised": True,
            "instrument_url": "https://registry.example.org/coop-statute",
        },
    },
    "fork": {
        "legally_permitted": True,
        "license_permissive": True,
        "artifacts_available": True,
        "constructed_barriers": [],
        "natural_barriers": ["member network effects"],
        "successful_forks": ["regional-registry-fork-2024"],
    },
    "corrigibility_claim": {"EXIT": True, "CODE": True, "AUDIT": True, "GOVERN": True, "FORK": True},
    "calibration_profile": {"id": "default-2026"},
}
sign(dpi_manifest, op_sk, "operator_signature", "2026-08-01T00:00:00Z")
dpi_manifest_hash = sha(dpi_manifest)
write("examples/dpi/infrastructure.example.json", dpi_manifest)

dpi_audit = {
    "protocol_version": "4.0",
    "system_id": "exemplar-civic-registry",
    "audit_id": "3e9a9c1e-1111-4222-8333-444455556666",
    "timestamp": "2026-08-02T00:00:00Z",
    "valid_until": "2027-08-01T00:00:00Z",
    "previous_audit_hash": None,
    "audited_manifest_version": "1.0.0",
    "audited_manifest_hash": dpi_manifest_hash,
    "verification_depth": "behavior",
    "tests": {"EXIT": "pass", "CODE": "pass", "AUDIT": "pass", "GOVERN": "pass", "FORK": "pass"},
    "determination": {"result": "corrigible", "computed_at": "2026-08-02T00:00:00Z"},
    "evaluation_stratum": {
        "stratum_description": "Rural members with intermittent connectivity and no smartphone",
        "identification_method": "Member survey p10 by connectivity and device access",
        "quantile": "p10",
        "distributions_reported": True,
    },
    "layer_verification": [
        {"layer_id": "protocol", "tests": {"CODE": "pass", "FORK": "pass"}},
        {"layer_id": "service", "tests": {"CODE": "pass", "AUDIT": "pass"}},
    ],
    "exit_verification": {
        "penalty_ratio_measured": 1.05,
        "alternative_tested": True,
        "discharge_path": "literal_exit",
    },
    "code_verification": {
        "source_repo_accessed": True,
        "license_validated": True,
        "build_reproduced": True,
        "build_proof_hash": "sha256:" + hashlib.sha256(b"reproducible build transcript (fictional)").hexdigest(),
        "decision_rule_legibility_verified": True,
    },
    "audit_verification": {
        "endpoints_probed": True,
        "logs_accessed": True,
        "third_party_publication_unrestricted": True,
        "permission_required_encountered": False,
    },
    "subject_receipt_verification": {
        "issued_verified": True,
        "inclusion_proof_verified": True,
        "independent_channel_verified": True,
    },
    "governance_verification": {
        "grievance_exists": True,
        "grievance_functional": True,
        "binding_mechanism_tested": True,
        "binding_proof_resolved": True,
        "binding_proof_hash_matched": True,
        "enforcement_history_verified": True,
        "collective_standing_verified": True,
    },
    "fork_verification": {
        "legally_permitted": True,
        "license_permissive": True,
        "artifacts_verified": True,
        "data_portability_tested": True,
        "constructed_barriers_identified": [],
        "reproduction_attempted": True,
        "reproduction_successful": True,
    },
    "findings": [
        {
            "test": "EXIT",
            "finding": "Exit procedure requires a paper form at two rural offices; measured penalty ratio 1.05 stays within profile threshold but the p10 stratum bears the travel cost.",
            "severity": "minor",
        }
    ],
    "auditor": AUDITOR,
    "calibration_profile": {"id": "default-2026"},
}
sign(dpi_audit, au_sk, "auditor_signature", "2026-08-02T00:00:00Z")
write("examples/dpi/audit.example.json", dpi_audit)

# ---- EPI: an API-deployed decision-support system, honestly mixed ----------
epi_manifest = {
    "protocol_version": "4.0",
    "system_id": "exemplar-benefits-triage-assistant",
    "manifest_version": "1.0.0",
    "previous_manifest_hash": None,
    "timestamp": "2026-08-01T00:00:00Z",
    "operator": {
        "entity": "Municipal Services Lab (fictional)",
        "jurisdiction": "KE",
        "identity_tier": 2,
        "verification_method": {
            "controller": "did:web:services.example.go.ke",
            "public_key_multibase": op_pub,
        },
    },
    "tier": "decision_support",
    "topology": "market_platform",
    "layers": [
        {"layer_id": "inference", "layer_type": "inference", "introduced_at": "2026-01-15", "spec_open": False, "implementation_open": False},
        {"layer_id": "orchestration", "layer_type": "orchestration", "introduced_at": "2026-01-15", "spec_open": True, "implementation_open": True},
        {"layer_id": "retrieval", "layer_type": "retrieval", "introduced_at": "2026-02-01", "spec_open": True, "implementation_open": True},
    ],
    "lwd_r": {
        "logic": {
            "attestor": "operator",
            "inspectable": True,
            "deterministic_envelope": True,
            "orchestration_url": "https://git.example.org/triage-orchestration",
        },
        "weights": {
            "attestor": "unattested",
            "open": False,
            "model_id": "vendor-frontier-model-2026-06",
            "notes": "API deployment; the vendor has not attested weights disclosure to us and we cannot see them.",
        },
        "data": {
            "attestor": "unattested",
            "provenance_documented": False,
            "local_storage": True,
            "rag_filtering": True,
            "notes": "Vendor training-data provenance is not disclosed to API customers; local RAG corpus is documented.",
        },
        "representation": {
            "attestor": "operator",
            "bias_assessed": True,
            "communities_consulted": ["disability advocates council", "informal workers union"],
            "assessment_url": "https://services.example.go.ke/triage/bias-assessment",
        },
    },
    "code": {
        "source_available": True,
        "source_repository_url": "https://git.example.org/triage-orchestration",
        "license_open": True,
        "license_id": "Apache-2.0",
        "build_reproducible": True,
        "build_proof_url": "https://git.example.org/triage-orchestration/repro",
        "decision_rule_legible": True,
    },
    "audit_surface": {
        "production_probeable": True,
        "logs_accessible": True,
        "third_party_testing_permitted": True,
        "error_rates_publishable": True,
    },
    "action_boundaries": {
        "enforced": True,
        "mechanism": "policy_engine",
        "executed_outside_llm_context": True,
        "termination_criteria_explicit": True,
        "permitted_actions": ["draft_recommendation", "request_document"],
        "prohibited_actions": ["final_determination", "payment_change"],
        "human_required_for": ["all determinations"],
        "boundary_spec_url": "https://services.example.go.ke/triage/boundary-spec",
        "enforcement_placement": "effect_surface",
        "specification_lifetime_days": 90,
        "renewal_requires_fresh_grant": True,
        "scale_bounds": {"fan_out_limit": 1, "action_rate_limit": 100, "enforced": True},
        "explicit_exception_pathways": True,
        "guaranteed_fallbacks": True,
        "fallback_spec_url": "https://services.example.go.ke/triage/fallbacks",
    },
    "machine_verifiable_legitimacy": {
        "authority_credentials_machine_interpretable": True,
        "revocation_propagation_observable": True,
        "execution_traces_tamper_evident": True,
        "incident_mitigation_automated": False,
    },
    "origination_marking": {
        "records_operator_kind": True,
        "positive_signed_marker_required": True,
        "marker_narrows_authority_only": True,
    },
    "subject_receipts": {
        "issued": True,
        "inclusion_proof": False,
        "delivery_channel_independent": False,
        "machine_readable": True,
        "notes": "Receipts issue from the same logging stack; independent-channel delivery is on the roadmap, so the field says false.",
    },
    "compute": {
        "inference_accessible": True,
        "training_accessible": False,
        "estimated_inference_cost_usd": 25000,
        "swap_time_minutes": 2880,
        "alternative_vendors": ["second-frontier-vendor", "open-weights-provider"],
        "training_code_available": False,
        "data_manifest_available": False,
        "notes": "Training cost unknown to us; vendor does not disclose.",
    },
    "data": {
        "training_corpus_reproducible": False,
        "public_substitute_equivalence_auditable": False,
        "upstream_dependencies": {
            "synthetic_data_from_proprietary_models": True,
            "distilled_outputs_from_closed_apis": True,
            "proprietary_evaluation_sets": True,
            "rlhf_traces_or_preference_data_undisclosed": True,
            "reward_models_unavailable": True,
            "tokenizer_or_filter_rules_undisclosed": True,
        },
    },
    "revalidation": {
        "monitoring_enabled": True,
        "monitoring_frequency": "monthly",
        "drift_threshold": 0.15,
        "last_revalidation": "2026-07-01",
    },
    "exit": {
        "rag_opt_out": True,
        "regeneration_resistant": False,
        "discharge_path": "literal_exit",
        "deletion_procedure_url": "https://services.example.go.ke/triage/deletion",
        "deletion_sla_days": 30,
        "notes": "Local RAG deletion is verified; we cannot warrant vendor-side regeneration resistance, so the field says false.",
    },
    "governance": {
        "grievance_channel": True,
        "binding_mechanism": True,
        "binding_proof_url": "https://services.example.go.ke/ordinance-2026-14.pdf",
        "binding_proof_hash": "sha256:" + hashlib.sha256(b"municipal ordinance 2026-14 (fictional instrument bytes)").hexdigest(),
        "binding_proof_type": "regulation",
        "enforcement_history_url": "https://services.example.go.ke/oversight/rulings",
        "collective_standing": {"legally_protected": True, "historically_exercised": False},
    },
    "fork": {
        "inference_forkable": True,
        "training_forkable": False,
        "license_permissive": False,
        "constructed_barriers": ["vendor API terms prohibit output distillation"],
        "governance_artifacts": {
            "eval_suites_available": True,
            "red_team_scenarios_available": False,
            "failure_registry_available": True,
            "incident_logs_available": False,
            "harness_docs_available": True,
            "artifacts_url": "https://services.example.go.ke/triage/artifacts",
        },
    },
    "corrigibility_claim": {"EXIT": False, "CODE": False, "AUDIT": True, "GOVERN": True, "FORK": False},
    "calibration_profile": {"id": "default-2026"},
}
sign(epi_manifest, op_sk, "operator_signature", "2026-08-01T00:00:00Z")
epi_manifest_hash = sha(epi_manifest)
write("examples/epi/infrastructure.example.json", epi_manifest)

epi_audit = {
    "protocol_version": "4.0",
    "system_id": "exemplar-benefits-triage-assistant",
    "audit_id": "7b1d2f3a-8888-4999-a000-bbbbccccdddd",
    "timestamp": "2026-08-03T00:00:00Z",
    "valid_until": "2027-02-01T00:00:00Z",
    "previous_audit_hash": None,
    "audited_manifest_version": "1.0.0",
    "audited_manifest_hash": epi_manifest_hash,
    "verification_depth": "behavior",
    "tests": {"EXIT": "fail", "CODE": "fail", "AUDIT": "pass", "GOVERN": "pass", "FORK": "fail"},
    "determination": {"result": "not_corrigible", "computed_at": "2026-08-03T00:00:00Z"},
    "tier_appropriate": True,
    "evaluation_stratum": {
        "stratum_description": "Applicants filing through assisted kiosks in low-connectivity wards",
        "identification_method": "Ward-level service statistics, lower decile by completion rate",
        "quantile": "p10",
        "distributions_reported": True,
    },
    "lwd_r_verification": {
        "logic_verified": True,
        "weights_verified": False,
        "data_verified": False,
        "representation_verified": True,
        "operative_r_reproduced": False,
        "notes": "Weights and data pillars are unattested by declaration; nothing to verify against.",
    },
    "action_boundary_verification": {
        "enforced": True,
        "mechanism_verified": "policy_engine",
        "executed_outside_llm_context_verified": True,
        "prompt_injection_tested": True,
        "escapes_found": 0,
        "gdos_mitigation_verified": True,
        "enforcement_placement_verified": True,
        "specification_lifetime_verified": True,
        "accountable_authority_verified": True,
        "scale_bounds_verified": True,
        "exception_pathways_verified": True,
        "origination_marking_verified": True,
    },
    "legitimacy_verification": {
        "authority_credentials_verified": True,
        "revocation_propagation_verified": True,
        "traces_tamper_evident_verified": True,
        "incident_mitigation_verified": False,
    },
    "audit_verification": {
        "endpoints_probed": True,
        "logs_accessed": True,
        "third_party_publication_unrestricted": True,
        "permission_required_encountered": False,
    },
    "subject_receipt_verification": {
        "issued_verified": True,
        "inclusion_proof_verified": False,
        "independent_channel_verified": False,
    },
    "drift_assessment": {
        "measured": True,
        "methodology_url": "https://audits.example.net/methods/drift-2026",
        "baseline_date": "2026-02-01",
        "trend": "increasing",
        "revalidation_triggered": False,
    },
    "compute_verification": {
        "inference_access_verified": True,
        "training_access_verified": False,
        "swap_tested": True,
        "swap_time_actual_minutes": 4320,
        "compute_captured": True,
        "training_cost_to_community_ratio": 40.0,
        "notes": "Vendor training cost estimated from public filings; ratio computed under default-2026 kappa.",
    },
    "data_verification": {
        "corpus_reproducibility_verified": False,
        "required_to_accessible_ratio": 12.0,
        "substitute_equivalence_verified": False,
        "data_captured": True,
    },
    "workflow_capture_assessment": {
        "s1_workflow_reproducibility": 0.7,
        "s2_ontological_substitutability": 0.4,
        "s3_model_portability": 0.5,
        "methodology_url": "https://audits.example.net/methods/wcc-2026",
    },
    "fork_verification": {
        "training_code_verified": False,
        "data_manifest_verified": False,
        "reproduction_attempted": False,
        "reproduction_successful": False,
        "notes": "Reproduction not attempted: both capture axes already established against the profile constants.",
    },
    "fork_viability": "not_reproducible",
    "exit_verification": {
        "rag_opt_out_tested": True,
        "rag_opt_out_honored": True,
        "regeneration_resistant_verified": False,
        "discharge_path": "literal_exit",
    },
    "governance_verification": {
        "grievance_exists": True,
        "grievance_functional": True,
        "binding_mechanism_tested": True,
        "binding_proof_resolved": True,
        "binding_proof_hash_matched": True,
        "enforcement_history_verified": True,
        "collective_standing_verified": False,
        "collective_standing_constraint": "No documented exercise of collective standing by the affected applicant class within the audit window.",
        "citizen_constraint_registry_verified": False,
        "injunction_hook_tested": False,
    },
    "findings": [
        {"test": "CODE", "finding": "Weights and data pillars unattested under API deployment; LWD-R cannot complete from the operator seat.", "severity": "critical"},
        {"test": "DATA", "finding": "All six §5.2 upstream dependencies present and non-reproducible; data capture established at ratio 12.0 under default-2026.", "severity": "critical"},
        {"test": "COMPUTE", "finding": "Training inaccessible; cost-to-community ratio 40.0 under default-2026 kappa.", "severity": "critical"},
        {"test": "EXIT", "finding": "Vendor-side regeneration resistance unverifiable; local RAG opt-out honored.", "severity": "major"},
        {"test": "GOVERN", "finding": "Binding ordinance verified with enforcement history; collective standing not exercised within the window — recorded as the stratum constraint, not a GOVERN failure.", "severity": "observation"},
    ],
    "auditor": AUDITOR,
    "calibration_profile": {"id": "default-2026"},
}
sign(epi_audit, au_sk, "auditor_signature", "2026-08-03T00:00:00Z")
write("examples/epi/audit.example.json", epi_audit)

print("\nverify: signatures + hashes")
for name, doc, pub in [("dpi manifest", dpi_manifest, op_pub), ("dpi audit", dpi_audit, au_pub), ("epi manifest", epi_manifest, op_pub), ("epi audit", epi_audit, au_pub)]:
    print(f"  {name}: signed, hash {sha(doc)[:20]}…")
