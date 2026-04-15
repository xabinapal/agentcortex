#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
from pathlib import Path

IGNORE_DIRS = {
    ".git",
    ".hg",
    ".svn",
    "__pycache__",
    ".venv",
    "venv",
    "node_modules",
    "dist",
    "build",
    "coverage",
    "target",
    ".next",
    ".turbo",
}

ROOT_MANIFESTS = (
    "package.json",
    "pnpm-workspace.yaml",
    "pyproject.toml",
    "uv.lock",
    "requirements.txt",
    "Cargo.toml",
    "go.mod",
    "Gemfile",
    "composer.json",
)

WORKFLOW_SURFACE_NAMES = (
    "Makefile",
    "justfile",
    "Taskfile.yml",
    "Taskfile.yaml",
    "turbo.json",
    "nx.json",
    "Procfile",
    "Tiltfile",
    "docker-compose.yml",
    "docker-compose.yaml",
    "compose.yml",
    "compose.yaml",
    ".tool-versions",
    ".python-version",
    ".node-version",
    ".nvmrc",
    ".envrc",
    "shell.nix",
    "flake.nix",
)

SURFACE_DIRS = (
    "scripts",
    "bin",
    ".github",
    ".mise",
    ".devcontainer",
)

AGENT_FILES = (
    "AGENTS.md",
    "AGENT.md",
    "CLAUDE.md",
    "CLAUDE.local.md",
    "GEMINI.md",
    "GPT.md",
    ".github/copilot-instructions.md",
)


def shallow_find(root: Path, predicate, max_depth: int = 3) -> list[Path]:
    matches: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        current = Path(dirpath)
        depth = len(current.relative_to(root).parts)
        dirnames[:] = [name for name in dirnames if name not in IGNORE_DIRS]
        if depth > max_depth:
            dirnames[:] = []
            continue
        for filename in filenames:
            path = current / filename
            if predicate(path):
                matches.append(path)
    return sorted(matches)


def relpaths(root: Path, paths: list[Path]) -> list[str]:
    return [str(path.relative_to(root)) for path in paths]


def root_workflow_surfaces(root: Path) -> list[str]:
    surfaces: list[str] = []
    for name in WORKFLOW_SURFACE_NAMES:
        if (root / name).exists():
            surfaces.append(name)

    for child in sorted(root.iterdir()):
        if child.name.startswith(".") and child.name not in SURFACE_DIRS:
            continue
        if child.name in IGNORE_DIRS:
            continue
        if child.is_dir() and child.name in SURFACE_DIRS:
            surfaces.append(child.name + "/")
            continue
        if not child.is_file():
            continue
        lower = child.name.lower()
        if child.name in ROOT_MANIFESTS or child.name in AGENT_FILES:
            continue
        if lower.startswith("mise") and child.suffix == ".toml":
            surfaces.append(child.name)
            continue
        if lower.endswith("file"):
            surfaces.append(child.name)
            continue
        if any(token in lower for token in ("task", "workflow", "build", "deploy", "release", "dev", "env", "tool")):
            surfaces.append(child.name)

    seen: set[str] = set()
    ordered: list[str] = []
    for item in surfaces:
        if item not in seen:
            ordered.append(item)
            seen.add(item)
    return ordered


def main() -> int:
    parser = argparse.ArgumentParser(description="List stable repository signals for AGENTS drafting.")
    parser.add_argument("repo", nargs="?", default=".", help="Repository path")
    args = parser.parse_args()

    root = Path(args.repo).resolve()
    if not root.exists():
        raise SystemExit(f"Repository path does not exist: {root}")

    manifests = [name for name in ROOT_MANIFESTS if (root / name).exists()]
    workflow_surfaces = root_workflow_surfaces(root)
    workflows = relpaths(root, sorted((root / ".github" / "workflows").glob("*"))) if (root / ".github" / "workflows").exists() else []
    agent_files = [name for name in AGENT_FILES if (root / name).exists()]

    shallow_agent_files = shallow_find(
        root,
        lambda path: path.name in {"AGENTS.md", "CLAUDE.md", "GEMINI.md"} and path.parent != root,
    )
    mcp_files = shallow_find(
        root,
        lambda path: "mcp" in path.name.lower() or path.name in {"settings.json"} and ".claude" in str(path.parent),
    )
    top_dirs = [
        child.name + "/"
        for child in sorted(root.iterdir())
        if child.is_dir() and child.name not in IGNORE_DIRS and not child.name.startswith(".")
    ]

    print(f"# Repository Signals: {root.name}\n")
    print("## Root manifests")
    if manifests:
        for item in manifests:
            print(f"- {item}")
    else:
        print("- none detected")

    print("\n## Workflow authority surfaces")
    if workflow_surfaces:
        for item in workflow_surfaces:
            print(f"- {item}")
    else:
        print("- none detected")

    print("\n## CI workflows")
    if workflows:
        for item in workflows:
            print(f"- {item}")
    else:
        print("- none detected")

    print("\n## Agent context files at root")
    if agent_files:
        for item in agent_files:
            print(f"- {item}")
    else:
        print("- none detected")

    print("\n## Nested agent context files")
    nested = relpaths(root, shallow_agent_files)
    if nested:
        for item in nested:
            print(f"- {item}")
    else:
        print("- none detected")

    print("\n## MCP or agent-integration files")
    mcp_rel = relpaths(root, mcp_files)
    if mcp_rel:
        for item in mcp_rel:
            print(f"- {item}")
    else:
        print("- none detected")

    print("\n## Top-level directories")
    if top_dirs:
        for item in top_dirs:
            print(f"- {item}")
    else:
        print("- none detected")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
