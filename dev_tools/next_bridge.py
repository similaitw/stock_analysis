from __future__ import annotations

import contextlib
import json
import os
import sys
from typing import Any

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from data.fetcher import DataFetcher


def _safe_float(value: Any) -> float | None:
    try:
        if value is None or value == "":
            return None
        return float(value)
    except (TypeError, ValueError):
        return None


def _history_payload(ticker: str) -> dict[str, Any]:
    # Keep stdout reserved for the final JSON payload so the Next.js bridge can
    # safely parse the response. Existing data-layer logs are redirected to stderr.
    with contextlib.redirect_stdout(sys.stderr):
        name, industry, description = DataFetcher.get_stock_info(ticker)
        current_price = DataFetcher.fetch_current_price(ticker)
        fundamentals = DataFetcher.fetch_fundamentals(ticker)
        history = DataFetcher.fetch_history(ticker, period="6mo")

    candles: list[dict[str, Any]] = []
    if not history.empty:
        tail = history.tail(60).reset_index()
        date_key = tail.columns[0]
        for _, row in tail.iterrows():
            date_value = row[date_key]
            candles.append(
                {
                    "date": getattr(date_value, "strftime", lambda fmt: str(date_value))("%Y-%m-%d"),
                    "close": _safe_float(row.get("Close")),
                    "volume": _safe_float(row.get("Volume")),
                }
            )

    return {
        "ticker": ticker,
        "name": name,
        "industry": industry,
        "description": description,
        "currentPrice": _safe_float(current_price),
        "fundamentals": fundamentals,
        "history": candles,
    }


def main() -> int:
    if len(sys.argv) < 3:
        print(json.dumps({"error": "Usage: next_bridge.py research <ticker>"}))
        return 1

    command = sys.argv[1]
    ticker = sys.argv[2]

    if command != "research":
        print(json.dumps({"error": f"Unknown command: {command}"}))
        return 1

    payload = _history_payload(ticker)
    print(json.dumps(payload, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
