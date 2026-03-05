
# AIUC-1 Skills: Build & Distribution Plan

## Summary

Four role-based skills for AIUC-1 compliance. Each skill is a standalone Claude Agent Skills directory with its own `SKILL.md` and an embedded copy of the full AIUC-1 spec context as a reference file. Built to the `anthropics/skills` standard. Installable via git clone or the Claude plugin marketplace.

---

## Reference Architecture

Both `anthropics/skills` and `anthropics/financial-services-plugins` follow the same core pattern:

- A skill is a **directory** containing `SKILL.md` (YAML frontmatter + markdown body)
- Optional `references/` subdirectory for supporting context files
- No build step needed for the skill instructions — they're authored markdown
- A `marketplace.json` enables bulk installation from a marketplace command
- Installation: `claude plugin install <skill-name>@<repo>` or git clone a subdirectory

**Key distinction**: financial-services-plugins uses a _plugin_ wrapper (plugin.json manifest + `skills/` + `commands/` subdirs). The simpler `anthropics/skills` pattern treats each skill as its own installable unit with no wrapper. We'll follow the simpler pattern since we have no MCP connectors or slash commands (yet).

---

## Repository Layout (after implementation)

```
aiuc-1-context/
│
├── skills/                         # Authored skill templates (source of truth)
│   ├── aiuc-1-assessor/
│   │   └── SKILL.md
│   ├── aiuc-1-auditor/
│   │   └── SKILL.md
│   ├── aiuc-1-implementer/
│   │   └── SKILL.md
│   └── aiuc-1-advisor/
│       └── SKILL.md
│
├── dist/                           # Built output — committed, installable
│   ├── .claude-plugin/
│   │   └── marketplace.json        # Enables: claude plugin marketplace add ...
│   ├── aiuc-1-assessor/
│   │   ├── SKILL.md                # Copied from skills/
│   │   └── references/
│   │       └── aiuc-1-spec.md      # Injected from data/ai-context/aiuc-1-context-latest.md
│   ├── aiuc-1-auditor/
│   │   ├── SKILL.md
│   │   └── references/
│   │       └── aiuc-1-spec.md
│   ├── aiuc-1-implementer/
│   │   ├── SKILL.md
│   │   └── references/
│   │       └── aiuc-1-spec.md
│   └── aiuc-1-advisor/
│       ├── SKILL.md
│       └── references/
│           └── aiuc-1-spec.md
│
├── src/
│   ├── build_skills_dist.py        # NEW: replaces build_agent_skills.py
│   └── build_agent_skills.py       # REMOVED (replaced by build_skills_dist.py)
│
└── data/
    └── agent-skills/
        └── skill-library.md        # REMOVED (replaced by dist/)
```

---

## The Four Skills

### 1. `aiuc-1-assessor`

**Role:** Pre-certification readiness assessor
**Persona:** Expert AI compliance professional conducting a readiness review before formal certification
**When active:** User asks to assess an AI system, check compliance posture, or identify gaps against AIUC-1
**Core capabilities:**
- Run a full or scoped AIUC-1 readiness assessment across all 51 requirements
- Filter requirements by modality (text, voice, image, automation, etc.) using scoping rules
- Produce a gap analysis: Met / Partial / Unmet / N/A per requirement
- Generate prioritized remediation list with effort estimates
- Produce an evidence checklist of what artifacts are still needed
- Map findings to specific controls from the evidence-controls reference

---

### 2. `aiuc-1-auditor`

**Role:** Formal certification auditor
**Persona:** Accredited third-party auditor conducting a formal AIUC-1 certification audit
**When active:** User is conducting or preparing for a formal audit; verifying evidence against controls
**Core capabilities:**
- Verify evidence artifacts against specific control requirements
- Check compliance with mandatory review frequencies (quarterly vs. annual)
- Identify retired requirements (e.g., E007) that should be excluded
- Produce formal audit findings: conforming, non-conforming, observation
- Check crosswalk alignment (e.g., is this control satisfying the required EU AI Act article?)
- Draft audit opinion and certification recommendation

---

### 3. `aiuc-1-implementer`

**Role:** Engineering lead implementing AIUC-1 controls
**Persona:** Senior engineer tasked with building or remediating AI systems to meet AIUC-1
**When active:** User needs to implement a specific control, write code/config, or produce implementation artifacts
**Core capabilities:**
- Look up the Core (Shoulds) and Supplemental (Mays) implementation requirements per control
- Suggest concrete technical implementations (input filters, output monitoring, access controls, etc.)
- Help draft policies and documentation required as evidence
- Identify the correct evidence artifact type for each control
- Prioritize controls by frequency (quarterly first, then annual)
- Map controls to specific implementation patterns per domain

---

### 4. `aiuc-1-advisor`

**Role:** Strategic AI compliance advisor
**Persona:** Senior compliance consultant advising an organization on AI compliance strategy
**When active:** User needs strategic guidance on AIUC-1 adoption, vendor evaluation, or compliance planning
**Core capabilities:**
- Conduct a high-level gap analysis and produce a compliance roadmap
- Evaluate AI vendors against AIUC-1 requirements (generate vendor questionnaire)
- Map AIUC-1 requirements to other frameworks the org already operates (ISO 42001, SOC 2, GDPR)
- Advise on scoping decisions (which modalities/capabilities trigger which controls)
- Explain the business case for specific requirements
- Draft executive summaries of compliance posture

---

## `SKILL.md` Format

Each authored `SKILL.md` follows the Claude Agent Skills specification:

```markdown
---
name: AIUC-1 Assessor
description: Assess AI agent systems for readiness against the AIUC-1 security, safety, and reliability standard.
version: 1.0.0
---

[Full markdown body with role instructions, when to activate, step-by-step process,
output formats, and reference to references/aiuc-1-spec.md]
```

The YAML frontmatter fields are: `name`, `description`, `version`.
The body is freeform markdown — it's the actual instructions Claude follows when this skill is active.

---

## `dist/.claude-plugin/marketplace.json` Format

```json
{
  "name": "aiuc-1-skills",
  "description": "Role-based skills for AIUC-1 AI agent compliance: assessment, audit, implementation, and advisory.",
  "version": "1.0.0",
  "skills": [
    { "name": "aiuc-1-assessor",    "path": "aiuc-1-assessor",    "description": "Pre-certification readiness assessment" },
    { "name": "aiuc-1-auditor",     "path": "aiuc-1-auditor",     "description": "Formal certification audit" },
    { "name": "aiuc-1-implementer", "path": "aiuc-1-implementer", "description": "Control implementation guidance" },
    { "name": "aiuc-1-advisor",     "path": "aiuc-1-advisor",     "description": "Strategic compliance advisory" }
  ]
}
```

---

## `src/build_skills_dist.py` — Build Script

Replaces `src/build_agent_skills.py`. Responsibilities:

1. **Validate prerequisite**: Check that `data/ai-context/aiuc-1-context-latest.md` exists (run `build_ai_context.py` first if not).
2. **Clean `dist/`**: Remove and recreate `dist/` (except `.git` artifacts).
3. **For each skill in `skills/`**:
   a. Copy `skills/<name>/SKILL.md` → `dist/<name>/SKILL.md`
   b. Copy `data/ai-context/aiuc-1-context-latest.md` → `dist/<name>/references/aiuc-1-spec.md`
4. **Write `dist/.claude-plugin/marketplace.json`** from the known skill list.
5. **Print summary**: skill count, total size of dist/.

Usage: `uv run src/build_skills_dist.py`

---

## Installation Instructions (for dist/ README)

```bash
# Add this repo's dist/ as a marketplace source
claude plugin marketplace add joncutrer/aiuc-1-context/dist

# Install individual skills
claude plugin install aiuc-1-assessor@aiuc-1-skills
claude plugin install aiuc-1-auditor@aiuc-1-skills
claude plugin install aiuc-1-implementer@aiuc-1-skills
claude plugin install aiuc-1-advisor@aiuc-1-skills

# Or: clone a single skill directly
git clone --filter=blob:none --sparse https://github.com/joncutrer/aiuc-1-context.git
cd aiuc-1-context
git sparse-checkout set dist/aiuc-1-assessor
```

---

## Implementation Steps

1. Create `skills/aiuc-1-assessor/SKILL.md` — author full role instructions
2. Create `skills/aiuc-1-auditor/SKILL.md`
3. Create `skills/aiuc-1-implementer/SKILL.md`
4. Create `skills/aiuc-1-advisor/SKILL.md`
5. Create `src/build_skills_dist.py` — build script
6. Run `uv run src/build_ai_context.py && uv run src/build_skills_dist.py` — generate `dist/`
7. Delete `src/build_agent_skills.py` and `data/agent-skills/skill-library.md`
8. Update `src/run_periodic.py` — replace `build_agent_skills` call with `build_skills_dist`
9. Update `CLAUDE.md` — reflect new `skills/` and `dist/` structure, updated scripts table
10. Commit and push

---
