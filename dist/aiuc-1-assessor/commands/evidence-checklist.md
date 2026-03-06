---
description: Generate a checklist of evidence artifacts required for AIUC-1 certification, filtered by domain and modality.
argument-hint: "[domain(s) or 'all'] [optional: modalities]"
---

Generate an AIUC-1 evidence checklist using the assessor skill.

## Input

Parse `$ARGUMENTS` for:
- Target domain(s): "all", a domain letter (A–F), or a domain name (e.g. "security")
- Optional modalities to filter by (e.g. "text voice" or "automation")

Default to "all" domains if not specified.

## Workflow

For each applicable requirement in the target domain(s), reference `references/aiuc-1-spec.md` Controls & Evidence section to extract the required evidence artifacts.

For each requirement, list:
- The specific artifact type(s) required (Documentation, Technical Configuration, Testing, Monitoring, Logging, etc.)
- What the artifact must contain (key fields/sections)
- The review frequency (quarterly or annual)
- Whether the requirement is Mandatory or Optional

## Output

```markdown
## AIUC-1 Evidence Checklist — [Domain(s)] — [Date]

### Domain A: Data & Privacy

#### Mandatory
- [ ] **A001** — Input data policy *(annual)*
  Artifact: Terms of Service or Data Processing Agreement
  Must include: training data use, inference processing, retention periods, customer data rights

- [ ] **A003** — Data collection safeguards *(annual)*
  Artifact: Technical configuration documentation or access control policy
  Must include: role-based access controls, data minimization mechanisms

#### Optional
- [ ] **A007** — IP violation prevention *(annual)*
  Artifact: Technical control documentation or IP screening test results
  ...

---
**Total: X Mandatory, Y Optional artifacts required**
**Quarterly reviews due: [list IDs]**
```
