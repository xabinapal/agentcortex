---
name: agents-md-builder
description: Research a repository and generate or refresh a concise, durable AGENTS.md focused on stable operational context such as repository purpose, stack, major directories, workflows, commands, commit conventions, MCPs, and existing agent tooling. Use when creating AGENTS.md, CLAUDE.md, GEMINI.md, or related agent-instruction files; when an existing file is too verbose, too volatile, or too generator-driven; when deciding whether a repo needs one root AGENTS.md or a small hierarchy of scoped files; or when converting scattered agent rules into a shared root document.
disable-model-invocation: true
user-invocable: true
context: fork
license: MIT
metadata:
  author: Xabier Napal
  version: "1.0"
---

# AGENTS.md Builder

## Goal

- Produce agent instructions that help future agents work effectively without
  encoding brittle walkthroughs of every feature, screen, or file.
- Favor stable, reusable context over exhaustive documentation.
- Keep automation narrow. Use scripts for evidence gathering, not for deciding
  the final wording or structure by themselves.

## Workflow

1. Determine whether the repo is greenfield / low-signal or mature enough for evidence-led drafting.
2. If the repo is greenfield or under-documented, start from `references/base-behavior-profile.md`
   and `assets/templates/base-AGENTS.bootstrap.md`, then specialize it with the
   minimum user input required.
3. Determine the repo archetype using `references/repo-archetypes.md`.
4. If the runtime supports subagents, use them explicitly:
   - copy or adapt the files in `assets/subagents/`
   - run `purpose-layout-researcher`, `tooling-workflow-researcher`, and `conventions-integrations-researcher`
5. If the runtime does not support subagents, simulate the same workflow in
   three passes yourself.
6. Optionally run the helper scripts for evidence gathering only:
   - `scripts/repo_signals.py <repo>`
   - `scripts/commit_signals.py <repo>`
7. Read only the files that materially improve accuracy:
   - `README*`, `CONTRIBUTING*`, existing `AGENTS.md` / `CLAUDE.md` / `GEMINI.md`
   - top-level manifests and package-definition files
   - workflow authority surfaces such as task runners, env/toolchain config, CI workflows, and automation directories
   - commit and release config such as `commitlint`, `.changeset`, `release-please`, `semantic-release`
   - MCP and agent config such as `.mcp.json`, `.claude/*`, `.codex/*`, `.agents/*`, `.cursor/*`
8. Use `references/agent-tooling-policy.md` before writing anything about MCPs,
   skills, or other agent-side tooling.
9. Classify visible tooling as repo-committed/shared, project-local discovered,
   or globally available before deciding how to write about it.
10. Treat repo-shared or user-approved tooling as in-scope, but never auto-enumerate
   globally available tools into shared docs without user confirmation.
11. Use `references/content-rubric.md` to decide which sections belong in the output.
12. Use `references/section-emission-policy.md` to decide which sections belong in
    the root file, which belong in scoped files, and which should be omitted.
13. Use `references/precedence.md` before writing nested files or cross-tool compatibility rules.
14. Use `references/escalation-triggers.md` to decide when the file should tell future agents to stop and ask.
15. Use `references/change-coupling.md` to capture stable "if X changes, also update Y" rules.
16. Use `references/completion-and-validation.md` to encode definition of done,
    validation order, and failure-reporting expectations.
17. Draft the root `AGENTS.md` from `assets/templates/root-AGENTS.template.md` or
   the bootstrap template, depending on repository maturity.
18. Use `references/scoping.md` before creating nested `AGENTS.md` files.
19. Create nested `AGENTS.md` files only when a subtree has a distinct toolchain,
   command set, deployment boundary, or ownership model.
20. For monorepos, treat the root file as the whole-repository contract and treat
   major areas such as frontend, backend, BFF, database, infra, or packages as
   candidates for scoped files only when they have meaningful local rules.
21. If the work changes repository structure, major area boundaries, commands,
    quality gates, or commit workflow, update the relevant `AGENTS.md` files in
    the same task.
22. If the work changes behavior described in stable project docs such as
    `README.md`, `CONTRIBUTING.md`, `DESIGN.md`, architecture docs, or setup docs,
    update those docs in the same task or flag the drift explicitly.
23. Run the anti-pattern check in `references/anti-patterns.md`.
24. Use `references/cross-tool-compatibility.md` when the repository wants
    `CLAUDE.md`, `GEMINI.md`, or other tool-specific instruction filenames.
25. Prefer symlinks from tool-specific files back to `AGENTS.md` instead of
    mirrored copies.
26. Use `scripts/link_agent_files.py <repo> CLAUDE.md GEMINI.md ...` to create
    those symlinks safely when needed.
27. Ask the user for decisions only after the repo scan has narrowed the unknowns,
    except in greenfield repos where a small bootstrap questionnaire is necessary.
28. If the repository needs tool-specific instruction filenames, link them back
    to `AGENTS.md` instead of maintaining mirrored content.

## Keep / Exclude

Include:

- Repository purpose and major boundaries
- Base stack, runtime, package managers, and main dependencies
- Common build, test, lint, format, and release commands
- Stable repository layout at the level of major directories or packages
- Validation scope and whether narrow checks should be preferred over full-repo checks
- Safety boundaries such as deploy restrictions and destructive-command defaults
- Escalation triggers for high-risk or ambiguous work that must pause for user input
- Generated-vs-source guidance when the repo has generated artifacts or vendored output
- Dependency policy when the repo has stable rules for adding or updating dependencies
- Environment model when environment files or provisioning materially affect the work
- Change-coupling rules such as env-var, schema, or API changes that require related updates
- Change discipline and concrete engineering guardrails when they are stable project policy
- Commit and PR conventions when they can be verified
- Commit cadence: when not to commit, when to commit, and what counts as a stable checkpoint
- Commit trailer and signing policy when sign-off, GPG signing, or `Co-Authored-By` rules exist
- Definition of done, validation order, and failure-reporting expectations when they are stable enough to encode
- Relevant MCPs, skill folders, agent context files, and security constraints
- Relevant agent tooling, with correct distinction between repo-shared, project-local, and globally available
- Cross-tool compatibility strategy when tool-specific filenames are required
- Precedence and inheritance rules when both root and scoped files exist
- When `AGENTS.md` itself must be updated because the repository contract changed
- When stable repository docs must be updated to avoid drift
- Durable editing expectations such as testing requirements or unsafe commands to avoid

Exclude:

- File-by-file inventories
- Screen-by-screen or endpoint-by-endpoint feature tours
- Temporary tickets, migration notes, roadmap items, and sprint context
- Developer-local secrets, sandbox URLs, and ephemeral environment details
- Repeated README prose that does not change agent behavior
- Generic engineering slogans with no concrete behavioral meaning

## Research Standards

- Treat helper-script output as inventory, not as truth.
- Prefer config-file evidence over file-name inference.
- Prefer short, verified commands over generic recommendations.
- Look for sources of truth by category first: package manifests, task surfaces,
  environment/toolchain config, CI, automation directories, and docs.
- Trace indirection. If one surface delegates to another, follow the delegation
  until you find the real source of truth.
- When a source disagrees with repository evidence, trust the repository.
- When writing nested files, root guidance is the baseline and scoped files should
  only add local deltas or explicit overrides.
- When the repository is ambiguous, use a short TODO or ask the user instead of guessing.

## Monorepo Strategy

- The root `AGENTS.md` should describe the whole repository, not just one package.
- Describe major areas such as frontend, backend, BFF, database, infra, or
  shared packages at a high level.
- Do not create one `AGENTS.md` per directory.
- Create scoped files for logical areas only when they need local commands,
  stack details, safety rules, or ownership boundaries that would clutter the root.
- In scoped files, document local deltas only; keep shared rules in the root file.

## Maintenance And Commit Defaults

- Structural changes should trigger `AGENTS.md` updates by default.
- Update the relevant root or scoped file when the work changes:
  - major repository areas or boundaries
  - canonical commands or task runners
  - quality gates, deployment flow, or release workflow
  - commit policy or review expectations
- Do not wait for the user to explicitly request that update when the change is material.
- Apply the same default to stable project docs such as `README.md`,
  `CONTRIBUTING.md`, `DESIGN.md`, and setup or architecture docs when the change
  would make them inaccurate.
- Investigation, reproduction, debugging, and back-and-forth validation are not commit points.
- Commit at stable checkpoints: after the change is coherent, tested to the repo's standard,
  and described accurately.
- Avoid both extremes: no commit spam during iteration, and no giant catch-all commit after a long session.

## Ask The User Only For Material Gaps

- Confirm the repository purpose if the scan only finds technical artifacts.
- For greenfield repos, ask the minimum bootstrap questions from `references/base-behavior-profile.md`.
- Confirm whether the user wants a single root file or a root file plus a small
  number of scoped subtree files.
- Confirm which top-level areas are true operational boundaries only when the
  monorepo shape is unclear from repository evidence.
- Confirm cross-tool syncing if the repo uses `CLAUDE.md`, `GEMINI.md`, Cursor
  rules, Copilot instructions, or other agent-specific formats.
- Confirm whether project-local discovered tooling in `.agents/`, `.claude/`,
  `.codex/`, or similar directories should be enforced or only mentioned as optional.
- Confirm which globally available MCPs or skills should be referenced only when
  the user wants them included.
- Confirm which tool-specific filenames should be symlinked to `AGENTS.md` only
  when the repository intends to support those tools.
- Confirm high-risk escalation rules only when repository evidence and user intent
  disagree on actions such as deploys, migrations, destructive operations, or
  security-sensitive changes.
- Confirm coupled-update rules only when a repo clearly has them but the exact
  surfaces remain ambiguous, such as env files, generated clients, or API specs.
- Confirm the intended commit format when config and git history are both ambiguous.
- Confirm whether sign-off, GPG signing, or `Co-Authored-By` trailers are required,
  optional, or forbidden when repository evidence is ambiguous.

Ask at most one to three short questions at a time. Prefer a reasonable default
when the repo clearly suggests one.

## Subagent Strategy

If the runtime supports subagents, use them explicitly for large or messy repositories.
The bundled subagent files are concrete starting points, not just prompt notes.

- `assets/subagents/purpose-layout-researcher.md`
- `assets/subagents/tooling-workflow-researcher.md`
- `assets/subagents/conventions-integrations-researcher.md`

Read `references/subagents.md` for the handoff contract and merge rules.

## Output Shape

Use this section order unless the repo strongly suggests another order:

1. `Repository Purpose`
2. `Primary Stack`
3. `Common Commands`
4. `Repository Layout`
5. `Quality Gates` or `Testing`
6. `Validation Scope` when the repo supports narrow/package-level validation
7. `Approval Boundaries` or `Safety Boundaries` when the repo has operational limits that affect behavior
8. `Escalation Triggers` when high-risk work must pause for user input
9. `Generated vs Source Files` when generated artifacts are part of the repo
10. `Dependency Policy` when dependency changes have explicit rules
11. `Environment Model` when env setup materially affects development
12. `Change Coupling` when certain changes require related docs, specs, clients, or config updates
13. `Change Discipline` or `Engineering Guardrails` when the project wants durable coding behavior rules
14. `Commit / PR Conventions`
15. `Definition of Done` or `Reporting Expectations` when the repo has a stable completion contract
16. `AGENTS.md Maintenance` when the repository is likely to evolve materially
17. `Documentation Maintenance` when stable docs are likely to drift
18. `Agent Context` or `MCP / Skills`
19. `Instruction Precedence` when nested `AGENTS.md` files exist or should exist
20. `Cross-Tool Compatibility` when tool-specific filenames must point to `AGENTS.md`
21. `Scoped Files` only if nested `AGENTS.md` files exist or should exist

Keep sections short. Most repositories do not need more than one root file and a
small number of bullets per section.

For greenfield repos, it is acceptable to start with a smaller base-policy file
and add repo-specific sections later.

If tool-specific filenames are required, prefer symlinks back to `AGENTS.md`
instead of mirrored or imported copies.

## Resources

- `scripts/repo_signals.py`
  - Inventory manifests, workflows, agent files, MCP files, and top-level directories.
- `scripts/commit_signals.py`
  - Inventory commit-related config and summarize recent commit-title patterns.
- `scripts/link_agent_files.py`
  - Create symlinks from tool-specific instruction filenames back to `AGENTS.md`.
- `references/design-principles.md`
  - Distilled guidance from current AGENTS.md / CLAUDE.md sources.
- `references/inspection-checklist.md`
  - Stable signals to inspect before writing.
- `references/repo-archetypes.md`
  - Choose the right shape for apps, libraries, infra repos, monorepos, and tooling repos.
- `references/scoping.md`
  - Decide when a root file is enough and when nested files are justified.
- `references/precedence.md`
  - Define how root and scoped `AGENTS.md` files interact and how tool-specific symlinks behave.
- `references/escalation-triggers.md`
  - Define when an agent should stop and ask before continuing high-risk or ambiguous work.
- `references/change-coupling.md`
  - Capture stable "if X changes, also update Y" rules such as env vars, contracts, or generated clients.
- `references/completion-and-validation.md`
  - Define definition of done, validation order, and failure-reporting expectations.
- `references/anti-patterns.md`
  - Remove common failure modes such as overexplaining, guessing, and conflicting scopes.
- `references/agent-tooling-policy.md`
  - Distinguish repo-shared, project-local discovered, and globally available agent tooling.
- `references/base-behavior-profile.md`
  - Bootstrap sane default agent behavior for greenfield or low-signal repos.
- `references/commit-policy.md`
  - Distinguish commit format, cadence, trailers, and signing requirements.
- `references/content-rubric.md`
  - Decide what must always be included, what is conditional, and what should be excluded.
- `references/cross-tool-compatibility.md`
  - Keep `AGENTS.md` canonical and link tool-specific files back to it.
- `references/section-emission-policy.md`
  - Decide what belongs in the root file, what should move to scoped files, and what should be omitted.
- `references/engineering-guardrails.md`
  - Translate static engineering values into concrete, enforceable agent behavior.
- `references/maintenance.md`
  - Decide when AGENTS files and stable docs must change and how commit cadence should be described.
- `references/questionnaire.md`
  - User questions to ask only when repo evidence is insufficient.
- `references/research-notes.md`
  - Source-backed findings that informed this skill.
- `references/subagents.md`
  - Subagent prompts and role boundaries for parallel repo analysis.
- `assets/templates/root-AGENTS.template.md`
  - Starter shape for a root file.
- `assets/templates/base-AGENTS.bootstrap.md`
  - Minimal starting point for a new repository before strong repo evidence exists.
- `assets/templates/subtree-AGENTS.template.md`
  - Starter shape for a scoped subtree file.
- `assets/subagents/*.md`
  - Copyable Claude Code subagent definitions for repository research.

## Final Check

- Re-read the draft and remove anything that will drift quickly.
- Ensure commands are real and repo-specific.
- Ensure directory descriptions stay at the package or subsystem level.
- Ensure the root file is still readable in one quick pass.
- Ensure the root file contains only the sections that materially change agent behavior.
- Ensure any nested files contain local deltas rather than a copy of the root file.
- Ensure commit format and commit cadence are both stated when the repository cares about commits.
- Ensure sign-off, GPG signing, and `Co-Authored-By` policy are stated when the repo has evidence for them.
- Ensure AGENTS maintenance expectations are present when structural drift would otherwise be likely.
- Ensure stable project-doc maintenance expectations are present when repo docs are likely to drift.
- Ensure any static coding principles are written as concrete rules, not abstract slogans.
- Ensure tool-specific instruction files are symlinks to `AGENTS.md` when the repo supports those tools.
- Prefer certainty over completeness; leave short TODO markers instead of making up facts.
