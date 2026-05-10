import { existsSync, readFileSync } from "fs";
import path from "path";

import { getAnalysisStorageMode } from "@/lib/analysis-results";

type CheckState = "ready" | "warning" | "action";

export type SettingsCheck = {
  id: string;
  title: string;
  state: CheckState;
  current: string;
  why: string;
  prompt: string;
  command?: string;
};

export type SettingsDiagnostics = {
  summary: {
    ready: number;
    warning: number;
    action: number;
  };
  environment: {
    runtime: string;
    storageMode: string;
    projectName: string;
    gitRemote: string;
    gitAuthor: string;
  };
  checks: SettingsCheck[];
};

function hasUsefulEnv(name: string) {
  const value = process.env[name];
  return Boolean(value && value.trim() && value !== "your_token_here");
}

function readTextIfExists(filePath: string) {
  try {
    return existsSync(filePath) ? readFileSync(filePath, "utf-8") : "";
  } catch {
    return "";
  }
}

function parseGitConfigValue(config: string, section: string, key: string) {
  const lines = config.split(/\r?\n/);
  let inSection = false;

  for (const line of lines) {
    const trimmed = line.trim();
    if (trimmed.startsWith("[") && trimmed.endsWith("]")) {
      inSection = trimmed === section;
      continue;
    }
    if (inSection && trimmed.startsWith(`${key} =`)) {
      return trimmed.split("=").slice(1).join("=").trim();
    }
  }

  return "";
}

function stateRank(state: CheckState) {
  return state === "action" ? 0 : state === "warning" ? 1 : 2;
}

export async function getSettingsDiagnostics(): Promise<SettingsDiagnostics> {
  const root = process.cwd();
  const gitConfig = readTextIfExists(path.join(root, ".git", "config"));
  const vercelProject = readTextIfExists(path.join(root, ".vercel", "project.json"));
  const hasManagedDatabase = getAnalysisStorageMode() === "managed-database";
  const hasLocalSqlite = getAnalysisStorageMode() === "local-file";
  const hasPythonBridge = existsSync(path.join(root, ".venv", "Scripts", "python.exe"))
    && existsSync(path.join(root, "dev_tools", "next_bridge.py"));
  const hasWorkspaceData = existsSync(path.join(root, "data", "workspace"));
  const isVercel = Boolean(process.env.VERCEL);
  const dataSource = process.env.DATA_SOURCE ?? "AUTO";
  const hasVercelProject = Boolean(vercelProject);
  const hasVercelLocalAuth = existsSync(path.join(root, ".vercel-global", "auth.json"));
  const gitRemote = parseGitConfigValue(gitConfig, "[remote \"origin\"]", "url");
  const gitName = parseGitConfigValue(gitConfig, "[user]", "name");
  const gitEmail = parseGitConfigValue(gitConfig, "[user]", "email");

  const checks: SettingsCheck[] = [
    {
      id: "managed-database",
      title: "Managed DATABASE_URL",
      state: hasManagedDatabase ? "ready" : "action",
      current: hasManagedDatabase
        ? "已接上 managed Postgres"
        : hasLocalSqlite
          ? "目前是本機 SQLite"
          : "雲端尚未設定",
      why: "分析結果要在 Vercel 正式寫入，需要 Neon、Supabase 或其他 managed Postgres。",
      prompt: hasManagedDatabase
        ? "可以寫入雲端分析結果。"
        : "請在 Vercel 加入 production DATABASE_URL，值使用 managed Postgres 連線字串。",
      command: "vercel env add DATABASE_URL production --global-config .vercel-global"
    },
    {
      id: "vercel-env",
      title: "Vercel Environment Variables",
      state: isVercel
        ? hasManagedDatabase ? "ready" : "action"
        : "warning",
      current: isVercel ? "目前在 Vercel runtime" : "目前是本機 runtime",
      why: "部署後只能讀取 Vercel 專案上的 env，不能依賴本機 .env。",
      prompt: isVercel
        ? "若看到 action，代表 production env 還缺必要設定。"
        : "部署前用 vercel env ls 確認 production 是否已配置 DATABASE_URL、FINMIND_API_TOKEN 等項目。",
      command: "vercel env ls --global-config .vercel-global"
    },
    {
      id: "python-bridge",
      title: "Local Python Bridge",
      state: hasPythonBridge ? "ready" : isVercel ? "warning" : "action",
      current: hasPythonBridge ? "本機 Python bridge 可用" : "找不到 .venv 或 next_bridge.py",
      why: "完整盤後篩選與 XQ 掃描仍以 Python 分析核心最完整；Vercel 目前使用 Node/Yahoo fallback。",
      prompt: hasPythonBridge
        ? "本機開發可跑完整 Python 掃描；雲端大型掃描下一步要拆成 managed worker 或 API service。"
        : "若要本機跑完整掃描，先建立 .venv 並安裝 requirements。",
      command: ".\\.venv\\Scripts\\python.exe -m pytest tests\\test_after_market_bridge.py"
    },
    {
      id: "cloud-scanner",
      title: "Cloud Scanner Fallback",
      state: "ready",
      current: "Node/Yahoo fallback 已內建",
      why: "Vercel 沒有 Python bridge 時，盤後篩選與 XQ 條件掃描仍可回應，不再直接 503。",
      prompt: "可用於小批量線上掃描；All/TSE/OTC 大批量掃描仍建議改 queue worker。",
      command: "POST /api/after-market-screening/scan"
    },
    {
      id: "queue-worker",
      title: "Managed Worker / Queue",
      state: "warning",
      current: "尚未拆出背景 worker",
      why: "大型股票池掃描可能超過 Vercel Function 執行時間，應改成排程、佇列或獨立 API service。",
      prompt: "下一階段可接 Vercel Cron + Queue、或把 Python 掃描核心部署成長任務服務。",
      command: "設計 /api/scan-jobs + worker 狀態表"
    },
    {
      id: "finmind-token",
      title: "FINMIND_API_TOKEN",
      state: hasUsefulEnv("FINMIND_API_TOKEN") ? "ready" : "warning",
      current: hasUsefulEnv("FINMIND_API_TOKEN") ? "已設定，不顯示內容" : "未設定或仍是範例值",
      why: "Python 資料來源使用 FinMind 時需要 token；純 Yahoo fallback 不需要。",
      prompt: hasUsefulEnv("FINMIND_API_TOKEN")
        ? "本機完整資料來源可用；若雲端 worker 要使用 FinMind，也要把 token 放到 Vercel env。"
        : "需要完整籌碼/法人資料時，請補 FinMind token。",
      command: "vercel env add FINMIND_API_TOKEN production --global-config .vercel-global"
    },
    {
      id: "data-source",
      title: "DATA_SOURCE",
      state: ["AUTO", "FINMIND", "YFINANCE"].includes(dataSource.toUpperCase()) ? "ready" : "action",
      current: dataSource,
      why: "Python 分析核心會依這個值決定資料來源優先順序。",
      prompt: "建議 production 使用 AUTO；本機除錯才固定 FINMIND 或 YFINANCE。",
      command: "DATA_SOURCE=AUTO"
    },
    {
      id: "workspace-data",
      title: "Workspace Data",
      state: hasWorkspaceData ? "ready" : "warning",
      current: hasWorkspaceData ? "本機 data/workspace 存在" : "找不到 data/workspace",
      why: "首頁、策略頁會讀取既有 JSON workspace 作為歷史掃描與回測資料。",
      prompt: hasWorkspaceData
        ? "本機歷史資料可讀；Vercel 已排除上傳 data/workspace，雲端應改走資料庫。"
        : "若要顯示舊資料，請確認 data/workspace 是否已同步到本機。",
      command: "npm run db:push"
    },
    {
      id: "vercel-link",
      title: "Vercel Project Link",
      state: hasVercelProject ? "ready" : "action",
      current: hasVercelProject ? "已連到 Vercel project" : "尚未 link",
      why: "部署、查 env、查 logs 都需要 .vercel/project.json。",
      prompt: hasVercelProject
        ? "專案已可用 Vercel CLI 部署。"
        : "請先 link 到正確的 Vercel project。",
      command: "vercel link --yes --global-config .vercel-global"
    },
    {
      id: "vercel-auth",
      title: "Vercel CLI Auth",
      state: hasVercelLocalAuth ? "ready" : "warning",
      current: hasVercelLocalAuth ? "本機 .vercel-global auth 存在" : "本機 auth 檔不存在",
      why: "這台 Windows 上預設 Vercel auth 路徑曾經受限，使用 .vercel-global 較穩。",
      prompt: "若部署失敗，先重新登入 Vercel CLI。",
      command: "vercel login --global-config .vercel-global"
    },
    {
      id: "github",
      title: "GitHub Remote / Author",
      state: gitRemote.includes("similaitw/stock_analysis") && gitEmail === "similai.tw@gmail.com" ? "ready" : "action",
      current: gitRemote
        ? `${gitRemote} / ${gitName || "unknown"} <${gitEmail || "unknown"}>`
        : "找不到 Git remote",
      why: "後續 push 與協作交接要固定到你的 GitHub 與指定作者。",
      prompt: "應使用 similaitw/stock_analysis 與 similai.tw@gmail.com。",
      command: "git config user.email similai.tw@gmail.com"
    }
  ];

  const summary = checks.reduce(
    (acc, item) => {
      acc[item.state] += 1;
      return acc;
    },
    { ready: 0, warning: 0, action: 0 }
  );

  return {
    summary,
    environment: {
      runtime: isVercel ? `Vercel ${process.env.VERCEL_ENV ?? "unknown"}` : "Local Next.js",
      storageMode: getAnalysisStorageMode(),
      projectName: process.env.VERCEL_PROJECT_PRODUCTION_URL ?? "stock_analysis",
      gitRemote: gitRemote || "unknown",
      gitAuthor: gitEmail ? `${gitName || "unknown"} <${gitEmail}>` : "unknown"
    },
    checks: checks.toSorted((left, right) => stateRank(left.state) - stateRank(right.state))
  };
}
