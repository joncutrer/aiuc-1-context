---
description: Draft a policy document that satisfies one or more AIUC-1 requirements. Produces a structured template with required sections pre-populated.
argument-hint: "[requirement ID(s) or policy type, e.g. A001 or 'data use policy']"
---

Draft an AIUC-1-compliant policy document using the implementer skill.

## Input

Parse `$ARGUMENTS` for:
- Requirement ID(s) (e.g., A001, A002 or "A001 A002") or a policy type (e.g., "data use policy", "AI acceptable use policy", "AI failure response plan")
- Optional: organization name to personalize the template

If not provided, ask:
1. Which requirement(s) or policy type are you drafting for?
2. What is the organization/product name? (for placeholder text)

## Policy type mapping

Common policies and the requirements they satisfy:
- **Input data policy** → A001 (input data use, training, retention, customer rights)
- **Output data policy** → A002 (output ownership, usage, opt-out, deletion)
- **AI acceptable use policy** → E010 (user-facing AUP covering permissible uses)
- **AI failure response plan** → E001, E002, E003 (incident response for security breaches, harmful outputs, hallucinations)
- **AI transparency policy** → E017 (system transparency disclosures)
- **Vendor due diligence policy** → E006 (third-party AI vendor assessment process)
- **AI risk taxonomy** → C001 (definition of harmful/out-of-scope/hallucination risk categories)

## Workflow

1. Look up the target requirement(s) in `references/aiuc-1-spec.md`
2. Extract all Core criteria that the policy must address
3. Draft a complete policy template with:
   - Required sections based on Core criteria
   - Placeholder text (`[ORGANIZATION NAME]`, `[DATE]`, `[CONTACT]`, etc.)
   - Annotations showing which AIUC-1 control each section satisfies

## Output

Produce a complete, ready-to-edit Markdown policy document:

```markdown
# [Policy Title]

**Version:** 1.0
**Effective date:** [DATE]
**Owner:** [ROLE / TEAM]
**Review cycle:** [quarterly / annual — per AIUC-1 requirement]

> *This policy satisfies AIUC-1 requirements: [IDs]*

## 1. [Required section]
[Placeholder content addressing Core criteria]

## 2. ...

---
*Last reviewed: [DATE] | Next review due: [DATE]*
```

After the policy, list which Core criteria are satisfied by which section.
