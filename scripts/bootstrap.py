"""Add missing research-workflow template files to an existing project.

Never overwrites, deletes, or copies large research artifacts.
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


FILES = (
    ".gitignore",
    "AGENTS.md",
    "handoff.md",
    "brainstorm.md",
    "dataset.md",
    "dataset/README.md",
    "related_work/README.md",
    "复现/README.md",
    "experiment/evaluation.md",
    "experiment/results.md",
)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path, help="existing project directory")
    parser.add_argument("--dry-run", action="store_true", help="show changes without writing")
    args = parser.parse_args()

    template_root = Path(__file__).resolve().parent.parent
    project_root = args.project.expanduser().resolve()
    if not project_root.is_dir():
        parser.error(f"project directory does not exist: {project_root}")
    if project_root == template_root:
        parser.error("target project must differ from the template repository")

    for relative in FILES:
        source = template_root / relative
        destination = project_root / relative
        if destination.exists():
            print(f"SKIP existing: {relative}")
            continue
        if args.dry_run:
            print(f"WOULD ADD:     {relative}")
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        print(f"ADDED:         {relative}")


if __name__ == "__main__":
    main()
