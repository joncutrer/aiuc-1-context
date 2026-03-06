---
description: Get concrete implementation guidance for a specific AIUC-1 requirement. Returns Core (must) and Supplemental (recommended) steps, technical patterns, and evidence artifacts to produce.
argument-hint: "[requirement ID, e.g. B001 or C003]"
---

Get AIUC-1 implementation guidance using the implementer skill.

## Input

Parse `$ARGUMENTS` for a requirement ID (e.g., B001, C003, E015).

If not provided, ask: Which AIUC-1 requirement do you need to implement? (Provide the ID or describe the topic.)

## Workflow

Look up the requirement in `references/aiuc-1-spec.md` and extract:
- Full requirement text
- All controls under this requirement
- For each control: Core (Shoulds) and Supplemental (Mays) criteria
- Required evidence artifact type and what it must contain
- Review frequency (quarterly or annual)
- Applicable modalities/capabilities

Then produce practical implementation guidance:

1. **What this requirement means** — plain-language explanation of intent
2. **Core implementation** — the specific technical/process steps required to satisfy Core criteria (these are the minimum for conformance)
3. **Supplemental enhancements** — additional steps from the Mays criteria that strengthen the control
4. **Evidence to produce** — exactly what to document/generate, what it must contain, and how long to retain it
5. **Code/config patterns** — concrete technical implementation examples where applicable (input filters, output scanners, access controls, logging configs, policy templates, etc.)
6. **Review cadence** — when and how to re-evaluate this control

## Output Format

```
## Implementing [ID]: [Title]
Status: [Mandatory / Optional] | Frequency: [quarterly / annual]
Applies to: [modalities]

### What it means
[1-2 sentence plain-language explanation]

### Core implementation (required for conformance)
1. [Specific step derived from Core/Shoulds criteria]
2. ...

### Supplemental enhancements (recommended)
- [Step from Mays criteria]
- ...

### Evidence artifact
Type: [Documentation / Technical Config / Test Report / Log / etc.]
Must contain: [specific fields/sections required]
Retention: [duration]

### Implementation example
[Code snippet, config example, or policy template section]

### Review cadence
[What triggers a re-review and what the review must cover]
```
