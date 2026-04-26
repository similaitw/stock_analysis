from pathlib import Path

import pandas as pd
import streamlit as st

from data.workspace_models import ResearchNote, Watchlist
from data.workspace_store import WorkspaceStore
from monitor.engine import MonitorEngine
from portfolios import PortfolioManager


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


def render_collaboration_page() -> None:
    store = WorkspaceStore()
    pm = PortfolioManager()

    st.header("🤝 協作 / 監控")
    st.caption("共享 watchlist、研究筆記、近期交接上下文與手動監控快照。")

    top_left, top_right = st.columns(2)
    with top_left:
        st.subheader("共享 Watchlists")
        watchlists = store.list_watchlists(limit=50)
        if watchlists:
            watchlist_map = {f"{item.name} ({item.owner})": item.id for item in watchlists}
            selected_label = st.selectbox("選擇 watchlist", list(watchlist_map.keys()), key="collab_watchlist_select")
            watchlist = store.get_watchlist(watchlist_map[selected_label])
            if watchlist:
                st.write({
                    "description": watchlist.description,
                    "stocks": watchlist.stocks,
                    "updated_at": watchlist.updated_at,
                })
                if st.button("以此 watchlist 執行監控", key="monitor_watchlist"):
                    monitor = MonitorEngine(watchlist.stocks)
                    st.session_state["collab_monitor_results"] = monitor.check_signals(strategy_name="MA Crossover")
        else:
            st.info("目前沒有共享 watchlist。")

        with st.expander("建立共享 watchlist", expanded=False):
            watchlist_name = st.text_input("名稱", key="collab_new_watchlist_name")
            watchlist_owner = st.text_input("Owner", value="team", key="collab_new_watchlist_owner")
            watchlist_stocks = st.text_input("股票（逗號分隔）", value="2330,2317", key="collab_new_watchlist_stocks")
            watchlist_desc = st.text_area("描述", key="collab_new_watchlist_desc")
            if st.button("建立 watchlist", key="collab_create_watchlist"):
                watchlist = Watchlist(
                    name=watchlist_name,
                    owner=watchlist_owner,
                    stocks=[item.strip() for item in watchlist_stocks.split(",") if item.strip()],
                    description=watchlist_desc,
                )
                store.save_watchlist(watchlist)
                st.success("watchlist 已建立。")
                st.rerun()

    with top_right:
        st.subheader("研究筆記共享")
        recent_notes = store.list_research_notes(limit=10)
        if recent_notes:
            st.dataframe(
                pd.DataFrame(
                    [
                        {
                            "標題": note.title,
                            "股票": note.stock_id,
                            "作者": note.author,
                            "更新": note.updated_at,
                        }
                        for note in recent_notes
                    ]
                ),
                width="stretch",
                hide_index=True,
            )
        else:
            st.info("目前沒有共享筆記。")

        with st.expander("新增協作筆記", expanded=False):
            note_title = st.text_input("標題", key="collab_note_title")
            note_stock = st.text_input("股票代碼（可空白）", key="collab_note_stock")
            note_author = st.text_input("作者", value="team", key="collab_note_author")
            note_tags = st.text_input("標籤", value="handoff,team", key="collab_note_tags")
            note_content = st.text_area("內容", key="collab_note_content")
            if st.button("保存協作筆記", key="collab_save_note"):
                note = ResearchNote(
                    title=note_title,
                    stock_id=note_stock or None,
                    tags=[item.strip() for item in note_tags.split(",") if item.strip()],
                    content=note_content,
                    author=note_author,
                )
                store.save_research_note(note)
                st.success("協作筆記已保存。")
                st.rerun()

    monitor_results = st.session_state.get("collab_monitor_results")
    if isinstance(monitor_results, pd.DataFrame) and not monitor_results.empty:
        st.markdown("---")
        st.subheader("手動監控結果")
        st.dataframe(monitor_results, width="stretch", hide_index=True)

    st.markdown("---")
    extra_left, extra_right = st.columns(2)
    with extra_left:
        st.subheader("近期工作日誌")
        for entry in _extract_recent_worklog_entries(Path(__file__).resolve().parents[1] / "WORKLOG.md"):
            with st.expander(entry.splitlines()[0], expanded=False):
                st.markdown("\n".join(entry.splitlines()[1:]))

    with extra_right:
        st.subheader("Legacy 投組狀態")
        portfolios = pm.list_portfolios()
        st.metric("Legacy Portfolios", len(portfolios))
        if portfolios:
            st.dataframe(
                pd.DataFrame(
                    [
                        {
                            "名稱": item.get("name"),
                            "策略": item.get("strategy"),
                            "更新": item.get("updated_at", "")[:19],
                        }
                        for item in portfolios[:10]
                    ]
                ),
                width="stretch",
                hide_index=True,
            )
