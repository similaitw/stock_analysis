from pathlib import Path

import pandas as pd
import streamlit as st

from data.workspace_store import WorkspaceStore


def _extract_recent_worklog_entries(worklog_path: Path, limit: int = 3) -> list[str]:
    if not worklog_path.exists():
        return []

    sections: list[list[str]] = []
    current: list[str] = []

    for raw_line in worklog_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        if line.startswith("## 20"):
            if current:
                sections.append(current)
            current = [line]
        elif current and line:
            current.append(line)

    if current:
        sections.append(current)

    return ["\n".join(section) for section in sections[-limit:]][::-1]


def render_home_page() -> None:
    store = WorkspaceStore()
    snapshot = store.get_dashboard_snapshot()
    counts = snapshot["counts"]
    project_root = Path(__file__).resolve().parents[1]

    st.header("🏠 研究首頁")
    st.caption("台股優先、小團隊研究協作與模擬執行工作台。")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Screen Runs", counts["screen_runs"])
    c2.metric("Signals", counts["signal_events"])
    c3.metric("Backtests", counts["backtest_runs"])
    c4.metric("Pending Orders", counts["pending_orders"])

    c5, c6, c7, c8 = st.columns(4)
    c5.metric("Trade Plans", counts["trade_plans"])
    c6.metric("Paper Orders", counts["paper_orders"])
    c7.metric("Watchlists", counts["watchlists"])
    c8.metric("Research Notes", counts["research_notes"])

    st.markdown("---")
    st.subheader("交接狀態")
    docs = pd.DataFrame(
        [
            {"文件": "PLAN.md", "狀態": "Ready" if (project_root / "PLAN.md").exists() else "Missing"},
            {"文件": "WORKLOG.md", "狀態": "Ready" if (project_root / "WORKLOG.md").exists() else "Missing"},
        ]
    )
    st.dataframe(docs, width="stretch", hide_index=True)

    recent_col1, recent_col2 = st.columns(2)

    with recent_col1:
        st.subheader("最近 Screen Runs")
        screen_runs = snapshot["recent_screen_runs"]
        if screen_runs:
            screen_df = pd.DataFrame(
                [
                    {
                        "名稱": run.name,
                        "市場": run.market_scope,
                        "命中數": run.result_count,
                        "時間": run.executed_at,
                    }
                    for run in screen_runs
                ]
            )
            st.dataframe(screen_df, width="stretch", hide_index=True)
        else:
            st.info("目前還沒有保存過的 ScreenRun。")

        st.subheader("最近回測")
        backtests = snapshot["recent_backtests"]
        if backtests:
            bt_df = pd.DataFrame(
                [
                    {
                        "股票": f"{item.stock_id} {item.stock_name}".strip(),
                        "策略": item.strategy_name,
                        "報酬(%)": round(item.total_return_pct, 2),
                        "時間": item.executed_at,
                    }
                    for item in backtests
                ]
            )
            st.dataframe(bt_df, width="stretch", hide_index=True)
        else:
            st.info("還沒有保存過的回測結果。")

    with recent_col2:
        st.subheader("待處理模擬委託")
        orders = snapshot["recent_orders"]
        if orders:
            orders_df = pd.DataFrame(
                [
                    {
                        "股票": f"{item.stock_id} {item.stock_name}".strip(),
                        "方向": item.side,
                        "狀態": item.status,
                        "目標價": item.intended_price,
                        "更新": item.updated_at,
                    }
                    for item in orders
                ]
            )
            st.dataframe(orders_df, width="stretch", hide_index=True)
        else:
            st.info("目前沒有模擬委託。")

        st.subheader("最近工作日誌")
        for entry in _extract_recent_worklog_entries(project_root / "WORKLOG.md"):
            with st.expander(entry.splitlines()[0], expanded=False):
                st.markdown("\n".join(entry.splitlines()[1:]))
