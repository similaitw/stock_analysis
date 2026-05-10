# Frontend Work Log: Daily After-Market Screening

## 完成內容

- 新增 `components/after-market-screening-workbench.tsx`，提供每日盤後篩選工作台。
- 在 `app/strategy/page.tsx` 接入新工作台，保留既有 `XQStrategyWorkbench`。
- 在 `app/globals.css` 追加 `after-market-*` 樣式，涵蓋桌面與手機版面、表格橫向捲動、loading/error/empty states。
- UI 支援 TEST/Tw50/All/Custom 股票池、模式、最大掃描數、是否輸出避開名單、自訂股票清單與執行掃描。
- 結果顯示 A 級、B 級、避開三區，並呈現 score、riskScore、分項分數、reasons、risks、nextDayPlan。

## UI Contract

前端送出：

```json
{
  "date": "2026-05-10",
  "marketType": "TEST",
  "stockList": ["2330", "2317"],
  "profile": "balanced",
  "maxStocks": 80,
  "includeRiskList": true,
  "weights": {
    "technical": 40,
    "chip": 30,
    "volume": 15,
    "relativeStrength": 15
  }
}
```

API endpoint：`POST /api/after-market-screening/scan`

前端預期回傳：

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

每筆股票可包含：

```json
{
  "stockId": "2330",
  "stockName": "台積電",
  "score": 82,
  "riskScore": -5,
  "rank": 1,
  "technicalScore": 35,
  "chipScore": 24,
  "volumeScore": 12,
  "relativeStrengthScore": 11,
  "reasons": ["均線多頭排列"],
  "risks": [],
  "nextDayPlan": "觀察是否守住昨高與開盤低點"
}
```

## 測試方式

- `npm run lint`
- `npm run build`
- API 尚可不存在；UI 會顯示 fetch/API error，不會 import 尚未完成的 backend runtime code。

## 後續交接

- 後端工程師完成 `app/api/after-market-screening/scan/route.ts` 後，請對齊上述 payload 與 response。
- 若後端欄位命名不同，優先在 API route normalize，避免前端直接依賴 Python/raw bridge 格式。
- 第二階段可加入最近一次掃描讀取、隔日盤中監控頁與自訂權重編輯。
