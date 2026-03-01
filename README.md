# Corrigibility Schema Protocol

Machine-readable standards for evaluating whether public digital infrastructure can be corrected, contested, and controlled by the communities it serves.

[![Release](https://img.shields.io/github/v/release/anivar/corrigibility-schema)](https://github.com/anivar/corrigibility-schema/releases/latest)

## Downloads

| Asset | Description |
|-------|-------------|
| [dpi-infrastructure.json](https://github.com/anivar/corrigibility-schema/releases/latest/download/dpi-infrastructure.json) | DPI operator manifest |
| [dpi-audit.json](https://github.com/anivar/corrigibility-schema/releases/latest/download/dpi-audit.json) | DPI assessment |
| [epi-infrastructure.json](https://github.com/anivar/corrigibility-schema/releases/latest/download/epi-infrastructure.json) | EPI LWD-R manifest |
| [epi-audit.json](https://github.com/anivar/corrigibility-schema/releases/latest/download/epi-audit.json) | EPI assessment |
| [skills-assess-v2.0.zip](https://github.com/anivar/corrigibility-schema/releases/latest/download/skills-assess-v2.0.zip) | Assessment skills |

## Overview

This protocol defines schemas for:
- **DPI** (Digital Public Infrastructure) — identity, payments, data systems
- **EPI** (Epistemic Public Infrastructure) — AI/ML systems in public services

Two independent documents per system:
1. `infrastructure.json` — Operator's declaration of system structure
2. `audit.json` — Independent auditor's verification

## The Five Tests

A system is **corrigible** only if it passes ALL five tests:

| Test | Question |
|------|----------|
| **EXIT** | Can users leave without penalty? |
| **CODE** | Is the source code inspectable? |
| **AUDIT** | Can independent parties verify claims? |
| **GOVERN** | Do affected communities have binding input? |
| **FORK** | Can the system be replicated independently? |

Failure of ANY test = **Structurally Incorrigible**

## Quick Start

### For Operators

1. Create `infrastructure.json` using schema
2. Declare your corrigibility claims
3. Sign with your organization's key
4. Publish at `/.well-known/corrigibility/infrastructure.json`

### For Auditors

1. Fetch and hash operator's manifest
2. Conduct independent verification
3. Create `audit.json` with results
4. Sign and publish

### For Evaluators

See [docs/llm-instructions.md](docs/llm-instructions.md) for machine reasoning protocol.

## Assessment Skills

Skills for LLM-based evaluation following the [Agentic Skills](https://agenticskills.io) specification.

| Skill | Purpose |
|-------|---------|
| [assess/SKILL.md](skills/assess/SKILL.md) | Evaluate infrastructure against five tests |
| [assess/rules/](skills/assess/rules/) | Test definitions: EXIT, CODE, AUDIT, GOVERN, FORK |

### Rules

| Rule | Description |
|------|-------------|
| `test-exit.md` | Reversibility of participation |
| `test-code.md` | Transmission clarity (LWD-R for EPI) |
| `test-audit.md` | Independent verification |
| `test-govern.md` | Constitutive constraint |
| `test-fork.md` | Independent reproduction |
| `layer-decomposition.md` | Multi-layer test application |
| `variety-drift.md` | Persistence condition monitoring |
| `action-boundary.md` | Deterministic envelope for agentic systems |

## Tiered Adoption (EPI)

| Tier | Use Case | Requirements |
|------|----------|--------------|
| **trivial** | Translation, summarization | Action boundaries, closed APIs permitted |
| **decision_support** | Search, RAG over govt data | Open weights, local data storage |
| **high_stakes** | Policing, welfare, courts | Full EPI compliance, human-in-loop |

## Tools

```bash
# Validate a manifest
python tools/validate.py path/to/infrastructure.json

# Generate hash for audit
python tools/hash.py path/to/infrastructure.json

# Canonicalize for signing
python tools/canonicalize.py path/to/infrastructure.json
```

## Protocol Version

Current: **2.0**

See [PROTOCOL.md](PROTOCOL.md) for versioning rules and [CHANGELOG.md](CHANGELOG.md) for history.

## Related

| Resource | Link |
|----------|------|
| Papers | [corrigibility-framework v2.0](https://github.com/anivar/corrigibility-framework/releases/tag/v2.0) |
| Website | [anivar.net/corrigibility](https://anivar.net/corrigibility) |

## License

[CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) (Public Domain)

## Author

**Anivar A Aravind** · [ORCID: 0009-0009-8995-0005](https://orcid.org/0009-0009-8995-0005)
