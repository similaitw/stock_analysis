# Scanner / Workspace Worklog

## 完成內容

- 新增 `scanner/daily_after_market.py`，提供 `run_after_market_scan(payload, data_fetcher=DataFetcher, store=WorkspaceStore())`。
- 支援 `TEST`、`Tw50`、`All` 與自訂 `stockList`，並處理 `maxStocks`、`profile`、`weights`、`includeRiskList`。
- 每檔股票獨立抓取與評分，OHLCV 不足或單檔例外會寫入 `skipped`，不會中斷整批掃描。
- `scanner/scoring.py` 採延遲 import；若尚未存在，使用最小 OHLCV fallback scoring，方便另一位工程師後續替換與測試 monkeypatch。
- 掃描完成後保存 `AfterMarketScan`，並由 A/B 名單建立 `NextDayWatchlist`。

## 資料模型

- `AfterMarketScan`
  - `id`：`after_market_YYYYMMDD_xxxxxxxx`
  - `date`、`market_scope`、`profile`、`executed_at`
  - `weights`、`counts`
  - `a_list`、`b_list`、`avoid_list`
  - `skipped`、`raw_results`、`request_payload`
- `NextDayWatchlist`
  - `id`
  - `source_scan_id`
  - `trade_date`
  - `stocks`
  - `monitoring_rules`
  - `created_at`
- `WorkspaceStore`
  - 新增 `after_market_scans` collection 與 `save/list/get_after_market_scan`
  - 新增 `next_day_watchlists` collection 與 `save/list/get_next_day_watchlist`

## 測試命令

```powershell
.\.venv\Scripts\python.exe -m pytest tests/test_after_market_scan.py tests/test_workspace_models.py tests/test_workspace_store.py
```

## 後續交接

- `scanner/scoring.py` 完成後，只要提供 `score_stock` callable 即可由 orchestration 自動延遲載入。
- 建議 scoring 回傳欄位使用 camelCase：`stockId`、`stockName`、`score`、`riskScore`、`technicalScore`、`chipScore`、`volumeScore`、`relativeStrengthScore`、`reasons`、`risks`、`nextDayPlan`。
- Bridge/API 工程師可直接呼叫 `run_after_market_scan`，stdout/API 回傳 payload 已符合 spec 的 `scanId`、`counts`、`aList`、`bList`、`avoidList`、`skipped` 結構。
- 目前 fallback scoring 只作 MVP 與測試保底，完整技術、籌碼、量能、相對強弱與風險扣分應以 `scanner/scoring.py` 為準。
