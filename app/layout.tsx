import type { Metadata } from "next";

import { SiteNav } from "@/components/site-nav";

import "./globals.css";

export const metadata: Metadata = {
  title: "台股研究協作平台",
  description: "Next.js + React front-end for the Taiwan stock analysis workspace"
};

const skinBootScript = `
try {
  var skin = window.localStorage.getItem("stock-analysis-skin");
  if (["cedar", "graphite", "jade", "harbor", "crimson"].indexOf(skin) !== -1) {
    document.documentElement.dataset.skin = skin;
  }
} catch (error) {}
`;

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="zh-Hant" data-skin="cedar" suppressHydrationWarning>
      <head>
        <script dangerouslySetInnerHTML={{ __html: skinBootScript }} />
      </head>
      <body>
        <div className="app-shell">
          <div className="app-frame">
            <SiteNav />
            {children}
          </div>
        </div>
      </body>
    </html>
  );
}
