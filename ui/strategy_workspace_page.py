import pandas as pd
import streamlit as st

from data.workspace_models import ScreenRun, Watchlist
from data.workspace_store import WorkspaceStore
from ui.strategy_page import render_strategy_page


def render_strategy_workspace_page() -> None:
    st.header("🧠 策略工作台")
    st.caption("沿用現有策略實驗室能力，並補上可追溯的 ScreenRun 保存與共享 watchlist。")

    render_strategy_page()

    store = WorkspaceStore()
    df_results = st.session_state.get("strategy_scan_results", pd.DataFrame())
    meta = st.session_state.get("strategy_scan_meta", {})

    if df_results.empty:
        st.info("先在上方策略實驗室執行掃描，再把結果保存進工作流。")
        return

    st.markdown("---")
    st.subheader("保存與交接")
    default_name = meta.get("run_name") or f"{meta.get('market', 'Scan')} {meta.get('time', '')}".strip()
    run_name = st.text_input("ScreenRun 名稱", value=default_name or "策略掃描", key="screen_run_name")
    run_notes = st.text_area("備註", value="保存本次掃描結果，供驗證中心與協作頁使用。", key="screen_run_notes")

    action_col1, action_col2 = st.columns(2)
    with action_col1:
        if st.button("儲存為 ScreenRun", key="save_screen_run"):
            screen_run = ScreenRun.from_scan_results(
                name=run_name,
                market_scope=meta.get("market", meta.get("market_code", "Custom")),
                stock_pool=meta.get("stock_pool", []),
                strategy_names=meta.get("strategies", []),
                match_mode=meta.get("mode", "AND"),
                results=df_results.to_dict(orient="records"),
                strategy_params=meta.get("parameters", {}),
                source_page="strategy_workspace",
                notes=run_notes,
            )
            store.save_screen_run(screen_run)
            st.session_state["latest_screen_run_id"] = screen_run.id
            st.success(f"ScreenRun 已保存：{screen_run.name}")

    with action_col2:
        if st.button("建立共享 watchlist", key="create_watchlist_from_screen"):
            watchlist = Watchlist(
                name=f"{run_name} Watchlist",
                owner="team",
                stocks=df_results["Stock ID"].astype(str).tolist(),
                description=f"由策略工作台建立，來源：{run_name}",
            )
            store.save_watchlist(watchlist)
            st.success("已從本次掃描建立共享 watchlist。")

    recent_runs = store.list_screen_runs(limit=5)
    if recent_runs:
        st.caption("最近保存的 ScreenRuns")
        st.dataframe(
            pd.DataFrame(
                [
                    {
                        "名稱": item.name,
                        "市場": item.market_scope,
                        "命中數": item.result_count,
                        "時間": item.executed_at,
                    }
                    for item in recent_runs
                ]
            ),
            width="stretch",
            hide_index=True,
        )
