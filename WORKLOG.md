# WORKLOG

## 記錄規則
- 每次有 repo 變更都必須追加一筆日誌。
- 每筆日誌固定包含：日期時間、Agent/操作者、目標、變更摘要、涉及模組、決策、驗證結果、未解問題、下一位接手建議。
- 純唯讀探索不需要寫日誌。
- 若一次工作包含多次修正，可以合併成同一個 change batch 記錄，但要覆蓋最終結果。

## 日誌模板
## YYYY-MM-DD HH:MM:SS +TZ
- Agent/操作者：
- 目標：
- 變更摘要：
- 涉及模組：
- 決策：
- 驗證結果：
- 未解問題：
- 下一位接手建議：

## 2026-04-23 02:28:02 +08:00
- Agent/操作者：Codex GPT-5
- 目標：實作「台股研究協作與模擬執行平台」第一批重構，建立交接基準文件、新導航骨架、共享資料模型與最小可用工作流。
- 變更摘要：新增 `PLAN.md` / `WORKLOG.md`；建立 workspace domain models 與 JSON persistence store；重構主導航為首頁、研究、策略、驗證、模擬執行、協作/監控六區；新增 research/validation/execution/collaboration/home 頁面；補上 models/store/navigation/docs 測試；讓策略掃描結果可保存為 `ScreenRun`，回測結果可保存為 `BacktestRun`，並可建立 `TradePlan` 與 `PaperOrder`。
- 涉及模組：`ui/app.py`、`ui/*.py` 新頁面、`data/workspace_models.py`、`data/workspace_store.py`、`PLAN.md`、`WORKLOG.md`、`tests/*`。
- 決策：保留現有掃描與資料抓取邏輯作為需求來源；正式回測先只接已穩定的 MA crossover 路徑；協作資料先採本地 JSON 儲存；AI 預測保留為研究頁附屬能力。
- 驗證結果：預計以 `pytest` 跑 smoke tests、workspace models/store/navigation/docs 測試；並檢查新主頁與工作流頁能成功 import。
- 未解問題：更多策略尚未對齊回測引擎；排程與通知歷史尚未實作；自動生成策略 warnings 尚未清理。
- 下一位接手建議：優先補回測策略映射與驗證中心的策略多樣性，再往排程掃描與通知歷史前進。

## 2026-04-25 12:53:20 +08:00
- Agent/操作者：Codex GPT-5
- 目標：擴充驗證中心的回測能力，讓統一工作流不再只支援單一 MA crossover 路徑。
- 變更摘要：重構 `backtest/engine.py` 為統一回測入口，新增策略目錄、動態參數規格與 `run_named_backtest`；正式支援 `MA Crossover`、`RSI Oversold`、`Bollinger Buy` 的 Backtrader 回測；為 XScript / registry 策略加入 signal simulation fallback；更新 `ui/validation_page.py` 讓回測策略與參數動態生成，並把驗證模式、手續費與 fallback note 一起保存到 `BacktestRun`；補上 `tests/test_backtest_engine.py`；將 `backtrader` 補進 `requirements.txt`；同步更新 `PLAN.md`。
- 涉及模組：`backtest/engine.py`、`ui/validation_page.py`、`tests/test_backtest_engine.py`、`requirements.txt`、`PLAN.md`、`WORKLOG.md`。
- 決策：保持 `BacktestRun` / `TradePlan` 現有資料模型不變，優先把策略映射集中在 engine 層，避免把 UI 綁死在個別策略；對尚未有正式事件型回測器的策略，先提供透明的 signal simulation fallback，而不是完全不讓驗證中心使用。
- 驗證結果：`python -m pytest tests/test_backtest_engine.py` 通過；`python -m pytest` 全數通過（14 passed）；另外以 `py_compile` 驗證 `backtest/engine.py`、`ui/validation_page.py`、`tests/test_backtest_engine.py` 可成功編譯。
- 未解問題：大量 auto-generated strategy 仍會在 registry 初始化時噴出 `SyntaxWarning`；signal simulation 仍是簡化模型，尚未覆蓋更細的出場條件、分批進出與多倉位管理。
- 下一位接手建議：優先把常用的 XScript / registry 策略逐步升級成更正式的事件型回測器，並順手處理 registry 初始化時的 warnings，讓驗證中心的體驗更穩定。

## 2026-04-25 14:30:00 +08:00
- Agent/操作者：Codex GPT-5
- 目標：把主 UI 從 Streamlit 遷移到 Next.js + React，並建立可落地的分析結果資料庫基礎設施。
- 變更摘要：新增 Next.js App Router 頁面、導航、workspace dashboard API、研究用 Python bridge API、分析結果 CRUD / 匯入 API，以及 `AnalysisResult` 的 Prisma/SQLite 模型；將 `run.bat` 改為 Next.js 啟動入口，保留 `run_streamlit_legacy.bat` 作為舊 UI fallback；補齊 Next/TypeScript module 設定、flat ESLint config，更新 smoke tests 讓新舊兩種啟動方式都有明確驗證；另外把 `db:push` 收斂成可重複執行的 SQLite bootstrap script，避開目前 Prisma schema engine 在此環境的失敗。
- 涉及模組：`app/*`、`components/*`、`lib/*`、`prisma/schema.prisma`、`dev_tools/next_bridge.py`、`package.json`、`next.config.js`、`tsconfig.json`、`run.bat`、`run_streamlit_legacy.bat`、`tests/test_smoke.py`、`PLAN.md`、`WORKLOG.md`。
- 決策：採取漸進式遷移，先保留 Python 分析核心與 workspace JSON store，使用 Next API routes 作為新前端邊界；分析結果先進 SQLite，其他工作流資料後續再逐步正規化到資料庫，避免一次性重寫過大。
- 驗證結果：`npm run db:generate` 通過；`npm run db:push` 通過並建立 `prisma/dev.db`；`npm run lint` 通過；`npm run build` 通過；`.venv\Scripts\python.exe -m pytest` 通過（15 passed）。另有既存 `nest_asyncio` deprecation warnings 與 auto-generated strategies `SyntaxWarning`，但不影響本輪流程。
- 未解問題：目前 `db:push` 採自製 SQLite bootstrap script，而非 Prisma CLI migration；其餘 JSON workspace 模型尚未進入正式 DB；研究、驗證、執行頁多數仍是前端工作台殼層，後續需要更深的寫入與查詢流程。
- 下一位接手建議：先把 `ScreenRun`、`SignalEvent`、`TradePlan`、`PaperOrder` 納入正式 DB 模型，再逐步把頁面互動從展示型工作台接成完整資料流；若未來要恢復 Prisma CLI migration，再集中處理該環境的 schema engine 相容性問題。

## 2026-04-25 13:47:00 +08:00
- Agent/操作者：Codex GPT-5
- 目標：修復 Next.js 研究頁查詢 2330 無反應的問題。
- 變更摘要：定位出 `dev_tools/next_bridge.py` 在抓資料時會讓 `DataFetcher` 將 log 印到 stdout，導致 `lib/python-bridge.ts` 的 `JSON.parse(stdout)` 失敗；修正 bridge 讓資料層 log 全部改走 stderr，並在 TypeScript 端改為解析最後一行 JSON payload；新增 `tests/test_next_bridge.py` 回歸測試，確保 bridge stdout 只輸出 JSON。
- 涉及模組：`dev_tools/next_bridge.py`、`lib/python-bridge.ts`、`tests/test_next_bridge.py`、`WORKLOG.md`。
- 決策：同時在 Python 與 TypeScript 兩端補防呆，避免未來資料層再印出 stdout 時又把 Next API 弄壞。
- 驗證結果：直接執行 `.venv\Scripts\python.exe dev_tools\next_bridge.py research 2330` 時，stdout 已為單一 JSON payload；以 Node 匯入 `fetchResearchSnapshot('2330')` 成功取得資料；`pytest tests/test_next_bridge.py tests/test_smoke.py` 通過；`npm run build` 通過；啟動 dev server 後，`http://127.0.0.1:3000/api/research/2330` 回 `200` 並帶回 60 筆 history。
- 未解問題：PowerShell 顯示中文名稱時仍有編碼雜訊，但 API payload 本身是正確的 UTF-8 JSON；既有 auto-generated strategy warnings 仍存在。
- 下一位接手建議：如果研究頁還要再強化，下一步可以把 loading / error 狀態做得更明顯，並加入 request timeout 與 retry UX，讓使用者更容易分辨是查詢中還是失敗。

## 2026-04-26 00:20:00 +08:00
- Agent/操作者：Codex GPT-5
- 目標：將專案整理成可上 GitHub / Vercel 的部署相容版本，排除本機專屬依賴。
- 變更摘要：新增 `lib/research-data.ts`，將研究 API 改為以 `yahoo-finance2` 直接抓取市場資料，移除部署時對 `.venv` / Python bridge 的硬依賴；更新研究頁文案以反映新的資料來源；為分析結果資料層加入 storage mode 判斷，在 Vercel 且未提供 managed `DATABASE_URL` 時改為唯讀 fallback，避免檔案型 SQLite 在 serverless 環境寫入失敗；同步強化 `.gitignore`，排除 `.env`、`.vercel` 與暫存 log，並新增 `.vercelignore` 排除部署時不需要的 Python / 測試資產。
- 涉及模組：`lib/research-data.ts`、`app/api/research/[ticker]/route.ts`、`components/research-workbench.tsx`、`lib/analysis-results.ts`、`app/api/analysis-results/route.ts`、`app/api/analysis-results/import-workspace/route.ts`、`.gitignore`、`.vercelignore`、`PLAN.md`、`WORKLOG.md`、`package.json`。
- 決策：優先把部署相容性做對，再處理 GitHub / Vercel 遠端資源；研究資料在雲端先改用 Node market data service，資料庫則採「本地可寫、雲端需 managed DB 才開寫入」的策略，避免假性上線。
- 驗證結果：`npm run lint` 通過；`npm run build` 通過；模擬雲端環境的 `$env:VERCEL='1'; npm run build` 通過；啟動 dev server 後，`http://127.0.0.1:3000/api/research/2330` 回 `200`，帶回 `2330 / 60 筆 history / currentPrice 2185`；`.venv\Scripts\python.exe -m pytest` 通過（16 passed）。
- 未解問題：目前尚未有新的 GitHub repository 可供 push，且 Vercel CLI token 已失效；若要在 Vercel 啟用分析結果寫入，仍需配置 managed `DATABASE_URL`。
- 下一位接手建議：取得 GitHub repo URL 與有效的 Vercel 登入後，先 push 再建立 Vercel project；若要正式啟用分析結果寫入，部署前先接上 Postgres / Neon / Supabase 類型的 managed database。
