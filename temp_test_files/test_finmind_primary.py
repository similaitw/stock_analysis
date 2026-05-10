from data.fetcher import DataFetcher
from config import Config

print("=== 測試 FinMind 作為主要資料來源 ===\n")

print(f"Config 狀態:")
print(f"  - should_use_finmind: {Config.should_use_finmind()}")
print()

# Test 1: Historical Data
print("=" * 60)
print("測試 1: 歷史資料 (2330, 1個月)")
print("=" * 60)
df_history = DataFetcher.fetch_history("2330", period="1mo")
if not df_history.empty:
    print(f"✅ 成功取得 {len(df_history)} 筆歷史資料")
    print(f"欄位: {df_history.columns.tolist()}")
    print(f"\n最新 3 筆:")
    print(df_history.tail(3))
else:
    print("❌ 未取得歷史資料")

print("\n" + "=" * 60)
print("測試 2: 即時價格 (2330)")
print("=" * 60)
price = DataFetcher.fetch_current_price("2330")
print(f"最新價格: {price}")

print("\n" + "=" * 60)
print("測試 3: 三大法人 (2330)")
print("=" * 60)
df_inst = DataFetcher.fetch_institutional_investors("2330", days=10)
if not df_inst.empty:
    print(f"✅ 成功取得 {len(df_inst)} 筆三大法人資料")
    print(df_inst.tail(5))
else:
    print("❌ 未取得三大法人資料")

print("\n=== 測試完成 ===")
