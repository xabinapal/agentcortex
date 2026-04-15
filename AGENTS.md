# AGENTS.md

## Repository Purpose

- Agent Cortex manages reusable AI agent assets and installable plugin packages
  across Codex, Claude Code, OpenCode, and similar runtimes.
- The product-facing structure is domain-first: `skills/`, `commands/`,
  `prompts/`, `agents/`, `tools/`, and `plugins/`.

## Primary Stack

- Content types: Markdown, JSON, and Git-managed repository metadata.
- Committed install surface: `.claude-plugin/plugin.json` lets the repository
  root install directly as a Claude Code plugin.
- No package manager, task runner, CI workflow, or repo-wide automation is
  committed yet.

## Common Commands

- `python3 -m json.tool .claude-plugin/plugin.json >/dev/null` - validate the
  Claude Code plugin manifest.
- `git log --oneline --max-count=5` - inspect the current commit convention.
- `git status --short` - confirm the worktree before and after changes.

## Repository Layout

- `.claude-plugin/` - Claude Code plugin manifest at the repository root.
- `skills/`, `commands/`, `prompts/`, `agents/`, `tools/` - source areas for
  reusable agent assets.
- `plugins/` - additional packaged distributions.
- `docs/` - stable architecture and compatibility docs.
- `scripts/` - future export and validation automation; do not assume scripts
  exist beyond what is committed.

## Quality Gates

- No canonical test, lint, or build workflow is committed yet.
- Validate the specific files you touch and keep JSON and Markdown consistent
  with the docs.

## Validation Scope

- Prefer narrow checks over broad verification.
- Validate only the affected manifest or docs unless the repo later adds
  stronger quality gates.

## Safety Boundaries

- Do not invent package managers, CI workflows, MCP config, or runtime-specific
  directories that are not committed.
- Ask before dependency installs, network-changing operations, destructive file
  removals, or forceful git history edits.
- Treat the product-facing layout and install surfaces as deliberate; do not
  reintroduce maintainer-only files into the product model without an explicit
  request.

## Change Discipline

- Stay focused on the requested area and avoid unrelated cleanup or structural
  churn.
- Preserve user changes and keep the source layout domain-first unless the user
  asks to change that boundary.

## Commit / PR Conventions

- Commit format: lowercase Conventional Commits.
- Include a short descriptive body for non-trivial commits.
- Commit only at stable checkpoints or when the user asks.
- Add co-author trailers when requested.

## AGENTS.md Maintenance

- Update this file when repository purpose, top-level layout, install surfaces,
  canonical commands, or commit rules change.

## Documentation Maintenance

- Update `README.md`, `docs/repository-architecture.md`, and
  `docs/compatibility-matrix.md` when product positioning or compatibility
  assumptions change.

## Agent Context

- Repo-shared agent tooling currently committed: `.claude-plugin/plugin.json`.
- No repo-shared `.claude/`, `.agents/`, `.opencode/`, or MCP configuration is
  currently committed.
