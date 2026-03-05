"""
build_agent_skills.py — Generate a library of reusable agent skill definitions
from the AIUC-1 AI context document.

Usage:
    python src/build_agent_skills.py

Output: data/agent-skills/skill-library.md  (always overwritten)
"""

import os
from datetime import date

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTEXT_PATH = os.path.join(REPO_ROOT, "data", "ai-context", "aiuc-1-context-latest.md")
SKILLS_DIR = os.path.join(REPO_ROOT, "data", "agent-skills")
OUT_PATH = os.path.join(SKILLS_DIR, "skill-library.md")

# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------

def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def write_file(path: str, content: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def read_file(path: str) -> str:
    if not os.path.isfile(path):
        return ""
    with open(path, encoding="utf-8") as f:
        return f.read()


# ---------------------------------------------------------------------------
# Skill definitions
# ---------------------------------------------------------------------------

SKILLS = [
    {
        "name": "assess-agent-against-domain",
        "trigger": "User asks to evaluate an AI agent or system against a specific AIUC-1 domain (e.g., Security, Safety, Data & Privacy).",
        "input": "Description of the AI agent/system; target domain (A–F or domain name).",
        "output": "Gap analysis listing which requirements are met, partially met, or unmet, with evidence notes.",
        "steps": [
            "Read the relevant domain section from `data/ai-context/aiuc-1-context-latest.md`.",
            "For each requirement in the domain, ask the user (or infer from provided docs) whether the control is implemented.",
            "Classify each requirement as: Met / Partial / Unmet / Not Applicable.",
            "List unmet requirements with their IDs and recommended remediation steps.",
            "Summarize the overall compliance posture for the domain.",
        ],
        "reference": "All six domains (A–F); `/scoping` for modality-based control filtering.",
    },
    {
        "name": "map-control-to-framework",
        "trigger": "User asks how a specific AIUC-1 requirement maps to an external framework (ISO 42001, NIST AI RMF, OWASP, EU AI Act, MITRE ATLAS, CSA AICM).",
        "input": "AIUC-1 requirement ID (e.g., B003) or domain name; target framework name.",
        "output": "List of mapped framework elements with clause/section references and gap assessment.",
        "steps": [
            "Look up the requirement ID in the `crosswalks` section of `aiuc-1-context-latest.md`.",
            "Extract all framework mappings for the requested target framework.",
            "For each mapping, note: framework element ID, clause/section, content summary, gap assessment.",
            "If the requirement has no mapping to the target framework, state this explicitly.",
        ],
        "reference": "`data/spec-versions/*/crosswalks.md`; `data/ai-context/aiuc-1-context-latest.md`.",
    },
    {
        "name": "generate-evidence-checklist",
        "trigger": "User needs a checklist of evidence artifacts required for AIUC-1 certification preparation.",
        "input": "Target domain(s) or 'all'; optional: list of modalities in scope (text, voice, image, video, files, code).",
        "output": "A checklist of required evidence items, organized by requirement ID.",
        "steps": [
            "Read the Evidence Requirements section for each targeted domain from `aiuc-1-context-latest.md`.",
            "Filter requirements by modality if modalities are specified (use scoping rules).",
            "For each requirement, list the specific evidence artifacts required (config files, logs, policies, test reports, etc.).",
            "Mark which requirements are Mandatory vs. Optional.",
            "Format output as a Markdown checklist: `- [ ] B001: <evidence artifact>`.",
        ],
        "reference": "Evidence Requirements sections in all domain pages; `/scoping` for modality filtering.",
    },
    {
        "name": "summarize-domain-requirements",
        "trigger": "User wants a concise summary of all requirements in a specific AIUC-1 domain.",
        "input": "Domain name or letter (A–F).",
        "output": "A structured summary table of all requirements: ID, title, status (Mandatory/Optional), one-sentence description.",
        "steps": [
            "Read the specified domain section from `aiuc-1-context-latest.md`.",
            "For each requirement, extract: ID, title, Mandatory/Optional status, and a one-sentence summary from the control description.",
            "Present as a Markdown table with columns: ID | Title | Status | Summary.",
            "Append a count: 'X Mandatory, Y Optional requirements in this domain.'",
        ],
        "reference": "Domain pages: data-and-privacy (A), security (B), safety (C), reliability (D), accountability (E), society (F).",
    },
    {
        "name": "compare-versions",
        "trigger": "User asks what changed between two AIUC-1 releases.",
        "input": "Two version identifiers (e.g., 2026-Q1 and 2026-Q2).",
        "output": "A human-readable summary of additions, removals, and modifications by domain.",
        "steps": [
            "Check `data/spec-diffs/` for a pre-generated diff file matching the two versions.",
            "If found, read and summarize the diff by domain.",
            "If not found, instruct the user to run `python src/diff_specs.py <v1> <v2>` first.",
            "Highlight the most significant changes (new requirements, retired requirements, revised Shoulds/Mays).",
            "Cross-reference with `data/changelog/` for the official change notes.",
        ],
        "reference": "`data/spec-diffs/`; `data/changelog/`.",
    },
    {
        "name": "explain-requirement",
        "trigger": "User asks for an explanation of a specific AIUC-1 requirement by ID.",
        "input": "Requirement ID (e.g., C002, A007).",
        "output": "Full explanation including: title, status, summary, Shoulds, Mays, evidence requirements, and framework crosswalks.",
        "steps": [
            "Look up the requirement ID in `aiuc-1-context-latest.md`.",
            "Extract: ID, title, Mandatory/Optional, summary description, Shoulds, Mays, keywords, frequency, crosswalks, evidence.",
            "Present in a structured format with clear section headings.",
            "If the user asks for implementation guidance, use the Shoulds as the primary implementation checklist.",
        ],
        "reference": "All domain pages in `data/ai-context/aiuc-1-context-latest.md`.",
    },
    {
        "name": "scope-assessment",
        "trigger": "User wants to determine which AIUC-1 requirements apply to their specific AI agent deployment.",
        "input": "Description of the agent system: modalities used (text, voice, image, video, files, code), internal vs. external-facing, third-party vs. custom-built.",
        "output": "A scoped list of applicable requirements (Mandatory and Optional) based on the agent's configuration.",
        "steps": [
            "Review `/scoping` guidance in `aiuc-1-context-latest.md`.",
            "Apply modality filters: identify which controls are triggered by the agent's active modalities.",
            "Distinguish internal-facing vs. external-facing controls.",
            "Produce a filtered requirement list: 'X of 130 controls apply to your configuration.'",
            "Group by domain and mark each as Mandatory or Optional.",
        ],
        "reference": "`data/spec-versions/*/index.md`; `/scoping` page content.",
    },
]


def format_skill(skill: dict) -> str:
    steps_md = "\n".join(f"{i+1}. {step}" for i, step in enumerate(skill["steps"]))
    return (
        f"## Skill: {skill['name']}\n\n"
        f"**Trigger:** {skill['trigger']}\n\n"
        f"**Input:** {skill['input']}\n\n"
        f"**Output:** {skill['output']}\n\n"
        f"**Steps:**\n{steps_md}\n\n"
        f"**Reference:** {skill['reference']}\n\n"
        f"---\n\n"
    )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    context_exists = os.path.isfile(CONTEXT_PATH)
    if not context_exists:
        print("WARNING: AI context file not found at:", CONTEXT_PATH)
        print("Run 'python src/build_ai_context.py' first for best results.")
        print("Generating skill library from static definitions anyway ...\n")

    today = date.today().isoformat()
    header = (
        "# AIUC-1 Agent Skill Library\n\n"
        f"**Generated:** {today}  \n"
        "**Source context:** `data/ai-context/aiuc-1-context-latest.md`\n\n"
        "A library of reusable agent skill definitions for AIUC-1 compliance, auditing, "
        "and implementation tasks.\n\n"
        "---\n\n"
    )

    skill_blocks = [format_skill(s) for s in SKILLS]
    output = header + "".join(skill_blocks)

    ensure_dir(SKILLS_DIR)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"Agent skill library written → {OUT_PATH}")
    print(f"  {len(SKILLS)} skills defined.")


if __name__ == "__main__":
    main()
