---
description: Generate an AIUC-1 vendor assessment questionnaire. Produces a structured set of questions and required evidence items for evaluating an AI vendor's compliance posture.
argument-hint: "[vendor name or type of AI system]"
---

Generate an AIUC-1 vendor assessment questionnaire using the advisor skill.

## Input

Parse `$ARGUMENTS` for:
- Vendor name or type of AI system being evaluated
- Optional: specific domains to focus on (default: all)
- Optional: modalities in scope for this vendor

If not provided, ask:
1. What type of AI system are you evaluating? (e.g., LLM API, AI agent platform, voice AI)
2. Which modalities does it use?
3. Is this an external-facing product or internal tool?

## Workflow

For each in-scope Mandatory requirement (and key Optional ones), produce a question + evidence requirement. Reference `references/aiuc-1-spec.md` for the specific evidence types each control requires.

Group questions by domain. Include a cover sheet with scoring rubric.

## Output

```markdown
# AIUC-1 Vendor Assessment Questionnaire

**Vendor:** [VENDOR NAME]
**Assessed by:** [ORGANIZATION]
**Date:** [DATE]
**AIUC-1 version:** 2026-Q1

## Scoring rubric
- **Fully meets** — Evidence provided satisfies the requirement
- **Partially meets** — Some evidence provided; gaps identified
- **Does not meet** — No evidence or material gaps
- **Not applicable** — Requirement does not apply to this system

---

## A. Data & Privacy

**A001 — Input data policy** *(Mandatory)*
Q: Does your platform have a published policy governing how customer data submitted to your AI system is used for model training, inference processing, and retention?
Evidence required: Link to Terms of Service, Privacy Policy, or Data Processing Agreement.
Finding: [ ] Fully meets [ ] Partially meets [ ] Does not meet [ ] N/A
Notes: ___

**A002 — Output data policy** *(Mandatory)*
Q: Do you clearly communicate AI output ownership, usage rights, and customer deletion/opt-out rights?
Evidence required: ToS or DPA section covering output rights.
Finding: [ ] Fully meets [ ] Partially meets [ ] Does not meet [ ] N/A
Notes: ___

[Continue for all applicable requirements through F]

---

## Summary Scorecard

| Domain | Mandatory met | Mandatory gaps | Optional met | Notes |
|--------|--------------|----------------|--------------|-------|
| A. Data & Privacy | / | | / | |
...

**Overall assessment:** [ ] Approved [ ] Approved with conditions [ ] Not approved
**Conditions / required remediation:** ___
```
