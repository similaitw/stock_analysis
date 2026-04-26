from data.workspace_models import BacktestRun, PaperOrder, ResearchNote, ScreenRun, TradePlan, Watchlist
from data.workspace_store import WorkspaceStore


def test_workspace_store_roundtrip(tmp_path):
    store = WorkspaceStore(base_dir=str(tmp_path / "workspace"))

    screen_run = ScreenRun.from_scan_results(
        name="Test Run",
        market_scope="TEST",
        stock_pool=["2330", "2303"],
        strategy_names=["MA Crossover"],
        match_mode="OR",
        results=[{"Stock ID": "2330", "Name": "TSMC", "Price": 950.0, "Signal": "Golden Cross"}],
    )
    store.save_screen_run(screen_run)

    backtest_run = BacktestRun.from_engine_result(
        stock_id="2330",
        stock_name="TSMC",
        strategy_name="MA Crossover",
        period="1y",
        starting_cash=1_000_000,
        final_value=1_050_000,
        trades=[{"Action": "BUY"}],
        screen_run_id=screen_run.id,
    )
    store.save_backtest_run(backtest_run)

    trade_plan = TradePlan(
        screen_run_id=screen_run.id,
        backtest_run_id=backtest_run.id,
        stock_id="2330",
        stock_name="TSMC",
        strategy_name="MA Crossover",
        thesis="Follow through after validation",
    )
    store.save_trade_plan(trade_plan)
    store.update_trade_plan_status(trade_plan.id, "ready")

    paper_order = PaperOrder(
        trade_plan_id=trade_plan.id,
        stock_id="2330",
        stock_name="TSMC",
        side="BUY",
        quantity=1000,
        intended_price=950.0,
    )
    store.save_paper_order(paper_order)
    store.update_paper_order_status(paper_order.id, "filled", 952.5)

    watchlist = Watchlist(name="Team Focus", owner="team", stocks=["2330"])
    store.save_watchlist(watchlist)
    store.add_stock_to_watchlist(watchlist.id, "2317")

    note = ResearchNote(title="Morning note", stock_id="2330", content="Watch reaction around support.")
    store.save_research_note(note)

    assert len(store.list_screen_runs()) == 1
    assert len(store.list_signal_events()) == 1
    assert store.get_backtest_run(backtest_run.id).stock_id == "2330"
    assert store.get_trade_plan(trade_plan.id).status == "ready"
    assert store.get_paper_order(paper_order.id).filled_price == 952.5
    assert store.get_watchlist(watchlist.id).stocks == ["2330", "2317"]
    assert len(store.list_research_notes(stock_id="2330")) == 1

    snapshot = store.get_dashboard_snapshot()
    assert snapshot["counts"]["screen_runs"] == 1
    assert snapshot["counts"]["pending_orders"] == 0
