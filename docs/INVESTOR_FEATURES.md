# 投資決策中控台功能規格

## 目標

投資使用者需要的不是一般資料 dashboard，而是每天能回答下列問題的決策工作台：

1. 今日可研究候選有哪些？
2. 哪些股票或條件需要風險觀察？
3. 候選是否有分析結果或回測支持？
4. 下一步交易計畫是否清楚？
5. 目前資料是否夠新，能否支撐今天決策？

## 優先順序

### P0 已落地

- 新增 `/investor` 投資決策中控台。
- 只使用 `getWorkspaceDashboardSnapshot()` 與 `listAnalysisResults()` 的既有資料。
- 合併最新盤後掃描、分析結果、回測、交易計畫與次日觀察規則。
- 在缺少交易計畫或回測時，明確提示投資人下一步該補的決策欄位。

### P1 下一階段

- 把 next day watchlist 的 stocks 欄位擴成可顯示進場條件、降級條件與觀察價位。

### P1 已新增

- 每日盤後掃描加入市場/產業分類勾選，避免一次掃完整市場。
- 同一天同股票池、模式、權重與風險設定再次掃描時，先讀 `after_market_scan_cache`。
- managed database 可用時快取寫入資料庫；本機開發且無 managed database 時落到 `data/workspace/after_market_scan_cache`。
- 每日盤後掃描前端加入股票池選擇器：可點選市場/產業、搜尋代碼/名稱/產業、手選多檔、全部股票、依批次大小分段掃描。
- 分批掃描每一批都走同一個 cache key 規則，掃完即寫入當天 cache，重跑同批會顯示 cache hit。
- `/strategy` 會列出所選日期已寫入 `after_market_scan_cache` 的批次，可刷新並直接用 `scanId` 載入當日已掃結果，包含終端機或網頁觸發的掃描。
- 候選排序加入決策分數，綜合盤後分數、風險扣分、分析/回測支持與資料新鮮度。
- 執行頁加入候選轉 TradePlan 草稿表單；投資中控台只顯示決策，不直接寫入。
- `POST /api/trade-plans` 使用 settings session 權限檢查，local workspace 寫入只在非 Vercel runtime 開放。
- analysis results 的 backtest payload 會標準化 `backtestMetrics`：期間、總報酬、benchmark 報酬、最大回撤、勝率、交易次數、最終資產、起始資金、手續費率。
- 驗證頁與投資中控台會優先讀取 `payload.backtestMetrics`，而不是只能顯示摘要文字。

### P2 進階功能

- 加入投資人偏好設定：短線/波段、最大單筆風險、最大同族群曝險。
- 建立候選到交易計畫的審核流程與紀錄。
- 加入部位層級的總風險視圖，但仍避免從 UI 顯示任何 secret 或環境設定值。

## 系統師整合點

- `lib/workspace.ts`：維持 snapshot 聚合邊界，投資頁不要自行讀任意檔案。
- `lib/analysis-results.ts`：提供分析與回測支持資料，未來可增加標準化 payload schema。
- `app/investor/page.tsx`：server component，負責平行讀取 snapshot 與 analysis results。
- `components/investor-decision-cockpit.tsx`：純 server UI，無 client state、無 raw HTML。
- `components/site-nav.tsx`：投資決策入口。
- `lib/stock-universe.ts`：從既有台股清單產生市場/產業分類，不接受動態檔案路徑。
- `lib/stock-universe.ts`：也提供股票搜尋選項，含代碼、名稱、市場、產業與 client-side 搜尋字串。
- `lib/after-market-scan-cache.ts`：每日掃描快取，managed database 優先。
- `app/api/after-market-screening/cache/route.ts`：只回傳當日掃描摘要，不暴露 cache key、連線資訊或原始檔案路徑。
- `app/execution/page.tsx`：承接候選到 TradePlan 的工作流入口。
- `components/trade-plan-draft-form.tsx`：TradePlan 草稿表單，送出到受保護 API。
- `lib/trade-plans.ts`：TradePlan payload 驗證與固定 workspace 寫入。
- `lib/analysis-results.ts`：標準化 backtest metrics，並讓 local/managed database 都能匯入 workspace backtests。
- `app/validation/page.tsx`：顯示 DB 中標準化回測欄位。

## 資安檢查點

- 不顯示 `.env`、`DATABASE_URL`、API key 或任何 secret。
- 不新增 raw HTML 或 `dangerouslySetInnerHTML`。
- 不新增任意檔案讀取 API。
- 不新增 shell、exec 或 Python 執行入口。
- 投資中控台只讀既有 server-side 聚合函式，不直接暴露 workspace 檔案路徑。
- 每日掃描分類只回傳股票代碼清單，不回傳環境變數或資料庫連線資訊。
- 掃描快取鍵由日期、股票池、模式、權重與風險設定雜湊產生，不使用使用者可控檔名。
- 當日 cache 清單 API 僅接受 `YYYY-MM-DD` 日期與 1-200 筆 limit，回傳摘要欄位後再用既有報告 API 讀取單筆結果。
- TradePlan API 必須通過 settings session；production 若未登入應回 `401 Unauthorized`。
- TradePlan 本機寫入使用固定 `data/workspace/trade_plans` 目錄與系統產生 ID，不接受使用者提供檔名。
- Backtest 標準化只處理既有 workspace/analysis payload，不新增 Python 或外部資料請求入口。
