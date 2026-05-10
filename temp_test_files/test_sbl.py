
from FinMind.data import DataLoader
import pandas as pd
import datetime

api = DataLoader()
stock_id = "2330"
start_date = (datetime.date.today() - datetime.timedelta(days=30)).strftime("%Y-%m-%d")

print(f"Fetching SBL data for {stock_id} from {start_date}...")

try:
    # Try taiwan_stock_securities_lending first
    df = api.taiwan_stock_securities_lending(
        stock_id=stock_id,
        start_date=start_date
    )
    print(f"SBL Data (taiwan_stock_securities_lending):\n{df.head()}")
    if not df.empty:
        print("Columns:", df.columns)
except Exception as e:
    print(f"Error fetching SBL: {e}")
