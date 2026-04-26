import { ResearchWorkbench } from "@/components/research-workbench";

export default function ResearchPage() {
  return (
    <main className="page-shell">
      <section className="page-hero">
        <p className="eyebrow">Research</p>
        <h2>研究工作台</h2>
        <p>這裡透過 Next API route 呼叫 Python bridge，沿用原本 `DataFetcher` 的抓資料邏輯。</p>
      </section>
      <ResearchWorkbench />
    </main>
  );
}
