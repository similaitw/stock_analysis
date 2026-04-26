from FinMind.data import DataLoader
import pandas as pd

api = DataLoader()
stock_id = "2330"
start_date = "2023-01-01"

print(f"Fetching financial statements for {stock_id} since {start_date}...")
df = api.taiwan_stock_financial_statement(stock_id=stock_id, start_date=start_date)

if not df.empty:
    print("Unique Types found:")
    types = df['type'].unique()
    for t in sorted(types):
        print(f"- {t}")
    
    # Check specifically for Book Value related terms
    relevant = [t for t in types if 'Book' in t or 'Equity' in t or 'Asset' in t or 'Liability' in t]
    print("\nRelevant types for PBR:")
    print(relevant)
else:
    print("No data returned.")
