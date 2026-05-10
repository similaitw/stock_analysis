# Team Quant Scoring Worklog

## 完成內容

- 新增 `scanner/scoring.py`，提供每日盤後篩選的純函式評分核心。
- 新增 `ScoreBreakdown`、`ScoreComponent`、`RiskComponent` 資料結構，讓呼叫端可直接取得總分、分項分數、命中原因、風險原因與 skip reason。
- 實作 `score_stock` 與 `classify_result`，支援傳入 `price_df`、`chip_cache`、`market_df`、`industry_df`，不直接抓取外部資料。
- 評分涵蓋技術面、量能、籌碼、相對強弱與風險扣分，並保留可讀 reasons/risks。
- 新增 `tests/test_after_market_scoring.py`，涵蓋 A 級、B 級、避開、資料不足 skip 與分級門檻。

## 重要決策

- 本輪只新增 scoring core，不串接 DataFetcher、workspace persistence、Next bridge 或前端，以符合指定寫入範圍。
- 基礎濾網失敗時回傳 `classification="skip"`，不丟例外，讓後續批次掃描可以累積 skip reason。
- 風險扣分會先進入 `risk_score`，再併入總分；重大風險或風險分數小於等於 -30 時，分級一律為 `avoid`。
- `chip_cache` 採用既有風格鍵名：`institutional`、`margin`、`sbl`；法人資料支援 `net` 欄，也支援 `buy`/`sell` 推導。
- 相對強弱先以 20 日報酬比較大盤與產業，`industry_df` 可直接給單一 DataFrame，也可給 `{stock_id: DataFrame}` 或 `default` mapping。

## 測試命令

```powershell
H:\AI_Project\stock_analysis\.venv\Scripts\python.exe -m pytest tests/test_after_market_scoring.py
H:\AI_Project\stock_analysis\.venv\Scripts\python.exe -m pytest -q
```

結果：新增測試 5 passed；全套 Python 測試 24 passed。全套測試仍會顯示既有 auto-generated XScript strategy 的 SyntaxWarning，非本輪新增檔案造成。

## 後續交接

- 下一位可在 `scanner/daily_after_market.py` 串接 DataFetcher，將每檔股票資料整理後呼叫 `score_stock`。
- 若要保存掃描結果，可直接使用 `ScoreBreakdown.to_dict()` 作為 workspace JSON 的 raw item。
- 注意/處置股目前透過 price_df 的 `Attention`、`Disposition`、`注意股`、`處置股` 欄位標記；之後接官方資料時只要補進欄位即可。
- 後續 bridge/API 層應保留 skip 結果統計，避免單檔缺資料造成整批盤後掃描失敗。
