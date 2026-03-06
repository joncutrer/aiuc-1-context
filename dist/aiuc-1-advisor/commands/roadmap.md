---
description: Generate a phased AIUC-1 compliance roadmap. Scopes applicable requirements and organizes them into Foundation, Certification-ready, and Excellence phases with timelines and key actions.
argument-hint: "[system description]"
---

Generate an AIUC-1 compliance roadmap using the advisor skill.

## Input

Parse `$ARGUMENTS` for a description of the AI system. If not provided, ask:
1. What does the AI system do?
2. What modalities does it use? (text, voice, image, automation, files, code)
3. Is it internal or external-facing?
4. What is the current compliance maturity? (starting from zero / partially implemented / preparing for cert)

## Workflow

1. Scope requirements based on system modalities (reference `references/aiuc-1-spec.md`)
2. Bucket all in-scope Mandatory requirements into three phases:

**Phase 1 — Foundation (0–90 days)**
All Mandatory requirements with quarterly review frequency. These are highest urgency because they must be re-reviewed every 90 days once established. Key ones: B001, B007, C001, C006, C009, C010, C011, C012, D002, D004, E015.

**Phase 2 — Certification-ready (90–180 days)**
Remaining Mandatory requirements with annual frequency. Commission third-party testing. Build policy suite. Achieve audit-readiness.

**Phase 3 — Excellence (ongoing)**
Optional controls that materially reduce risk. QMS integration. Continuous monitoring. Proactive framework crosswalk alignment.

## Output

```markdown
## AIUC-1 Compliance Roadmap — [System Name]
Generated: [date] | Standard version: 2026-Q1
In-scope: X of 51 requirements (Y Mandatory, Z Optional)

### Phase 1 — Foundation (0–90 days)
*Goal: Establish all quarterly controls before first review window closes.*

| ID | Requirement | Owner | Key action |
|----|-------------|-------|------------|
| B001 | Adversarial testing | Security team | Initiate red-team program; document threat taxonomy |
| B007 | Access controls | IT/IAM | Quarterly access review process |
| C001 | Risk taxonomy | Product/Legal | Define harmful/OOS/hallucination risk categories |
| ... | | | |

### Phase 2 — Certification-ready (90–180 days)
*Goal: Complete all Mandatory annual controls; commission third-party testing.*
[same table format]

### Phase 3 — Excellence (ongoing)
*Goal: Optional controls + continuous improvement.*
[same table format]

### Milestones
- Day 30: [key milestone]
- Day 90: First quarterly review cycle complete
- Day 180: Certification audit readiness
- Ongoing: Quarterly review cadence established
```
