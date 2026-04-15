# Cross-Tool Compatibility

Use `AGENTS.md` as the canonical project instruction file.

## Policy

- Do not maintain mirrored copies of the same guidance across `AGENTS.md`,
  `CLAUDE.md`, `GEMINI.md`, or other tool-specific files.
- Prefer symlinks from tool-specific filenames to `AGENTS.md`.
- Treat mirrored copies as drift-prone and avoid them by default.

## Preferred Strategy

1. Create or update `AGENTS.md`.
2. For any tool that requires a specific filename and does not read `AGENTS.md`
   directly, create a symlink pointing back to `AGENTS.md`.
3. Keep any tool-specific file as a real file only when it truly contains
   tool-specific local deltas that cannot live in `AGENTS.md`.

## Why Symlinks

- one source of truth
- no mirrored drift
- simple maintenance
- easy to audit

## Fallbacks

Avoid fallbacks unless the filesystem, platform, or hosting environment blocks symlinks.

If a fallback is unavoidable:
- prefer a minimal wrapper or import-based file over a full mirrored copy
- state explicitly that `AGENTS.md` remains canonical
- treat the fallback as an exception, not the default strategy

## Candidate Filenames

Examples of tool-specific files that may need to point to `AGENTS.md`:

- `CLAUDE.md`
- `GEMINI.md`
- other tool-required root instruction filenames

Only create links for tools the repository actually uses or intends to support.
