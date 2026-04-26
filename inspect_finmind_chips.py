
from data.fetcher import DataFetcher
import pandas as pd

stock_id = "2330"
print(f"Fetching institutional investors for {stock_id}...")
df = DataFetcher.fetch_institutional_investors(stock_id, days=10)

if not df.empty:
    print("Columns:", df.columns)
    print("Unique names:", df['name'].unique())
    print(df.head())
else:
    print("No data returned.")
