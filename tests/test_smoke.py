from pathlib import Path


def test_config_import_and_env_discovery():
    from config import Config
    import config

    env_path = Path(config.__file__).resolve().with_name(".env")

    assert env_path.exists()
    assert isinstance(Config.has_finmind_token(), bool)
    assert isinstance(Config.should_use_finmind(), bool)


def test_core_modules_import():
    import backtest.engine  # noqa: F401
    import data.fetcher  # noqa: F401
    import monitor.engine  # noqa: F401
    import portfolios.manager  # noqa: F401


def test_generated_strategy_package_import():
    from strategies.auto_generated.選股.p_02_基本技術指標.strategies import (
        Cat02基本技術指標Strategies,
    )

    assert hasattr(Cat02基本技術指標Strategies, "MACD黃金交叉")


def test_strategy_registry_exposes_expected_categories():
    from strategies.registry import StrategyRegistry

    StrategyRegistry.initialize()
    categories = StrategyRegistry.get_all_strategies()

    assert "04_Price_Volume" in categories
    assert "05_Pattern" in categories
    assert "00_XScript_Common" in categories


def test_run_bat_targets_next_ui():
    run_bat = Path(__file__).resolve().parents[1] / "run.bat"
    contents = run_bat.read_text(encoding="utf-8")

    assert "npm run db:generate" in contents
    assert "npm run db:push" in contents
    assert "npm run dev" in contents


def test_legacy_run_bat_targets_streamlit_app():
    run_bat = Path(__file__).resolve().parents[1] / "run_streamlit_legacy.bat"
    contents = run_bat.read_text(encoding="utf-8")

    assert "streamlit run ui\\app.py" in contents
