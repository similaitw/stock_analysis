import os
import sys


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


def main() -> int:
    try:
        from strategies.auto_generated.選股.p_02_基本技術指標.strategies import (
            Cat02基本技術指標Strategies,
        )

        strategy_count = len(
            [name for name in dir(Cat02基本技術指標Strategies) if not name.startswith("_")]
        )
        print(
            "Import success: Cat02基本技術指標Strategies "
            f"({strategy_count} public attributes)"
        )
        return 0
    except Exception as exc:
        print(f"Import failed: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
