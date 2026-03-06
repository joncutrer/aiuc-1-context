---
description: Map AIUC-1 requirements to another compliance framework (ISO 42001, EU AI Act, NIST AI RMF, MITRE ATLAS, OWASP, SOC 2, GDPR). Shows alignment, gaps, and what AIUC-1 compliance buys you.
argument-hint: "[framework name]"
---

Map AIUC-1 to another framework using the advisor skill.

## Input

Parse `$ARGUMENTS` for the target framework name. Supported:
- ISO 42001
- EU AI Act
- NIST AI RMF
- MITRE ATLAS
- OWASP Top Ten for LLM Applications
- OWASP AIVSS
- CSA AICM
- SOC 2 (note: AIUC-1 does not duplicate SOC 2)
- GDPR (note: AIUC-1 does not duplicate GDPR)
- ISO 27001 (note: AIUC-1 does not duplicate ISO 27001)

If not provided, ask: Which framework would you like to map AIUC-1 to?

## Workflow

Reference the Framework Crosswalks section in `references/aiuc-1-spec.md`.

For the requested framework:
1. Explain the relationship (AIUC-1 builds on it / AIUC-1 supplements it / AIUC-1 does not duplicate it)
2. Produce a mapping table showing which AIUC-1 requirements address which framework elements
3. Identify gaps: framework obligations not covered by AIUC-1 (and vice versa)
4. Provide an executive summary: "If you're already AIUC-1 certified, what does that mean for your [framework] obligations?"

## Output

```markdown
## AIUC-1 → [Framework] Crosswalk

### Relationship summary
[1-2 paragraphs explaining how AIUC-1 and this framework relate]

### Mapping table
| AIUC-1 ID | AIUC-1 Requirement | [Framework] Clause/Control | Alignment | Gap |
|-----------|-------------------|---------------------------|-----------|-----|
| B001 | Adversarial testing | NIST AI RMF: MEASURE 2.5 | Strong | AIUC-1 requires quarterly cadence; NIST has no frequency requirement |
| ... | | | | |

### What AIUC-1 certification provides toward [Framework]
- [Specific clause/obligation] ✓ Addressed by [AIUC-1 IDs]
- [Another clause] ⚠ Partially addressed — also requires [additional step]
- [Another clause] ✗ Not addressed by AIUC-1 — requires separate compliance work

### Remaining gaps (not covered by AIUC-1)
- [Gap + recommended action]

### Summary
Completing AIUC-1 certification provides [strong / moderate / limited] coverage of [Framework] obligations. [1-2 sentences on what additional work is needed.]
```
