from __future__ import annotations

import os
import sqlite3
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
ENV_PATH = PROJECT_ROOT / ".env"
DEFAULT_DB_PATH = PROJECT_ROOT / "prisma" / "dev.db"


def read_database_url() -> str:
    if "DATABASE_URL" in os.environ:
        return os.environ["DATABASE_URL"]

    if ENV_PATH.exists():
        for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
            if line.startswith("DATABASE_URL="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")

    return "file:./dev.db"


def resolve_db_path(database_url: str) -> Path:
    if not database_url.startswith("file:"):
        return DEFAULT_DB_PATH

    relative_path = database_url.removeprefix("file:")
    if not relative_path:
        return DEFAULT_DB_PATH

    if relative_path.startswith("/"):
        return Path(relative_path)

    return (PROJECT_ROOT / "prisma" / relative_path).resolve()


def initialize_database(db_path: Path) -> None:
    db_path.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(db_path)
    try:
        connection.executescript(
            """
            CREATE TABLE IF NOT EXISTS "AnalysisResult" (
                "id" TEXT NOT NULL PRIMARY KEY,
                "sourceKey" TEXT,
                "kind" TEXT NOT NULL,
                "stockId" TEXT NOT NULL,
                "stockName" TEXT,
                "strategyName" TEXT,
                "title" TEXT NOT NULL,
                "summary" TEXT NOT NULL,
                "payload" TEXT,
                "tags" TEXT,
                "source" TEXT NOT NULL DEFAULT 'next-ui',
                "createdAt" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                "updatedAt" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
            );

            CREATE UNIQUE INDEX IF NOT EXISTS "AnalysisResult_sourceKey_key"
            ON "AnalysisResult"("sourceKey");
            """
        )
        connection.commit()
    finally:
        connection.close()


def main() -> int:
    database_url = read_database_url()
    db_path = resolve_db_path(database_url)
    initialize_database(db_path)
    print(f"SQLite database ready at {db_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
