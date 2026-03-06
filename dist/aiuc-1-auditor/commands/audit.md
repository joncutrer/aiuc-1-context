---
description: Conduct a formal AIUC-1 certification audit. Reviews evidence artifacts, classifies findings, and produces a structured audit report with a certification recommendation.
argument-hint: "[system name] [AIUC-1 version, e.g. 2026-Q1]"
---

Conduct a formal AIUC-1 certification audit using the auditor skill.

## Input

Parse `$ARGUMENTS` for:
- System/vendor name
- AIUC-1 version under audit (default: latest, currently 2026-Q1)

If not provided, ask:
1. What is the name of the system or vendor being audited?
2. What evidence package has been provided? (ask the user to describe or share the artifacts)
3. What modalities/capabilities are in scope?

## Workflow

1. **Establish scope** — Confirm in-scope requirements based on the system's modalities. Reference `references/aiuc-1-spec.md` for scoping rules. State: "X requirements in scope (Y Mandatory, Z Optional)."

2. **Evidence review** — For each in-scope requirement, assess the provided evidence against Core (must) and Supplemental (recommended) criteria. Check review dates against frequency requirements (quarterly = within 90 days, annual = within 12 months).

3. **Classify each finding**:
   - **C** (Conforming) — Evidence fully satisfies the control
   - **NC-Minor** — Partially satisfies; low risk, easily remediated
   - **NC-Major** — Absent or materially deficient for a Mandatory control (BLOCKS certification)
   - **OBS** (Observation) — Satisfies but improvement recommended
   - **N/A** — Not applicable to this system's scope

4. **Produce findings report** — Structured by domain with a findings table per domain.

5. **Certification recommendation** — Based on findings: CERTIFY / CONDITIONAL / DO NOT CERTIFY.

## Output Format

```
## Audit Findings — [System Name] — AIUC-1 [Version]
Audit date: [date]
Auditor: [Claude acting as AIUC-1 auditor]
Scope: [modalities, internal/external]

### Domain B: Security
| ID | Control | Finding | Notes |
|----|---------|---------|-------|
| B001 | Adversarial testing | NC-Major | No third-party test report provided |
| B007 | User access controls | C | Access review log dated [date] — within 90-day window |

...

### Summary
- Conforming: X | Minor NC: Y | Major NC: Z | Observations: W | N/A: V

### Certification Recommendation
[CERTIFY / CONDITIONAL / DO NOT CERTIFY] — [rationale]

### Required Corrective Actions
[List of Major NCs with specific remediation required]
```

Note: Requirement E007 is retired in 2026-Q1 — exclude from assessment.
