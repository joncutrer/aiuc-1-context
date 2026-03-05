# AIUC-1 Agent Skill Library

**Generated:** 2026-03-05  
**Source context:** `data/ai-context/aiuc-1-context-latest.md`

A library of reusable agent skill definitions for AIUC-1 compliance, auditing, and implementation tasks.

---

## Skill: assess-agent-against-domain

**Trigger:** User asks to evaluate an AI agent or system against a specific AIUC-1 domain (e.g., Security, Safety, Data & Privacy).

**Input:** Description of the AI agent/system; target domain (A–F or domain name).

**Output:** Gap analysis listing which requirements are met, partially met, or unmet, with evidence notes.

**Steps:**
1. Read the relevant domain section from `data/ai-context/aiuc-1-context-latest.md`.
2. For each requirement in the domain, ask the user (or infer from provided docs) whether the control is implemented.
3. Classify each requirement as: Met / Partial / Unmet / Not Applicable.
4. List unmet requirements with their IDs and recommended remediation steps.
5. Summarize the overall compliance posture for the domain.

**Reference:** All six domains (A–F); `/scoping` for modality-based control filtering.

---

## Skill: map-control-to-framework

**Trigger:** User asks how a specific AIUC-1 requirement maps to an external framework (ISO 42001, NIST AI RMF, OWASP, EU AI Act, MITRE ATLAS, CSA AICM).

**Input:** AIUC-1 requirement ID (e.g., B003) or domain name; target framework name.

**Output:** List of mapped framework elements with clause/section references and gap assessment.

**Steps:**
1. Look up the requirement ID in the `crosswalks` section of `aiuc-1-context-latest.md`.
2. Extract all framework mappings for the requested target framework.
3. For each mapping, note: framework element ID, clause/section, content summary, gap assessment.
4. If the requirement has no mapping to the target framework, state this explicitly.

**Reference:** `data/spec-versions/*/crosswalks.md`; `data/ai-context/aiuc-1-context-latest.md`.

---

## Skill: generate-evidence-checklist

**Trigger:** User needs a checklist of evidence artifacts required for AIUC-1 certification preparation.

**Input:** Target domain(s) or 'all'; optional: list of modalities in scope (text, voice, image, video, files, code).

**Output:** A checklist of required evidence items, organized by requirement ID.

**Steps:**
1. Read the Evidence Requirements section for each targeted domain from `aiuc-1-context-latest.md`.
2. Filter requirements by modality if modalities are specified (use scoping rules).
3. For each requirement, list the specific evidence artifacts required (config files, logs, policies, test reports, etc.).
4. Mark which requirements are Mandatory vs. Optional.
5. Format output as a Markdown checklist: `- [ ] B001: <evidence artifact>`.

**Reference:** Evidence Requirements sections in all domain pages; `/scoping` for modality filtering.

---

## Skill: summarize-domain-requirements

**Trigger:** User wants a concise summary of all requirements in a specific AIUC-1 domain.

**Input:** Domain name or letter (A–F).

**Output:** A structured summary table of all requirements: ID, title, status (Mandatory/Optional), one-sentence description.

**Steps:**
1. Read the specified domain section from `aiuc-1-context-latest.md`.
2. For each requirement, extract: ID, title, Mandatory/Optional status, and a one-sentence summary from the control description.
3. Present as a Markdown table with columns: ID | Title | Status | Summary.
4. Append a count: 'X Mandatory, Y Optional requirements in this domain.'

**Reference:** Domain pages: data-and-privacy (A), security (B), safety (C), reliability (D), accountability (E), society (F).

---

## Skill: compare-versions

**Trigger:** User asks what changed between two AIUC-1 releases.

**Input:** Two version identifiers (e.g., 2026-Q1 and 2026-Q2).

**Output:** A human-readable summary of additions, removals, and modifications by domain.

**Steps:**
1. Check `data/spec-diffs/` for a pre-generated diff file matching the two versions.
2. If found, read and summarize the diff by domain.
3. If not found, instruct the user to run `python src/diff_specs.py <v1> <v2>` first.
4. Highlight the most significant changes (new requirements, retired requirements, revised Shoulds/Mays).
5. Cross-reference with `data/changelog/` for the official change notes.

**Reference:** `data/spec-diffs/`; `data/changelog/`.

---

## Skill: explain-requirement

**Trigger:** User asks for an explanation of a specific AIUC-1 requirement by ID.

**Input:** Requirement ID (e.g., C002, A007).

**Output:** Full explanation including: title, status, summary, Shoulds, Mays, evidence requirements, and framework crosswalks.

**Steps:**
1. Look up the requirement ID in `aiuc-1-context-latest.md`.
2. Extract: ID, title, Mandatory/Optional, summary description, Shoulds, Mays, keywords, frequency, crosswalks, evidence.
3. Present in a structured format with clear section headings.
4. If the user asks for implementation guidance, use the Shoulds as the primary implementation checklist.

**Reference:** All domain pages in `data/ai-context/aiuc-1-context-latest.md`.

---

## Skill: scope-assessment

**Trigger:** User wants to determine which AIUC-1 requirements apply to their specific AI agent deployment.

**Input:** Description of the agent system: modalities used (text, voice, image, video, files, code), internal vs. external-facing, third-party vs. custom-built.

**Output:** A scoped list of applicable requirements (Mandatory and Optional) based on the agent's configuration.

**Steps:**
1. Review `/scoping` guidance in `aiuc-1-context-latest.md`.
2. Apply modality filters: identify which controls are triggered by the agent's active modalities.
3. Distinguish internal-facing vs. external-facing controls.
4. Produce a filtered requirement list: 'X of 130 controls apply to your configuration.'
5. Group by domain and mark each as Mandatory or Optional.

**Reference:** `data/spec-versions/*/index.md`; `/scoping` page content.

---

