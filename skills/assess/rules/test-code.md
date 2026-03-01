---
title: CODE - Inspectability of Logic
impact: CRITICAL
impactDescription: Transmission clarity in feedback loop
tags: code, transparency, inspection, LWD-R, lessig
---

# CODE Test

## Definition

CODE tests whether the rules determining outcomes are visible to those they govern.

Power in a digital system resides in execution. Code determines what people can or cannot do in the first place (Lessig). This is regulation without appeal. If the execution path remains hidden, that power is absolute—not merely unaccountable but structurally unobservable.

## The Layer Problem

Open specs with closed implementation = unverifiable power.

| System | Spec Layer | Implementation Layer | Result |
|--------|------------|---------------------|--------|
| UPI | Open (API published) | Closed (NPCI switching) | FAIL |
| Aadhaar | Partial (APIs) | Closed (CIDR matching) | FAIL |
| Let's Encrypt | Open | Open (Boulder CA) | PASS |

Publishing specifications while retaining proprietary execution is spec-as-source: you can interface with the system but cannot understand why it produces specific outputs.

## DPI Assessment

| Question | Evidence Required |
|----------|-------------------|
| Is source code published? | Repository URL |
| Is license open? | License text (OSI-approved) |
| Are builds reproducible? | Build documentation |
| Is execution auditable? | Deployment verification |

## EPI Extensions: LWD-R

For learned systems, "source" is distributed across the training pipeline. Publishing inference code alone does not satisfy CODE.

| Layer | Artifact | Question | Evidence |
|-------|----------|----------|----------|
| Logic | Orchestration | Is inference pipeline inspectable? | Orchestration code/YAML |
| Weights | Parameters | Are weights publicly available? | Model repository |
| Data | Training corpus | Is provenance documented? | Data cards, lineage |
| Representation | Embeddings | Are category boundaries inspectable? | Bias assessments |

**LWD-R Complete**: CODE passes for EPI only if all four layers are transparent.

## Verification Levels

| Level | Method | Example |
|-------|--------|---------|
| presence | Documentation exists | README says "open source" |
| behavior | Verified accessible | Repository cloned and built |
| proof | Reproducible execution | Deterministic builds verified |

## Pass/Fail Determination

**PASS if**:
- Source code available under open license
- Builds are reproducible
- For EPI: All LWD-R layers documented

**FAIL if**:
- Core execution logic proprietary
- Open spec but closed implementation
- For EPI: Any LWD-R layer withheld

## Propagation Rule

If system has multiple layers, apply CODE to each. Failure at any layer fails the test.

Example layers for payment infrastructure:
1. Protocol specification
2. Switching implementation
3. Settlement logic
4. Dispute resolution

If layer 2 (switching) is closed, system fails CODE despite open layer 1 (protocol).

## Common Failures

| System | CODE Status | Reason |
|--------|-------------|--------|
| Aadhaar CIDR | FAIL | Matching algorithm proprietary |
| UPI | FAIL | NPCI switching closed |
| Let's Encrypt | PASS | Boulder CA fully open |
| Llama | Partial | Weights open, training data withheld |

## Schema Fields

DPI infrastructure.json:
```json
"layers": [{
  "layer_id": "...",
  "layer_type": "...",
  "spec_open": true,
  "implementation_open": true
}]
```

EPI infrastructure.json:
```json
"lwd_r": {
  "logic": {
    "inspectable": true,
    "orchestration_url": "..."
  },
  "weights": {
    "open": true,
    "model_id": "...",
    "license": "..."
  },
  "data": {
    "provenance_documented": true,
    "provenance_url": "..."
  },
  "representation": {
    "bias_assessed": true,
    "assessment_url": "..."
  }
}
```
