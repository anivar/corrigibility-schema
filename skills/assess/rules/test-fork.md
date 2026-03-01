---
title: FORK - Independent Reproduction
impact: CRITICAL
impactDescription: Selection pressure in feedback loop
tags: fork, reproduction, barriers, swapability, compute
---

# FORK Test

## Definition

FORK tests whether the system can be reproduced without permission from current steward.

The ultimate check on power is the ability to recreate it. Fork is credible replaceability in extremis—a threat, not a preference. Without fork, competition fails. A monopoly cannot be fixed from outside if no outside can exist.

## Exit vs Fork

| Action | Mechanism | Scope |
|--------|-----------|-------|
| EXIT | Choose between providers | Escape from operator |
| FORK | Reproduce infrastructure | Escape from architecture |

Choosing between AWS and Azure is EXIT. Reproducing the infrastructure itself is FORK. Substitution allows escape from operator; reproduction allows escape from architecture.

## Natural vs Constructed Barriers

| Type | Example | FORK Status |
|------|---------|-------------|
| Natural | Network effects, capital requirements | May reduce likelihood, does not fail test |
| Constructed | Legal prohibition, regulatory monopoly | Fails test |

FORK fails only when constructed barriers prevent reproduction. Bitcoin requires massive capital to fork effectively (natural barrier); does not fail FORK. Aadhaar cannot be legally replicated (constructed barrier); fails FORK.

## DPI Assessment

| Question | Evidence Required |
|----------|-------------------|
| Is forking legally permitted? | Legal analysis, regulatory framework |
| Are technical artifacts available? | Repository access, build documentation |
| Is data portable? | Data export mechanisms |
| Are there constructed monopolies? | Exclusive licenses, regulatory capture |

## EPI Extensions: Resource Barriers

For learned systems, resource barriers replace legal barriers:

| Layer | Cost | Barrier Type |
|-------|------|--------------|
| Inference code | Minimal | None |
| Running open weights | Low | Minor |
| Fine-tuning | Moderate | Economic |
| Retraining from scratch | Very high | Structural |

When compute costs are prohibitive, full FORK may be impossible. However, structural compute barriers differ from constructed legal barriers.

## Swapability as Practical FORK

When full compute parity is impossible, swapability provides functional equivalent:

**Swapability Test**: Can system swap to alternative model provider with:
- Zero downtime
- Under 60 minutes transition time
- No structural dependency on single vendor

Swapability satisfies FORK for EPI systems when:
1. Multiple alternative providers exist
2. Switching mechanism is tested and documented
3. No single vendor can create lock-in

## Pass/Fail Determination

**PASS if**:
- Forking legally permitted
- Technical artifacts available for reproduction
- For EPI: Swapability demonstrated or compute costs are natural (not constructed)

**FAIL if**:
- Legal barriers prevent reproduction
- Exclusive licenses create monopoly
- Regulatory capture blocks alternatives
- For EPI: Single vendor dependency with no swap path

## Common Failures

| System | FORK Status | Reason |
|--------|-------------|--------|
| Aadhaar | FAIL | Legal monopoly, UIDAI exclusive |
| UPI | Partial | NPCI exclusive but protocol open |
| Let's Encrypt | PASS | ACME protocol, Boulder CA open |
| Bitcoin | PASS | Full protocol reproduction possible |
| Linux | PASS | GPL ensures reproduction rights |

## Constructed vs Natural Analysis

When assessing barriers, distinguish:

**Constructed barriers** (fail FORK):
- Patents blocking implementation
- Exclusive government licenses
- Regulatory requirements that only incumbent can meet
- Trade secret protection of essential methods

**Natural barriers** (do not fail FORK):
- Capital requirements
- Network effects
- Technical complexity
- Talent scarcity

## Schema Fields

DPI infrastructure.json:
```json
"fork": {
  "legally_permitted": true,
  "artifacts_available": true,
  "data_portable": true,
  "constructed_barriers": [],
  "natural_barriers": []
}
```

EPI infrastructure.json:
```json
"fork": {
  "inference_forkable": true,
  "training_forkable": false,
  "constructed_barriers": [],
  "compute_capture_status": "none|moderate|captured"
},
"compute": {
  "inference_accessible": true,
  "training_accessible": false,
  "estimated_training_cost_usd": 50000000,
  "swap_time_minutes": 30,
  "alternative_vendors": ["vendor1", "vendor2"],
  "training_code_available": false,
  "data_manifest_available": false
}
```

DPI audit.json:
```json
"fork_verification": {
  "legally_permitted": true,
  "artifacts_verified": true,
  "data_portability_tested": true,
  "constructed_barriers_identified": [],
  "reproduction_attempted": true,
  "reproduction_successful": true
}
```

EPI audit.json:
```json
"fork_verification": {
  "inference_forkable": true,
  "training_forkable": false,
  "training_code_verified": true,
  "data_manifest_verified": true,
  "reproduction_attempted": true,
  "reproduction_successful": false,
  "swapability_tested": true,
  "swapability_passed": true
},
"compute_verification": {
  "inference_accessible": true,
  "training_accessible": false,
  "swap_tested": true,
  "swap_time_actual_minutes": 45,
  "compute_capture_assessed": true,
  "compute_capture_result": "captured"
}
```

Findings:
```json
{
  "test": "FORK",
  "finding": "...",
  "severity": "critical|major|minor|observation"
}
```
