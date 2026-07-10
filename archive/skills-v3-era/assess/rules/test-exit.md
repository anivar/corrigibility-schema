---
title: EXIT - Reversibility of Participation
impact: CRITICAL
impactDescription: Error signal in feedback loop
tags: exit, participation, penalty, FEE, hirschman
---

# EXIT Test

## Definition

EXIT tests whether affected subjects can refuse participation without material penalty.

Irrevocable consent functions structurally as conscription. When a system becomes a prerequisite for existence, refusal acts as self-immolation rather than feedback.

## Theoretical Basis

**Hirschman (1970)**: Exit and voice exist in productive tension.

- Exit without voice → abandonment (users flee rather than fight)
- Voice without exit → capture (complaints lack credibility)
- Effectiveness of voice depends on credibility of exit

**Cybernetic Function**: EXIT constitutes the primary negative feedback loop. Blocking this channel silences the user's error signal. This blockade overloads the political layer with demands that the technical layer has suppressed.

## DPI Assessment

| Question | Evidence Required |
|----------|-------------------|
| Is enrollment mandatory by law? | Legal mandate documentation |
| Does functional offline alternative exist? | Alternative service channels |
| What happens if someone refuses? | Penalty documentation, ToS |

## Penalty Severity Classification

| Level | Definition | Example |
|-------|------------|---------|
| none | No consequence | Optional loyalty program |
| inconvenience | Minor friction | Office visit instead of online |
| economic | Financial impact | Higher fees, lost benefits |
| essential_service_denial | Survival impact | No banking, no ration, no healthcare |

## FEE (Functional Exit Equivalence)

When literal exit is impossible for essential services, FEE provides architectural guarantees:

1. **Federated providers**: Multiple independent operators
2. **Protocol-level portability**: Switch without data loss
3. **Statutory fallback**: Legal guarantee of non-digital alternative

FEE satisfies EXIT only if error-signal strength is equivalent to market exit.

## EPI Extensions

| Question | Evidence Required |
|----------|-------------------|
| Can citizens opt out of RAG/retrieval? | Opt-out mechanism documentation |
| Can citizens block inference on their data? | Inference blocking capability |
| Is human fallback guaranteed? | Human appeal process |
| Is there AI disclosure? | Disclosure policy |

## Pass/Fail Determination

**PASS if**:
- Voluntary enrollment AND no penalty for refusal
- OR mandatory BUT FEE exists with equivalent error-signal strength
- For EPI: Human fallback guaranteed

**FAIL if**:
- Mandatory + essential_service_denial + no FEE
- For EPI: No human fallback for consequential decisions

## Common Failures

| System | EXIT Status | Reason |
|--------|-------------|--------|
| Aadhaar | FAIL | Mandatory for PDS, banking, SIM |
| UPI | Partial | Voluntary but economic pressure |
| Let's Encrypt | PASS | Fully voluntary |
| Linux | PASS | No survival penalty |

## Schema Fields

DPI infrastructure.json:
```json
"exit": {
  "data_portability": true,
  "deletion_available": true,
  "alternative_exists": true,
  "penalty_free": true
}
```

EPI infrastructure.json:
```json
"exit": {
  "rag_opt_out": true,
  "inference_blocking": true,
  "deletion_procedure_url": "https://example.gov/ai-opt-out",
  "deletion_sla_days": 7
}
```

Audit findings:
```json
{
  "test": "EXIT",
  "finding": "...",
  "severity": "critical|major|minor|observation"
}
```
