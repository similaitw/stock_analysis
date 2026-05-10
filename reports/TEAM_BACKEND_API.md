# Backend/API Handoff - Daily After-Market Screening

## Completed

- Added `lib/after-market-screening.ts` as the Next.js wrapper for Python bridge commands.
- Added `POST /api/after-market-screening/scan` for daily after-market scans.
- Added `GET /api/after-market-screening/report/[scanId]` for loading saved scan reports when the scanner/report backend is available.
- Extended `dev_tools/next_bridge.py` with `after_market_scan` and `after_market_report` commands while preserving existing `research`, `xq_catalog`, and `xq_scan` commands.
- Added `tests/test_after_market_bridge.py` with monkeypatched scanner coverage so the bridge can be tested before `scanner/daily_after_market.py` is merged.

## API Contract

### Scan

`POST /api/after-market-screening/scan`

Request:

```json
{
  "date": "2026-05-10",
  "marketType": "TEST",
  "stockList": ["2330", "2317"],
  "profile": "balanced",
  "maxStocks": 500,
  "includeRiskList": true,
  "weights": {
    "technical": 40,
    "chip": 30,
    "volume": 15,
    "relativeStrength": 15
  }
}
```

Success response:

```json
{
  "scanId": "after_market_20260510_xxxxxxxx",
  "executedAt": "2026-05-10T18:05:00",
  "marketType": "TEST",
  "counts": {
    "scanned": 1200,
    "aList": 12,
    "bList": 36,
    "avoidList": 44
  },
  "aList": [],
  "bList": [],
  "avoidList": []
}
```

Error response:

```json
{
  "error": "Clear error message",
  "route": "after-market-screening/scan"
}
```

### Report

`GET /api/after-market-screening/report/[scanId]`

The route calls `python dev_tools/next_bridge.py after_market_report <scan_id>`. The bridge first tries scanner-provided report functions, then falls back to `data/workspace/after_market_scans/<scanId>.json`.

Error response:

```json
{
  "error": "Clear error message",
  "route": "after-market-screening/report"
}
```

## Python Bridge Contract

Commands:

```bash
python dev_tools/next_bridge.py after_market_scan <json_payload>
python dev_tools/next_bridge.py after_market_report <scan_id>
```

The bridge keeps stdout reserved for the final JSON object. Scanner logs printed to stdout are redirected to stderr during scanner import/calls.

Supported scanner entry points:

- Module scan functions: `after_market_scan`, `run_after_market_scan`, `scan_after_market`, `run_scan`, `scan`
- Scanner classes: `DailyAfterMarketScanner` or `AfterMarketScanner` with `after_market_scan`, `run_scan`, or `scan`
- Module report functions: `after_market_report`, `get_after_market_report`, `load_after_market_report`, `load_report`, `get_report`
- Scanner report classes: `DailyAfterMarketScanner` or `AfterMarketScanner` with `after_market_report`, `get_report`, or `load_report`

## Test Commands

```bash
.\.venv\Scripts\python.exe -m pytest tests\test_after_market_bridge.py tests\test_next_bridge.py
npm run lint
npm run build
```

## Follow-Up

- Scanner engineer should expose one of the supported scan entry points in `scanner/daily_after_market.py`.
- Scanner engineer should ensure saved report JSON uses the same top-level fields: `scanId`, `executedAt`, `marketType`, `counts`, `aList`, `bList`, and `avoidList`.
- Frontend engineer can call the scan route directly from the strategy page without needing Python details.
