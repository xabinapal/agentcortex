# Agent Cortex

Agent Cortex is a repository for managing reusable AI agent assets across
OpenAI Codex, Anthropic Claude Code, OpenCode, and similar runtimes.

It is intended to host shared skills, commands, prompts, agents, tools, and
installable plugin packages that can be adapted or distributed across multiple
agent ecosystems.

## Design goals

- Use semantic, domain-first directories at the repository root.
- Prefer open standards where runtimes overlap, especially `SKILL.md`.
- Separate local discovery from distributable plugin packaging.
- Keep room for future install, export, and validation automation.

## Repository layout

- `.claude-plugin/`: Claude Code plugin manifest for installing this repository
  directly in Claude Code.
- `skills/`: reusable skills based on the Agent Skills model.
- `commands/`: reusable command definitions.
- `prompts/`: reusable prompt templates and fragments.
- `agents/`: reusable agent or subagent definitions.
- `tools/`: reusable tool metadata, wrappers, or adapters.
- `plugins/`: distributable plugin packages.
- `scripts/`: reserved for future sync, export, and validation automation.
- `docs/`: architecture and compatibility documentation.

## Planned workflow

1. Author reusable assets in the semantic root directories.
2. Keep shared skills aligned with the open `SKILL.md` standard.
3. Package installable distributions under `plugins/`.
4. Add export and validation automation under `scripts/` when real content
   exists.

## Supported compatibility targets

- OpenAI Codex
- Anthropic Claude Code, including direct installation from the repository root
  via `.claude-plugin/plugin.json`
- OpenCode

See [docs/repository-architecture.md](docs/repository-architecture.md) and
[docs/compatibility-matrix.md](docs/compatibility-matrix.md) for details.
