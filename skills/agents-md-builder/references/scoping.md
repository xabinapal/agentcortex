# Scoping

## Default

Start with one root `AGENTS.md`.

In a monorepo, that root file should describe the whole repository and its major
areas, not just the package currently being edited.

Split only when a subtree has its own:
- runtime or package manager
- command set or CI checks
- deployment boundary
- security or data-handling rules
- team ownership strong enough to justify local instructions

## Root File Responsibilities

- Explain repository-wide purpose and conventions.
- Describe the major areas of the monorepo such as frontend, backend, BFF,
  database, infra, or shared packages when those areas exist.
- Define shared commands and quality gates.
- Point to major packages or subsystems.
- Say when nested files exist and what they are for.

## Subtree File Responsibilities

- Add only local deltas.
- Represent a logical area or subproject, not just an arbitrary directory.
- Define local commands, runtime details, or safety constraints.
- Avoid repeating shared root guidance unless a local exception exists.

## Precedence

- The closest relevant `AGENTS.md` should win for files in that subtree.
- Use this to keep the root broad and subtree files specific.
- Avoid deep hierarchies unless the repo is genuinely that segmented.

## Suggested Depth

- Root only for most repos
- Root plus one subtree layer for many monorepos
- More than two layers only when the repository structure is already highly segmented

## Practical Rule

- Think in terms of areas, not folders.
- `frontend/`, `backend/`, `bff/`, and `database/` may each deserve scoped files
  if they really behave differently.
- `src/components/button/` almost never does.
