# Repository Architecture

## Intent

This repository is organized to support two concerns at the same time:

1. A source layout that is natural for humans maintaining a shared asset
   repository.
2. Compatibility with runtimes that ultimately expect fixed installation paths.

## Layers

| Layer | Purpose |
| --- | --- |
| `.claude-plugin/` | Claude Code plugin manifest so the repository root can be installed directly as a Claude Code plugin. |
| `skills/` | Shared skills authored as reusable repository assets. |
| `commands/` | Shared command definitions. |
| `prompts/` | Prompt templates and fragments. |
| `agents/` | Agent or subagent definitions. |
| `tools/` | Tool metadata, wrappers, or helper adapters. |
| `plugins/` | Distributable plugin packages. |
| `scripts/` | Future export, sync, and validation automation. |
| `docs/` | Human-readable architecture and compatibility documentation. |

## Design choices

- The repository root is domain-first because this is a product/source
  repository, not an installed runtime configuration folder.
- The portable layer is the file format, especially `SKILL.md` for shared
  skills.
- The current root layout also matches Claude Code's plugin component layout,
  so this repository can be installed directly in Claude Code with a manifest
  at `.claude-plugin/plugin.json`.
- Runtime-specific layouts are still relevant, but they belong in install
  targets, generated output, or plugin packages.
- Plugin packaging is separate because Codex, Claude Code, and OpenCode do not
  share one plugin manifest format.
- Automation is reserved but not implemented yet.

## Source vs install layout

This repository is the source layout.

Installed runtime layouts are different and may look like:

- Codex: `AGENTS.md`, `.agents/skills/`, `.agents/plugins/marketplace.json`
- Claude Code standalone: `.claude/skills/`, `.claude/commands/`,
  `.claude/agents/`
- Claude Code plugin: repository root with `.claude-plugin/plugin.json`, plus
  `skills/`, `commands/`, and `agents/`
- OpenCode: `.opencode/skills/`, `.opencode/commands/`, `.opencode/agents/`,
  `.opencode/plugins/`

Those target layouts should be generated, packaged, or documented when actual
content exists.
