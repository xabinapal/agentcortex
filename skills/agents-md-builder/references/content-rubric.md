# Content Rubric

Use this rubric to decide what belongs in the generated file.

After deciding that a topic belongs somewhere, use `section-emission-policy.md`
to decide whether it belongs in the root file, a scoped file, or should be omitted.

## Must Include

- Repository purpose
- Base agent defaults when the repo is greenfield or low-signal
- Primary stack
- Workflow authority and common commands
- Repository layout at the area or package level
- Quality gates or testing expectations
- Commit format and commit cadence when commits matter
- Agent context, MCPs, and scoped-file policy

## Include If Present

- Validation scope
  - Prefer narrow or package-level checks when the repo supports them.
- Instruction precedence
  - Explain how root and scoped `AGENTS.md` files interact when both exist.
- Approval boundaries
  - Explain which operations require explicit approval.
- Safety boundaries
  - Examples: no deploys unless explicitly asked, no production access, no destructive commands by default.
- Escalation triggers
  - Explain when the agent must stop and ask before proceeding with high-risk or ambiguous work.
- Generated vs source files
  - Examples: `dist/`, generated clients, compiled assets, vendored output.
- Dependency policy
  - Examples: exact pinning, lockfile update rules, internet verification before install.
- Area boundaries
  - Explain stable responsibilities of frontend, backend, BFF, database, infra, shared packages, or similar areas.
- Environment model
  - Explain where env files live, which are committed vs local-only, and how environments are provisioned.
- Change discipline
  - Examples: stay focused on the requested task, avoid unrelated refactors, preserve user changes.
- Change coupling
  - Explain when changing one surface requires updating docs, configs, specs, generated code, or clients.
- Engineering guardrails
  - Only include concrete, enforceable guidance, not vague slogans.
- Release or deploy workflow
  - Only if stable and relevant to agent behavior.
- Documentation maintenance
  - Explain when `README.md`, `CONTRIBUTING.md`, `DESIGN.md`, and similar stable docs must be updated.
- Commit trailer and signing policy
  - Explain sign-off, GPG signing, and `Co-Authored-By` rules when the repo has evidence for them.
- Cross-tool compatibility
  - Explain that `AGENTS.md` is canonical and tool-specific filenames should symlink to it.
- Repo-shared MCPs and skills
  - Explain only the MCPs, skills, or agent tooling that are repository-shared or explicitly approved for inclusion.
- Project-local discovered tooling
  - Explain local `.agents/`, `.claude/`, `.codex/`, or similar tooling when the user confirms it is expected for this project, often with `if available` wording.
- Globally available tooling
  - Explain only if the user explicitly wants it included, usually with `if available` wording.
- Response or handoff format
  - Explain what the AI should report back after making changes.
- Definition of done
  - Explain what must be true before the AI considers the work complete.
- Search or navigation strategy
  - Explain how the agent should explore the repo efficiently.
- Validation order
  - Explain the fastest-safe sequence of checks when that matters.
- Failure reporting
  - Explain how to report skipped checks, ambiguous policy, or unverifiable behavior.
- Mutation boundaries
  - Explain what should not be edited directly.
- Schema or migration discipline
  - Explain how database or schema changes are handled, if present.
- Contract discipline
  - Explain how APIs, schemas, clients, or shared interfaces should stay in sync.
- Secrets or data handling
  - Explain how env files, credentials, fixtures, or production-like data must be handled.
- Workspace hygiene
  - Explain how to avoid clobbering unrelated user changes.
- Refactor thresholds
  - Explain when refactors should be proposed, done narrowly, or left alone.
- Observability or debugging entry points
  - Explain where logs, fixtures, repro scripts, seeds, or dashboards live if stable enough.
- Branch or PR workflow
  - Explain branch naming, draft PR expectations, screenshots, changelog notes, or similar rules when stable.
- Area-specific invariants
  - Explain only the small number of durable rules that are easy to violate.

## Prioritization Reminder

- Not every "include if present" topic deserves a root section.
- Prefer root sections for behavior that affects most work in the repository.
- Push area-local rules into scoped files.
- Omit sections that only restate sane defaults without adding meaningful guidance.

## Never Include By Default

- File-by-file inventories
- Product feature tours
- Temporary roadmap or sprint notes
- Personal preferences that are not project policy
- Unverified commands
- Generic slogans with no concrete behavioral translation
- Mirrored tool-specific instruction files when a symlink would work
- Auto-listed personal MCPs or local-only skills
- Tooling wording that assumes project-local or global tools exist for every collaborator
- Nested file hierarchies with no explicit precedence rule
- Completion language that claims success without saying what was verified

## Translation Rule

If a team value is expressed as a slogan such as `SOLID`, `KISS`, `YAGNI`, or `DRY`,
translate it into specific agent behavior:

- "check for an existing reusable component before creating a new one"
- "avoid mixing unrelated concerns in one file"
- "prefer cohesive functions over huge functions"
- "avoid extracting tiny helper functions with no reuse or clarity benefit"
- "flag duplicated code and propose a targeted refactor when it is clearly worth it"

Do not leave the slogan alone as the rule.
