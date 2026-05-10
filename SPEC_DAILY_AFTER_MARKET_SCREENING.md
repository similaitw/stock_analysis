# Daily After-Market Screening Development Spec

## 目標

建立每日盤後選股流程，用技術面、籌碼面、量能、相對強弱與風險條件，篩出隔日可能上漲的觀察標的，並另外產出應避開的風險名單。

此功能要接到既有 Next.js 策略頁與 Python 分析核心，成為 XQ-like 模組化策略系統的一部分。

## 使用情境

1. 使用者在每日收盤後執行「盤後篩選」。
2. 系統更新個股日線、三大法人、融資融券、借券賣出與大盤/產業資料。
3. 系統用可組合指標計算每檔股票的多空分數與風險扣分。
4. 系統輸出三類清單：
   - A 級觀察：隔日優先追蹤
   - B 級觀察：等待盤中確認
   - 避開名單：隔日不追或降低權重
5. 隔日盤中可載入前一日清單，監控開盤強弱、量能延續與破線風險。

## 資料來源

優先使用既有 `DataFetcher`，缺資料時逐步補強。

必要資料：

| 類型 | 欄位 | 用途 |
| --- | --- | --- |
| 日線 OHLCV | Open, High, Low, Close, Volume | 技術指標、型態、量能 |
| 三大法人 | 外資、投信、自營商買賣超 | 籌碼加分/扣分 |
| 融資融券 | 融資餘額、融券餘額 | 散戶追高、軋空/回補判斷 |
| 借券賣出 | 借券賣出餘額 | 空方壓力與回補判斷 |
| 大盤/產業 | TAIEX、OTC、產業指數 | 相對強弱 |
| 股票基本資料 | 股票代號、名稱、市場別、產業 | 分群與結果顯示 |

## 盤後流程

```text
更新資料
  -> 建立可交易股票池
  -> 基礎流動性濾網
  -> 技術面評分
  -> 量能評分
  -> 籌碼面評分
  -> 相對強弱評分
  -> 風險扣分
  -> 分級與保存
  -> 隔日盤中監控名單
```

## 基礎濾網

股票先通過基礎條件才進入評分。

預設條件：

| 條件 | 預設值 | 說明 |
| --- | --- | --- |
| 近 20 日平均成交量 | >= 500 張 | 避免流動性不足 |
| 今日成交量 | >= 300 張 | 避免無量訊號 |
| 股價 | >= 10 元 | 避免低價股雜訊 |
| 近 60 日資料數 | >= 45 筆 | 避免資料不足 |
| 處置/注意股 | 排除或標記 | 初版可先標記，後續接官方資料 |

## 評分模型

總分滿分 100，風險扣分可讓分數降低。

| 分類 | 分數 |
| --- | --- |
| 技術面 | 0-40 |
| 籌碼面 | 0-30 |
| 量能 | 0-15 |
| 相對強弱 | 0-15 |
| 風險扣分 | 0 到 -50 |

分級：

| 等級 | 條件 |
| --- | --- |
| A 級觀察 | 總分 >= 75，且風險扣分 > -30 |
| B 級觀察 | 總分 55-74，且風險扣分 > -30 |
| 避開名單 | 風險扣分 <= -30，或重大避開條件成立 |
| 不顯示 | 總分 < 55 且無重大風險 |

## 技術面加分

| 指標 | 分數 | 條件 |
| --- | ---: | --- |
| 均線多頭排列 | +10 | Close > MA5 > MA20 > MA60 |
| 突破 20 日高 | +10 | 今日收盤突破前 20 日高 |
| 均線黃金交叉 | +6 | MA5 上穿 MA20 |
| MACD 黃金交叉 | +6 | MACD 上穿 Signal |
| KD 黃金交叉 | +4 | K 上穿 D |
| RSI 低檔轉強 | +4 | RSI 由 30 下方向上站回 |
| 布林上軌突破 | +4 | Close 突破 Bollinger Upper |

技術面最高計 40 分。

## 量能加分

| 指標 | 分數 | 條件 |
| --- | ---: | --- |
| 成交量放大 | +8 | 今日量 >= 20 日均量 1.5 倍 |
| 價量同步創高 | +5 | 收盤與成交量同創 N 日高 |
| OBV 上升 | +4 | OBV 近 5 日上升 |

量能最高計 15 分。

## 籌碼面加分

| 指標 | 分數 | 條件 |
| --- | ---: | --- |
| 外資連續買超 | +8 | 外資連 3 買且累計達門檻 |
| 投信連續買超 | +10 | 投信連 3 買且累計達門檻 |
| 三大法人同步買超 | +8 | 外資、投信、自營商同日買超 |
| 投信首日介入 | +6 | 今日投信買超，前 5 日安靜 |
| 借券賣出餘額下降 | +4 | 近 5 日借券賣出餘額下降 |
| 融券回補 | +4 | 近 3 日融券餘額下降 |

籌碼面最高計 30 分。

## 相對強弱加分

| 指標 | 分數 | 條件 |
| --- | ---: | --- |
| 強於大盤 | +6 | 近 20 日報酬高於 TAIEX |
| 強於產業 | +6 | 近 20 日報酬高於同產業平均 |
| 大盤弱勢仍抗跌 | +3 | 大盤下跌時個股收紅或守住均線 |

相對強弱最高計 15 分。

## 避開條件與扣分

| 條件 | 扣分 | 說明 |
| --- | ---: | --- |
| 爆量長上影 | -20 | 今日量 >= 20 日均量 2 倍，且上影線過長 |
| 開高走低 | -12 | 開盤強但收盤接近低點 |
| 跌破 MA20 | -12 | 收盤跌破 MA20 |
| 跌破 MA60 | -20 | 收盤跌破 MA60 |
| 融資大增但價格不漲 | -15 | 融資增加且收盤漲幅不足 |
| 外資投信同步賣超 | -20 | 法人籌碼同向偏空 |
| 投信連買後轉賣 | -15 | 原本強勢籌碼鬆動 |
| 借券賣出餘額大增 | -12 | 空方壓力增加 |
| 漲停打開 | -15 | 強勢失敗，隔日容易震盪 |
| 注意/處置股 | -30 | 初版可標記為避開 |

任一重大避開條件成立時，即使總分高，也要列入「避開/風險」區。

## 後端設計

### Python modules

新增或擴充：

| 檔案 | 責任 |
| --- | --- |
| `strategies/indicator_library.py` | 單一指標定義與 evaluator |
| `scanner/daily_after_market.py` | 每日盤後評分流程 |
| `scanner/scoring.py` | 加分、扣分、分級邏輯 |
| `data/workspace_models.py` | 新增盤後篩選結果模型 |
| `dev_tools/next_bridge.py` | 新增 bridge command |

### Bridge commands

```bash
python dev_tools/next_bridge.py after_market_scan <json_payload>
python dev_tools/next_bridge.py after_market_report <scan_id>
```

### Request payload

```json
{
  "date": "2026-05-10",
  "marketType": "All",
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

### Response payload

```json
{
  "scanId": "after_market_20260510_xxxxxxxx",
  "executedAt": "2026-05-10T18:05:00",
  "marketType": "All",
  "counts": {
    "scanned": 1200,
    "aList": 12,
    "bList": 36,
    "avoidList": 44
  },
  "aList": [
    {
      "stockId": "2330",
      "stockName": "台積電",
      "score": 82,
      "riskScore": -5,
      "rank": 1,
      "reasons": ["均線多頭排列", "外資連續買超", "成交量放大"],
      "risks": [],
      "nextDayPlan": "觀察是否守住昨高與開盤低點"
    }
  ],
  "avoidList": [
    {
      "stockId": "0000",
      "stockName": "Example",
      "score": 68,
      "riskScore": -35,
      "reasons": ["突破 20 日高"],
      "risks": ["爆量長上影", "融資大增但價格不漲"]
    }
  ]
}
```

## Workspace 保存

新增 collection：

```text
data/workspace/after_market_scans/
data/workspace/next_day_watchlists/
```

建議模型：

```python
AfterMarketScan
  id
  date
  market_scope
  profile
  executed_at
  weights
  counts
  a_list
  b_list
  avoid_list
  raw_results

NextDayWatchlist
  id
  source_scan_id
  trade_date
  stocks
  monitoring_rules
  created_at
```

## 前端設計

新增頁面或放在 Strategy 頁內分頁：

```text
/strategy
  - XQ 條件組合器
  - 每日盤後篩選
  - 隔日盤中監控
```

每日盤後篩選畫面：

1. 掃描設定
   - 股票池：TEST / Tw50 / All / 自訂
   - 模式：保守 / 均衡 / 積極
   - 最大掃描數
   - 是否輸出避開名單

2. 分數摘要
   - 掃描股票數
   - A 級數量
   - B 級數量
   - 避開數量
   - 前 5 大加分因子
   - 前 5 大風險因子

3. 結果表
   - Rank
   - 股票代號/名稱
   - 總分
   - 技術分
   - 籌碼分
   - 量能分
   - 相對強弱分
   - 風險扣分
   - 命中原因
   - 避開原因
   - 隔日計畫

4. 隔日監控
   - 開盤價 vs 昨收
   - 是否站上昨高
   - 是否跌破開盤低點
   - 盤中量能是否延續
   - 大盤與同族群是否同步

## 隔日盤中確認規則

A/B 名單隔日不直接追價，需通過盤中確認。

| 條件 | 動作 |
| --- | --- |
| 開高後守住昨高 | 保留觀察 |
| 開高跌破開盤低點 | 降級或移入風險 |
| 量能延續且價格站穩 | 升級 |
| 大盤轉弱且個股破均線 | 移入避開 |
| 同族群同步轉強 | 加強信號 |

## MVP 範圍

第一階段先完成：

1. 盤後日線掃描，不做即時串流。
2. 使用目前可取得的日線、法人、融資融券、借券資料。
3. 產出 A 級、B 級、避開三張表。
4. 結果保存到 workspace JSON。
5. Strategy 頁可執行掃描與查看最近結果。
6. 測試涵蓋 scoring、分級、避開規則與 bridge payload。

第二階段：

1. 加入產業相對強弱。
2. 加入注意股/處置股官方資料。
3. 加入隔日盤中監控頁。
4. 加入歷史驗證：統計 A/B 名單隔日、3 日、5 日勝率。
5. 加入自訂權重與模板。

## 驗收條件

1. `npm run build` 通過。
2. `npm run lint` 通過。
3. `python -m pytest` 相關測試通過。
4. 使用 TEST 股票池可在 30 秒內完成盤後掃描。
5. 掃描結果包含 A 級、B 級與避開名單。
6. 每筆結果都要有分數、命中原因與風險原因。
7. 執行後會保存 workspace JSON，首頁/策略頁可讀到最近結果。
8. 無資料或資料不足時，不讓整批掃描失敗，要回傳 skip reason。

## 開發拆分

1. `scanner/scoring.py`
   - 實作 score card 與風險扣分。
   - 加 unit tests。

2. `scanner/daily_after_market.py`
   - 串接 DataFetcher、indicator library、scoring。
   - 支援 TEST/Tw50/All/自訂股票池。

3. `workspace_models.py`
   - 新增 AfterMarketScan 與 NextDayWatchlist。

4. `next_bridge.py`
   - 新增 `after_market_scan` command。
   - stdout 只輸出 JSON。

5. `lib/after-market-screening.ts`
   - Next.js bridge wrapper。

6. `app/api/after-market-screening/scan/route.ts`
   - API route。

7. `components/after-market-screening-workbench.tsx`
   - 前端設定、執行、結果表。

8. `app/strategy/page.tsx`
   - 將每日盤後篩選接入策略頁。

## 非目標

此功能不承諾預測一定上漲，也不產生自動下單建議。第一階段只提供「隔日觀察清單」與「避開清單」，交易決策仍需人工確認。
