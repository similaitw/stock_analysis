from pathlib import Path

from ui.navigation import NAVIGATION_SECTIONS


def test_navigation_has_six_primary_sections():
    ids = [section.id for section in NAVIGATION_SECTIONS]

    assert ids == ["home", "research", "strategy", "validation", "execution", "collab"]


def test_plan_and_worklog_exist_with_required_sections():
    project_root = Path(__file__).resolve().parents[1]
    plan = (project_root / "PLAN.md").read_text(encoding="utf-8")
    worklog = (project_root / "WORKLOG.md").read_text(encoding="utf-8")

    assert "## 產品定位" in plan
    assert "## 核心資料模型" in plan
    assert "## 記錄規則" in worklog
    assert "## 2026-04-23 02:28:02 +08:00" in worklog
