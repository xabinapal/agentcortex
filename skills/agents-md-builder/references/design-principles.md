# Design Principles

## Core Rules

1. Treat `AGENTS.md` as a README for agents, not as a second human README.
2. Optimize for action: commands, boundaries, constraints, and examples matter
   more than philosophy.
3. Keep the root file stable. Favor repository purpose, stack, workflows, and
   conventions over file maps and feature catalogs.
4. Use progressive disclosure. Put extra detail in scoped files, imports, or
   referenced docs only when the root file would become noisy.
5. Prefer concrete, local evidence. A verified command or file path is stronger
   than a generalized suggestion.
6. Prefer examples over abstractions. Reference the package, workflow, or config
   file that encodes the convention when possible.
7. Model categories, not brands. Search for task surfaces, env/toolchain config,
   CI, automation, and docs before you decide which named tool matters.

## Practical Implications

- A good root file is usually short enough to scan in one pass.
- Commands should be real and narrow. If the repo uses file-scoped checks, say so.
- Follow indirection. If `Makefile` calls `mise`, or `mise` calls `.mise/tasks`,
  or scripts are wrappers around another tool, record the true authority chain.
- Nested files should only carry local deltas, not duplicate the root.
- Tool-specific files should stay thin when imports or references are available.
- Iteration is expected. Start concise, then add rules only after observing agent mistakes.

## Why This Skill Avoids A Monolithic Generator

- Repositories vary too much for one script to decide final structure reliably.
- Evidence gathering can be automated, but deciding what is stable, useful, and
  non-drifting still needs agent judgment.
- Small helper scripts are easier to trust, maintain, and adapt across environments.

## Useful Links

- `https://github.com/agentsmd/agents.md`
- `https://docs.anthropic.com/en/docs/claude-code/memory`
- `https://github.com/openai/codex/blob/main/AGENTS.md`
- `https://mcpmarket.com/tools/skills/agents-md-builder`
- `https://prpm.dev/blog/agents-md-deep-dive`
- `https://www.builder.io/blog/agents-md`
- `https://www.builder.io/c/docs/agents-md`
