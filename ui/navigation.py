from dataclasses import dataclass


@dataclass(frozen=True)
class NavigationSection:
    id: str
    label: str
    icon: str
    description: str

    @property
    def nav_label(self) -> str:
        return f"{self.icon} {self.label}"


NAVIGATION_SECTIONS = [
    NavigationSection("home", "首頁", "🏠", "市場總覽、最近訊號、回測與交接摘要"),
    NavigationSection("research", "研究", "🔎", "單一股票研究工作台"),
    NavigationSection("strategy", "策略", "🧠", "策略目錄、參數設定與掃描工作台"),
    NavigationSection("validation", "驗證", "🧪", "回測、績效摘要與建立交易計畫"),
    NavigationSection("execution", "模擬執行", "📝", "TradePlan 與 PaperOrder 狀態追蹤"),
    NavigationSection("collab", "協作/監控", "🤝", "共享 watchlist、研究筆記與監控快照"),
]


def get_navigation_options() -> list[str]:
    return [section.nav_label for section in NAVIGATION_SECTIONS]


def get_section_by_label(label: str) -> NavigationSection:
    for section in NAVIGATION_SECTIONS:
        if section.nav_label == label:
            return section
    return NAVIGATION_SECTIONS[0]
