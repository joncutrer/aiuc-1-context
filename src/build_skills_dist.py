"""
build_skills_dist.py — Assemble the AIUC-1 skills bundle into dist/.

For each skill in skills/, copies SKILL.md to dist/<skill>/ and injects
the latest AI context document as dist/<skill>/references/aiuc-1-spec.md.
Also writes dist/.claude-plugin/marketplace.json.

Replaces the old build_agent_skills.py / data/agent-skills/skill-library.md.

Usage:
    uv run src/build_skills_dist.py

Prerequisites:
    data/ai-context/aiuc-1-context-latest.md must exist.
    Run src/build_ai_context.py first if it does not.
"""

import json
import os
import shutil
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_SRC = os.path.join(REPO_ROOT, "skills")
DIST_DIR = os.path.join(REPO_ROOT, "dist")
CONTEXT_PATH = os.path.join(REPO_ROOT, "data", "ai-context", "aiuc-1-context-latest.md")

MARKETPLACE_META = {
    "name": "aiuc-1-skills",
    "description": (
        "Role-based Claude skills for AIUC-1 AI agent compliance: "
        "pre-certification assessment, formal audit, control implementation, "
        "and strategic advisory."
    ),
    "version": "1.0.0",
    "repository": "https://github.com/joncutrer/aiuc-1-context",
}


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def read_frontmatter_name(skill_md_path: str) -> str:
    """Extract the 'name' field from a SKILL.md YAML frontmatter block."""
    with open(skill_md_path, encoding="utf-8") as f:
        lines = f.readlines()
    in_front = False
    for line in lines:
        if line.strip() == "---":
            if not in_front:
                in_front = True
                continue
            else:
                break
        if in_front and line.startswith("name:"):
            return line.split(":", 1)[1].strip()
    return ""


def read_frontmatter_description(skill_md_path: str) -> str:
    """Extract the 'description' field from a SKILL.md YAML frontmatter block."""
    with open(skill_md_path, encoding="utf-8") as f:
        lines = f.readlines()
    in_front = False
    for line in lines:
        if line.strip() == "---":
            if not in_front:
                in_front = True
                continue
            else:
                break
        if in_front and line.startswith("description:"):
            return line.split(":", 1)[1].strip()
    return ""


def discover_skills() -> list[str]:
    """Return sorted list of skill directory names from skills/."""
    if not os.path.isdir(SKILLS_SRC):
        return []
    return sorted(
        d for d in os.listdir(SKILLS_SRC)
        if os.path.isdir(os.path.join(SKILLS_SRC, d))
        and os.path.isfile(os.path.join(SKILLS_SRC, d, "SKILL.md"))
    )


def build_skill(skill_name: str, context_text: str) -> dict:
    """
    Copy SKILL.md and inject context reference for one skill.
    Returns the skill metadata dict for marketplace.json.
    """
    src_skill_dir = os.path.join(SKILLS_SRC, skill_name)
    dst_skill_dir = os.path.join(DIST_DIR, skill_name)
    refs_dir = os.path.join(dst_skill_dir, "references")

    ensure_dir(dst_skill_dir)
    ensure_dir(refs_dir)

    # Copy SKILL.md
    src_skill_md = os.path.join(src_skill_dir, "SKILL.md")
    dst_skill_md = os.path.join(dst_skill_dir, "SKILL.md")
    shutil.copy2(src_skill_md, dst_skill_md)

    # Inject AI context as reference file
    ref_path = os.path.join(refs_dir, "aiuc-1-spec.md")
    with open(ref_path, "w", encoding="utf-8") as f:
        f.write(context_text)

    # Read metadata from SKILL.md for marketplace.json
    name = read_frontmatter_name(src_skill_md)
    description = read_frontmatter_description(src_skill_md)

    skill_size = os.path.getsize(dst_skill_md) + os.path.getsize(ref_path)
    print(f"  ✓ {skill_name:<28} SKILL.md + {len(context_text):,} char spec ref  ({skill_size:,} bytes total)")

    return {
        "name": skill_name,
        "path": skill_name,
        "displayName": name,
        "description": description,
    }


def write_marketplace_json(skills_meta: list[dict]) -> None:
    plugin_dir = os.path.join(DIST_DIR, ".claude-plugin")
    ensure_dir(plugin_dir)

    marketplace = {**MARKETPLACE_META, "skills": skills_meta}
    out_path = os.path.join(plugin_dir, "marketplace.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(marketplace, f, indent=2)
        f.write("\n")
    print(f"  ✓ .claude-plugin/marketplace.json  ({len(skills_meta)} skills listed)")


def clean_dist() -> None:
    """Remove all skill directories and plugin config from dist/ (preserve .git if present)."""
    if not os.path.isdir(DIST_DIR):
        return
    for entry in os.listdir(DIST_DIR):
        if entry == ".git":
            continue
        target = os.path.join(DIST_DIR, entry)
        if os.path.isdir(target):
            shutil.rmtree(target)
        else:
            os.remove(target)


def main():
    # Validate prerequisite
    if not os.path.isfile(CONTEXT_PATH):
        print(f"ERROR: AI context file not found: {CONTEXT_PATH}")
        print("Run 'uv run src/build_ai_context.py' first.")
        sys.exit(1)

    with open(CONTEXT_PATH, encoding="utf-8") as f:
        context_text = f.read()

    skills = discover_skills()
    if not skills:
        print(f"ERROR: No skills found in {SKILLS_SRC}")
        print("Expected: skills/<skill-name>/SKILL.md")
        sys.exit(1)

    print(f"Building dist/ from {len(skills)} skill(s) in skills/")
    print(f"Context source: {CONTEXT_PATH} ({len(context_text):,} chars)")
    print()

    clean_dist()
    ensure_dir(DIST_DIR)

    skills_meta = []
    for skill_name in skills:
        meta = build_skill(skill_name, context_text)
        skills_meta.append(meta)

    write_marketplace_json(skills_meta)

    total_bytes = sum(
        os.path.getsize(os.path.join(DIST_DIR, s, f))
        for s in skills
        for f in ("SKILL.md", os.path.join("references", "aiuc-1-spec.md"))
    )

    print()
    print(f"dist/ built: {len(skills)} skills, {total_bytes:,} bytes total")
    print(f"Location: {DIST_DIR}")
    print()
    print("Installation:")
    print("  claude plugin marketplace add joncutrer/aiuc-1-context/dist")
    for s in skills:
        print(f"  claude plugin install {s}@aiuc-1-skills")


if __name__ == "__main__":
    main()
