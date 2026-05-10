from data.fetcher import DataFetcher

def test_macro():
    print("Testing USD/TWD...")
    df = DataFetcher.fetch_macro_data('USD/TWD', '5d')
    if not df.empty:
        print(f"USD/TWD:\n{df.tail()}")
    else:
        print("USD/TWD Empty")

    print("\nTesting US10Y...")
    df = DataFetcher.fetch_macro_data('US10Y', '5d')
    if not df.empty:
        print(f"US10Y:\n{df.tail()}")
    else:
        print("US10Y Empty")

if __name__ == "__main__":
    test_macro()
