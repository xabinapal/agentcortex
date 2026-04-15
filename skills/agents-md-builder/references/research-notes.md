# Research Notes

These notes capture external findings that shaped this skill.

## AGENTS.md

- `agents.md` frames `AGENTS.md` as a predictable home for build steps, tests,
  conventions, and nested subproject guidance.
- The public examples focus on commands, testing instructions, and PR rules
  rather than exhaustive architecture docs.

## OpenAI Codex

- OpenAI's published guidance emphasizes scope and precedence: nested files apply
  to their directory tree and deeper files win on conflicts.
- It also explicitly expects agents to run listed programmatic checks.

## Anthropic Claude Code Memory

- Project memory is intended for commands, coding standards, and workflows.
- `CLAUDE.md` supports `@path` imports, which makes thin top-level files viable.
- Nested memory files are discovered based on the current working subtree.

## Anthropic Subagents

- Subagents are project-shareable Markdown files with frontmatter in `.claude/agents/`.
- They are valuable for parallel research because each one gets a separate context window.
- Focused subagents are recommended over one do-everything agent.

## Builder.io Guidance

- Keep the file small and clear.
- Use concrete examples and specific commands.
- Add rules because of observed agent mistakes, not because a template says so.
- Prefer file-scoped or narrow validation commands when the repository supports them.
