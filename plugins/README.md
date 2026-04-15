# Plugins

`plugins/` is reserved for distributable artifacts that need native packaging
per platform rather than repo-local discovery.

The repository root itself is already a Claude Code plugin package via
`.claude-plugin/plugin.json`.

Each plugin package can define its own internal layout depending on the target
runtime.

This repository currently keeps `plugins/` empty on purpose.
