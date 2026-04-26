from data.fetcher import DataFetcher
import pandas as pd

def test_fetch_index():
    print("Testing TSE Index...")
    df = DataFetcher.fetch_market_index('TSE', '5d')
    if not df.empty:
        print(f"TSE Data:\n{df.tail()}")
    else:
        print("TSE Data Empty!")

    print("\nTesting OTC Index...")
    df_otc = DataFetcher.fetch_market_index('OTC', '5d')
    if not df_otc.empty:
        print(f"OTC Data:\n{df_otc.tail()}")
    else:
        print("OTC Data Empty!")

def test_borrowing():
    print("\nTesting SBL (Borrowing) for 2330...")
    # SBL data might update daily evening.
    df = DataFetcher.fetch_borrowing_sell('2330', days=10)
    if not df.empty:
        print(f"SBL Data:\n{df.tail()}")
    else:
        print("SBL Data Empty (Might be normal if no connection or paid data required?)")

def test_inst_detail():
    print("\nTesting Inst Detail for 2330...")
    df = DataFetcher.fetch_institutional_investors('2330', days=5)
    if not df.empty:
        print(f"Inst Data:\n{df.tail()}")
    else:
        print("Inst Data Empty")

if __name__ == "__main__":
    test_fetch_index()
    test_borrowing()
    test_inst_detail()
