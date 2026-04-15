# Section Emission Policy

Use this after the content rubric. Its job is to keep the root file compact.

The builder should decide for each candidate section:

- always emit in root
- emit in root when repo evidence exists
- emit in root when defaults are overridden or risk is high
- move to scoped docs
- omit

## 1. Always Emit In Root

These establish the minimum repository contract:

- `Repository Purpose`
- `Primary Stack`
- `Common Commands` or equivalent workflow entrypoints
- `Repository Layout`
- `Quality Gates` or `Testing`
- `Commit / PR Conventions` when commits are part of the workflow
- `Agent Context` or `MCP / Skills` when any agent-tooling context exists
- `Cross-Tool Compatibility` when the repository supports tools that require a specific filename
- `Instruction Precedence` when nested files or tool-specific filenames exist

For greenfield repos, `Base Agent Defaults` is also effectively always emitted.

## 2. Emit In Root When Repo Evidence Exists

These belong in the root file when the repository clearly defines them and they
affect day-to-day agent behavior:

- `Validation Scope`
- `Generated vs Source Files`
- `Dependency Policy`
- `Environment Model`
- `Change Coupling`
- `Documentation Maintenance`
- `Definition of Done`
- `Release / Deploy Workflow`
- `Schema / Migration Discipline`
- `Contract Discipline`
- `Search / Navigation Strategy`
- `Observability / Debugging Entry Points`
- `Branch / PR Workflow`

If the rule is real but applies only to one area, move it to a scoped file.

## 3. Emit In Root When Defaults Are Overridden Or Risk Is High

These are important, but only deserve root space when the repository has
non-default expectations or the risk of getting them wrong is high:

- `Approval Boundaries`
- `Safety Boundaries`
- `Escalation Triggers`
- `Change Discipline`
- `Engineering Guardrails`
- `Failure Reporting`
- `Reporting Expectations`
- `Workspace Hygiene`
- `Mutation Boundaries`
- `Secrets / Data Handling`
- `Refactor Thresholds`

Examples:

- If the default is "do not deploy unless asked," you may keep that in a greenfield
  bootstrap file but omit it from a mature root file unless deploy rules are special.
- If the repo has production access risks, secrets, or dangerous generators, keep
  those boundaries explicit in the root file.

## 4. Move To Scoped Docs

Push a section down to a scoped `AGENTS.md` when:

- it is true only for one major area
- it needs local commands or local quality gates
- it would add noise for contributors working elsewhere

Good examples:

- database migration rules that apply only to `database/`
- frontend component guardrails that apply only to `frontend/`
- deployment rules that apply only to `infra/`

## 5. Omit

Omit a candidate section when:

- it repeats another section without adding behavior
- it only restates sane defaults and the repo has no exception worth calling out
- it is vague or slogan-only
- it would push the root file toward checklist sprawl
- it recommends mirrored tool files where a symlink would keep one source of truth

## Compression Rule

If the root file starts accumulating too many optional sections:

- merge related items into a stronger umbrella section
- keep the root as a high-signal summary
- push local details into scoped docs

Examples:

- merge `Approval Boundaries` and `Safety Boundaries` when they are short
- merge `Escalation Triggers` into `Safety Boundaries` when the repo only needs a short list
- merge `Change Discipline` and `Engineering Guardrails` when the rules are brief
- merge `Definition of Done` and `Reporting Expectations` when the repo only needs a concise completion contract
- merge `Branch / PR Workflow` into `Commit / PR Conventions` when only a few lines are needed

## Root Size Heuristic

The root file should usually stay readable in one quick pass.

When in doubt:
- prefer fewer sections with stronger bullets
- preserve the most behavior-changing rules
- remove sections that do not materially change how the agent acts
