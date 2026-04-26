from data.fetcher import DataFetcher
import pandas as pd

stock_id = "2330"
print(f"Fetching fundamentals for {stock_id}...")
data = DataFetcher.fetch_fundamentals(stock_id)

print("\nResults:")
for k, v in data.items():
    print(f"{k}: {v}")

if data['Yield'] > 0 or data['Margin'] > 0:
    print("\nSUCCESS: Data fetched (Yield or Margin present).")
else:
    print("\nWARNING: Yield/Margin is 0. Check data source.")
