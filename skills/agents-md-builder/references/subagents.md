# Subagents

Use subagents explicitly when the runtime supports them and the repository is
large enough that parallel discovery will save context and protect the main thread.

Anthropic documents project subagents as Markdown files with YAML frontmatter in
`.claude/agents/`. This skill bundles ready-to-copy examples in `assets/subagents/`.

## Roles

- `purpose-layout-researcher`
  - Determine repository purpose, top-level boundaries, whether nested files are justified, and what the precedence rule should be.
- `tooling-workflow-researcher`
  - Determine runtimes, task runners, workflows, commands, validation gates, and coupled-update surfaces.
- `conventions-integrations-researcher`
  - Determine commit conventions, release tooling, agent files, MCPs, safety constraints, and escalation triggers.

## Handoff Contract

Require every subagent to return:
- Findings
- Evidence
- Uncertainties
- Recommendation
- Couplings or follow-up surfaces when relevant

The output should stay concise and evidence-first.

## Merge Rule

- Keep only findings supported by repository evidence.
- Prefer config-file evidence over filename inference.
- If subagents disagree, keep the stronger evidence and mark the weaker item as uncertain.
- Do not merge feature tours or speculative architecture explanations into the final file.
