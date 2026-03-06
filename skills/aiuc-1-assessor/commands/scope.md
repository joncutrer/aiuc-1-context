---
description: Determine which AIUC-1 requirements apply to a specific AI system based on its modalities, deployment context, and capabilities.
argument-hint: "[system description]"
---

Determine the AIUC-1 scope for an AI system using the assessor skill.

## Input

Parse `$ARGUMENTS` for a description of the AI system. If missing, ask:
1. What modalities does the system use? (text generation, voice generation, image generation, automation/agentic tool use, file processing, code generation)
2. Is it internal-facing (employees only) or external-facing (end users/customers)?
3. Is it a third-party AI product or custom-built?

## Workflow

Apply scoping rules from `references/aiuc-1-spec.md`:

- **Universal** (35 requirements) — Always in scope regardless of modality
- **Automation** — In scope if the system executes tool calls, API calls, or agentic workflows (adds B006, D003, D004)
- **Text-generation** — In scope if the system generates text output (adds B005, B009, C003, C004, C010, C011, and others)
- **Voice-generation** — In scope if the system generates voice/audio (adds B005, B009, C003, C004, C010)
- **Image-generation** — In scope if the system generates images (adds A007, C003, C010)
- **External-facing** — In scope if end users interact directly (adds A007 and others)

## Output

Produce a scoping summary:

```
## AIUC-1 Scope — [System Name]

Modalities in scope: [list]
Deployment: [internal / external]

Total requirements in scope: X of 51
  Mandatory: Y
  Optional: Z

### In-Scope Requirements by Domain
| Domain | Mandatory | Optional | Requirements |
|--------|-----------|----------|--------------|
| A. Data & Privacy | X | Y | A001, A002, ... |
...

### Out-of-Scope Requirements
[list with reason why each is excluded]
```
