# 台股研究協作與模擬執行平台

## 產品定位
- 定位：台股優先、給小團隊使用的研究協作與模擬執行平台。
- 目標：把目前分散的個股分析、策略掃描、回測、監控、投組與研究紀錄，整理成可交接、可追溯、可延伸的研究工作流。
- 本期邊界：不做真券商串接、不做自動下單、不做公開註冊/計費、不做多市場同時交付。

## 目標使用者
- 研究主導者：需要快速驗證策略、保存研究脈絡、形成交易計畫。
- 協作成員：需要接手上一位成員的工作上下文，查看最近決策、結果與未完成事項。
- 監控操作者：需要查看 watchlist、排程訊號、紙上委託狀態與異常提醒。

## 核心工作流
1. 研究：從股票研究頁面查看技術面、基本面、籌碼面與輔助 AI 觀察。
2. 策略：在策略工作台組合條件、設定參數、指定股票池，執行掃描並保存 `ScreenRun`。
3. 驗證：從掃描結果挑選標的進入驗證中心，執行回測並保存 `BacktestRun`。
4. 執行：根據回測或訊號建立 `TradePlan`，再轉成 `PaperOrder` 進行模擬執行追蹤。
5. 協作：透過共享 watchlist、研究筆記、最近工作日誌與監控結果，讓其他 agent 或成員可快速接手。

## 頁面地圖
- 首頁：市場總覽、最近訊號、最近回測、待處理模擬委託、資料健康狀態、交接文件狀態。
- 研究：單一股票研究工作台，整合價格圖、技術指標、基本面、籌碼、研究筆記。
- 策略：策略目錄、參數設定、股票池、掃描結果、命中原因與 `ScreenRun` 保存。
- 驗證：候選標的、回測設定、績效摘要、交易明細、`BacktestRun` 保存與建立交易計畫。
- 模擬執行：`TradePlan` 管理、`PaperOrder` 建立與狀態追蹤。
- 協作/監控：共享 watchlist、研究筆記、近期工作日誌、手動監控快照與歷史脈絡。

## 核心資料模型
### StrategyDefinition
- 用途：描述策略名稱、來源、分類與參數。
- 主要欄位：`name`、`category`、`source`、`parameters`。

### ScreenRun
- 用途：保存一次策略掃描的完整上下文。
- 主要欄位：`market_scope`、`stock_pool`、`strategies`、`match_mode`、`executed_at`、`results`、`result_count`。

### SignalEvent
- 用途：把 `ScreenRun` 的命中結果轉成可追蹤事件。
- 主要欄位：`screen_run_id`、`stock_id`、`stock_name`、`strategy_names`、`reason`、`price`、`detected_at`。

### BacktestRun
- 用途：保存回測設定與績效結果。
- 主要欄位：`screen_run_id`、`stock_id`、`strategy_name`、`period`、`starting_cash`、`commission_rate`、`final_value`、`total_return_pct`、`benchmark_return_pct`、`trades`。

### TradePlan
- 用途：保存研究決策與風險檢查，不等於實際委託。
- 主要欄位：`stock_id`、`strategy_name`、`thesis`、`entry_idea`、`stop_loss`、`take_profit`、`risk_checks`、`status`。

### PaperOrder
- 用途：保存模擬執行紀錄。
- 主要欄位：`trade_plan_id`、`side`、`quantity`、`intended_price`、`status`、`filled_price`、`notes`。

### Watchlist
- 用途：保存共享股票清單與協作上下文。
- 主要欄位：`name`、`owner`、`stocks`、`description`。

### ResearchNote
- 用途：保存股票或策略研究筆記。
- 主要欄位：`title`、`stock_id`、`tags`、`content`、`author`、`related_watchlist_id`、`related_screen_run_id`。

## 分期 Roadmap
### Phase 0
- 建立 `PLAN.md`、`WORKLOG.md`、交接規則與基線紀錄。
- 狀態：已完成。

### Phase 1
- 重畫 UI 導航為 6 個主區。
- 先以現有能力重新分區，不重寫既有策略邏輯。
- 狀態：已完成基礎導航與主頁骨架。

### Phase 2
- 建立共享 domain models 與 JSON persistence store。
- 讓掃描結果可保存成 `ScreenRun`，並衍生 `SignalEvent`。
- 讓回測結果可保存成 `BacktestRun`。
- 狀態：已完成基礎資料模型與保存機制。

### Phase 3
- 完成 `TradePlan` 與 `PaperOrder` 的最小可用流程。
- 狀態：已完成基礎 UI 與狀態流，後續可補更多風控欄位。

### Phase 4
- 補共享 watchlist、研究筆記與近期交接上下文視圖。
- 狀態：已完成基礎 UI，後續需補通知與多人協作細節。

### Phase 5
- 補排程掃描、通知、資料健康檢查、失敗可追蹤性。
- 狀態：待實作。

### Phase 6
- 將 UI 從 Streamlit 遷移到 Next.js + React，先保留 Python 分析核心，透過 API route / bridge 串接。
- 以 Prisma + SQLite 建立分析結果資料庫，讓原本 JSON persistence 可逐步過渡。
- 狀態：進行中，已完成 App Router 殼層，並將研究 API 收斂成 Vercel 可部署的 Node 版本；分析結果資料庫目前支援本地 SQLite，雲端環境則待接 managed database。

## 當前現況
### 已有能力
- 資料抓取：`yfinance`、`twstock`、`FinMind` fallback。
- 策略層：大量 XScript 與動態 registry。
- UI：原有個股分析、策略實驗室、選股回測、投組與監控頁面。
- 驗證：已有 smoke tests，並補上新的 pytest 基礎結構。

### 本輪新增能力
- 單一事實來源文件：`PLAN.md`。
- 單一追加式工作日誌：`WORKLOG.md`。
- Workspace domain models 與 JSON store。
- 新的 6 區導航骨架與工作流頁面。
- `ScreenRun` → `BacktestRun` → `TradePlan` → `PaperOrder` 的最小串接。
- 驗證中心改為統一回測入口，支援 `MA Crossover`、`RSI Oversold`、`Bollinger Buy` 的 Backtrader 回測，並提供 signal simulation fallback 來驗證 XScript / registry 策略。
- Next.js App Router UI 骨架、Next API routes、Python research bridge 與 Prisma/SQLite 分析結果資料庫雛形。
- 研究 API 改為 Vercel 可部署的 Node market data service，避免雲端環境依賴本機 `.venv`。
- 分析結果資料層新增 deployment-safe fallback：若 Vercel 未配置 managed `DATABASE_URL`，頁面可唯讀啟動、寫入 API 會回傳明確的 `503` 提示。
- 針對 models、store、導航與文件的最小單元測試。

## 已知風險
- 目前正式 Backtrader 策略已支援 `MA Crossover`、`RSI Oversold`、`Bollinger Buy`；其餘策略多數仍走 signal simulation，後續仍需更完整的事件模型與出場邏輯。
- 自動生成策略檔仍有多個 `SyntaxWarning`，雖不影響目前流程，但需要後續清理。
- 目前 persistence 正處於 JSON + SQLite 並存的過渡期；分析結果已能進 DB，但其餘工作流資料仍待逐步正規化。
- 若部署到 Vercel 而仍使用 `file:` 型 `DATABASE_URL`，分析結果寫入會被刻意停用，避免 serverless 檔案系統造成錯誤或假持久化。
- 協作/監控目前以手動觸發為主，尚未有真正的排程中心與通知歷史。

## 下一步
1. 將更多 registry / XScript 策略從 signal simulation 升級成更貼近實盤的回測模型，補齊事件型出場與倉位管理。
2. 將協作筆記與 watchlist 補上編輯/刪除與衝突處理。
3. 為 `SignalEvent`、`BacktestRun`、`TradePlan` 增加更完整的篩選與搜尋 UI。
4. 建立排程掃描與通知歷史頁，補足營運能力。
5. 清理自動生成策略的 warning 與回測接口不一致問題。
6. 將 `ScreenRun`、`SignalEvent`、`TradePlan`、`PaperOrder` 從 JSON store 逐步搬到正式資料庫模型。
7. 佈署前接上 managed database，完成 GitHub / Vercel 專案與正式環境變數配置。
