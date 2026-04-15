#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create tool-specific symlinks pointing to AGENTS.md."
    )
    parser.add_argument("repo", nargs="?", default=".", help="Repository path")
    parser.add_argument(
        "--source",
        default="AGENTS.md",
        help="Canonical source file to link to (default: AGENTS.md)",
    )
    parser.add_argument(
        "targets",
        nargs="*",
        help="Tool-specific filenames to symlink, e.g. CLAUDE.md GEMINI.md",
    )
    args = parser.parse_args()

    root = Path(args.repo).resolve()
    source = root / args.source
    targets = args.targets or ["CLAUDE.md"]

    if not source.exists():
        raise SystemExit(f"Canonical source file does not exist: {source}")

    for target_name in targets:
        target = root / target_name
        if target.exists() or target.is_symlink():
            if target.is_symlink() and target.resolve() == source.resolve():
                print(f"ok: {target_name} already links to {args.source}")
                continue
            raise SystemExit(
                f"Refusing to overwrite existing path: {target}. "
                "Remove it first if you want to replace it with a symlink."
            )
        target.symlink_to(source.name)
        print(f"linked: {target_name} -> {args.source}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
