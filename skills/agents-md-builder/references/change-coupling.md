# Change Coupling

Use this to capture stable "if X changes, also update Y" rules.

Only include couplings that are backed by repository evidence or explicit user policy.

## Common Couplings

- If commands, task runners, or workflow entrypoints change, update `AGENTS.md`
  and any stable docs that point to them.
- If env vars change, update `.env.example`, config schemas, setup docs, and any
  deployment or CI config that must stay aligned.
- If schema or migration rules change, update migrations, seeds, fixtures,
  generated types, and relevant docs or rollback notes as required by the repo.
- If an API or contract changes, update the spec, generated clients, shared
  types, fixtures, integration tests, and downstream callers that depend on it.
- If dependencies change, update lockfiles, package manager metadata, and any
  docs or release notes the repo treats as coupled.
- If generated artifacts change, update the source inputs and regenerate instead
  of hand-editing derived output.
- If major area boundaries or ownership surfaces change, update root and scoped
  `AGENTS.md` files plus any stable architecture docs.

## Writing Rule

- Favor concrete repository-specific couplings over generic reminders.
- Merge related couplings into one short section when they share the same trigger.
- Omit couplings that are already obvious from another stronger section.
