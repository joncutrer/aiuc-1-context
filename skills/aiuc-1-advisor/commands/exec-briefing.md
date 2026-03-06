---
description: Generate an executive briefing on AIUC-1 compliance status. Produces a concise, business-focused summary suitable for leadership, board, or customer communication.
argument-hint: "[system name] [optional: audience e.g. 'board' or 'customer']"
---

Generate an executive AIUC-1 compliance briefing using the advisor skill.

## Input

Parse `$ARGUMENTS` for:
- System or organization name
- Optional target audience: board/leadership, customer/prospect, regulator (default: leadership)

If not provided, ask:
1. What system or organization is this briefing for?
2. Who is the audience? (internal leadership / customer / regulatory)
3. What is the current compliance status? (provide a summary or gap count)

## Workflow

Tailor the briefing to the audience:
- **Leadership/board**: Focus on risk exposure, investment required, competitive positioning
- **Customer/prospect**: Focus on trust, data protection, what certification means for them
- **Regulatory**: Focus on framework alignment, control coverage, audit readiness

Reference `references/aiuc-1-spec.md` for the AIUC-1 standard description and requirement counts.

## Output

```markdown
## AIUC-1 Compliance Briefing
**Organization/System:** [NAME]
**Date:** [DATE]
**Prepared for:** [AUDIENCE]

---

### What is AIUC-1?
AIUC-1 (AI Use Case standard 1) is the world's first security, safety, and reliability standard designed specifically for AI agents, developed with 100+ Fortune 500 CISOs. It covers 51 requirements across six domains: Data & Privacy, Security, Safety, Reliability, Accountability, and Society. The standard is updated quarterly and maps to ISO 42001, EU AI Act, NIST AI RMF, MITRE ATLAS, and OWASP.

### Why it matters for [ORGANIZATION]
[1-2 sentences specific to audience: customer trust / regulatory readiness / enterprise contract velocity]

### Current compliance posture
| Domain | Status | Notes |
|--------|--------|-------|
| A. Data & Privacy | [Met / Partial / Gap] | |
| B. Security | | |
| C. Safety | | |
| D. Reliability | | |
| E. Accountability | | |
| F. Society | | |

**Overall:** X of Y applicable requirements met. Z Mandatory gaps remain.

### Top risks if unaddressed
1. [Risk] — [Business consequence]
2. [Risk] — [Business consequence]
3. [Risk] — [Business consequence]

### Recommended next steps
| Action | Owner | Timeline | Investment |
|--------|-------|----------|------------|
| [Action] | [Team] | [30/60/90 days] | [Low/Med/High] |

### Bottom line
[2-3 sentences: where we are, where we're going, what it means for the audience]
```
