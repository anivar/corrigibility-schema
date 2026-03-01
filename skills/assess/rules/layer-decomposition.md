---
title: Layer Decomposition
impact: HIGH
impactDescription: Multi-layer test application
tags: layers, propagation, weakest-layer, decomposition
---

# Layer Decomposition

## Definition

Complex infrastructure stratifies into distinct functional layers. Tests must be applied to each layer separately.

## When to Decompose

Apply layer decomposition when:

1. Multiple functional layers exist (protocol, implementation, data, presentation)
2. Different operators control different layers
3. Mixed transparency (some layers open, some closed)
4. Mixed governance (different rules at different layers)

## The Propagation Rule

A system that passes a test at one layer but fails at another does not achieve "partial" compliance. It fails the test.

```
T_system = T(L₁) ∧ T(L₂) ∧ ... ∧ T(Lₙ)
```

Where T is any test, L₁...Lₙ are layers ordered by proximity to user impact.

**Evaluation Order**: Proceed from the layer closest to user impact upward. Failure at any layer propagates to the whole.

## The Weakest-Layer Principle

A system's corrigibility status equals its weakest layer across any test dimension.

Strength at one layer cannot compensate for failure at another.

## DPI Layer Types

| Layer Type | Examples | Common Issues |
|------------|----------|---------------|
| protocol | W3C DID, VC Data Model, NPCI specs | Often passes CODE |
| implementation | Resolver, wallet, switching logic | May fail CODE (proprietary) |
| operations | Registry, helpdesk, dispute | May fail GOVERN (operator-controlled) |
| data | User records, transaction logs | May fail EXIT (non-portable) |

## EPI Layer Types

| Layer Type | Examples | Common Issues |
|------------|----------|---------------|
| inference | Model execution, prediction | May fail CODE (opaque) |
| orchestration | Workflow engine, agent framework | May fail GOVERN (proprietary) |
| retrieval | RAG, vector stores | May fail EXIT (no opt-out) |
| training | Data pipeline, RLHF | May fail FORK (compute gated) |
| evaluation | Testing, drift monitoring | May fail AUDIT (operator-controlled) |
| action | Tool execution, API calls | Requires action boundaries |

## Application: UPI Example

UPI passes CODE at protocol layer (spec published) but fails CODE at implementation layer (NPCI switching logic closed). Since implementation is closer to user impact, system fails CODE.

| Layer | CODE Status | Reason |
|-------|-------------|--------|
| Protocol | PASS | NPCI publishes specifications |
| Implementation | FAIL | Switching logic proprietary |
| **System** | **FAIL** | Propagation rule applies |

## Application: Identity Infrastructure

| Layer | Typical Components | Failure Mode |
|-------|-------------------|--------------|
| Protocol | W3C DID, VC Data Model | Often passes CODE |
| Implementation | Specific resolver, wallet | May fail CODE (proprietary) |
| Operations | UIDAI registry, helpdesk | May fail GOVERN (self-regulated) |
| Data | Biometric DB, demographics | May fail EXIT (non-portable) |

## Full Corrigibility Determination

```
Corrigibility = ∧ᵢ ∧ⱼ T_j(L_i)
```

Where i indexes layers and j indexes tests. This double conjunction formalizes the "weakest link" principle.

## Assessment Questions

| Question | Evidence Required |
|----------|-------------------|
| What are the functional layers? | Architecture documentation |
| Who controls each layer? | Operator mapping |
| Which tests fail at which layer? | Per-layer test results |
| What is the closest layer to user impact? | Impact analysis |

## Schema Fields

DPI/EPI infrastructure.json:
```json
"layers": [{
  "layer_id": "switching",
  "layer_type": "implementation",
  "introduced_at": "2016-04-11",
  "spec_open": true,
  "implementation_open": false
}]
```

DPI/EPI audit.json:
```json
"layer_verification": {
  "switching": {
    "spec_verified": true,
    "implementation_verified": false,
    "gap_identified": true,
    "gap_description": "Switching logic proprietary despite open spec"
  }
}
```
