#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import re
import subprocess
from collections import defaultdict
from pathlib import Path

COMMIT_CONFIGS = (
    "commitlint.config.js",
    "commitlint.config.cjs",
    ".commitlintrc",
    ".commitlintrc.json",
    ".commitlintrc.yml",
    ".commitlintrc.yaml",
    ".czrc",
    "cz.toml",
    "release-please-config.json",
    ".releaserc",
    ".releaserc.json",
    ".gitmessage",
    ".gitmessage.txt",
    ".gitmessage.md",
    "commit-template.txt",
)

IGNORE_DIRS = {
    ".git",
    "node_modules",
    "dist",
    "build",
    "coverage",
    "target",
    ".next",
    ".turbo",
    "__pycache__",
}

DOC_EXTENSIONS = {".md", ".markdown", ".txt", ".rst", ".adoc", ".yml", ".yaml", ".json", ".toml", ".js", ".cjs"}
DOC_NAME_HINTS = (
    "readme",
    "contributing",
    "security",
    "design",
    "governance",
    "commit",
    "dco",
    "pull_request_template",
    "pr_template",
    "gitmessage",
)

CONVENTIONAL_RE = re.compile(r"^[a-z]+(\([^)]+\))?!?: .+")
SIGNED_OFF_BY_RE = re.compile(r"^Signed-off-by:\s+.+", re.IGNORECASE | re.MULTILINE)
CO_AUTHORED_BY_RE = re.compile(r"^Co-authored-by:\s+.+", re.IGNORECASE | re.MULTILINE)

TOKEN_PATTERNS = {
    "signoff": (
        "signed-off-by",
        "sign-off",
        "developer certificate of origin",
        " dco",
        "git commit -s",
    ),
    "gpg": (
        "gpg",
        "signed commit",
        "signed commits",
        "verified commit",
        "verified commits",
        "git commit -S",
        "gpgsign",
    ),
    "coauth": (
        "co-authored-by",
        "co-authored",
        "coauthored",
    ),
}

REQUIRED_HINTS = ("required", "must", "always", "mandatory", "mandated", "every commit")
FORBIDDEN_HINTS = ("must not", "do not", "don't", "never", "forbidden", "disallow", "not allowed")
OPTIONAL_HINTS = ("optional", "may", "can", "allowed", "permitted")


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return ""


def run_git(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return ""
    return result.stdout


def recent_commits(root: Path, limit: int = 20) -> list[dict[str, str]]:
    output = run_git(root, "log", f"-n{limit}", "--pretty=%H%x1f%G?%x1f%B%x1e")
    commits: list[dict[str, str]] = []
    for record in output.split("\x1e"):
        record = record.strip()
        if not record:
            continue
        parts = record.split("\x1f", 2)
        if len(parts) != 3:
            continue
        commit_hash, signature_status, body = parts
        subject = body.splitlines()[0].strip() if body.splitlines() else ""
        commits.append(
            {
                "hash": commit_hash.strip(),
                "signature_status": signature_status.strip(),
                "subject": subject,
                "body": body,
            }
        )
    return commits


def doc_candidates(root: Path, max_depth: int = 2, max_files: int = 80) -> list[Path]:
    candidates: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        current = Path(dirpath)
        depth = len(current.relative_to(root).parts)
        dirnames[:] = [name for name in dirnames if name not in IGNORE_DIRS]
        if depth > max_depth:
            dirnames[:] = []
            continue
        for filename in filenames:
            path = current / filename
            name_lower = filename.lower()
            if path.name in COMMIT_CONFIGS:
                candidates.append(path)
                continue
            if path.suffix.lower() not in DOC_EXTENSIONS and not name_lower.startswith(".gitmessage"):
                continue
            in_docs_area = any(part in {"docs", ".github"} for part in path.relative_to(root).parts[:-1])
            hinted_name = any(hint in name_lower for hint in DOC_NAME_HINTS)
            if current == root or in_docs_area or hinted_name:
                candidates.append(path)
            if len(candidates) >= max_files:
                return sorted(set(candidates))
    return sorted(set(candidates))


def classify_line(line: str) -> str:
    lower = line.lower()
    if any(hint in lower for hint in FORBIDDEN_HINTS):
        return "forbidden"
    if any(hint in lower for hint in REQUIRED_HINTS):
        return "required"
    if any(hint in lower for hint in OPTIONAL_HINTS):
        return "optional"
    return "mentioned"


def doc_policy(root: Path, candidates: list[Path], key: str) -> tuple[str, list[str]]:
    token_patterns = TOKEN_PATTERNS[key]
    states: dict[str, set[str]] = defaultdict(set)
    for path in candidates:
        text = read_text(path)
        if not text:
            continue
        for line in text.splitlines():
            lower = line.lower()
            if any(token in lower for token in token_patterns):
                states[classify_line(line)].add(str(path.relative_to(root)))
    for state in ("forbidden", "required", "optional", "mentioned"):
        if states[state]:
            return state, sorted(states[state])[:5]
    return "none", []


def recent_subjects(commits: list[dict[str, str]], limit: int = 12) -> list[str]:
    return [commit["subject"] for commit in commits[:limit] if commit["subject"]]


def summarize_history(commits: list[dict[str, str]]) -> dict[str, int]:
    total = len(commits)
    conventional = sum(1 for commit in commits if CONVENTIONAL_RE.match(commit["subject"]))
    signoff = sum(1 for commit in commits if SIGNED_OFF_BY_RE.search(commit["body"]))
    coauth = sum(1 for commit in commits if CO_AUTHORED_BY_RE.search(commit["body"]))
    signed = sum(1 for commit in commits if commit["signature_status"] and commit["signature_status"] != "N")
    return {
        "total": total,
        "conventional": conventional,
        "signoff": signoff,
        "coauth": coauth,
        "signed": signed,
    }


def guess_subject_style(configs: list[str], history: dict[str, int]) -> str:
    total = history["total"]
    if configs:
        return "A commit convention is likely enforced by config or release tooling."
    if total and history["conventional"] / total >= 0.6:
        return f"Conventional Commits appear common ({history['conventional']}/{total} recent subjects match)."
    if total:
        return "No strong subject convention inferred from recent commit subjects."
    return "No guess available."


def guess_signoff(doc_state: str, files: list[str], history: dict[str, int]) -> str:
    total = history["total"]
    if doc_state == "forbidden":
        return f"Sign-off appears forbidden or discouraged in docs ({', '.join(files)})."
    if doc_state == "required":
        return f"Sign-off appears required or strongly expected in docs ({', '.join(files)})."
    if doc_state == "optional":
        return f"Sign-off appears allowed or optional in docs ({', '.join(files)})."
    if total and history["signoff"] / total >= 0.8:
        return f"Signed-off-by trailers are common in recent history ({history['signoff']}/{total}); likely expected."
    if history["signoff"]:
        return f"Signed-off-by trailers appear in some recent commits ({history['signoff']}/{total}); policy is unclear."
    return "No clear sign-off policy detected."


def guess_gpg(doc_state: str, files: list[str], history: dict[str, int]) -> str:
    total = history["total"]
    if doc_state == "forbidden":
        return f"GPG or signed commits appear forbidden or discouraged in docs ({', '.join(files)})."
    if doc_state == "required":
        return f"GPG or signed commits appear required or strongly expected in docs ({', '.join(files)})."
    if doc_state == "optional":
        return f"GPG or signed commits appear allowed or optional in docs ({', '.join(files)})."
    if total and history["signed"] / total >= 0.8:
        return f"Most recent commits are signed ({history['signed']}/{total}); signing is likely expected."
    if history["signed"]:
        return f"Some recent commits are signed ({history['signed']}/{total}); signing policy is unclear."
    return "No clear GPG or commit-signing policy detected."


def guess_coauth(doc_state: str, files: list[str], history: dict[str, int]) -> str:
    total = history["total"]
    if doc_state == "forbidden":
        return f"Co-Authored-By trailers appear forbidden or discouraged in docs ({', '.join(files)})."
    if doc_state == "required":
        return f"Co-Authored-By trailers appear required or strongly expected in docs ({', '.join(files)})."
    if doc_state == "optional":
        return f"Co-Authored-By trailers appear allowed or optional in docs ({', '.join(files)})."
    if history["coauth"]:
        return f"Co-Authored-By trailers appear in recent history ({history['coauth']}/{total}); likely allowed, but not proven required."
    return "No clear Co-Authored-By policy detected."


def main() -> int:
    parser = argparse.ArgumentParser(description="List commit-style signals for AGENTS drafting.")
    parser.add_argument("repo", nargs="?", default=".", help="Repository path")
    args = parser.parse_args()

    root = Path(args.repo).resolve()
    if not root.exists():
        raise SystemExit(f"Repository path does not exist: {root}")

    configs = [name for name in COMMIT_CONFIGS if (root / name).exists()]
    if (root / ".changeset").exists():
        configs.append(".changeset/")

    commits = recent_commits(root)
    subjects = recent_subjects(commits)
    history = summarize_history(commits)

    candidates = doc_candidates(root)
    signoff_doc_state, signoff_doc_files = doc_policy(root, candidates, "signoff")
    gpg_doc_state, gpg_doc_files = doc_policy(root, candidates, "gpg")
    coauth_doc_state, coauth_doc_files = doc_policy(root, candidates, "coauth")

    print(f"# Commit Signals: {root.name}\n")
    print("## Config evidence")
    if configs:
        for item in configs:
            print(f"- {item}")
    else:
        print("- none detected")

    print("\n## Documentation evidence")
    if signoff_doc_state != "none":
        print(f"- sign-off: {signoff_doc_state} ({', '.join(signoff_doc_files)})")
    else:
        print("- sign-off: no documentation evidence")
    if gpg_doc_state != "none":
        print(f"- GPG/signing: {gpg_doc_state} ({', '.join(gpg_doc_files)})")
    else:
        print("- GPG/signing: no documentation evidence")
    if coauth_doc_state != "none":
        print(f"- Co-Authored-By: {coauth_doc_state} ({', '.join(coauth_doc_files)})")
    else:
        print("- Co-Authored-By: no documentation evidence")

    print("\n## Recent commit subjects")
    if subjects:
        for line in subjects:
            print(f"- {line}")
    else:
        print("- no commits detected or git history unavailable")

    print("\n## Recent trailer and signing history")
    if history["total"]:
        print(f"- Signed-off-by trailers: {history['signoff']}/{history['total']}")
        print(f"- Co-Authored-By trailers: {history['coauth']}/{history['total']}")
        print(f"- Signed commits: {history['signed']}/{history['total']}")
    else:
        print("- no commit history available")

    print("\n## Conservative guess")
    print(f"- Subject style: {guess_subject_style(configs, history)}")
    print(f"- Sign-off: {guess_signoff(signoff_doc_state, signoff_doc_files, history)}")
    print(f"- GPG/signing: {guess_gpg(gpg_doc_state, gpg_doc_files, history)}")
    print(f"- Co-Authored-By: {guess_coauth(coauth_doc_state, coauth_doc_files, history)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
