import importlib
import os
import sys

import streamlit as st


PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

try:
    import config

    importlib.reload(config)
    from config import Config
except ImportError:
    class Config:  # type: ignore[override]
        @staticmethod
        def has_finmind_token() -> bool:
            return False

        @staticmethod
        def should_use_finmind() -> bool:
            return False

from ui.collaboration_page import render_collaboration_page
from ui.execution_page import render_execution_page
from ui.home_page import render_home_page
from ui.navigation import get_navigation_options, get_section_by_label
from ui.research_page import render_research_page
from ui.strategy_workspace_page import render_strategy_workspace_page
from ui.validation_page import render_validation_page


st.set_page_config(page_title="台股研究協作與模擬執行平台", layout="wide")

st.title("台股研究協作與模擬執行平台")
st.caption("台股優先 | 小團隊工具 | 模擬執行邊界 | 交接文件驅動")

st.sidebar.header("Workspace")
selected_label = st.sidebar.radio("主區導航", get_navigation_options(), index=0)
selected_section = get_section_by_label(selected_label)

st.sidebar.markdown("---")
st.sidebar.subheader("資料來源狀態")
if Config.has_finmind_token():
    st.sidebar.success("FinMind Token 已連線")
else:
    st.sidebar.info("目前以 yfinance / twstock fallback 為主")

st.sidebar.markdown("---")
st.sidebar.caption(selected_section.description)
st.sidebar.caption("交接規則：每次 repo 變更後同步更新 WORKLOG.md")

if selected_section.id == "home":
    render_home_page()
elif selected_section.id == "research":
    render_research_page()
elif selected_section.id == "strategy":
    render_strategy_workspace_page()
elif selected_section.id == "validation":
    render_validation_page()
elif selected_section.id == "execution":
    render_execution_page()
elif selected_section.id == "collab":
    render_collaboration_page()
