from FinMind.data import DataLoader
import pandas as pd

api = DataLoader()
stock_id = "2330"
start_date = "2023-01-01"

print(f"Fetching PER/PBR for {stock_id}...")
# Note: Method name check needed. Usually taiwan_stock_per
try:
    df = api.taiwan_stock_per_pbr(stock_id=stock_id, start_date=start_date)
    if not df.empty:
        print("PER/PBR Data Found:")
        print(df.tail())
        print("\nColumns:", df.columns)
    else:
        print("PER/PBR Empty")
except Exception as e:
    print(f"Error: {e}")
