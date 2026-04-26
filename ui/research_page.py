import pandas as pd
import streamlit as st

from ai.predictor import StockPredictor
from data.fetcher import DataFetcher
from data.storage import Storage
from data.workspace_models import ResearchNote, Watchlist
from data.workspace_store import WorkspaceStore
from ui.charts import render_interactive_chart


def _load_stock_options() -> tuple[list[str], pd.DataFrame]:
    try:
        df_stocks = Storage.load_stock_list()
        if not df_stocks.empty:
            df_stocks = df_stocks.copy()
            df_stocks["label"] = (
                df_stocks["code"].astype(str)
                + " "
                + df_stocks["name"].astype(str)
                + " ("
                + df_stocks["market"].astype(str)
                + ")"
            )
            return df_stocks["label"].tolist(), df_stocks
    except Exception:
        pass
    return [], pd.DataFrame()


def render_research_page() -> None:
    store = WorkspaceStore()
    stock_options, _ = _load_stock_options()

    st.header("🔎 股票研究")
    st.caption("單一股票研究工作台，整合圖表、基本面、籌碼、研究筆記與輔助 AI 觀察。")

    ticker = "2330"
    controls = st.columns([3, 1])
    with controls[0]:
        if stock_options:
            selected = st.selectbox("選擇股票", stock_options, index=0)
            ticker = selected.split(" ")[0]
        else:
            ticker = st.text_input("股票代碼", value="2330")
    with controls[1]:
        period = st.selectbox("期間", ["3mo", "6mo", "1y", "2y", "5y"], index=2)

    name, industry, desc = DataFetcher.get_stock_info(ticker)
    st.subheader(f"{ticker} {name} | {industry}")
    if desc:
        st.caption(desc)

    df = DataFetcher.fetch_history(ticker, period=period)
    if df.empty:
        st.error("目前無法取得這檔股票的歷史資料。")
        return

    current_price = DataFetcher.fetch_current_price(ticker)
    first_close = df["Close"].iloc[0]
    total_return = ((df["Close"].iloc[-1] - first_close) / first_close) * 100 if first_close else 0.0
    recent_signals = store.list_signal_events(stock_id=ticker, limit=10)

    metrics = st.columns(4)
    metrics[0].metric("現價", f"{current_price:.2f}")
    metrics[1].metric("期間報酬", f"{total_return:+.2f}%")
    metrics[2].metric("資料筆數", len(df))
    metrics[3].metric("近期訊號", len(recent_signals))

    fig = render_interactive_chart(
        df,
        ticker,
        overlays=["MA20", "MA60", "Bollinger"],
        indicators=["Volume", "RSI"],
    )
    st.plotly_chart(fig, width="stretch")

    st.markdown("---")
    st.subheader("研究摘要")
    fundamentals = DataFetcher.fetch_fundamentals(ticker)
    f1, f2, f3, f4 = st.columns(4)
    f1.metric("Revenue YoY", f"{fundamentals.get('Revenue YoY', 0):.2f}%")
    f2.metric("Margin", f"{fundamentals.get('Margin', 0):.2f}%")
    f3.metric("EPS", f"{fundamentals.get('EPS', 0):.2f}")
    f4.metric("Yield", f"{fundamentals.get('Yield', 0):.2f}%")

    with st.expander("🤖 AI 輔助觀察", expanded=False):
        st.caption("AI 預測保留為研究附屬能力，不作為主決策依據。")
        if st.button("產生 AI 觀察", key="research_ai_predict"):
            predictor = StockPredictor()
            prediction = predictor.predict_next_day(ticker)
            if not prediction:
                st.warning("目前無法產生 AI 預測。")
            elif prediction.get("error"):
                st.warning(prediction["error"])
            else:
                st.write(
                    {
                        "prediction": prediction["prediction"],
                        "probability_up": round(prediction["probability_up"], 4),
                        "probability_down": round(prediction["probability_down"], 4),
                        "last_date": str(prediction["last_date"]),
                    }
                )

    st.markdown("---")
    note_col, watchlist_col = st.columns(2)

    with note_col:
        st.subheader("研究筆記")
        note_title = st.text_input("筆記標題", value=f"{ticker} 研究筆記", key="note_title")
        note_author = st.text_input("作者", value="codex-agent", key="note_author")
        note_tags = st.text_input("標籤（逗號分隔）", value=f"{ticker},research", key="note_tags")
        note_content = st.text_area("內容", height=180, key="note_content")
        if st.button("儲存研究筆記", key="save_research_note"):
            note = ResearchNote(
                title=note_title,
                stock_id=ticker,
                tags=[tag.strip() for tag in note_tags.split(",") if tag.strip()],
                content=note_content,
                author=note_author,
            )
            store.save_research_note(note)
            st.success("研究筆記已保存。")

        notes = store.list_research_notes(stock_id=ticker, limit=5)
        if notes:
            st.caption("最近筆記")
            for note in notes:
                with st.expander(f"{note.title} | {note.updated_at}"):
                    st.write(note.content)
                    if note.tags:
                        st.caption("Tags: " + ", ".join(note.tags))

    with watchlist_col:
        st.subheader("共享 Watchlist")
        watchlists = store.list_watchlists(limit=20)
        if watchlists:
            mapping = {f"{item.name} ({item.owner})": item.id for item in watchlists}
            selected_watchlist = st.selectbox("加入既有 watchlist", list(mapping.keys()), key="research_watchlist_select")
            if st.button("加入至 watchlist", key="add_to_watchlist"):
                store.add_stock_to_watchlist(mapping[selected_watchlist], ticker)
                st.success(f"已將 {ticker} 加入 {selected_watchlist}。")
        else:
            st.info("目前沒有既有 watchlist，可直接建立新的。")

        new_watchlist_name = st.text_input("新 watchlist 名稱", value=f"{ticker} Focus List", key="new_watchlist_name")
        new_watchlist_owner = st.text_input("Owner", value="team", key="new_watchlist_owner")
        if st.button("建立含此股票的 watchlist", key="create_watchlist"):
            watchlist = Watchlist(
                name=new_watchlist_name,
                owner=new_watchlist_owner,
                stocks=[ticker],
                description=f"由研究頁建立，初始股票：{ticker}",
            )
            store.save_watchlist(watchlist)
            st.success("watchlist 已建立。")

        if recent_signals:
            signal_df = pd.DataFrame(
                [
                    {
                        "時間": event.detected_at,
                        "原因": event.reason,
                        "價格": event.price,
                    }
                    for event in recent_signals
                ]
            )
            st.caption("近期訊號")
            st.dataframe(signal_df, width="stretch", hide_index=True)
