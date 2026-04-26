import streamlit as st
import pandas as pd
import sys
import os
import inspect

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from strategies.registry import StrategyRegistry
from scanner.engine import ScannerEngine
from data.fetcher import DataFetcher

st.set_page_config(page_title="XScript Strategy Lab", layout="wide")

def main():
    st.title("🧪 XScript Strategy Lab")
    st.markdown("Explore and test 1000+ strategies converted from XScript.")

    # Initialize Registry
    StrategyRegistry.initialize()
    tree = StrategyRegistry.get_strategy_tree()

    # Sidebar: Navigation
    st.sidebar.header("Strategy Library")
    
    # Simple recursive renderer for sidebar
    # For Streamlit sidebar, deep nesting is tricky. We can use SelectBox for levels.
    
    # Level 1: Top Categories
    top_cats = sorted([k for k in tree.keys() if k != '__strategies__'])
    selected_top = st.sidebar.selectbox("Category", top_cats)
    
    current_node = tree.get(selected_top, {})
    breadcrumbs = [selected_top]
    
    # Dive deeper if there are sub-categories (folders)
    while True:
        sub_dirs = sorted([k for k in current_node.keys() if k != '__strategies__'])
        if not sub_dirs:
            break
            
        selected_sub = st.sidebar.selectbox(f"Sub-Category ({breadcrumbs[-1]})", sub_dirs)
        breadcrumbs.append(selected_sub)
        current_node = current_node.get(selected_sub, {})

    # Now we are at a leaf or intermediate node. Check for strategies.
    strategies = current_node.get('__strategies__', [])
    
    if not strategies:
        st.info("No strategies found in this category.")
        return

    # Select Strategy
    selected_strat_name = st.sidebar.selectbox("Select Strategy", strategies)
    
    # --- Main Content ---
    
    # 1. Strategy Info
    st.sidebar.text(f"Path: {'/'.join(breadcrumbs)}")
    
    # 1. Strategy Info
    st.subheader(f"📌 {selected_strat_name}")
    st.caption(f"Path: {' > '.join(breadcrumbs)}")
    
    # Get Strategy Function
    category_key = "/".join(breadcrumbs)

    # DEBUG info
    # st.write(f"**Debug Info**")
    # st.write(f"- Category Key: `{category_key}`")
    # st.write(f"- Strategy Name: `{selected_strat_name}`")
    # st.write(f"- Total Strategies in Category: {len(strategies)}")

    func = StrategyRegistry.get_strategy(category_key, selected_strat_name)
    
    if not func:
        # Fallback: Try searching all categories for this name (unlikely collisions but possible)
        st.warning(f"Could not directly locate strategy in category '{category_key}'. Searching globally...")
        for cat, strats in StrategyRegistry.get_all_strategies().items():
            if selected_strat_name in strats:
                func = StrategyRegistry.get_strategy(cat, selected_strat_name)
                st.success(f"Found in category: {cat}")
                break
    
    if func:
        # Check if implemented
        try:
            source = inspect.getsource(func)
            is_skeleton = "# TODO: Implement indicators" in source or "return False, \"\"" in source
        except:
            source = ""
            is_skeleton = False

        if is_skeleton:
            st.warning("⚠️ This strategy is currently a SKELETON (Placeholder). Running it will always return 'No Signal'.")

        # Display Docstring (Original XS Logic)
        with st.expander("📖 Original XScript Logic & Docstring", expanded=True):
            st.code(inspect.getdoc(func) or "No docstring available.", language='text')

        # Display Source Code
        with st.expander("🐍 Python Source Code", expanded=False):
            if source:
                st.code(source, language='python')
            else:
                st.error("Could not retrieve source code.")

        # 2. Test Execution
        st.divider()
        st.subheader("⚙️ Test Bench")
        
        col1, col2 = st.columns([1, 3])
        
        with col1:
            test_stock = st.text_input("Stock Code", value="2330")
        
        with col2:
            # Dynamic Parameters
            params = StrategyRegistry.get_strategy_params(selected_strat_name)
            input_params = {}
            if params:
                st.write("Parameters:")
                p_cols = st.columns(min(len(params), 4))
                for idx, (p_name, p_info) in enumerate(params.items()):
                    with p_cols[idx % 4]:
                        default_val = p_info.get('default', 0)
                        # Ensure default_val is compatible with number_input if it's a number
                        if p_info['type'] in ['int', 'float']:
                             input_params[p_name] = st.number_input(p_name, value=float(default_val) if isinstance(default_val, (int, float)) else 0.0)
                        else:
                             input_params[p_name] = st.text_input(p_name, value=str(default_val))
            else:
                st.write("No parameters.")

        if st.button("🚀 Run Strategy Test"):
            with st.spinner(f"Fetching data for {test_stock} and running {selected_strat_name}..."):
                # Fetch Data
                df = DataFetcher.fetch_history(test_stock, period="1y")
                
                if df.empty:
                    st.error("Failed to fetch data or invalid stock code.")
                else:
                    st.success(f"Loaded {len(df)} candles for {test_stock}.")
                    
                    # Run Strategy
                    is_match, reason = ScannerEngine._check_strategy(selected_strat_name, df, test_stock, params=input_params)
                    
                    # Display Result
                    if is_match:
                        st.success(f"✅ SIGNAL MATCHED! Reason: {reason}")
                    else:
                        if is_skeleton:
                             st.info(f"⚪ No Signal (Skeleton Code). Reason: {reason}")
                        else:
                             st.info(f"⚪ No Signal. {reason}")
                        
                    # Visualization (Basic)
                    st.line_chart(df['Close'])

    else:
        st.error("Function object not found in Registry.")

if __name__ == "__main__":
    main()
