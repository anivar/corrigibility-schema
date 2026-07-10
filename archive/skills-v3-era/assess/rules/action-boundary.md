---
title: Action Boundary Protocol
impact: CRITICAL
impactDescription: Deterministic constraint on stochastic inference
tags: action-boundary, GDoS, agentic, deterministic, EPI
---

# Action Boundary Protocol

## Definition

The Action Boundary Protocol separates probabilistic inference from deterministic execution through enforceable validation layers.

**Principle**: If the state cannot govern the neural network's weights, it must govern the action boundary: the deterministic envelope that wraps stochastic inference.

## Why This Matters

In agentic systems, learned inference should not directly trigger irreversible action. Without action boundaries, agentic systems exercise unbounded epistemic power.

## Architectural Components

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   LLM/Model     │───►│ Action Proposal │───►│  Deterministic  │
│   Inference     │    │                 │    │   Validator     │
│  (Stochastic)   │    │                 │    │    (GOVERN)     │
└─────────────────┘    └─────────────────┘    └────────┬────────┘
                                                       │
                                              ┌────────┴────────┐
                                              │                 │
                                        ┌─────▼─────┐     ┌─────▼─────┐
                                        │  Execute  │     │  REJECT   │
                                        │           │     │  (Logged) │
                                        └───────────┘     └───────────┘
```

The vertical ACTION BOUNDARY separates the inference domain from the execution domain.

## Protocol Specification

1. **Hard-coded preconditions**: Actions validated before execution
2. **Deterministic tool execution**: Enforcement outside LLM context
3. **Explicit termination criteria**: Prevents Governance Denial of Service (GDoS)

## Governance Denial of Service (GDoS)

**Definition**: Governance capacity saturation under agentic scaling.

When autonomous agents encounter errors, they retry programmatically rather than waiting patiently. Governance mechanisms designed for human patience collapse under machine speed.

| Load Type | Response Pattern | Result |
|-----------|------------------|--------|
| Human users | Patient, accepts delays | Governance functions |
| AI agents | Retry loops, no patience | Governance collapses |

## The Human Friction Buffer

Incorrigible infrastructures may appear stable under human load because humans absorb friction through delay, compliance, and informal workaround.

Autonomous agents remove this buffering layer, exposing structural failures.

## Action Boundary Enforcement Mechanisms

| Mechanism | Description | Strength |
|-----------|-------------|----------|
| hard_coded | Constraints in execution environment | Strong |
| policy_engine | External policy evaluation | Medium |
| human_approval | Requires human sign-off | Strong (but slow) |
| hybrid | Combination of above | Variable |

## Assessment Questions

| Question | Evidence Required |
|----------|-------------------|
| Are action boundaries enforced? | Enforcement mechanism documentation |
| Is enforcement deterministic? | Execution environment specification |
| Can LLM bypass boundaries? | Prompt injection testing results |
| Are termination criteria explicit? | Termination policy |
| Is GDoS mitigated? | Rate limiting, queue management |

## Pass/Fail for Agentic Systems

**PASS if**:
- Action boundaries enforced deterministically
- Boundaries executed outside LLM context (not in system prompt)
- Termination criteria prevent infinite loops
- GDoS mitigation in place

**FAIL if**:
- Boundaries are advisory only
- Boundaries can be bypassed via prompt injection
- No termination criteria
- GDoS vulnerability exists

## Schema Fields

EPI infrastructure.json:
```json
"action_boundaries": {
  "enforced": true,
  "mechanism": "hard_coded",
  "permitted_actions": ["read", "summarize", "notify"],
  "prohibited_actions": ["delete", "modify_record", "financial_transfer"],
  "human_required_for": ["benefit_determination", "account_closure"],
  "boundary_spec_url": "https://example.gov/ai-boundaries"
}
```

EPI audit.json:
```json
"action_boundary_verification": {
  "enforced": true,
  "mechanism_verified": "hard_coded|policy_engine|human_approval|hybrid|none",
  "escapes_found": 0,
  "escapes_documented": true
}
```

Findings:
```json
{
  "test": "BOUNDARY",
  "finding": "...",
  "severity": "critical|major|minor|observation"
}
```

## Relationship to GOVERN Test

Action boundaries are the architectural instantiation of GOVERN for agentic systems:

| GOVERN Component | Action Boundary Equivalent |
|------------------|---------------------------|
| Binding constraint | Hard-coded boundary |
| Community representation | Permitted/prohibited lists |
| Override capacity | Human approval requirements |
| Enforcement | Deterministic validator |
