# Agent Tooling Policy

Use this when deciding how `AGENTS.md` should talk about MCPs, skills, and other
agent-side tooling.

## Goal

Encourage use of relevant agent tooling without leaking assumptions about what
every collaborator has installed.

## Discovery Classes

Classify tooling into these buckets before writing about it:

### 1. Repo-Committed / Shared

Tooling that is configured in committed repository files or clearly documented
as part of the project.

Examples:

- repo-configured MCP servers
- committed project skill folders
- committed `.claude/`, `.codex/`, `.agents/`, or similar project agent config

### 2. Project-Local Discovered

Tooling discovered inside the current project working tree but not clearly known
to be committed or shared yet.

Examples:

- local `.agents/` directory in the project
- local project skill folders
- project-local subagent definitions
- local `.claude/` or `.codex/` setup visible in the current checkout

These are strong candidates for inclusion, but the builder should ask the user
whether they are expected project tooling or just local setup.

### 3. Globally Available

Tooling the runtime exposes as available to the current user globally, but which
is not project-local or repo-committed.

Examples:

- globally available MCP servers
- globally installed skills
- user-level agent tooling

These should never be assumed to exist for every collaborator.

## Include In Shared AGENTS.md

Include tooling automatically only when one of these is true:

- it is repo-committed / shared
- it is required for normal project work
- the user explicitly asked to include it

Project-local discovered tooling should usually trigger a question.

## Ask Before Referencing Non-Committed Tooling

If tooling is visible but not clearly repo-committed:

- ask whether it should be referenced
- ask whether it is expected project tooling or just local setup
- ask whether it should be enforced, recommended, or mentioned only as optional

Use these defaults:

- repo-committed/shared: include directly
- project-local discovered: ask; if included, often phrase as `if available`
- globally available only: ask; default to optional `if available` wording or omit

## Use `If Available` Wording

When tooling is relevant but not guaranteed for every collaborator, prefer wording like:

- "Use the project-local subagents in `.agents/` if available."
- "Use the shared MCP configuration documented here; if you also have compatible global tooling available, it is optional."
- "If the project-local skills are present in this working copy, use them before falling back to generic exploration."

## Preferred Wording

Prefer wording like:

- "Use the repo-configured MCPs and project-shared skills documented here."
- "Use project-local skills or subagents discovered in this repository if available."
- "If you have additional global tooling available, treat it as optional unless this repo explicitly depends on it."

Avoid wording like:

- "Use your installed MCPs"
- "Use all available skills"
- "Everyone should use these tools" when they are not clearly shared
- any text that assumes every collaborator has the same local agent setup

## Shared vs Local Split

- Shared `AGENTS.md` should document repo-committed / shared tooling directly.
- Project-local discovered tooling can be documented when the user confirms it is
  expected for this project, often with `if available` wording if portability is uncertain.
- Globally available tooling should be opt-in and usually optional.
