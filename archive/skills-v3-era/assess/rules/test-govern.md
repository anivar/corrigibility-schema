---
title: GOVERN - Constitutive Constraint
impact: CRITICAL
impactDescription: Actuator in feedback loop
tags: govern, binding, grievance, ostrom
---

# GOVERN Test

## Definition

GOVERN tests whether binding constraints limit system behavior in ways the operator cannot override.

Governance exists only when affected populations have binding authority. This framework distinguishes structural governance from administrative functions like consultation, multi-stakeholder meetings, or feedback forms.

## Grievance Is Not Governance

Critical distinction between grievance and governance:

```
∂S/∂G = 0
```

Where S = system state, G = grievance input.

Grievance channels that record dissatisfaction without binding mechanisms to modify execution, policy, or eligibility logic do not constitute a feedback loop. They serve an aesthetic function—mimicking responsiveness while preserving controller rigidity.

Under Ashby's Law: if controller response variety does not increase in response to signal, regulation has failed.

## The Post-Execution Fallacy

| Mechanism | Timescale | Problem |
|-----------|-----------|---------|
| Courts | Months to years | Bureaucratic time |
| Ombudsmen | Weeks to months | Bureaucratic time |
| Grievance officers | Days to weeks | Bureaucratic time |
| Digital execution | Milliseconds | Digital time |

A system that executes harmful action (wrongful deletion, denial of service) and relies on court order to reverse it six months later is structurally ungoverned for that duration.

True governance must function within the system's execution loop to block prohibited states before they manifest.

## Assessment Questions

| Question | Evidence Required |
|----------|-------------------|
| Does governance body exist? | Charter, incorporation |
| Is authority binding on operator? | Legal instruments |
| Are affected communities represented? | Representation structure |
| Can governance override operator? | Decision records |
| Is there cryptographic chain of custody? | Signed authority chain |

## Binding vs Non-Binding

| Type | Example | GOVERN Status |
|------|---------|---------------|
| Advisory committee | Recommendations only | FAIL |
| Stakeholder forum | Consultation only | FAIL |
| Board with legal authority | Can modify policies | Requires verification |
| Community veto power | Can block changes | PASS |
| Cryptographic governance | On-chain voting | PASS |

## Pass/Fail Determination

**PASS if**:
- Governance body has binding legal authority
- Affected communities are represented
- Governance can override operator decisions
- Decisions enforceable within execution timeframe

**FAIL if**:
- Governance is advisory only
- Operator can ignore governance decisions
- No community representation
- Only post-hoc remedies available

## Common Failures

| System | Pattern | Result |
|--------|---------|--------|
| Aadhaar | UIDAI governs itself | FAIL |
| UPI | NPCI majority-owned by participating banks | Conflict of interest |
| Let's Encrypt | ISRG charter legally binding, community board | PASS |
| Bitcoin | BIP process with fork history | PASS |
| PostgreSQL | Contributor agreement prevents capture | PASS |

## Schema Fields

DPI/EPI infrastructure.json:
```json
"governance": {
  "grievance_channel": true,
  "binding_mechanism": true,
  "representation_body": "...",
  "governance_charter_url": "..."
}
```

DPI/EPI audit.json:
```json
"governance_verification": {
  "grievance_exists": true,
  "grievance_functional": true,
  "binding_mechanism_exists": true,
  "binding_mechanism_tested": true,
  "community_represented": true
}
```
