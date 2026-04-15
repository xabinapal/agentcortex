# Compatibility Matrix

## Repository source layout

| Asset type | Source location in this repo | Most portable format |
| --- | --- | --- |
| Skills | `skills/` | `SKILL.md` |
| Commands | `commands/` | Runtime-specific |
| Prompts | `prompts/` | Markdown or text |
| Agents | `agents/` | Runtime-specific |
| Tools | `tools/` | Runtime-specific |
| Plugins | `plugins/` | Runtime-specific |

## Installed runtime targets

| Target | Installed layout | Notes |
| --- | --- | --- |
| OpenAI Codex | `AGENTS.md`, `.agents/skills/*/SKILL.md`, `.agents/plugins/marketplace.json` | `SKILL.md` is portable; marketplace metadata is Codex-specific. |
| Claude Code standalone | `.claude/skills/`, `.claude/commands/`, `.claude/agents/` | Skills follow the open standard; commands and agents are Claude-specific. |
| Claude Code plugins | plugin root with `.claude-plugin/plugin.json`, plus `skills/`, `agents/`, `commands/` | This repository root now follows that shape and can be installed directly as a Claude Code plugin. |
| OpenCode standalone | `.opencode/skills/`, `.opencode/commands/`, `.opencode/agents/`, `.opencode/plugins/` | OpenCode also understands `.agents/skills/` and `.claude/skills/`. |
| OpenAI Codex plugins | plugin root with `.codex-plugin/plugin.json`, plus `skills/` and optional `.mcp.json` or `.app.json` | Plugin manifest and marketplace wiring are Codex-specific. |

## Portability strategy

- Keep repository assets in semantic root directories.
- Use open standards where they exist, especially `SKILL.md`.
- Treat commands, agents, tools, and plugin manifests as adapter layers that
  vary by runtime.
- Add install/export automation only when there is real content to move.

## Reference docs

- AGENTS.md standard: `https://agents.md`
- Agent Skills specification: `https://agentskills.io/specification`
- OpenAI Codex skills: `https://developers.openai.com/codex/skills`
- OpenAI Codex plugins: `https://developers.openai.com/codex/plugins/build`
- Claude Code settings: `https://docs.anthropic.com/en/docs/claude-code/settings`
- Claude Code skills: `https://docs.anthropic.com/en/docs/claude-code/slash-commands`
- Claude Code plugins: `https://docs.anthropic.com/en/docs/claude-code/plugins`
- OpenCode skills: `https://opencode.ai/docs/skills`
- OpenCode commands: `https://opencode.ai/docs/commands`
- OpenCode agents: `https://opencode.ai/docs/agents`
- OpenCode plugins: `https://opencode.ai/docs/plugins`
