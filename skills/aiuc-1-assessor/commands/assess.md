---
description: Run a full AIUC-1 readiness assessment. Scopes applicable requirements, evaluates compliance posture, and produces a gap analysis with prioritized remediation steps.
argument-hint: "[system description or 'help' for guidance]"
---

Run a complete AIUC-1 readiness assessment using the assessor skill.

## Input

Parse `$ARGUMENTS` for:
- A description of the AI system being assessed (modalities, internal vs external, custom vs third-party)
- Optional: a specific domain to scope to (e.g. "security only" or "domain B")

If `$ARGUMENTS` is empty or "help", ask:
1. What does the AI system do? (brief description)
2. What modalities does it use? (text generation, voice, image, automation/agentic, files, code)
3. Is it internal-facing or external-facing?

## Workflow

1. **Scope** — Identify which of the 51 requirements apply based on the system's modalities and deployment context. State the count: "X of 51 requirements are in scope."

2. **Assess** — For each applicable requirement, ask the user (or infer from provided documentation) whether the control is implemented. Classify each as: Met / Partial / Unmet / N/A.

3. **Gap analysis** — Produce a table:
   | ID | Title | Status | Gap |
   |----|-------|--------|-----|

4. **Summary** — X Met, Y Partial, Z Unmet. List all Mandatory blockers first.

5. **Remediation priorities** — Ordered list: Mandatory quarterly gaps first, then Mandatory annual, then Optional. 1–3 sentence fix for each.

6. **Evidence checklist** — For each Unmet/Partial, list the specific artifacts still needed formatted as `- [ ] ID — artifact`.

Reference `references/aiuc-1-spec.md` for requirement details, controls, and evidence guidance.
