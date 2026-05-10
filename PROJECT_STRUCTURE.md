# Stock Analysis Project Structure

本專案是台股研究與掃描平台。前端主介面已遷移到 Next.js App Router；Python 分析核心仍保留，雲端則以 Node/Yahoo fallback、managed Postgres 與 scan jobs API 支援 Vercel production。

## Top-Level Layout

| Path | Role |
| --- | --- |
| `app/` | Next.js App Router pages and API routes. Production UI lives here. |
| `components/` | React UI components used by the App Router pages. |
| `lib/` | Next.js server/client shared business logic, cloud fallback scanners, DB access, diagnostics, stock-name mapping. |
| `prisma/` | Prisma schema for the local SQLite development database. |
| `data/` | Python data layer, stock list CSV, cache/storage helpers, workspace models. |
| `scanner/` | Python scanner engine, daily after-market scan, scoring logic. |
| `strategies/` | Strategy registry, technical/chip strategies, generated XScript strategy modules. |
| `backtest/` | Python backtest engine. |
| `monitor/` | Python monitoring engine. |
| `portfolios/` | Portfolio management logic. |
| `alerts/` | Alert manager and LINE notify integration. |
| `ui/` | Legacy Streamlit UI kept for reference and local legacy workflows. |
| `dev_tools/` | Local developer bridge and conversion tools, including `next_bridge.py`. |
| `scripts/` | Utility scripts such as local analysis DB initialization. |
| `tests/` | Official pytest suite. Keep formal tests here. |
| `reports/` | Team handoff and module reports. |
| `temp_test_files/` | Temporary, ad hoc, or historical root-level test/debug files moved out of the project root. |

## Layout And Skins

The main UI uses a responsive operations layout:

- Desktop (`>=1180px`): sticky left sidebar navigation plus wide work surface.
- Tablet (`720px-1179px`): compact top command layout with nav grid.
- Mobile (`<720px`): compact header, horizontal scroll nav, single-column work surface.

Skin switching is handled by `components/skin-switcher.tsx` and CSS variables in `app/globals.css`. Available skins:

- `cedar`: warm wood default
- `graphite`: neutral professional grey
- `jade`: green/teal analysis desk
- `harbor`: blue operations console
- `crimson`: red finance desk

The selected skin is stored in `localStorage` and applied as `data-skin` on the document element.

## Next.js Pages

| Route | File | Function |
| --- | --- | --- |
| `/` | `app/page.tsx` | Dashboard snapshot for workspace counts and recent records. |
| `/research` | `app/research/page.tsx` | Stock research workbench using Next API market data. |
| `/strategy` | `app/strategy/page.tsx` | XQ condition builder and after-market screening workbench. |
| `/analysis-results` | `app/analysis-results/page.tsx` | Managed/local analysis result DB viewer and manual insert form. |
| `/settings` | `app/settings/page.tsx` | Environment and deployment diagnostics. |
| `/validation` | `app/validation/page.tsx` | Backtest and validation views. |
| `/execution` | `app/execution/page.tsx` | Trade plan and execution views. |
| `/collaboration` | `app/collaboration/page.tsx` | Watchlist and research note collaboration views. |

## API Routes

| Route | Function |
| --- | --- |
| `GET/POST /api/analysis-results` | List or create analysis result records. Uses managed Postgres on Vercel, SQLite locally. |
| `POST /api/analysis-results/import-workspace` | Import local workspace backtests into local DB. |
| `GET /api/research/[ticker]` | Fetch market research snapshot with Chinese Taiwan stock names. |
| `GET /api/workspace/dashboard` | Return local workspace dashboard snapshot. |
| `GET /api/xq-strategy/catalog` | Return available XQ indicators from Python bridge or cloud fallback catalog. |
| `POST /api/xq-strategy/scan` | Run XQ condition scan, using Python locally or Node/Yahoo fallback on Vercel. |
| `POST /api/after-market-screening/scan` | Run after-market scan, using Python locally or Node/Yahoo fallback on Vercel. |
| `GET /api/after-market-screening/report/[scanId]` | Fetch local Python report or short-lived cloud cached report. |
| `GET/POST /api/scan-jobs` | List recent scan jobs or enqueue a managed DB scan job. |
| `GET /api/scan-jobs/[jobId]` | Fetch a scan job by ID. |
| `POST /api/scan-jobs/process` | Claim and process the next queued scan job. Ready for Cron/Queue wiring. |

## Core `lib/` Modules

| File | Purpose |
| --- | --- |
| `analysis-results.ts` | Analysis result storage abstraction. Supports local Prisma SQLite and managed Postgres. |
| `scan-jobs.ts` | Managed `scan_jobs` table, queue operations, and job processor. |
| `research-data.ts` | Yahoo market snapshot for research route, with Taiwan stock-name enrichment. |
| `taiwan-stock-names.ts` | Taiwan stock code/name/industry resolver from `data/stock_list.csv` plus fallback map. |
| `cloud-market-scanner.ts` | Shared Yahoo OHLCV fetcher, stock pools, and concurrency helper. |
| `after-market-cloud.ts` | Vercel-compatible after-market scan fallback. |
| `after-market-screening.ts` | Bridge selector for local Python vs cloud after-market fallback. |
| `xq-cloud.ts` | Vercel-compatible XQ scan fallback. |
| `xq-strategy.ts` | Bridge selector for local Python vs cloud XQ fallback/catalog. |
| `settings-diagnostics.ts` | `/settings` environment checks and deployment prompts. |
| `workspace.ts` | Reads local `data/workspace` JSON collections. |
| `prisma.ts` | Prisma client singleton for local SQLite mode. |

## Runtime Modes

### Local Development

- Uses `.env` and local `DATABASE_URL=file:./dev.db` by default.
- Full Python bridge is available when `.venv/Scripts/python.exe` and `dev_tools/next_bridge.py` exist.
- Historical JSON data is read from `data/workspace`.
- Formal test command:

```powershell
npm run lint
npm run build
.\.venv\Scripts\python.exe -m pytest
```

### Vercel Production

- Uses managed `DATABASE_URL` from Neon/Postgres environment variables.
- Does not include `.venv`, `.git`, `.vercel-global`, or `data/workspace`.
- Small/medium scans run through Node/Yahoo fallback.
- Analysis results and scan jobs persist in managed Postgres.
- Large scans should go through `/api/scan-jobs` and later be connected to Cron/Queue or a dedicated worker.

## Current Production Capabilities

- Research API and UI with Chinese Taiwan stock names.
- XQ condition scan with cloud fallback.
- After-market scan with cloud fallback.
- Managed Postgres write/read for analysis results.
- Managed scan job queue table and process endpoint.
- `/settings` diagnostics for environment readiness.

## Temporary Test Files

Root-level ad hoc test/debug scripts and old logs have been moved to `temp_test_files/`. These are not the official test suite. Keep new formal tests in `tests/`; put throwaway diagnostics in `temp_test_files/` if they need to be retained temporarily.
