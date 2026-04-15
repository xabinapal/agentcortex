# Precedence

Use this whenever root and scoped `AGENTS.md` files may coexist.

## Default Rule

- The root `AGENTS.md` is the baseline contract for the whole repository.
- A scoped `AGENTS.md` applies only within its subtree.
- A scoped file should add local deltas or explicit overrides, not restate the root.
- Tool-specific filenames such as `CLAUDE.md` should be symlinks to `AGENTS.md`
  and must not introduce extra semantics.

## Conflict Rule

- If both root and scoped files apply, the scoped file wins only for its subtree
  and only on the rules it explicitly changes.
- Outside that subtree, the root file remains authoritative.
- If a scoped file would need to repeat most of the root file, the split is wrong.

## Writing Rule

- Keep shared repo-wide policy in the root file.
- Put area-local commands, boundaries, generators, safety rules, or validation
  details in the scoped file.
- When a local rule changes the whole-repo picture, update both root and scoped files.

## Suggested Rendering

When a repository has nested files, render a short section such as:

- `Instruction Precedence`
- Root `AGENTS.md` applies repo-wide.
- Nested `AGENTS.md` files add or override rules only for their subtree.
- Tool-specific filenames are symlinks to `AGENTS.md` and do not change behavior.
