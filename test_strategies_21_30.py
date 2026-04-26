
import sys
import os
import pandas as pd
import numpy as np

# Add project root to path
sys.path.append(os.getcwd())

try:
    from data.fetcher import DataFetcher
    from strategies.auto_generated.strat_02_基本技術指標 import Cat02基本技術指標Strategies as TechStrat

    print("Fetching data for 2330...")
    df = DataFetcher.fetch_history("2330", period='6mo')
    print(f"Data shape: {df.shape}")
    
    strategies = [
        "均線多頭排列", "均線空頭排列", 
        "布林通道超買", "布林通道超賣",
        "帶量突破均線", "成交量放大",
        "短期均線穿越長期均線", "短期均線跌破長期均線",
        "跌破糾結均線", 
        "週KD低檔黃金交叉", "週線月線黃金交叉且站穩"
    ]
    
    for s_name in strategies:
        func = getattr(TechStrat, s_name)
        try:
            res, msg = func(df)
            print(f"✅ [{s_name}] Result: {res}, Msg: '{msg}'")
        except Exception as e:
            print(f"❌ [{s_name}] Error: {e}")
            import traceback
            traceback.print_exc()

except ImportError as e:
    print(f"Import Error: {e}")
except Exception as e:
    print(f"General Error: {e}")
