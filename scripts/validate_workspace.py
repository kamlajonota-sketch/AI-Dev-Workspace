"""Check that essential AI-Dev-Workspace guidance files exist.

Run: python scripts/validate_workspace.py
This script uses only the Python standard library.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = (
    "README.md",
    "AGENTS.md",
    "docs/WORKFLOW.md",
    "docs/TESTING.md",
    "docs/SECURITY.md",
    "templates/PROJECT_BRIEF.md",
    "templates/TASK_PLAN.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
)


def main() -> int:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    if missing:
        print("Workspace validation failed. Missing required files:")
        for path in missing:
            print(f"  - {path}")
        return 1

    empty = [
        path for path in REQUIRED_FILES
        if not (ROOT / path).read_text(encoding="utf-8").strip()
    ]
    if empty:
        print("Workspace validation failed. Empty required files:")
        for path in empty:
            print(f"  - {path}")
        return 1

    print(f"Workspace validation passed ({len(REQUIRED_FILES)} required files checked).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
