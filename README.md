# aiuc-1-context

A repository that systematically fetches, archives, tracks, and analyzes the **AIUC-1 standard** — and distributes role-based Claude Agent Skills for working with it.

## What is AIUC-1?

[AIUC-1](https://www.aiuc-1.com/) (AI Use Case standard 1) is the world's first security, safety, and reliability standard designed specifically for AI agents. Developed with 100+ Fortune 500 CISOs, it covers 51 requirements across six domains:

| Domain | Description |
|--------|-------------|
| **A. Data & Privacy** | Input/output data policies, PII protection, IP safeguards |
| **B. Security** | Adversarial robustness, access controls, endpoint protection |
| **C. Safety** | Harmful output prevention, pre-deployment testing, monitoring |
| **D. Reliability** | Hallucination prevention, safe tool calls |
| **E. Accountability** | Failure plans, vendor due diligence, logging, transparency |
| **F. Society** | Cyber misuse prevention, catastrophic risk controls |

The standard maps to: ISO 42001 · MITRE ATLAS · EU AI Act · NIST AI RMF · OWASP Top Ten · CSA AICM

---

## Claude Agent Skills

This repo ships four installable Claude Agent Skills for AIUC-1 compliance work. Each skill gives Claude a specialized role and embeds the full AIUC-1 spec as a reference document.

### Install

```bash
# Add this repo's dist/ as a marketplace source
claude plugin marketplace add joncutrer/aiuc-1-context/dist

# Install the skills you need
claude plugin install aiuc-1-assessor@aiuc-1-skills
claude plugin install aiuc-1-auditor@aiuc-1-skills
claude plugin install aiuc-1-implementer@aiuc-1-skills
claude plugin install aiuc-1-advisor@aiuc-1-skills
```

### Skills overview

#### `aiuc-1-assessor` — Readiness Assessment
Pre-certification gap analysis. Evaluates an AI system against all applicable AIUC-1 requirements and produces a prioritized remediation plan.

| Command | Description |
|---------|-------------|
| `/assess` | Full readiness assessment with gap analysis |
| `/scope` | Determine which requirements apply to your system |
| `/evidence-checklist` | Generate a checklist of required evidence artifacts |

#### `aiuc-1-auditor` — Formal Certification Audit
Conducts formal AIUC-1 audits. Verifies evidence artifacts against controls, checks review frequency compliance, and produces structured findings with a certification recommendation.

| Command | Description |
|---------|-------------|
| `/audit` | Formal audit report with certification recommendation |
| `/verify` | Verify a specific evidence artifact against a control |

#### `aiuc-1-implementer` — Control Implementation
Engineering-focused guidance for building AIUC-1 controls. Provides concrete technical patterns, policy templates, and evidence artifact generation.

| Command | Description |
|---------|-------------|
| `/implement` | Implementation guidance for a specific requirement (by ID) |
| `/draft-policy` | Draft a policy document that satisfies one or more requirements |

#### `aiuc-1-advisor` — Strategic Advisory
Strategic compliance consulting. Produces roadmaps, vendor questionnaires, framework crosswalk mappings, and executive briefings.

| Command | Description |
|---------|-------------|
| `/roadmap` | Phased compliance roadmap (0–90 days, 90–180 days, ongoing) |
| `/vendor-questionnaire` | Vendor assessment questionnaire based on AIUC-1 requirements |
| `/crosswalk` | Map AIUC-1 to ISO 42001, EU AI Act, NIST AI RMF, MITRE ATLAS, etc. |
| `/exec-briefing` | Executive compliance briefing (leadership, customer, or regulatory) |

---

## Repository Structure

```
aiuc-1-context/
├── skills/                    # Authored skill source files (edit these)
│   ├── aiuc-1-assessor/
│   │   ├── SKILL.md
│   │   └── commands/
│   ├── aiuc-1-auditor/       (same structure)
│   ├── aiuc-1-implementer/   (same structure)
│   └── aiuc-1-advisor/       (same structure)
│
├── dist/                      # Built output — commit and distribute from here
│   ├── .claude-plugin/
│   │   └── marketplace.json
│   └── aiuc-1-{assessor,auditor,implementer,advisor}/
│       ├── SKILL.md
│       ├── commands/
│       └── references/
│           └── aiuc-1-spec.md
│
├── src/                       # Automation scripts
│   ├── fetch_spec.py          # Fetch a quarterly spec version from aiuc-1.com
│   ├── diff_specs.py          # Compare two spec versions
│   ├── fetch_news.py          # Harvest news/research articles
│   ├── build_ai_context.py    # Compile all spec data into AI-optimized context
│   ├── build_skills_dist.py   # Assemble skills bundle into dist/
│   └── run_periodic.py        # Orchestrate all tasks in order
│
└── data/
    ├── spec-versions/         # Raw spec snapshots (one folder per quarter)
    ├── changelog/             # Per-quarter changelogs
    ├── spec-diffs/            # Structured diffs between releases
    ├── ai-context/            # AI-optimized single source of truth
    └── news/                  # Monthly news/research digests
```

---

## Running the Pipeline

**Prerequisites:** Python 3.11+ and [uv](https://docs.astral.sh/uv/)

```bash
# Install dependencies
uv sync

# Run everything (fetch → diff → build context → build skills)
uv run src/run_periodic.py

# Or run individual steps
uv run src/fetch_spec.py 2026-Q1      # Fetch a specific spec version
uv run src/build_ai_context.py        # Rebuild the AI context doc
uv run src/build_skills_dist.py       # Rebuild dist/ from skills/
uv run src/fetch_news.py              # Harvest latest news articles
uv run src/diff_specs.py 2025-Q1 2026-Q1  # Diff two versions
```

**Typical cadence:**
- Run `run_periodic.py` quarterly when a new AIUC-1 release is announced
- Run `fetch_news.py` monthly to keep news digests current

---

## Customizing the Skills

1. Edit the source files in `skills/<skill-name>/SKILL.md` or `skills/<skill-name>/commands/<command>.md`
2. Rebuild: `uv run src/build_skills_dist.py`
3. The updated `dist/` is ready to install from

> **Never hand-edit files in `dist/`** — they are always overwritten by the build script.

---

## How It Works

```
aiuc-1.com  →  fetch_spec.py  →  data/spec-versions/YYYY-QN/
                                          ↓
                              build_ai_context.py  →  data/ai-context/aiuc-1-context-latest.md
                                          ↓
                              build_skills_dist.py  →  dist/aiuc-1-*/
                                                            ├── SKILL.md  (from skills/)
                                                            ├── commands/ (from skills/)
                                                            └── references/aiuc-1-spec.md  (injected)
```

The AI context document (`aiuc-1-context-latest.md`) is LLM-optimized: nav menus, marketing content, and duplicate text are stripped. It contains a requirements table with keywords, controls & evidence, domain descriptions, and framework crosswalk content — all in a single dense document.

---

## License

Apache 2.0
