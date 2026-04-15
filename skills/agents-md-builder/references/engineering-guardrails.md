# Engineering Guardrails

This file defines the kind of durable, mostly-static rules that can live in
`AGENTS.md` even when they are not directly derived from repository files.

## Use These Only When They Change Agent Behavior

A guardrail belongs in `AGENTS.md` if it tells the agent how to act differently.

Good:
- Check for an existing UI component before creating a new one.
- Prefer extending a shared component over injecting duplicate markup.
- Keep files cohesive; split when one file mixes unrelated areas.
- Avoid huge functions and also avoid micro-functions with no readability or reuse benefit.
- Propose a refactor when duplication is real and close enough in scope to justify it.
- Focus on the requested task; do not perform opportunistic cleanup unless asked.
- Prefer improving local code quality safely even if existing code is mediocre.

Weak:
- Follow SOLID.
- Write clean code.
- Prefer good abstractions.

## Suggested Guardrail Categories

### Reuse

- Search for existing components, helpers, services, or patterns before creating new ones.
- Prefer established primitives and shared abstractions when they already solve the problem.

### Scope Control

- Stay within the requested task.
- Avoid unrelated refactors, dependency churn, or broad formatting-only edits unless asked.

### File And Function Shape

- Avoid files that combine unrelated responsibilities.
- Avoid huge functions with multiple responsibilities.
- Avoid extracting tiny wrappers or helpers unless they improve reuse, testability, or clarity.

### Refactoring

- Flag duplicated code when it is meaningful.
- Propose or perform narrow refactors when they directly support the requested change.
- Do not reshape large areas of the codebase without user approval.

### Existing Code vs Better Patterns

- Do not copy a bad local pattern automatically just because it already exists.
- Prefer safer and clearer local improvements when they fit the task and do not broaden scope excessively.
- Preserve existing conventions when they are intentional, low-risk, and not actively harmful.

### UI / Component Discipline

- Check for existing components and design-system primitives first.
- Prefer reusable components when repetition is likely.
- Do not introduce one-off abstractions prematurely when direct code is clearer.

## Balance Rule

This section should constrain behavior, not enforce dogma. The target is better
default engineering decisions, not ideological purity.
