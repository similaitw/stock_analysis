import Link from "next/link";

const quickSteps = [
  {
    step: "01",
    title: "先看今日快取",
    body: "進入策略頁後先按「刷新今日快取」，如果今天已經掃過，就直接點批次載入，不必重新等待。"
  },
  {
    step: "02",
    title: "用台灣50練習",
    body: "新手先選「台灣50」與「保守」模式，股性相對容易理解，也比較適合練習判讀。"
  },
  {
    step: "03",
    title: "只把結果當觀察清單",
    body: "A 級不是買進指令，B 級不是追價理由，避開名單則代表今天先不要碰。"
  }
];

const examples = [
  {
    title: "範例一：第一次使用",
    actions: ["進入策略頁", "點台灣50", "模式選保守", "按掃描 50 檔", "先看 A 級觀察與避開原因"],
    note: "如果沒有 A 級，代表今天沒有明確標的。新手要先學會等待。"
  },
  {
    title: "範例二：讀取今天已掃資料",
    actions: ["按刷新今日快取", "在今日已掃批次點一筆", "看 B 級觀察", "記下命中原因與風險原因"],
    note: "B 級適合列入隔日觀察，不適合新手直接追價。"
  },
  {
    title: "範例三：查一檔股票",
    actions: ["在搜尋輸入 2330 或台積電", "勾選股票", "按掃描 1 檔", "比較總分、風險與原因"],
    note: "這個方法適合練習同一檔股票在不同日期的狀態變化。"
  }
];

const resultRules = [
  ["A 級觀察", "明天觀察，不等於直接買"],
  ["B 級觀察", "放進追蹤清單，等待確認"],
  ["避開名單", "短線先不要碰"],
  ["沒有候選", "今天休息也是決策"]
];

export default function BeginnerGuidePage() {
  return (
    <main className="page-shell beginner-guide-page">
      <section className="beginner-hero">
        <div>
          <p className="eyebrow">Beginner Guide</p>
          <h2>股市新手如何使用這個網站</h2>
          <p>
            這個網站不是叫你立刻買股票，而是幫你每天盤後整理觀察清單、風險名單與隔日檢查重點。
            新手先用它練習判讀，再慢慢建立自己的交易紀律。
          </p>
        </div>
        <div className="beginner-hero-card">
          <span>今日練習目標</span>
          <strong>先看懂，不急著下單</strong>
          <Link href="/strategy">開始操作</Link>
        </div>
      </section>

      <section className="beginner-step-grid" aria-label="新手三步驟">
        {quickSteps.map((item) => (
          <article key={item.step}>
            <span>{item.step}</span>
            <h3>{item.title}</h3>
            <p>{item.body}</p>
          </article>
        ))}
      </section>

      <section className="panel beginner-practice">
        <div className="panel-header">
          <div>
            <p className="eyebrow">Practice</p>
            <h2>三個教學範例</h2>
          </div>
          <Link className="secondary-button" href="/strategy">
            到策略頁練習
          </Link>
        </div>

        <div className="beginner-example-list">
          {examples.map((example) => (
            <article key={example.title}>
              <h3>{example.title}</h3>
              <ol>
                {example.actions.map((action) => (
                  <li key={action}>{action}</li>
                ))}
              </ol>
              <p>{example.note}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="beginner-rule-section">
        <div className="panel beginner-rules">
          <div>
            <p className="eyebrow">Reading Rules</p>
            <h2>結果怎麼判讀</h2>
          </div>
          <div className="beginner-rule-list">
            {resultRules.map(([label, action]) => (
              <div key={label}>
                <strong>{label}</strong>
                <span>{action}</span>
              </div>
            ))}
          </div>
        </div>

        <aside className="panel beginner-warning">
          <p className="eyebrow">Risk Note</p>
          <h2>新手先守住三件事</h2>
          <ul>
            <li>不要因為分數高就立刻買。</li>
            <li>每天最多只挑 1 到 3 檔觀察。</li>
            <li>連續練習 2 到 4 週，再用小資金測試。</li>
          </ul>
        </aside>
      </section>
    </main>
  );
}
