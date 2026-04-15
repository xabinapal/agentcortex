# Escalation Triggers

Use this to decide when the generated file should tell future agents to stop and ask.

## Ask Before Proceeding When

- The change would deploy, mutate infrastructure, or touch external stateful systems.
- The change involves ambiguous schema migrations, destructive data transforms,
  or irreversible generators.
- The change touches authentication, authorization, secrets, payments,
  permissions, or other security-sensitive boundaries.
- The change alters a public API, contract, or shared interface and downstream
  impact is unclear.
- The requested task appears to require a broad refactor or multi-area rewrite
  beyond the stated scope.
- Repository evidence conflicts on a high-risk behavior such as deploy flow,
  migration workflow, commit policy, or tool authority.
- The repo exposes project-local or globally available agent tooling and it is
  unclear whether shared guidance should enforce it.

## Default Rule

- Do not ask about low-risk details that can be resolved from repository evidence.
- Do ask when the uncertainty changes safety, scope, external side effects, or
  the shape of the repository contract.

## Suggested Rendering

- `Escalation Triggers`
- Ask before deploys, migrations, destructive operations, dependency installs,
  or changes to auth, security, or public contracts when policy is unclear.
