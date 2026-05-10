from FinMind.data import DataLoader
import pandas as pd

api = DataLoader()
try:
    print("Fetching Revenue...")
    df = api.taiwan_stock_month_revenue(stock_id='2330', start_date='2023-01-01')
    print("Columns:", df.columns)
    print("Head:", df.head(1))
    
    print("\nFetching Inst...")
    df_inst = api.taiwan_stock_institutional_investors(stock_id='2330', start_date='2024-01-01')
    print("Columns:", df_inst.columns)
    print("Head:", df_inst.head(1))

except Exception as e:
    print("Error:", e)
    import traceback
    traceback.print_exc()
