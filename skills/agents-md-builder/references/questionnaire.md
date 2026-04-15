# Questionnaire

Ask the user only after scanning the repository and only when the answer changes
the output materially.

## High-Value Questions

1. What is the shortest accurate description of the repository's purpose?
   - Ask this when the repo is all infrastructure, templates, or internal tooling
     and the purpose is not obvious from the files.
2. For a new or lightly-initialized repo, which base agent defaults should differ from the sane defaults?
   - Ask only if the user already signaled exceptions around deploys, commits, dependency installs, or similar behavior.
3. Do you want a single root `AGENTS.md`, or a root file plus a few scoped files?
   - Default to one root file unless the repo clearly has separate domains.
4. Which top-level areas are true operational boundaries?
   - Ask this only when a monorepo has ambiguous folders and it is unclear which
     areas really need local instructions.
5. Which tool-specific filenames such as `CLAUDE.md` or `GEMINI.md` should be
   symlinked to `AGENTS.md`?
   - Ask this only when those tools already appear in the repo or the user asked
     for cross-tool compatibility.
6. Should project-local discovered tooling in `.agents/`, `.claude/`, `.codex/`,
   or similar directories be enforced, recommended with `if available`, or ignored?
   - Ask this when such tooling is visible in the current project but is not clearly repo-shared.
7. Which globally available MCPs or skills should be mentioned, if any?
   - Ask this only when the runtime exposes them and the user wants them reflected in shared guidance.
8. Which commit format should the file state?
   - Ask only when both config and git history are inconclusive.
9. Are sign-off, GPG signing, or `Co-Authored-By` trailers required, optional, or forbidden?
   - Ask this only when docs, config, and recent history do not settle the policy clearly.
10. Which high-risk actions should always require a pause for approval or clarification?
   - Ask this only when the repo has sensitive boundaries but the exact escalation line is not documented.
11. Which follow-up updates are coupled to schema, env, API, or generated-code changes?
   - Ask this only when the repo clearly has coupling expectations but the exact surfaces are not discoverable from files alone.

## Defaults

- Default to one root file.
- Default to concise sections with a few bullets each.
- Default to omitting anything that cannot be verified.
- Default to preserving an existing convention instead of inventing a new one.
- Default to updating AGENTS guidance when structural changes make the old guidance stale.
- Default to describing commit cadence, not just commit syntax.
- Default to distinguishing subject format from trailer/signing policy.
- Default to using the base behavior profile for greenfield repos unless the user specifies exceptions.
- Default to using `if available` wording for tooling that is project-local or globally available but not clearly shared.
- Default to the root file as baseline and scoped files as local overrides only.
- Default to asking on high-risk ambiguity, not on low-risk detail.
