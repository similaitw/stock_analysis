import os
import sys
import importlib.util
import pandas as pd
import inspect
from data.fetcher import DataFetcher

# Add project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def load_module_from_path(path):
    try:
        module_name = os.path.splitext(os.path.basename(path))[0]
        spec = importlib.util.spec_from_file_location(module_name, path)
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
    except Exception as e:
        print(f"Error loading {path}: {e}")
    return None

def find_strategy_function(module):
    """Find the main strategy function in the module."""
    # Heuristic: function name matches filename or is the only public function
    # Or just look for a function that takes 'df' as first arg and returns tuple
    
    # Try to find function with same name as module
    module_name = module.__name__.split('.')[-1]
    if hasattr(module, module_name):
        return getattr(module, module_name)
        
    # Fallback: find any function that looks like a strategy
    for name, obj in inspect.getmembers(module, inspect.isfunction):
        if name.startswith('_'): continue
        if obj.__module__ != module.__name__: continue # Skip imported functions
        
        # Check signature? args should include df
        sig = inspect.signature(obj)
        params = list(sig.parameters.values())
        if len(params) > 0 and (params[0].name == 'df' or 'DataFrame' in str(params[0].annotation)):
             return obj
             
    return None

def run_verification():
    print("="*80)
    print("Verifying Strategies: 04 (Price-Volume), 05 (Pattern), 06 (Chip)")
    print("="*80)

    # 1. Setup Data
    tickers = ["2330", "2317"] # TSMC, Foxconn
    data_cache = {}
    
    for ticker in tickers:
        print(f"Fetching data for {ticker}...")
        try:
            df = DataFetcher.fetch_history(ticker, period='1y')
            if df is not None and not df.empty:
                # Add StockID for chip strategies if not present (fetch_history adds it but just in case)
                if 'StockID' not in df.columns:
                    df['StockID'] = ticker 
                data_cache[ticker] = df
                print(f"  Got {len(df)} rows.")
            else:
                print(f"  Failed to get data for {ticker}")
        except Exception as e:
            print(f"  Error fetching {ticker}: {e}")

    if not data_cache:
        print("No data available. Aborting.")
        return

    # 2. Verify Category 04 & 05 (Individual Files)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    categories = {
        '04_Price_Volume': os.path.join(base_dir, 'strategies', 'xscript', 'price_volume'),
        '05_Pattern': os.path.join(base_dir, 'strategies', 'xscript', 'pattern')
    }
    
    for cat_name, cat_path in categories.items():
        print(f"\nTesting Category: {cat_name}")
        print("-" * 60)
        
        if not os.path.exists(cat_path):
            print(f"  Directory not found: {cat_path}")
            continue
            
        files = [f for f in os.listdir(cat_path) if f.endswith('.py') and not f.startswith('__')]
        
        for f in files:
            path = os.path.join(cat_path, f)
            module = load_module_from_path(path)
            if not module: continue
            
            func = find_strategy_function(module)
            if not func:
                print(f"  [WARN] No strategy function found in {f}")
                continue
                
            print(f"  Running {f}...", end='', flush=True)
            
            error_count = 0
            pass_count = 0
            
            for ticker, df in data_cache.items():
                try:
                    result = func(df)
                    # Result should be (bool, str)
                    if isinstance(result, tuple) and len(result) == 2:
                        pass_count += 1
                        # if result[0]: print(f" [{ticker}: MATCH]", end='')
                    else:
                        print(f" [INVALID RET] {result}", end='')
                        error_count += 1
                except Exception as e:
                    print(f" [ERR: {e}]", end='')
                    error_count += 1
            
            if error_count == 0:
                print(" OK")
            else:
                print(" FAIL")

    # 3. Verify Category 06 (Class Static Methods)
    print(f"\nTesting Category: 06_Chip")
    print("-" * 60)
    
    # Import strat_06
    try:
        from strategies.auto_generated.strat_06_籌碼選股 import Cat06籌碼選股Strategies
        cls = Cat06籌碼選股Strategies
        
        # Get all static methods
        methods = [m for m in dir(cls) if not m.startswith('_') and callable(getattr(cls, m))]
        
        for m_name in methods:
            method = getattr(cls, m_name)
            print(f"  Running {m_name}...", end='', flush=True)
            
            error_count = 0
            
            for ticker, df in data_cache.items():
                try:
                    result = method(df)
                    if isinstance(result, tuple) and len(result) == 2:
                        pass
                        # if result[0]: print(f" [{ticker}: MATCH]", end='')
                    else:
                         print(f" [INVALID RET] {result}", end='')
                         error_count += 1
                except Exception as e:
                     print(f" [ERR: {e}]", end='')
                     error_count += 1
            
            if error_count == 0:
                print(" OK")
            else:
                print(" FAIL")
                
    except ImportError as e:
        print(f"  Could not import Category 06 strategies: {e}")
    except Exception as e:
        print(f"  Error testing Category 06: {e}")

if __name__ == "__main__":
    run_verification()
