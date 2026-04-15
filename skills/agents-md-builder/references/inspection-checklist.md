# Inspection Checklist

Inspect the repository in this order and stop once the stable picture is clear.

## Read First

- `README*` for repository purpose and major subprojects
- Existing `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`
- Existing scoped `AGENTS.md` files or tool-specific symlinks that imply precedence rules
- Top-level manifests and ecosystem definition files
- Workflow authority surfaces:
  - task runners and wrapper files
  - environment and toolchain config
  - automation directories such as `scripts/`, `bin/`, or similar
  - CI workflows such as `.github/workflows/*`
- Quality and release config:
  - `commitlint*`, `.changeset/`, `release-please*`, `.releaserc*`
- commit templates, hook config, DCO checks, and signed-commit checks
- env examples, config schemas, API specs, migration directories, generated clients,
  and similar files that reveal change-coupling expectations
- Agent and integration config:
  - `.mcp.json`, `mcp*.json`, `.claude/*`, `.codex/*`, `.agents/*`, `.cursor/*`, `.vscode/*`
  - project-local skill folders and committed agent-tooling config

## Trace Indirection

- If the README says to use one command, inspect where that command resolves.
- If a wrapper file shells out to another system, inspect the target system.
- If tasks are stored in a directory rather than a single file, inspect that directory.
- Stop only when you reach the repo's real source of truth for workflows.

## Extract

- Repository purpose in one or two sentences
- Primary languages and runtimes
- Package managers, environment/toolchain managers, task runners, and wrappers
- Stable commands for dev, test, lint, build, release, and validation
- Major directories or workspace boundaries
- Commit and PR conventions backed by config or history
- Sign-off, GPG/signing, and `Co-Authored-By` policy backed by docs, config, or history
- Precedence across root and scoped instruction files
- Coupled-update surfaces such as env examples, generated types, client SDKs, specs, or migrations
- MCPs, agent skills, and tool-specific instruction files
- Whether those tools are repo-committed/shared, project-local discovered, or globally available

## Ignore By Default

- Generated directories such as `node_modules`, `dist`, `build`, `target`, `.next`
- Deep feature trees unless they define their own toolchain or workflow
- Ticket references, backlog notes, and transient migration docs
- Verbose API descriptions that are better left in existing docs

## Add Scoped Files Only When

- A subtree has its own runtime or package manager
- A subtree has unique commands or quality gates
- A subtree has separate deployment or ownership boundaries
- A root file would become noisy without the split
