import pandas as pd
import streamlit as st

from backtest.engine import get_backtest_strategy_catalog, run_named_backtest
from data.fetcher import DataFetcher
from data.workspace_models import BacktestRun, TradePlan
from data.workspace_store import WorkspaceStore


def _get_source_options(store: WorkspaceStore) -> tuple[dict[str, tuple[str, str | None]], pd.DataFrame | None, dict]:
    options: dict[str, tuple[str, str | None]] = {}
    session_df = st.session_state.get("strategy_scan_results")
    session_meta = st.session_state.get("strategy_scan_meta", {})
    if isinstance(session_df, pd.DataFrame) and not session_df.empty:
        options["目前 session 掃描結果"] = ("session", None)
    for run in store.list_screen_runs(limit=20):
        options[f"{run.executed_at} | {run.name}"] = ("stored", run.id)
    return options, session_df, session_meta


def _render_strategy_params(strategy_name: str, spec: dict) -> dict[str, object]:
    param_specs = spec.get("params", {})
    if not param_specs:
        return {}

    st.markdown("#### 回測參數")
    values: dict[str, object] = {}
    columns = st.columns(2)

    for idx, (param_name, param_spec) in enumerate(param_specs.items()):
        label = param_spec.get("label", param_name)
        param_type = param_spec.get("type", "str")
        default_value = param_spec.get("default", 0)
        key = f"validation_param_{strategy_name}_{param_name}"

        with columns[idx % len(columns)]:
            if param_type == "int":
                input_kwargs = {
                    "value": int(default_value),
                    "step": int(param_spec.get("step", 1)),
                    "key": key,
                }
                if param_spec.get("min") is not None:
                    input_kwargs["min_value"] = int(param_spec["min"])
                if param_spec.get("max") is not None:
                    input_kwargs["max_value"] = int(param_spec["max"])
                values[param_name] = st.number_input(label, **input_kwargs)
            elif param_type == "float":
                input_kwargs = {
                    "value": float(default_value),
                    "step": float(param_spec.get("step", 0.1)),
                    "format": param_spec.get("format", "%.2f"),
                    "key": key,
                }
                if param_spec.get("min") is not None:
                    input_kwargs["min_value"] = float(param_spec["min"])
                if param_spec.get("max") is not None:
                    input_kwargs["max_value"] = float(param_spec["max"])
                values[param_name] = st.number_input(label, **input_kwargs)
            elif param_type == "bool":
                values[param_name] = st.checkbox(label, value=bool(default_value), key=key)
            else:
                values[param_name] = st.text_input(label, value=str(default_value), key=key)

            if param_spec.get("help"):
                st.caption(param_spec["help"])

    return values


def render_validation_page() -> None:
    store = WorkspaceStore()
    st.header("🧪 驗證中心")
    st.caption("從 ScreenRun 或目前 session 掃描結果挑選標的，執行回測並保存 BacktestRun。")

    source_options, session_df, session_meta = _get_source_options(store)
    if not source_options:
        st.warning("目前沒有可用的掃描結果。請先到策略工作台執行掃描。")
        return

    selected_source = st.selectbox("驗證來源", list(source_options.keys()), key="validation_source")
    source_type, source_id = source_options[selected_source]

    if source_type == "session":
        df_candidates = session_df.copy()
        meta = session_meta
        screen_run_id = st.session_state.get("latest_screen_run_id")
    else:
        screen_run = store.get_screen_run(source_id)
        if not screen_run:
            st.error("找不到指定的 ScreenRun。")
            return
        df_candidates = pd.DataFrame(screen_run.results)
        meta = {
            "strategies": [strategy.name for strategy in screen_run.strategies],
            "market": screen_run.market_scope,
            "mode": screen_run.match_mode,
            "time": screen_run.executed_at,
        }
        screen_run_id = screen_run.id

    if df_candidates.empty:
        st.warning("來源存在，但沒有候選標的。")
        return

    st.dataframe(df_candidates, width="stretch", hide_index=True)

    candidate_ids = df_candidates["Stock ID"].astype(str).tolist()
    source_strategy_names = meta.get("strategies", [])
    strategy_catalog = get_backtest_strategy_catalog(source_strategy_names)
    if not strategy_catalog:
        st.warning("目前沒有可用的回測策略。")
        return

    preferred_options = [name for name in source_strategy_names if name in strategy_catalog]
    strategy_options = preferred_options + [
        name for name in strategy_catalog.keys() if name not in preferred_options
    ]

    bt_col1, bt_col2, bt_col3, bt_col4 = st.columns(4)
    with bt_col1:
        stock_id = st.selectbox("股票", candidate_ids, key="validation_stock")
    with bt_col2:
        strategy_name = st.selectbox("回測策略", strategy_options, key="validation_strategy")
    with bt_col3:
        period = st.selectbox("回測期間", ["1y", "2y", "5y"], index=1, key="validation_period")
    with bt_col4:
        starting_cash = st.number_input(
            "起始資金",
            min_value=100_000,
            max_value=100_000_000,
            value=1_000_000,
            step=100_000,
            key="validation_starting_cash",
        )

    commission_rate = st.number_input(
        "手續費率",
        min_value=0.0,
        max_value=0.05,
        value=0.001425,
        step=0.0001,
        format="%.4f",
        key="validation_commission_rate",
    )

    selected_spec = strategy_catalog[strategy_name]
    if selected_spec["mode"] == "backtrader":
        st.info(f"目前以 Backtrader 執行：{selected_spec['description']}")
    else:
        st.info(selected_spec["fallback_note"])
        st.caption(selected_spec["description"])

    strategy_params = _render_strategy_params(strategy_name, selected_spec)

    if st.button("執行回測並保存", key="run_validation_backtest"):
        stock_name, _, _ = DataFetcher.get_stock_info(stock_id)
        try:
            result = run_named_backtest(
                stock_id=stock_id,
                strategy_name=strategy_name,
                period=period,
                strategy_params=strategy_params,
                starting_cash=float(starting_cash),
                commission_rate=float(commission_rate),
            )
        except Exception as exc:
            st.error(f"回測失敗：{exc}")
            return

        price_df = result["price_df"]
        benchmark_return_pct = 0.0
        if len(price_df) > 1 and price_df["Close"].iloc[0]:
            benchmark_return_pct = ((price_df["Close"].iloc[-1] - price_df["Close"].iloc[0]) / price_df["Close"].iloc[0]) * 100

        backtest_run = BacktestRun.from_engine_result(
            stock_id=stock_id,
            stock_name=stock_name,
            strategy_name=strategy_name,
            period=period,
            starting_cash=float(starting_cash),
            final_value=float(result["final_value"]),
            trades=result["trades"].to_dict(orient="records"),
            strategy_params=result["strategy_params"],
            screen_run_id=screen_run_id,
            benchmark_return_pct=benchmark_return_pct,
            notes=f"來源策略：{', '.join(meta.get('strategies', []))} | 驗證模式：{result['mode']}",
            fallback_note=result["fallback_note"],
            commission_rate=float(commission_rate),
        )
        store.save_backtest_run(backtest_run)
        st.session_state["latest_backtest_run_id"] = backtest_run.id
        st.success(f"BacktestRun 已保存：{backtest_run.id}")

    latest_id = st.session_state.get("latest_backtest_run_id")
    latest_backtest = store.get_backtest_run(latest_id) if latest_id else None
    if latest_backtest:
        st.markdown("---")
        st.subheader("最近回測結果")
        metrics = st.columns(4)
        metrics[0].metric("最終資產", f"{latest_backtest.final_value:,.0f}")
        metrics[1].metric("總報酬", f"{latest_backtest.total_return_pct:.2f}%")
        metrics[2].metric("基準報酬", f"{(latest_backtest.benchmark_return_pct or 0):.2f}%")
        metrics[3].metric("交易數", len(latest_backtest.trades))

        if latest_backtest.fallback_note:
            st.caption(latest_backtest.fallback_note)

        if latest_backtest.trades:
            st.dataframe(pd.DataFrame(latest_backtest.trades), width="stretch", hide_index=True)

        st.subheader("建立交易計畫")
        thesis = st.text_area(
            "投資論述",
            value=f"基於 {latest_backtest.strategy_name} 回測結果，評估 {latest_backtest.stock_id} 作為模擬交易候選。",
            key="trade_plan_thesis",
        )
        entry_idea = st.text_input("Entry Idea", value="等待下一個確認訊號後分批進場", key="trade_plan_entry")
        stop_loss = st.text_input("Stop Loss", value="跌破前波支撐即檢討", key="trade_plan_sl")
        take_profit = st.text_input("Take Profit", value="分段停利，至少保留一筆趨勢倉", key="trade_plan_tp")
        size_note = st.text_input("部位規劃", value="先用模擬資金 10% 建倉", key="trade_plan_size")
        risk_checks = st.text_input(
            "Risk Checks（逗號分隔）",
            value="確認流動性,確認停損條件,確認事件風險",
            key="trade_plan_risk_checks",
        )

        if st.button("建立 TradePlan", key="create_trade_plan"):
            trade_plan = TradePlan(
                screen_run_id=latest_backtest.screen_run_id,
                backtest_run_id=latest_backtest.id,
                stock_id=latest_backtest.stock_id,
                stock_name=latest_backtest.stock_name,
                strategy_name=latest_backtest.strategy_name,
                thesis=thesis,
                entry_idea=entry_idea,
                stop_loss=stop_loss,
                take_profit=take_profit,
                size_note=size_note,
                risk_checks=[item.strip() for item in risk_checks.split(",") if item.strip()],
                tags=["validation", latest_backtest.strategy_name],
            )
            store.save_trade_plan(trade_plan)
            st.session_state["latest_trade_plan_id"] = trade_plan.id
            st.success(f"TradePlan 已建立：{trade_plan.id}")
