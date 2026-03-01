# Corrigibility Schema Protocol

Machine-readable standards for evaluating whether public digital infrastructure can be corrected, contested, and controlled by the communities it serves.

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

## Directory Structure

```
corrigibility-schema/
├── schema/
│   ├── dpi/
│   │   ├── infrastructure.json
│   │   └── audit.json
│   └── epi/
│       ├── infrastructure.json
│       └── audit.json
├── skills/
│   └── assess/                     # Assessment skill
│       ├── SKILL.md                # Main skill definition
│       └── rules/                  # Test-specific rules
│           ├── test-exit.md
│           ├── test-code.md
│           ├── test-audit.md
│           ├── test-govern.md
│           ├── test-fork.md
│           ├── layer-decomposition.md
│           ├── variety-drift.md
│           └── action-boundary.md
├── archive/
│   └── v1/                         # Historical schemas
├── examples/
│   ├── dpi/
│   └── epi/
├── tools/
│   ├── canonicalize.py
│   ├── hash.py
│   └── validate.py
├── docs/
│   └── llm-instructions.md
├── PROTOCOL.md
├── CHANGELOG.md
└── LICENSE
```

## Skills

Assessment skills for LLM-based evaluation following the [Agentic Skills](https://agenticskills.io) specification:

### assess/
Evaluate infrastructure against the five corrigibility tests. Includes:
- **Test rules**: EXIT, CODE, AUDIT, GOVERN, FORK
- **Analysis rules**: Layer decomposition, variety drift, action boundaries
- **Output**: `audit.json` following Protocol 2.0

Usage: Load `skills/assess/SKILL.md` into your LLM agent.

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

Requires: `pip install jsonschema`

## Protocol Version

Current: **2.0**

See [PROTOCOL.md](PROTOCOL.md) for versioning rules and governance.

## References

Aravind, A. (2025). *Corrigibility Framework for Digital Public Infrastructure*.
https://github.com/anivar/corrigibility-framework

Aravind, A. (2025). *Epistemic Public Infrastructure*.
https://github.com/anivar/corrigibility-framework

## License

- **Schemas**: CC0 (public domain)
- **Documentation**: CC BY-SA 4.0
- **Tools**: MIT

See [LICENSE](LICENSE) for details.
