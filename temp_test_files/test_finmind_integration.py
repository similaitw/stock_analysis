from config import Config
from data.fetcher import DataFetcher

print("=== FinMind 整合測試 ===\n")

# 1. Config Test
print(f"1. Config 狀態:")
print(f"   - FinMind Token: {'已設定' if Config.has_finmind_token() else '未設定'}")
print(f"   - 使用 FinMind: {Config.should_use_finmind()}")
print()

# 2. Test Institutional Investors
print("2. 測試三大法人資料 (2330):")
try:
    df_inst = DataFetcher.fetch_institutional_investors("2330", days=30)
    if not df_inst.empty:
        print(f"   ✅ 成功取得 {len(df_inst)} 筆資料")
        print(f"   欄位: {df_inst.columns.tolist()}")
        print(f"   最新資料:\n{df_inst.tail(3)}")
    else:
        print("   ⚠️ 無資料")
except Exception as e:
    print(f"   ❌ 錯誤: {e}")
print()

# 3. Test Margin Trading
print("3. 測試融資融券資料 (2330):")
try:
    df_margin = DataFetcher.fetch_margin_trading("2330", days=30)
    if not df_margin.empty:
        print(f"   ✅ 成功取得 {len(df_margin)} 筆資料")
        print(f"   欄位: {df_margin.columns.tolist()}")
    else:
        print("   ⚠️ 無資料")
except Exception as e:
    print(f"   ❌ 錯誤: {e}")
print()

# 4. Test Shareholding
print("4. 測試大戶持股資料 (2330):")
try:
    df_hold = DataFetcher.fetch_shareholding("2330", days=90)
    if not df_hold.empty:
        print(f"   ✅ 成功取得 {len(df_hold)} 筆資料")
        print(f"   欄位: {df_hold.columns.tolist()}")
    else:
        print("   ⚠️ 無資料")
except Exception as e:
    print(f"   ❌ 錯誤: {e}")

print("\n=== 測試完成 ===")
