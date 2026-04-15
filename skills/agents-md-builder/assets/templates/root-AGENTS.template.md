# AGENTS.md

Use only the sections that materially change agent behavior for this repository.
Merge or omit optional sections when the root file would otherwise become noisy.

## Repository Purpose

- [One or two sentences about what the repository is for.]

## Primary Stack

- Languages: [primary languages]
- Runtime / package managers / task runners: [runtime, package manager, task runner]
- Main dependencies: [only the few dependencies that define the stack]

## Common Commands

- `[command]` - [what it does]
- `[command]` - [what it does]
- `[command]` - [what it does]

## Repository Layout

- `[path-or-package]` - [role]
- `[path-or-package]` - [role]
- `[path-or-package]` - [role]

For monorepos, describe the major areas here, such as frontend, backend, BFF,
database, infra, or shared packages.

## Quality Gates

- [tests, lint, formatting, CI expectations]

## Validation Scope

- [prefer area-level or package-level checks before full-repo checks, if applicable]
- [state the escalation from narrow checks to broader checks when it matters]

## Safety Boundaries

- [no deploys, no production access, no destructive commands, or similar rules]

## Escalation Triggers

- [cases where the agent must stop and ask before proceeding]

## Generated vs Source Files

- [what is generated, what should not be edited directly, and what to ignore by default]

## Dependency Policy

- [pinning rules, lockfile expectations, internet verification requirements, or approval rules]

## Environment Model

- [where env files live, which are local-only, and how environments are provisioned]

## Change Coupling

- [if commands, env vars, schemas, contracts, or generated inputs change, what else must be updated]

## Change Discipline

- [stay focused on the requested task, avoid unrelated changes, preserve user work]

## Engineering Guardrails

- [check for existing reusable components before creating new ones]
- [avoid mixing unrelated concerns in one file]
- [avoid huge functions and also avoid tiny abstractions with no payoff]
- [flag duplicated code and propose a targeted refactor when worthwhile]

## Commit / PR Conventions

- Commit format: [verified format]
- Commit cadence: [when to hold off on committing, and what counts as a stable checkpoint]
- Sign-off: [required / optional / not used / unknown]
- GPG signing: [required / optional / not used / unknown]
- Co-Authored-By: [allowed / required / forbidden / unknown]

## Definition of Done

- [what must be true before the task is considered complete]

## AGENTS.md Maintenance

- Update this file when major repository areas, commands, workflows, or commit
  policy change.

## Documentation Maintenance

- Update stable docs such as `README.md`, `CONTRIBUTING.md`, `DESIGN.md`, setup
  docs, or architecture docs when this work makes them inaccurate.

## Agent Context

- [repo-shared or explicitly approved MCPs, skills, existing agent files, safety constraints, or platform notes]
- [project-local discovered tooling can be enforced or recommended with `if available`, depending on user confirmation]
- [globally available tooling should only be mentioned when explicitly requested, usually with `if available` wording]

## Instruction Precedence

- [root `AGENTS.md` is the baseline contract]
- [scoped files add local deltas or overrides only for their subtree]

## Cross-Tool Compatibility

- `AGENTS.md` is canonical.
- Symlink tool-specific instruction filenames such as `CLAUDE.md` back to `AGENTS.md`.

## Scoped Files

- Add nested `AGENTS.md` files only if a subtree has distinct tooling, commands,
  or operational boundaries.
- Scope them to logical areas, not every directory.
