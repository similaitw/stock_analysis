import type { Metadata } from "next";

import { SiteNav } from "@/components/site-nav";

import "./globals.css";

export const metadata: Metadata = {
  title: "台股研究協作平台",
  description: "Next.js + React front-end for the Taiwan stock analysis workspace"
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="zh-Hant">
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
