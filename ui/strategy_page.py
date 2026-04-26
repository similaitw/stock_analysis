import streamlit as st
import pandas as pd
from datetime import datetime
from scanner.engine import ScannerEngine
from portfolios import PortfolioManager
from reports import ExcelReportGenerator
from ui.language import Language

def render_strategy_page():
    """渲染策略實驗室頁面"""
    st.header("🔬 策略實驗室 (Strategy Lab)")
    st.caption("Cross-combine strategies to find the best trading opportunities.")
    
    # === 1. 控制面板 ===
    with st.expander("🛠️ 策略設定 (Configuration)", expanded=True):
        
        # --- Presets & Clear ---
        col_preset, col_clear = st.columns([3, 1])
        with col_preset:
            presets = {
                "自訂 (Custom)": [],
                "保守型 (Conservative)": ["XScript - W底型態", "MA Crossover"],
                "積極型 (Aggressive)": ["XScript - 價量齊揚", "XScript - Momentum Breakout"],
                "技術指標型 (Technical)": ["XScript - KD黃金交叉", "XScript - MACD黃金交叉"],
                "籌碼型 (Chips)": ["XScript - 3 Red Soldiers"] # Example
            }
            
            selected_preset = st.selectbox(
                "✨ 快速組合 (Presets)", 
                list(presets.keys()),
                index=0,
                key="strat_preset_select"
            )
        
        with col_clear:
            st.write("") # Adjust alignment
            st.write("")
            if st.button("🗑️ 清除所有 (Clear)", width='stretch'):
                st.session_state.clear_strategies = True
                st.rerun()

        st.markdown("---")

        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.subheader("1. 掃描範圍")
            
            # Load stock list for industry filtering
            from data.storage import Storage
            df_stocks = Storage.load_stock_list()
            
            # Prepare options
            industries = ["Tw50", "Tw100", "All", "TEST"]
            if not df_stocks.empty and 'industry' in df_stocks.columns:
                unique_industries = sorted(df_stocks['industry'].dropna().unique().tolist())
                industries.extend([f"Industry: {ind}" for ind in unique_industries])
            
            market_type_select = st.selectbox(
                "Market Scope",
                industries,
                index=0,
                help="Select Tw50/All or a specific Industry sector."
            )
            
            # Determine actual market type and stock list
            stock_list = None
            market_type_label = market_type_select
            
            if market_type_select.startswith("Industry: "):
                selected_ind = market_type_select.split(": ")[1]
                if not df_stocks.empty:
                    stock_list = df_stocks[df_stocks['industry'] == selected_ind]['code'].tolist()
                    st.caption(f"Sector '{selected_ind}': {len(stock_list)} stocks")
                market_type = "Custom"
            else:
                market_type = market_type_select

            st.subheader("2. 篩選邏輯")
            match_mode = st.radio(
                "Match Logic",
                ["AND (Intersection)", "OR (Union)"],
                index=0,
                help="AND: Stock must match ALL strategies.\nOR: Stock can match ANY strategy."
            )
            mode_code = 'AND' if 'AND' in match_mode else 'OR'
            
        with col2:
            st.subheader("3. 選擇策略")
            
            # Handle Preset Logic
            default_selections = []
            if selected_preset != "自訂 (Custom)":
                default_selections = presets[selected_preset]
            
            # Handle Clear Logic
            if st.session_state.get('clear_strategies'):
                default_selections = []
                st.session_state.clear_strategies = False # Reset flag
            
            # Strategy Groups
            # Strategy Groups (Dynamic)
            strategy_groups = _get_lab_strategy_groups()
            
            selected_strategies = []
            tabs = st.tabs(list(strategy_groups.keys()))
            
            for i, (group_name, strategies) in enumerate(strategy_groups.items()):
                with tabs[i]:
                    # Determine defaults for this group based on preset
                    group_defaults = [s for s in default_selections if s in strategies]
                    
                    selection = st.multiselect(
                        f"Select {group_name}",
                        strategies,
                        default=group_defaults,
                        key=f"strat_select_{i}_{selected_preset}_{st.session_state.get('clear_strategies')}" 
                        # Key trick to force reset when preset changes
                    )
                    selected_strategies.extend(selection)
    
    # === 1.5 參數設定 (Parameter Configuration) ===
    # Stores parameters for each strategy: { 'strategy_name': { 'param': value } }
    strategy_params_config = {}
    
    if selected_strategies:
        # Import registry to get params
        from strategies.registry import StrategyRegistry
        
        # Check if any selected strategy has configurable parameters
        has_params = False
        temp_params = {} # params for each strategy
        
        for strat_name in selected_strategies:
            params = StrategyRegistry.get_strategy_params(strat_name)
            if params:
                has_params = True
                temp_params[strat_name] = params
        
        if has_params:
            with st.expander("⚙️ 策略參數設定 (Strategy Parameters)", expanded=True):
                st.caption("Adjust parameters for selected strategies.")
                
                # Create 2 columns for parameters to save space
                p_cols = st.columns(2)
                col_idx = 0
                
                for strat_name, params in temp_params.items():
                    # Use a container or just write headers
                    with p_cols[col_idx % 2]:
                        st.markdown(f"**{strat_name}**")
                        strat_config = {}
                        
                        for p_name, p_info in params.items():
                            default_val = p_info.get('default', 0)
                            p_type = p_info.get('type', 'str')
                            
                            label = f"{p_name}"
                            key = f"param_{strat_name}_{p_name}"
                            
                            # Determine input widget based on type
                            if p_type == 'int':
                                val = st.number_input(label, value=int(default_val), step=1, key=key)
                            elif p_type == 'float':
                                val = st.number_input(label, value=float(default_val), step=0.1, format="%.2f", key=key)
                            elif p_type == 'bool':
                                val = st.checkbox(label, value=bool(default_val), key=key)
                            else:
                                val = st.text_input(label, value=str(default_val), key=key)
                                
                            strat_config[p_name] = val
                        
                        strategy_params_config[strat_name] = strat_config
                        st.markdown("---")
                    
                    col_idx += 1

    # === 2. 執行按鈕 ===
    st.markdown("---")
    
    col_action1, col_action2, col_info = st.columns([1, 1, 2])
    with col_action1:
        run_scan = st.button("🚀 執行掃描 (Run Scan)", type="primary", width='stretch')
    
    with col_action2:
        run_backtest = st.button("📊 回測策略 (Backtest)", width='stretch')
    
    with col_info:
        if selected_strategies:
            st.info(f"已選擇 {len(selected_strategies)} 個策略: {', '.join(selected_strategies)}")
        else:
            st.warning("⚠️ 請至少選擇一個策略")
            
    # === 3. 結果顯示 ===
    if run_scan and selected_strategies:
        with st.spinner(f"🔍 Scanning {market_type_label} with {len(selected_strategies)} strategies..."):
            try:
                # Execute Scan with Parameters
                df_results = ScannerEngine.scan_strategies(
                    strategy_names=selected_strategies,
                    market_type=market_type,
                    match_mode=mode_code,
                    stock_list=stock_list,
                    strategy_params=strategy_params_config # Pass the configured parameters
                )
                
                if not df_results.empty:
                    st.success(f"✅ 找到 {len(df_results)} 檔符合條件的股票")
                    st.session_state.strategy_scan_results = df_results
                    st.session_state.strategy_scan_meta = {
                        'strategies': selected_strategies,
                        'market': market_type_label,
                        'mode': mode_code,
                        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    }
                else:
                    st.warning("⚠️ 沒有找到符合條件的股票 (No matches found)")
                    st.session_state.strategy_scan_results = pd.DataFrame()
            except Exception as e:
                st.error(f"❌ 掃描發生錯誤: {e}")
    
    # Display Results if they exist in session state
    if 'strategy_scan_results' in st.session_state and not st.session_state.strategy_scan_results.empty:
        df_res = st.session_state.strategy_scan_results
        meta = st.session_state.get('strategy_scan_meta', {})
        
        st.markdown(f"### 📊 掃描結果 (Latest Results)")
        if meta:
            st.caption(f"Scanned at: {meta['time']} | Market: {meta['market']} | Mode: {meta['mode']}")
        
        st.dataframe(
            df_res,
            width='stretch',
            column_config={
                "Stock ID": st.column_config.TextColumn("代碼"),
                "Name": st.column_config.TextColumn("名稱"),
                "Price": st.column_config.TextColumn("收盤價"),
                "Signal": st.column_config.TextColumn("觸發信號", width="large"),
                "Volume": st.column_config.NumberColumn("成交量"),
                "Date": st.column_config.DateColumn("資料日期")
            },
            hide_index=True
        )
        
        # Tools for results
        st.markdown("---")
        st.subheader("🛠️ 結果操作 (Actions)")
        
        tab_save, tab_export, tab_viz = st.tabs(["💾 儲存為組合", "📥 匯出報告", "📈 視覺化比較"])
        
        with tab_save:
            col_s1, col_s2 = st.columns([3, 1])
            with col_s1:
                default_name = f"Auto_{meta.get('mode', 'Scan')}_{datetime.now().strftime('%m%d_%H%M')}"
                pf_name = st.text_input("Portfolio Name", value=default_name)
                pf_desc = st.text_input("Description", value=f"Strategies: {', '.join(meta.get('strategies', []))}")
            
            with col_s2:
                st.write("") # Spacer
                st.write("")
                if st.button("儲存組合 (Save)", key="save_strat_pf"):
                    pm = PortfolioManager()
                    try:
                        pm.create_portfolio(
                            name=pf_name,
                            description=pf_desc,
                            strategy=" + ".join(meta.get('strategies', [])),
                            market=meta.get('market', 'Tw50'),
                            stocks=df_res['Stock ID'].tolist()
                        )
                        st.success(f"✅ 組合 '{pf_name}' 已儲存！")
                    except Exception as e:
                        st.error(f"❌ 儲存失敗: {e}")
        
        with tab_export:
            if st.button("匯出 Excel 報告", key="export_strat_excel"):
                gen = ExcelReportGenerator()
                try:
                    path = gen.generate_scanner_report(
                        strategy="Combined_Strategies",
                        market=meta.get('market', ""),
                        results=df_res
                    )
                    st.success(f"✅ 報告已匯出: {path}")
                except Exception as e:
                    st.error(f"❌ 匯出失敗: {e}")
        
        with tab_viz:
            st.info("💡 Tip: Use the 'Stock Comparison' page for detailed comparison.")
            if st.button("傳送到「多股票比較」", key="send_to_compare"):
                 st.session_state.comparison_stock_list = df_res['Stock ID'].tolist()
                 st.success("✅ 已傳送清單！請切換至「多股票比較」頁面查看。")


def _get_lab_strategy_groups():
    """取得策略實驗室的策略分組"""
    # Strategy Groups (Dynamic)
    from strategies.registry import StrategyRegistry
    registry_strats = StrategyRegistry.get_all_strategies()
    
    # Map categories to display names in Strategy Lab
    # We map registry keys to the tabs used in this UI
    lab_cat_map = {
        '04_Price_Volume': 'XScript - 價量策略',
        '05_Pattern': 'XScript - 型態選股',
        '06_Chip': '籌碼選股',
        '00_XScript_Common': 'XScript - 技術指標', # Mapping common/technical here if needed
        '00_Legacy': '傳統指標'
    }
    
    strategy_groups = {}
    
    # 1. Add Legacy strategies if not in registry (or merge them)
    # The registry might have '00_Legacy' if we added them there, otherwise keep hardcoded fallback for legacy
    if '00_Legacy' in registry_strats:
            strategy_groups['傳統指標'] = registry_strats['00_Legacy']
    else:
            strategy_groups['傳統指標'] = [
            "MA Crossover",
            "RSI Oversold",
            "Bollinger Buy",
            "Advanced Funnel"
            ]

    # 2. Add New Strategies
    for cat, strats in registry_strats.items():
        if not strats or cat == '00_Legacy': continue
        
        # Determine Tab Name
        tab_name = lab_cat_map.get(cat, cat)
        
        # Merge if key exists (e.g. valid technical indicators)
        if tab_name in strategy_groups:
            strategy_groups[tab_name].extend(strats)
        else:
            strategy_groups[tab_name] = strats
    
    # Ensure specific order of tabs if desired
    preferred_order = ['XScript - 價量策略', 'XScript - 技術指標', 'XScript - 型態選股', '籌碼選股', '傳統指標']
    ordered_groups = {k: strategy_groups.get(k, []) for k in preferred_order if k in strategy_groups}
    
    # Add any remaining categories
    for k, v in strategy_groups.items():
        if k not in ordered_groups:
            ordered_groups[k] = v
    
    return ordered_groups

