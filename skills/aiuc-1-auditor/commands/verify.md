---
description: Verify whether a specific evidence artifact satisfies an AIUC-1 control. Returns a conformance classification and identifies any gaps.
argument-hint: "[requirement ID, e.g. B001] [description of evidence]"
---

Verify a specific evidence artifact against an AIUC-1 control using the auditor skill.

## Input

Parse `$ARGUMENTS` for:
- Requirement ID (e.g., B001, C010, E015)
- Description or content of the evidence artifact being verified

If not fully provided, ask:
1. Which requirement ID are you verifying against?
2. Please describe or share the evidence artifact (policy document, test report, configuration, log, etc.)

## Workflow

1. Look up the requirement in `references/aiuc-1-spec.md` — retrieve the full requirement text, all controls under it, Core (must) criteria, Supplemental (recommended) criteria, required artifact type, and review frequency.

2. Compare the provided evidence against each control's Core criteria. For each criterion:
   - Does the artifact satisfy it? (Yes / Partially / No)
   - If partially or no — what specifically is missing?

3. Check recency: is the artifact dated within the required review window? (quarterly = 90 days, annual = 12 months)

4. Classify the overall finding: **Conforming / NC-Minor / NC-Major / Observation**

## Output

```
## Verification: [Requirement ID] — [Title]
Evidence reviewed: [description]
Review date on artifact: [date if present]

### Control Assessment
| Control | Core criteria | Satisfied? | Gap |
|---------|--------------|------------|-----|
| [ID].1 | [criterion] | Yes | — |
| [ID].2 | [criterion] | Partially | Missing: [specific field] |

### Recency Check
Required frequency: [quarterly / annual]
Artifact date: [date]
Status: [Current / EXPIRED — last review was X days ago]

### Finding: [Conforming / NC-Minor / NC-Major / Observation]
[1-2 sentence rationale]

### To achieve conformance
[Specific steps to close any gaps]
```
