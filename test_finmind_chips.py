from FinMind.data import DataLoader
import pandas as pd

api = DataLoader()
stock_id = "2330"

print(" fetching institutional investors...")
df_inst = api.taiwan_stock_institutional_investors(
    stock_id=stock_id,
    start_date='2024-01-01'
)
print(f"Institutional Investors: {len(df_inst)} rows")
if not df_inst.empty:
    print(df_inst.head())

print("\n fetching margin trading...")
df_margin = api.taiwan_stock_margin_purchase_short_sale(
    stock_id=stock_id,
    start_date='2024-01-01'
)
print(f"Margin Trading: {len(df_margin)} rows")
if not df_margin.empty:
    print(df_margin.head())

print("\n fetching shareholding...")
# Note: FinMind might not have this for free or API name differs.
# Common name: taiwan_stock_holding_shares_per
try:
    df_hold = api.taiwan_stock_holding_shares_per(
        stock_id=stock_id,
        start_date='2024-01-01'
    )
    print(f"Shareholding: {len(df_hold)} rows")
    if not df_hold.empty:
        print(df_hold.head())
except Exception as e:
    print(f"Shareholding error: {e}")
