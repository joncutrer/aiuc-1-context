"""
run_periodic.py — Orchestrator for all AIUC-1 fetch and build tasks.

Designed to be called by a scheduler (cron, GitHub Actions, etc.) or run manually.
Executes tasks in the correct dependency order. Exits non-zero on any failure.

Usage:
    python src/run_periodic.py [--force]

    --force   Re-fetch spec even if the current version already exists.

Execution order:
    1. fetch_spec        — detect and fetch the latest spec version
    2. fetch_news        — harvest articles from the current month
    3. diff_specs        — generate a diff if a new version was fetched
    4. build_ai_context  — always rebuild the AI context document
    5. build_agent_skills — always rebuild the agent skill library
"""

import argparse
import importlib.util
import os
import re
import sys
from datetime import datetime

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(REPO_ROOT, "src")
SPEC_DIR = os.path.join(REPO_ROOT, "data", "spec-versions")

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

def log(msg: str) -> None:
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


def log_section(title: str) -> None:
    log(f"{'='*60}")
    log(f"  {title}")
    log(f"{'='*60}")


# ---------------------------------------------------------------------------
# Module runner
# ---------------------------------------------------------------------------

def _load_module(name: str):
    """Dynamically load a script from src/ as a module."""
    path = os.path.join(SRC_DIR, f"{name}.py")
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_step(step_name: str, fn, *args, **kwargs) -> bool:
    """Run a callable step, log result, return True on success."""
    log_section(step_name)
    try:
        fn(*args, **kwargs)
        log(f"✓ {step_name} completed successfully.")
        return True
    except SystemExit as exc:
        if exc.code == 0:
            log(f"✓ {step_name} completed (exit 0).")
            return True
        log(f"✗ {step_name} failed with exit code {exc.code}.")
        return False
    except Exception as exc:
        log(f"✗ {step_name} raised an exception: {exc}")
        return False


# ---------------------------------------------------------------------------
# Version helpers (duplicated from fetch_spec to avoid circular import)
# ---------------------------------------------------------------------------

def _sorted_versions() -> list[str]:
    if not os.path.isdir(SPEC_DIR):
        return []
    pattern = re.compile(r"^\d{4}-Q[1-4]$")
    versions = [d for d in os.listdir(SPEC_DIR) if pattern.match(d)]

    def vkey(v):
        year, q = v.split("-Q")
        return int(year) * 10 + int(q)

    return sorted(versions, key=vkey)


# ---------------------------------------------------------------------------
# Main orchestration
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Run all AIUC-1 periodic fetch tasks")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-fetch spec even if current version already exists",
    )
    args = parser.parse_args()

    failures = []

    # ------------------------------------------------------------------
    # Step 1: Fetch spec
    # ------------------------------------------------------------------
    versions_before = set(_sorted_versions())

    fetch_spec = _load_module("fetch_spec")
    ok = run_step(
        "fetch_spec — detect and fetch latest spec version",
        lambda: fetch_spec.fetch_spec(fetch_spec.detect_latest_version(), force=args.force),
    )
    if not ok:
        failures.append("fetch_spec")

    versions_after = set(_sorted_versions())
    new_versions = versions_after - versions_before
    new_version_fetched = bool(new_versions)

    if new_version_fetched:
        log(f"New version(s) detected: {', '.join(sorted(new_versions))}")

    # ------------------------------------------------------------------
    # Step 2: Fetch news
    # ------------------------------------------------------------------
    fetch_news = _load_module("fetch_news")
    ok = run_step(
        "fetch_news — harvest articles from homepage",
        fetch_news.main,
    )
    if not ok:
        failures.append("fetch_news")

    # ------------------------------------------------------------------
    # Step 3: Diff specs (only if a new version was just fetched)
    # ------------------------------------------------------------------
    all_versions = _sorted_versions()
    if new_version_fetched and len(all_versions) >= 2:
        ver_a = all_versions[-2]
        ver_b = all_versions[-1]
        diff_specs = _load_module("diff_specs")
        # Patch sys.argv so diff_specs.main() picks up the version args
        _orig_argv = sys.argv[:]
        sys.argv = ["diff_specs.py", ver_a, ver_b]
        ok = run_step(
            f"diff_specs — generate diff {ver_a} → {ver_b}",
            diff_specs.main,
        )
        sys.argv = _orig_argv
        if not ok:
            failures.append("diff_specs")
    elif new_version_fetched:
        log("Only one version available — skipping diff (need at least two versions).")
    else:
        log("No new version fetched — skipping diff.")

    # ------------------------------------------------------------------
    # Step 4: Build AI context
    # ------------------------------------------------------------------
    build_ai_context = _load_module("build_ai_context")
    ok = run_step(
        "build_ai_context — compile AI context document",
        build_ai_context.main,
    )
    if not ok:
        failures.append("build_ai_context")

    # ------------------------------------------------------------------
    # Step 5: Build agent skills
    # ------------------------------------------------------------------
    build_agent_skills = _load_module("build_agent_skills")
    ok = run_step(
        "build_agent_skills — generate agent skill library",
        build_agent_skills.main,
    )
    if not ok:
        failures.append("build_agent_skills")

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    log_section("Run complete")
    if failures:
        log(f"FAILED steps: {', '.join(failures)}")
        sys.exit(1)
    else:
        log("All steps completed successfully.")
        sys.exit(0)


if __name__ == "__main__":
    main()
