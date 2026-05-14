from pathlib import Path

from conftest import load_src_module


run_periodic = load_src_module("run_periodic")


def test_sorted_versions_filters_and_orders(tmp_path: Path, monkeypatch):
    (tmp_path / "2026-Q1").mkdir()
    (tmp_path / "2025-Q4").mkdir()
    (tmp_path / "junk").mkdir()
    (tmp_path / "2026-Q5").mkdir()

    monkeypatch.setattr(run_periodic, "SPEC_DIR", str(tmp_path))

    assert run_periodic._sorted_versions() == ["2025-Q4", "2026-Q1"]


def test_run_step_handles_system_exit_zero():
    ok = run_periodic.run_step("step", lambda: (_ for _ in ()).throw(SystemExit(0)))
    assert ok is True


def test_run_step_handles_exceptions():
    ok = run_periodic.run_step("step", lambda: (_ for _ in ()).throw(RuntimeError("boom")))
    assert ok is False
