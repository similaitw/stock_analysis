import json
import sys
import types

from dev_tools import next_bridge


def _install_fake_after_market_module(monkeypatch):
    fake_module = types.ModuleType("scanner.daily_after_market")

    def after_market_scan(payload):
        print(f"[mock] after-market scan {payload['marketType']}")
        return {
            "scanId": "after_market_20260510_mock",
            "executedAt": "2026-05-10T18:05:00",
            "marketType": payload["marketType"],
            "counts": {"scanned": 2, "aList": 1, "bList": 0, "avoidList": 1},
            "aList": [
                {
                    "stockId": "2330",
                    "stockName": "台積電",
                    "score": 82,
                    "riskScore": -5,
                    "rank": 1,
                    "reasons": ["均線多頭排列"],
                    "risks": [],
                    "nextDayPlan": "觀察是否守住昨高與開盤低點",
                }
            ],
            "avoidList": [
                {
                    "stockId": "0000",
                    "stockName": "Example",
                    "score": 68,
                    "riskScore": -35,
                    "reasons": ["突破 20 日高"],
                    "risks": ["爆量長上影"],
                }
            ],
        }

    def after_market_report(scan_id):
        print(f"[mock] after-market report {scan_id}")
        return {
            "scanId": scan_id,
            "executedAt": "2026-05-10T18:05:00",
            "marketType": "TEST",
            "counts": {"scanned": 1, "aList": 0, "bList": 0, "avoidList": 0},
            "aList": [],
            "avoidList": [],
        }

    fake_module.after_market_scan = after_market_scan
    fake_module.after_market_report = after_market_report
    monkeypatch.setitem(sys.modules, "scanner.daily_after_market", fake_module)


def test_after_market_scan_emits_final_json_only(monkeypatch, capsys):
    _install_fake_after_market_module(monkeypatch)
    payload = {
        "date": "2026-05-10",
        "marketType": "TEST",
        "profile": "balanced",
        "stockList": ["2330", "0000"],
    }
    monkeypatch.setattr(
        sys,
        "argv",
        ["next_bridge.py", "after_market_scan", json.dumps(payload, ensure_ascii=False)],
    )

    assert next_bridge.main() == 0

    captured = capsys.readouterr()
    parsed = json.loads(captured.out)

    assert parsed["scanId"] == "after_market_20260510_mock"
    assert parsed["counts"]["aList"] == 1
    assert parsed["avoidList"][0]["risks"] == ["爆量長上影"]
    assert captured.out.strip().startswith("{")
    assert captured.out.strip().endswith("}")
    assert "[mock] after-market scan TEST" in captured.err


def test_after_market_report_emits_final_json_only(monkeypatch, capsys):
    _install_fake_after_market_module(monkeypatch)
    monkeypatch.setattr(
        sys,
        "argv",
        ["next_bridge.py", "after_market_report", "after_market_20260510_mock"],
    )

    assert next_bridge.main() == 0

    captured = capsys.readouterr()
    parsed = json.loads(captured.out)

    assert parsed["scanId"] == "after_market_20260510_mock"
    assert parsed["marketType"] == "TEST"
    assert "[mock] after-market report after_market_20260510_mock" in captured.err


def test_after_market_scan_missing_scanner_returns_json_error(monkeypatch, capsys):
    def fake_import_module(name):
        if name == "scanner.daily_after_market":
            raise ModuleNotFoundError(
                "No module named 'scanner.daily_after_market'",
                name="scanner.daily_after_market",
            )
        raise AssertionError(f"unexpected import: {name}")

    monkeypatch.setattr(next_bridge.importlib, "import_module", fake_import_module)
    monkeypatch.setattr(
        sys,
        "argv",
        ["next_bridge.py", "after_market_scan", json.dumps({"marketType": "TEST"})],
    )

    assert next_bridge.main() == 1

    captured = capsys.readouterr()
    parsed = json.loads(captured.out)

    assert "scanner.daily_after_market is not available yet" in parsed["error"]


def test_after_market_report_normalizes_persisted_scan_shape(monkeypatch, tmp_path, capsys):
    scan_id = "after_market_20260510_saved"
    scan_dir = tmp_path / "data" / "workspace" / "after_market_scans"
    scan_dir.mkdir(parents=True)
    (scan_dir / f"{scan_id}.json").write_text(
        json.dumps(
            {
                "id": scan_id,
                "date": "2026-05-10",
                "market_scope": "Custom",
                "profile": "balanced",
                "executed_at": "2026-05-10T18:05:00",
                "counts": {"scanned": 1, "aList": 1, "bList": 0, "avoidList": 0},
                "a_list": [{"stockId": "2330", "stockName": "台積電", "score": 82}],
                "b_list": [],
                "avoid_list": [],
                "raw_results": [{"stockId": "2330", "bucket": "A"}],
                "request_payload": {"marketType": "Custom"},
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    def fake_import_module(name):
        if name == "scanner.daily_after_market":
            raise ModuleNotFoundError(
                "No module named 'scanner.daily_after_market'",
                name="scanner.daily_after_market",
            )
        raise AssertionError(f"unexpected import: {name}")

    monkeypatch.setattr(next_bridge, "PROJECT_ROOT", str(tmp_path))
    monkeypatch.setattr(next_bridge.importlib, "import_module", fake_import_module)
    monkeypatch.setattr(sys, "argv", ["next_bridge.py", "after_market_report", scan_id])

    assert next_bridge.main() == 0

    captured = capsys.readouterr()
    parsed = json.loads(captured.out)

    assert parsed["scanId"] == scan_id
    assert parsed["executedAt"] == "2026-05-10T18:05:00"
    assert parsed["marketType"] == "Custom"
    assert parsed["aList"][0]["stockId"] == "2330"
    assert parsed["rawResults"][0]["bucket"] == "A"
