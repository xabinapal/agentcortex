# AGENTS.md

## Repository Purpose

- [Describe the repository in one or two sentences.]

## Base Agent Defaults

- Focus on the requested task and avoid unrelated changes.
- Ask before deploys, infra changes, schema migrations, dependency installs,
  destructive commands, or forceful git operations.
- Prefer narrow validation before full-repo validation.
- Use the root `AGENTS.md` as baseline and scoped files as local overrides only.
- Do not commit during investigation or interactive debugging.
- Commit only at stable, validated checkpoints or when the user asks.
- Update this file and other stable docs when the change makes them inaccurate.
- Preserve unrelated user changes.

## Approval Boundaries

- [List actions that require explicit approval.]

## Validation Scope

- [Prefer package-level, area-level, or targeted checks before broad checks.]

## Safety Boundaries

- [No deploys by default, no production access, no destructive commands, etc.]

## Escalation Triggers

- [Ask before high-risk or ambiguous actions such as auth changes, unclear migrations, or contract breaks.]

## Generated vs Source Files

- [What should not be edited directly.]

## Dependency Policy

- [Whether dependency changes are allowed and how versions should be chosen.]

## Environment Model

- [Where env files live and which are local-only.]

## Change Coupling

- [If env vars, commands, contracts, or generated inputs change, what else must be updated.]

## Change Discipline

- [Stay focused, avoid unrelated refactors, preserve user work.]

## Engineering Guardrails

- [Check for existing reusable components before creating new ones.]
- [Avoid mixing unrelated concerns in one file.]
- [Avoid huge functions and pointless micro-abstractions.]

## Commit / PR Conventions

- Commit format: [verified format or placeholder]
- Commit cadence: [validated checkpoints only]

## Definition of Done

- [Task change is coherent, relevant docs are updated, validation is run or skipped with explanation.]

## Documentation Maintenance

- Update stable docs such as `README.md`, `CONTRIBUTING.md`, or `DESIGN.md`
  when this work makes them inaccurate.

## Reporting Expectations

- Report changed files, validation performed, and remaining risks or open questions.
