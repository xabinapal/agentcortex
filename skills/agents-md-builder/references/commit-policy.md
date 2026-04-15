# Commit Policy

Use this reference when writing the `Commit / PR Conventions` section.

## What To Look For

Inspect:

- commitlint or release config
- `CONTRIBUTING.md`, `README.md`, `SECURITY.md`, or governance docs
- commit templates such as `.gitmessage*`
- recent commit history, including trailers and signature status
- committed hooks or workflow checks if they enforce DCO or signed commits

## Render These Separately When Evidence Exists

- commit format
- commit cadence
- sign-off policy
- GPG or signed-commit policy
- `Co-Authored-By` policy

Do not collapse these into a single vague sentence when the repo clearly cares.

## Recommended Wording

- `Commit format: Conventional Commits.`
- `Sign-off: required via \`git commit -s\`.`
- `GPG signing: required via \`git commit -S\`.`
- `Co-Authored-By: forbidden for AI assistance.`
- `Co-Authored-By: allowed when there is a real human co-author.`

## Ambiguity Rule

If evidence is weak:

- do not invent a policy
- say it is unclear in your working notes
- ask the user whether sign-off, GPG signing, or `Co-Authored-By` trailers are required, optional, or forbidden

## History Rule

Recent history can show what is common, but docs and committed config outrank history.

- history can suggest that a trailer is common or allowed
- history alone should rarely be used to claim a trailer is required
- a documented DCO or signed-commit rule is stronger than commit history
