"""
策略選股頁面
Strategy Scanner Page
"""
import streamlit as st
import pandas as pd
from datetime import datetime
from scanner.engine import ScannerEngine
from portfolios import PortfolioManager
from reports import ExcelReportGenerator

def render_scanner_page():
    """渲染策略選股頁面"""
    st.header("策略選股 (Strategy Scanner)")
    
    # === 主頁面參數設定 ===
    st.markdown("### 🔍 選股參數設定")
    
    col_market, col_strategy = st.columns([1, 2])
    
    with col_market:
        scan_market = st.selectbox("掃描範圍 (Market)", ["TEST", "Tw50", "Tw100", "All"], index=1)
    
    with col_strategy:
        scan_strategy = st.selectbox("選股策略 (Strategy)", _get_strategy_options(), index=1)
    
    st.markdown("---")
    
    # 載入組合功能
    _render_portfolio_loader()
    
    scan_btn = st.button("🚀 開始掃描", type="primary", width='stretch')
    
    if scan_btn:
        _execute_scan(scan_strategy, scan_market)


def _render_portfolio_loader():
    """渲染組合載入功能"""
    with st.expander("📂 載入已儲存的組合", expanded=False):
        pm = PortfolioManager()
        portfolios = pm.list_portfolios()
        
        if portfolios:
            portfolio_options = {
                f"{p['name']} ({p['updated_at'][:10]})": p['id'] 
                for p in portfolios
            }
            
            selected_portfolio_name = st.selectbox(
                "選擇組合",
                options=list(portfolio_options.keys()),
                key="portfolio_selector"
            )
            
            col_load1, col_load2 = st.columns([1, 3])
            
            with col_load1:
                if st.button("📥 載入組合", key="load_portfolio_btn"):
                    portfolio_id = portfolio_options[selected_portfolio_name]
                    portfolio = pm.load_portfolio(portfolio_id)
                    
                    if portfolio:
                        st.session_state.loaded_portfolio = portfolio
                        st.success(f"✅ 已載入組合：{portfolio['name']}")
                        st.info(f"策略: {portfolio['strategy']} | 市場: {portfolio['market']}")
                        
                        latest = pm.get_latest_result(portfolio_id)
                        if latest:
                            st.caption(f"最新選股時間: {latest['date']}")
                            st.caption(f"符合條件: {latest['count']} 檔")
            
            with col_load2:
                if st.button("🔄 重新執行組合", key="rerun_portfolio_btn"):
                    portfolio_id = portfolio_options[selected_portfolio_name]
                    portfolio = pm.load_portfolio(portfolio_id)
                    
                    if portfolio:
                        st.session_state.rerun_portfolio_id = portfolio_id
                        st.session_state.rerun_portfolio_strategy = portfolio['strategy']
                        st.session_state.rerun_portfolio_market = portfolio['market']
                        st.info(f"🔄 將使用 {portfolio['strategy']} 策略重新掃描...")
        else:
            st.info("尚無儲存的組合")


def _execute_scan(strategy: str, market: str):
    """執行選股掃描"""
    st.markdown("---")
    st.subheader(f"📊 選股結果: {strategy}")
    st.caption(f"市場範圍: {market}")
    
    # 初始化掃描引擎
    engine = ScannerEngine()
    
    # 執行掃描
    with st.spinner(f"🔍 正在掃描 {market} 市場..."):
        try:
            results = engine.scan(strategy=strategy, market=market)
            
            if results and len(results) > 0:
                df_res = pd.DataFrame(results)
                
                st.success(f"✅ 掃描完成！找到 {len(df_res)} 檔符合條件的股票")
                
                # 顯示結果
                st.dataframe(
                    df_res,
                    width='stretch',
                    hide_index=True
                )
                
                # 儲存到 session_state
                st.session_state.scan_results = df_res
                
                # 組合管理功能
                _render_portfolio_management(strategy, market, df_res)
                
                # 匯出報告
                _render_export_button(strategy, market, df_res)
                
                # 快速回測
                _render_quick_backtest(df_res)
                
            else:
                st.warning("⚠️ 沒有找到符合條件的股票")
                
        except Exception as e:
            st.error(f"❌ 掃描過程發生錯誤：{e}")
            with st.expander("📋 錯誤詳情"):
                st.exception(e)


def _render_portfolio_management(strategy: str, market: str, df_res: pd.DataFrame):
    """渲染組合管理功能"""
    st.markdown("---")
    st.subheader("💾 組合管理")
    
    col_save1, col_save2, col_save3 = st.columns([2, 2, 1])
    
    with col_save1:
        portfolio_name = st.text_input(
            "組合名稱",
            value=f"{strategy}_{market}_{datetime.now().strftime('%m%d')}",
            key="portfolio_name_input"
        )
    
    with col_save2:
        portfolio_desc = st.text_input(
            "組合描述（可選）",
            value=f"使用 {strategy} 策略在 {market} 市場選股",
            key="portfolio_desc_input"
        )
    
    with col_save3:
        if st.button("💾 儲存組合", type="secondary", key="save_portfolio_btn"):
            pm = PortfolioManager()
            stock_ids = df_res['Stock ID'].tolist()
            
            try:
                portfolio = pm.create_portfolio(
                    name=portfolio_name,
                    description=portfolio_desc,
                    strategy=strategy,
                    market=market,
                    stocks=stock_ids
                )
                st.success(f"✅ 組合已儲存：{portfolio_name}")
            except Exception as e:
                st.error(f"❌ 儲存失敗：{e}")


def _render_export_button(strategy: str, market: str, df_res: pd.DataFrame):
    """渲染匯出報告按鈕"""
    if st.button("📥 匯出選股報告", key="export_scanner"):
        generator = ExcelReportGenerator()
        try:
            filepath = generator.generate_scanner_report(
                strategy=strategy,
                market=market,
                results=df_res
            )
            st.success(f"✅ 報告已匯出：{filepath}")
        except Exception as e:
            st.error(f"❌ 匯出失敗：{e}")


def _render_quick_backtest(df_res: pd.DataFrame):
    """渲染快速回測功能"""
    st.markdown("---")
    st.subheader("📊 快速回測")
    
    col_bt1, col_bt2, col_bt3 = st.columns(3)
    
    with col_bt1:
        bt_ticker = st.selectbox(
            "選擇股票",
            options=df_res['Stock ID'].tolist(),
            key="quick_backtest_ticker"
        )
    
    with col_bt2:
        bt_period = st.selectbox(
            "回測期間",
            options=["3mo", "6mo", "1y"],
            index=2,
            key="quick_backtest_period"
        )
    
    with col_bt3:
        if st.button("🚀 執行回測", key="quick_backtest_btn"):
            st.info(f"正在回測 {bt_ticker}...")
            # 這裡可以整合回測功能
            st.warning("快速回測功能開發中...")


def _get_strategy_options():
    """取得選股策略清單"""
    # Load Strategy Registry
    from strategies.registry import StrategyRegistry
    
    # Base Legacy Strategies (Hardcoded in Engine)
    options = [
        "--- 傳統策略 (Legacy) ---",
        "MA Crossover",
        "RSI Oversold",
        "Bollinger Buy",
        "Advanced Funnel",
        "Best Combo"
    ]
    
    # Dynamic Strategies from Registry
    registry_strats = StrategyRegistry.get_all_strategies()
    
    # Map categories to display names
    cat_map = {
        '04_Price_Volume': 'XScript 價量選股 (Price/Vol)',
        '05_Pattern': 'XScript 型態選股 (Pattern)',
        '06_Chip': '籌碼選股 (Chip)',
        '00_XScript_Common': 'XScript 常用指標'
    }
    
    for cat, strats in registry_strats.items():
        if not strats: continue
        display_name = cat_map.get(cat, cat)
        options.append(f"--- {display_name} ---")
        options.extend(strats)
        
    return options
