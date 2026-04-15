# Maintenance

## When To Update AGENTS.md

Update the relevant root or scoped `AGENTS.md` when work changes the repository's
shared contract, including:

- major top-level areas or subsystem boundaries
- canonical commands, task runners, or workflow entrypoints
- test, lint, format, or CI expectations
- deployment, release, or review flow
- commit conventions or commit cadence guidance
- agent tooling, MCP integration points, or tool-specific instruction files

Do not wait for the user to ask for this explicitly when the change is material.

## When To Update Other Stable Docs

Update stable project docs in the same task when the work changes behavior they
describe, especially:

- `README.md`
- `CONTRIBUTING.md`
- `DESIGN.md`
- architecture docs
- setup or onboarding docs
- deployment or release docs

Use the same standard as for `AGENTS.md`: if the change would make the doc
inaccurate in a way that affects future contributors or agents, update it or
flag the drift explicitly.

## Root Vs Scoped Updates

- Update the root file when the change affects the whole repo or the repo map.
- Update a scoped file when the change is local to one area.
- Update both when a local area changes in a way that also changes the whole-repo picture.
- Apply the same reasoning to stable docs: update the broad doc for broad changes
  and the local doc for local changes.

## Commit Cadence Guidance

Document both format and rhythm, and add trailer or signing policy when the repo cares.

Format:
- state the verified convention, such as Conventional Commits

Rhythm:
- do not commit during initial exploration, reproduction, or interactive debugging
- do not commit on every conversational turn
- commit once a checkpoint is coherent and validated to the repo's standard
- prefer a small number of meaningful commits over one giant commit or many tiny noise commits

Trailers and signing:
- state whether `Signed-off-by` / `git commit -s` is required, optional, or not used
- state whether GPG or signed commits / `git commit -S` are required, optional, or not used
- state whether `Co-Authored-By` trailers are allowed, required, or forbidden

## Why This Belongs In AGENTS.md

Agents need guidance not just on how a commit should look, but also on when a
commit should happen. Without that, they tend to either commit too early during
investigation or wait too long and bundle unrelated work together.

Agents also need explicit expectations about doc maintenance. Without that, they
will often update code and leave stable docs drifting behind.
