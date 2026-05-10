"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

const NAV_ITEMS = [
  { href: "/", label: "首頁" },
  { href: "/research", label: "研究" },
  { href: "/strategy", label: "策略" },
  { href: "/validation", label: "驗證" },
  { href: "/execution", label: "執行" },
  { href: "/collaboration", label: "協作" },
  { href: "/analysis-results", label: "分析結果 DB" },
  { href: "/settings", label: "設定" }
];

export function SiteNav() {
  const pathname = usePathname();

  return (
    <nav className="site-nav">
      <div className="brand-block">
        <p className="eyebrow">Next.js + React</p>
        <h1>台股研究協作平台</h1>
        <p className="subtle">Python 分析核心保留，UI 改為 App Router 與 API route。</p>
      </div>
      <div className="nav-links">
        {NAV_ITEMS.map((item) => {
          const isActive = pathname === item.href;
          return (
            <Link
              key={item.href}
              href={item.href}
              className={`nav-link${isActive ? " active" : ""}`}
            >
              {item.label}
            </Link>
          );
        })}
      </div>
    </nav>
  );
}
