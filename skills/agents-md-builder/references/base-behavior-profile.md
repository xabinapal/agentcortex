# Base Behavior Profile

Use this when a repository is new, under-documented, or intentionally bootstrapped
before the real workflow surfaces exist.

The goal is to establish sane default agent behavior first, then layer repository
facts on top as they become available.

## Default-On Behaviors

### Approval Boundaries

- Ask before deploys, schema migrations, dependency installs, network calls that
  change state, destructive file operations, forceful git commands, or infra changes.
- Default to coding and validation only unless explicitly told to operate external systems.

### Scope Control

- Stay focused on the requested task.
- Avoid unrelated cleanup, opportunistic refactors, or broad formatting churn unless asked.

### Validation Strategy

- Prefer the narrowest meaningful validation first.
- Run broader checks only when they are necessary or when the repo defines them as required.
- If validation cannot be run, say what was skipped and why.

### Instruction Precedence

- Treat the root `AGENTS.md` as the baseline contract for the whole repository.
- Scoped `AGENTS.md` files should add local deltas only for their subtree.
- Tool-specific filenames should point back to `AGENTS.md` and not carry separate rules.

### Commit Behavior

- Do not commit during exploration, reproduction, or iterative debugging.
- Commit only at validated checkpoints or when the user asks.
- Do not assume sign-off, GPG signing, or `Co-Authored-By` policy when the repo has not defined it.

### Documentation Maintenance

- Update `AGENTS.md` and any stable docs that become inaccurate because of the change.

### Escalation Triggers

- Ask before deploys, destructive operations, ambiguous migrations, security-sensitive
  changes, or contract changes with unclear downstream impact.
- Ask when repository evidence conflicts on a high-risk behavior.

### Canonical Agent File

- Treat `AGENTS.md` as the canonical project instruction file.
- If a tool requires another filename such as `CLAUDE.md`, create a symlink to `AGENTS.md`
  instead of maintaining a mirrored copy.

### Shared Agent Tooling Only

- Document repo-shared MCPs, skills, or agent tooling when they are relevant.
- If project-local tooling is discovered in `.agents/`, `.claude/`, `.codex/`, or
  similar directories, ask whether it should be expected and enforced for this project.
- If globally available tooling is useful, ask which tools should be mentioned.
- Use `if available` wording for tooling that is not guaranteed for every collaborator.

### Workspace Hygiene

- Preserve unrelated user changes.
- Do not revert or overwrite work you did not create unless explicitly asked.

### Generated / Source Boundaries

- Avoid editing generated, vendored, or derived files directly unless that is the intended workflow.
- Prefer editing the source input and regenerating.

### Change Coupling

- If commands change, update agent guidance and stable docs that reference them.
- If env vars change, update examples, config schemas, and setup or deployment docs.
- If contracts or schemas change, update the coupled specs, clients, tests, or fixtures the repo expects.

### Dependency Hygiene

- Follow repo policy for dependency changes.
- If policy is unknown, ask before adding dependencies.
- If installing or upgrading, verify the intended version from the authoritative source first.

### Reuse And Guardrails

- Check for existing reusable components, helpers, or patterns before creating new ones.
- Keep files cohesive.
- Avoid huge functions and pointless micro-abstractions.
- Flag meaningful duplication and propose a narrow refactor when it helps the task.

### Reporting

- Report what changed, what was verified, and what remains uncertain or risky.
- Treat work as done only after the relevant checks and doc updates have either happened or been called out as missing.

## Suggested Rendering

These defaults can appear under sections such as:

- `Approval Boundaries`
- `Validation Scope`
- `Instruction Precedence`
- `Safety Boundaries`
- `Escalation Triggers`
- `Change Discipline`
- `Change Coupling`
- `Engineering Guardrails`
- `Commit / PR Conventions`
- `Documentation Maintenance`
- `Cross-Tool Compatibility`
- `Definition of Done`
- `Reporting Expectations`

## Greenfield Questions

For a brand-new repo, ask only the minimum needed to specialize the base profile:

1. What is this repository for?
2. What are the main areas or subsystems?
3. What is the expected workflow authority today?
4. Are deploys, schema changes, or dependency installs allowed by default?
5. What commit format or PR expectations should apply?
