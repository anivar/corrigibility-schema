---
title: AUDIT - Independent Verification
impact: CRITICAL
impactDescription: Sensor in feedback loop
tags: audit, verification, permissionless, tiers
---

# AUDIT Test

## Definition

AUDIT tests whether external, permissionless actors can verify system behavior.

While inspection (CODE) enables understanding, AUDIT enables truth. A system is verifiable only if independent actors can test its behavior, measure its error rates, and document its failure modes within production environments.

## Critical Distinction

AUDIT ≠ "everyone audits"
AUDIT = "no one can prevent auditing"

**Journalism analogy**: Not everyone investigates corruption. Democracy depends on the *possibility* of investigation. The problem is not that auditors exist; it's that operators can legally block them.

**Tradeoff**: Contestable expertise over unchallengeable authority.

## DPI Assessment

| Question | Evidence Required |
|----------|-------------------|
| Can independent parties audit without authorization? | Audit access policy |
| Are audit reports public? | Published audit reports |
| Is transaction-level verification possible? | Verification mechanisms |
| Can failure rates be independently measured? | Monitoring access |

## Verification Tiers

Depth of verification that external parties can achieve:

| Tier | Method | Strength | Example |
|------|--------|----------|---------|
| presence | Documentation exists | Weak | Audit policy published |
| behavior | Functionality tested | Medium | Red team exercises conducted |
| proof | Formal verification | Strong | Cryptographic proofs available |

## EPI Extensions

| Question | Evidence Required |
|----------|-------------------|
| Can researchers test model behavior at scale? | API access policy |
| Is drift monitoring externally accessible? | Monitoring endpoints |
| Are red-teaming results reproducible? | Methodology + data |
| Can bias assessments be independently verified? | Assessment methodology |

## Pass/Fail Determination

**PASS if**:
- Independent audit possible without operator permission
- Audit reports are public or can be published
- For EPI: External behavioral testing permitted

**FAIL if**:
- Audit requires operator authorization
- Audit scope restricted by operator
- For EPI: Independent adversarial testing blocked

## Capture Patterns

Incorrigible systems typically capture the audit function:

| System | Pattern | Result |
|--------|---------|--------|
| UPI | RBI can audit, but transaction verification requires NPCI | FAIL |
| Open-weights AI | Selective red-team publishing, blocked independent testing | FAIL |
| Bitcoin | Every transaction verifiable by any node | PASS |
| Let's Encrypt | Certificate Transparency logs public | PASS |

## Schema Fields

DPI audit.json:
```json
"verification_tier": "presence|behavior|proof",
"findings": [{
  "test": "AUDIT",
  "finding": "...",
  "severity": "critical|major|minor|observation"
}]
```

EPI audit.json:
```json
"lwd_r_verification": {
  "logic_verified": true,
  "weights_verified": true,
  "data_verified": true,
  "representation_verified": true,
  "lwd_r_complete": true
}
```
