# Anti-Patterns

Use this as a review checklist before finalizing any generated file.

## Common Failure Modes

1. File-by-file inventory
   - Wrong: listing dozens of paths and what each one does.
   - Better: describe major directories, packages, or subsystem boundaries.
2. Feature tour disguised as instructions
   - Wrong: screen-by-screen UX or endpoint-by-endpoint summaries.
   - Better: explain the stack, workflows, and where stable examples live.
3. Unverified commands
   - Wrong: inventing `npm run lint` because many repos have one.
   - Better: read the actual task runner or leave a TODO.
4. Giant root file
   - Wrong: one document trying to cover every app, package, and deployment flow.
   - Better: keep the root short and add scoped files only for real boundaries.
5. Generator-shaped prose
   - Wrong: rigid sections filled with guessed or redundant bullets.
   - Better: let repository evidence shape the output and drop empty sections.
6. Mirroring the README
   - Wrong: copying the whole project overview and getting-started guide.
   - Better: add only the agent-relevant delta.
7. Vague quality rules
   - Wrong: "write clean code" or "follow best practices."
   - Better: cite lint, test, formatting, PR, or commit requirements.
8. Leaking local-only data
   - Wrong: sandbox URLs, personal notes, internal credentials, or machine-specific paths.
   - Better: keep local-only preferences out of versioned project guidance.
9. Conflicting scopes
   - Wrong: a subtree file repeats the root but changes the rule subtly.
   - Better: subtree files should only add local rules or overrides.
10. Over-trusting automation
   - Wrong: accepting helper-script output as the final truth.
   - Better: use scripts to narrow the reading set, then verify manually.
11. Area-blind monorepo docs
   - Wrong: documenting only the current package and calling it the repo guide.
   - Better: let the root file cover the whole monorepo and add scoped files for real areas only.
12. One-file-per-directory sprawl
   - Wrong: creating nested `AGENTS.md` files in every folder.
   - Better: scope by operational area, not by raw directory count.
13. Stale AGENTS after structural change
   - Wrong: changing package boundaries, commands, or workflows without updating the guidance.
   - Better: treat `AGENTS.md` updates as part of the same change.
14. Premature commits during investigation
   - Wrong: committing while still reproducing a bug or iterating with the user.
   - Better: commit at validated checkpoints, not at every conversational step.
15. Slogan-only engineering rules
   - Wrong: listing `SOLID`, `KISS`, `YAGNI`, or `DRY` with no actionable meaning.
   - Better: translate them into concrete agent behavior such as reuse checks, file cohesion, and scope control.
16. Code-doc drift
   - Wrong: updating workflows, behavior, or structure without updating stable docs that describe them.
   - Better: update stable docs in the same task or flag the drift explicitly.
17. Mirrored agent files
   - Wrong: maintaining both `AGENTS.md` and `CLAUDE.md` as separate copies of the same content.
   - Better: keep `AGENTS.md` canonical and symlink tool-specific filenames to it.
18. Leaking personal agent tooling
   - Wrong: listing user-installed MCPs or local-only skills in shared repository guidance.
   - Better: distinguish repo-shared, project-local discovered, and globally available tooling; ask the user when in doubt and use `if available` wording where needed.
19. Incomplete commit policy
   - Wrong: documenting only subject format and ignoring sign-off, GPG signing, or `Co-Authored-By` rules that the repo enforces.
   - Better: separate commit syntax, cadence, trailers, and signing when the repo has evidence for them.
20. Missing precedence rule
   - Wrong: creating scoped files without saying how they interact with the root file.
   - Better: state that the root is baseline and scoped files override only within their subtree.
21. Silent high-risk autonomy
   - Wrong: letting the agent continue through migrations, deploys, auth changes, or destructive actions without a stop-and-ask rule.
   - Better: include escalation triggers for high-risk or ambiguous work.
22. Change-coupling blind spot
   - Wrong: changing env vars, APIs, schemas, or generated inputs without updating the coupled files and docs they imply.
   - Better: document stable "if X changes, also update Y" rules.
23. Declaring success without verification context
   - Wrong: saying the work is done without telling the next agent what was validated, skipped, or uncertain.
   - Better: encode a concise definition of done, validation order, and failure-reporting expectation.
