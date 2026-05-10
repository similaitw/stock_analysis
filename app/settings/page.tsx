import { getSettingsDiagnostics } from "@/lib/settings-diagnostics";
import { hasSettingsAccess, isSettingsPasswordConfigured } from "@/lib/settings-auth";

import { lockSettings, unlockSettings } from "./actions";

export const dynamic = "force-dynamic";

const STATE_COPY = {
  ready: "已就緒",
  warning: "可運作但需注意",
  action: "需要設定"
};

function stateClass(state: keyof typeof STATE_COPY) {
  return `settings-state settings-state-${state}`;
}

function SettingsLogin({ authFailed }: { authFailed: boolean }) {
  const passwordConfigured = isSettingsPasswordConfigured();

  return (
    <main className="page-shell settings-page">
      <section className="settings-lock-panel">
        <div className="settings-lock-card">
          <p className="eyebrow">Protected Settings</p>
          <h2>設定頁需要管理密碼</h2>
          <p>
            這裡包含部署、資料庫、Git 與 worker 狀態。請輸入 `SETTINGS_PASSWORD` 管理密碼後再查看。
          </p>

          {passwordConfigured ? (
            <form action={unlockSettings} className="settings-login-form">
              <label htmlFor="settings-password">管理密碼</label>
              <input
                id="settings-password"
                name="password"
                type="password"
                autoComplete="current-password"
                placeholder="輸入 SETTINGS_PASSWORD"
                required
              />
              {authFailed ? <p className="form-error">密碼不正確，請再試一次。</p> : null}
              <button type="submit">解鎖設定</button>
            </form>
          ) : (
            <div className="settings-lock-warning">
              <strong>尚未設定 SETTINGS_PASSWORD</strong>
              <p>正式環境會保持鎖定，請先在 Vercel 或本機環境變數加入管理密碼。</p>
              <code>vercel env add SETTINGS_PASSWORD production --global-config .vercel-global</code>
            </div>
          )}
        </div>
      </section>
    </main>
  );
}

export default async function SettingsPage({
  searchParams
}: {
  searchParams?: Promise<{ auth?: string }>;
}) {
  const params = await searchParams;
  const canAccessSettings = await hasSettingsAccess();
  if (!canAccessSettings) {
    return <SettingsLogin authFailed={params?.auth === "failed"} />;
  }

  const diagnostics = await getSettingsDiagnostics();
  const topActions = diagnostics.checks.filter((item) => item.state === "action").slice(0, 3);

  return (
    <main className="page-shell settings-page">
      <section className="page-hero">
        <p className="eyebrow">Settings</p>
        <h2>開發與部署設定</h2>
        <p>
          這裡會檢查目前環境，列出我接下來開發、部署、啟用雲端功能需要你補的設定。
          敏感值只顯示是否存在，不會顯示內容。
        </p>
        {isSettingsPasswordConfigured() ? (
          <form action={lockSettings} className="settings-lockout-form">
            <button type="submit" className="secondary-button">鎖定設定頁</button>
          </form>
        ) : null}
      </section>

      <section className="metric-grid">
        <div className="metric-card">
          <p className="metric-label">Ready</p>
          <p className="metric-value">{diagnostics.summary.ready}</p>
          <p className="metric-hint">可以直接使用</p>
        </div>
        <div className="metric-card">
          <p className="metric-label">Needs Attention</p>
          <p className="metric-value">{diagnostics.summary.warning}</p>
          <p className="metric-hint">功能可跑，但後續要規劃</p>
        </div>
        <div className="metric-card">
          <p className="metric-label">Action Required</p>
          <p className="metric-value">{diagnostics.summary.action}</p>
          <p className="metric-hint">需要你補設定或資源</p>
        </div>
      </section>

      {topActions.length > 0 ? (
        <section className="panel settings-next-panel">
          <div className="panel-header">
            <div>
              <p className="eyebrow">Next</p>
              <h2>最需要你先處理</h2>
            </div>
            <span className="status-pill">{topActions.length} 項</span>
          </div>
          <div className="settings-action-list">
            {topActions.map((item) => (
              <article key={item.id} className="settings-action-item">
                <strong>{item.title}</strong>
                <p>{item.prompt}</p>
                {item.command ? <code>{item.command}</code> : null}
              </article>
            ))}
          </div>
        </section>
      ) : null}

      <section className="settings-grid">
        <div className="panel settings-env-panel">
          <div className="panel-header">
            <h2>目前環境</h2>
          </div>
          <dl className="settings-env-list">
            <div>
              <dt>Runtime</dt>
              <dd>{diagnostics.environment.runtime}</dd>
            </div>
            <div>
              <dt>Analysis Storage</dt>
              <dd>{diagnostics.environment.storageMode}</dd>
            </div>
            <div>
              <dt>Project</dt>
              <dd>{diagnostics.environment.projectName}</dd>
            </div>
            <div>
              <dt>Git Remote</dt>
              <dd>{diagnostics.environment.gitRemote}</dd>
            </div>
            <div>
              <dt>Git Author</dt>
              <dd>{diagnostics.environment.gitAuthor}</dd>
            </div>
          </dl>
        </div>

        <div className="panel settings-guide-panel">
          <div className="panel-header">
            <h2>我會怎麼判斷下一步</h2>
          </div>
          <div className="settings-guide-copy">
            <p>
              如果是小批量掃描，我會直接用雲端 fallback；如果要正式保存分析結果，
              先看 managed database；如果要跑完整盤後/XQ 大量掃描，就需要 worker 或 API service。
            </p>
            <p>
              這頁會成為後續開發的檢查入口，避免每次部署前都靠聊天紀錄追設定。
            </p>
          </div>
        </div>
      </section>

      <section className="settings-checks">
        {diagnostics.checks.map((item) => (
          <article key={item.id} className="settings-check-card">
            <div className="settings-check-top">
              <h3>{item.title}</h3>
              <span className={stateClass(item.state)}>{STATE_COPY[item.state]}</span>
            </div>
            <dl>
              <div>
                <dt>目前</dt>
                <dd>{item.current}</dd>
              </div>
              <div>
                <dt>用途</dt>
                <dd>{item.why}</dd>
              </div>
              <div>
                <dt>提示</dt>
                <dd>{item.prompt}</dd>
              </div>
            </dl>
            {item.command ? <code>{item.command}</code> : null}
          </article>
        ))}
      </section>
    </main>
  );
}
