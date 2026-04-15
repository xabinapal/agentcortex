# Repository Archetypes

Choose an archetype before drafting. It keeps the output proportional.

## 1. Single Application

Use for one web app, mobile app, desktop app, or service in one runtime.

Include:
- Purpose
- Primary stack
- Main commands
- Layout
- Testing or quality gates

Usually avoid:
- Nested `AGENTS.md` files unless the repo contains a truly separate subsystem

## 2. Monorepo

Use for repos with multiple apps, packages, services, or workspaces.

Include:
- Purpose of the repo as a whole
- Workspace toolchain and workflow authority chain
- Cross-repo commands
- Major top-level packages
- Rule for when subtree files exist

Often add:
- Scoped `AGENTS.md` files for packages with distinct runtimes or workflows

## 3. Library / SDK

Use for publishable packages, SDKs, or frameworks.

Include:
- Supported language/runtime
- Build, test, lint, publish or release flow
- API stability or compatibility expectations
- Example directories or canonical package locations

Usually avoid:
- Product feature summaries

## 4. Infrastructure / Operations Repo

Use for Terraform, Pulumi, Helm, Kubernetes, CI/CD, or deployment automation.

Include:
- Environments and boundaries
- Safe command usage
- Validation and plan/apply workflow
- Secrets and state handling rules

Often add:
- Scoped files for each environment or platform if they differ materially

## 5. Tooling / Templates / Internal Automation

Use for skill repos, starter kits, generators, or build-tool collections.

Include:
- What the repo generates or enables
- Where reusable templates, scripts, and workflow sources of truth live
- How contributors validate changes
- How to avoid hard-coding one environment's assumptions

Usually avoid:
- Pretending the tool can infer everything automatically
