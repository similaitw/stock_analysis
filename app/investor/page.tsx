import { InvestorDecisionCockpit } from "@/components/investor-decision-cockpit";
import { listAnalysisResults } from "@/lib/analysis-results";
import { getWorkspaceDashboardSnapshot } from "@/lib/workspace";

export const dynamic = "force-dynamic";

export default async function InvestorPage() {
  const [snapshot, analysisResults] = await Promise.all([
    getWorkspaceDashboardSnapshot(),
    listAnalysisResults(30)
  ]);

  return (
    <main className="page-shell">
      <InvestorDecisionCockpit snapshot={snapshot} analysisResults={analysisResults} />
    </main>
  );
}
