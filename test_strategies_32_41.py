import sys
import os
import pandas as pd
import numpy as np

sys.path.append(os.getcwd())

try:
    from data.fetcher import DataFetcher
    from strategies.auto_generated.strat_03_進階技術分析 import Cat03進階技術分析Strategies as Strat03

    print("Fetching data for 2330...")
    df = DataFetcher.fetch_history("2330", period='12mo')
    print(f"Data shape: {df.shape}")
    
    strategies = [
        # Part 1: 32-41
        "KD與均線同步出現買進訊號",
        "K棒突破布林值上緣",
        "RSI黃金交叉且股價非盤整",
        "佔大盤成交量比開始上昇",
        "冷門股出量",
        "外盤成交變多",
        "多指標都出現買進訊號",
        "多空分數翻昇",
        "多空分數轉空",
        "天量後價量未再創新高",
        # Part 2: 42-55
        "布林帶寬大於N_",
        "布林帶寬小於N_",
        "帶量突破均線後未拉回",
        "底部越來越高且資金流入的蓄勢股",
        "波動幅度開始變大",
        "盤整後跌破",
        "突破糾結均線",
        "築底指標出現買進訊號",
        "股價下跌而外盤量佔比上升",
        "股價蠢蠢欲動",
        "股價跌破走跌後的高壓電線",
        "趨勢成形",
        "跌破均線後站不回",
        "雙KD向上"
    ]
    
    for s_name in strategies:
        func = getattr(Strat03, s_name)
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
