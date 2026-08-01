# Corrigibility Schema Protocol

[![Release](https://img.shields.io/github/v/release/anivar/corrigibility-schema)](https://github.com/anivar/corrigibility-schema/releases/latest)
[![Protocol](https://img.shields.io/badge/Protocol-4.0-blue.svg)](PROTOCOL.md)
[![License: CC0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0009--8995--0005-green.svg)](https://orcid.org/0009-0009-8995-0005)

Machine-readable standards for evaluating whether public digital infrastructure can be corrected, contested, and controlled by the communities it serves.

## Downloads

| Asset | Description |
|-------|-------------|
| [dpi-infrastructure.json](https://github.com/anivar/corrigibility-schema/releases/latest/download/dpi-infrastructure.json) | DPI operator manifest |
| [dpi-audit.json](https://github.com/anivar/corrigibility-schema/releases/latest/download/dpi-audit.json) | DPI assessment |
| [epi-infrastructure.json](https://github.com/anivar/corrigibility-schema/releases/latest/download/epi-infrastructure.json) | EPI LWD-R manifest |
| [epi-audit.json](https://github.com/anivar/corrigibility-schema/releases/latest/download/epi-audit.json) | EPI assessment |

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

## For Agents

Both protocol roles may be operated by agents. [AGENTS.md](AGENTS.md)
states the invariants: record-borne origination (`role_execution`),
answerability terminating at a sanctionable party, fresh grants, and,
for auditors, checker independence in operator and in substrate.

The schemas are the interface; the papers are the specification.
[docs/failure-modes.md](docs/failure-modes.md) indexes common operator
evasion patterns against the tests they degrade and the fields that catch
them. Hand-written assessment rule files from the 3.0 era are preserved
under [archive/skills-v3-era/](archive/skills-v3-era/).

## Tiered Adoption (EPI)

| Tier | Use Case | Requirements |
|------|----------|--------------|
| **trivial** | Translation, summarization | Action boundaries, closed APIs permitted |
| **decision_support** | Search, RAG over govt data | Open weights, local data storage |
| **high_stakes** | Policing, welfare, courts | Full verified LWD-R, accountable-authority checkpoint |

## Tools

```bash
# Install runtime deps
pip install 'jsonschema[format]>=4.18' referencing jcs

# Validate a manifest (auto-detects DPI/EPI × infrastructure/audit)
python tools/validate.py path/to/infrastructure.json

# RFC 8785 SHA-256 hash for chaining/anchoring
python tools/hash.py path/to/infrastructure.json

# RFC 8785 canonical bytes for signing
python tools/canonicalize.py path/to/infrastructure.json
```

## Protocol Version

Current: **4.0** (structural repair, breaking; the 3.x line is archived under `archive/v3/` and remains validatable — see [CHANGELOG.md](CHANGELOG.md)).

Schemas anchor every field to a specific paper section. Canonicalisation is
**RFC 8785 (JCS)**, signatures are **Ed25519** over a W3C DID-resolved key,
and binding-authority claims (Rule A.9) are enforced structurally via JSON
Schema conditionals.

See [PROTOCOL.md](PROTOCOL.md) for versioning rules.

## Related

| Resource | Link |
|----------|------|
| Papers | [corrigibility-framework](https://github.com/anivar/corrigibility-framework/releases/latest) |
| Website | [anivar.net/corrigibility](https://anivar.net/corrigibility) |

## License

[CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) (Public Domain)

## Author

**Anivar A Aravind** · [ORCID: 0009-0009-8995-0005](https://orcid.org/0009-0009-8995-0005)
