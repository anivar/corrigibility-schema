---
name: corrigibility-assess
description: Evaluate digital and AI infrastructure against the five corrigibility tests (EXIT, CODE, AUDIT, GOVERN, FORK). Use when assessing DPI systems (identity, payments, registries) or EPI systems (AI/ML in public services) for structural corrigibility.
license: CC0
metadata:
  author: anivar
  version: "2.0.0"
---

# Corrigibility Assessment

Evaluate infrastructure against five structural tests derived from cybernetics (Ashby), commons governance (Ostrom), and free software (Stallman). A system is corrigible only if ALL five tests pass.

## When to Apply

Reference these guidelines when:
- Assessing DPI systems (identity, payments, data exchange, registries)
- Evaluating EPI systems (AI/ML in public services)
- Creating an `audit.json` assessment document
- Verifying operator claims in `infrastructure.json`
- Analyzing layer-by-layer corrigibility

## Rule Categories by Priority

| Priority | Category | Scope | Prefix |
|----------|----------|-------|--------|
| 1 | Core Tests | Both DPI/EPI | `test-` |
| 2 | Layer Analysis | Both DPI/EPI | `layer-` |
| 3 | EPI Extensions | EPI only | varies |

## Quick Reference

### 1. Core Tests (Both DPI and EPI)

- `test-exit` - Penalty severity, FEE (Functional Exit Equivalence), human fallback
- `test-code` - Source inspection, open license, LWD-R for EPI systems
- `test-audit` - Verification tiers (presence, behavior, proof), independent access
- `test-govern` - Grievance vs binding mechanisms, post-execution fallacy
- `test-fork` - Constructed vs natural barriers, swapability

### 2. Layer Analysis

- `layer-decomposition` - Propagation rule, weakest-layer principle

### 3. EPI Extensions

- `variety-drift` - Temporal drift Δ(t), revalidation threshold τ
- `action-boundary` - GDoS prevention, deterministic envelope

## The Five Tests

| Test | Question | Control Function |
|------|----------|------------------|
| EXIT | Can users leave without penalty? | Error Signal |
| CODE | Is source code inspectable? | Transmission Clarity |
| AUDIT | Can independents verify? | Sensor |
| GOVERN | Do communities have binding input? | Actuator |
| FORK | Can system be replicated? | Selection Pressure |

## Conjunctive Requirement

```
Corrigibility = EXIT ∧ CODE ∧ AUDIT ∧ GOVERN ∧ FORK
```

Failure of ANY test = Structurally Incorrigible

## EPI Tier Classification

| Tier | Use Cases | Requirements |
|------|-----------|--------------|
| `trivial` | Translation, summarization | Action boundaries |
| `decision_support` | RAG over government data | Open weights, local data |
| `high_stakes` | Welfare, policing, judicial | Full LWD-R, human-in-loop |

## Output Format

Assessment produces `audit.json` following Protocol 2.0:

```json
{
  "protocol_version": "2.0",
  "results": {
    "EXIT": true,
    "CODE": false,
    "AUDIT": true,
    "GOVERN": false,
    "FORK": false
  },
  "findings": [
    {
      "test": "CODE",
      "finding": "Implementation proprietary despite open spec",
      "severity": "critical"
    }
  ]
}
```

## How to Use

Read individual rule files for detailed evaluation criteria:

```
rules/test-exit.md
rules/test-code.md
rules/test-audit.md
rules/test-govern.md
rules/test-fork.md
rules/layer-decomposition.md
rules/variety-drift.md
rules/action-boundary.md
```

Each rule file contains:
- Theoretical foundation
- Schema fields to verify
- Pass/fail criteria
- DPI and EPI variations

## Full Reference

For complete expanded guide: `AGENTS.md`

## References

- Ashby, W.R. (1956). Introduction to Cybernetics
- Hirschman, A.O. (1970). Exit, Voice, and Loyalty
- Ostrom, E. (1990). Governing the Commons
- Aravind, A. (2025). Corrigibility Framework
