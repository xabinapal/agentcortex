# Completion And Validation

Use this to encode how work is considered complete and how uncertainty should be reported.

## Definition Of Done

Work is done when:

- the requested change is implemented or the requested `AGENTS.md` update is drafted
- relevant `AGENTS.md` files and stable docs are updated or remaining drift is stated explicitly
- the most relevant validation available to the repo has been run, or the reason
  it was not run is stated clearly
- remaining risks, ambiguities, or follow-up items are called out concisely

## Validation Ladder

Prefer the fastest safe checks first:

1. syntax, type, or file-local checks
2. package-level or area-level checks
3. cross-boundary integration checks when interfaces changed
4. full-repo validation only when required or justified by the change

Do not invent commands. If the repo does not expose a check, say so.

## Failure Reporting

When something cannot be verified, report:

- what you intended to validate
- what actually ran
- what could not be verified and why
- whether user input is needed to proceed safely

## Suggested Rendering

- `Definition of Done`
- `Validation Scope`
- `Reporting Expectations`
