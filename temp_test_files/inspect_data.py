from FinMind.data import DataLoader
import pandas as pd

api = DataLoader()
stock_id = "2330"

print("--- Revenue ---")
df_rev = api.taiwan_stock_month_revenue(stock_id=stock_id, start_date='2023-01-01')
if not df_rev.empty:
    print(df_rev.tail(3).to_string())
else:
    print("Revenue empty")

print("\n--- Financial Statement ---")
df_fin = api.taiwan_stock_financial_statement(stock_id=stock_id, start_date='2023-01-01')
if not df_fin.empty:
    print(df_fin[df_fin['type'].str.contains('Margin', na=False)].tail(5).to_string())
    print("Types available:", df_fin['type'].unique())
else:
    print("Financial Statement empty")
