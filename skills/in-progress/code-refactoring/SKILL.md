---
name: code-refactoring
description: Refactor a declared repository scope so implementation conforms to approved docs/wiki knowledge, docs/design decisions, and docs/code standards while preserving frozen capabilities. Use this command for incremental frontend, backend, database, test, module-boundary, design-system, validation, error-handling, or architecture refactoring and conformance verification.
argument-hint: "[scope-id] [optional focus]"
arguments:
  - scope
disable-model-invocation: true
---

# Code Refactoring

Requested scope: `$scope`
Full invocation arguments: `$ARGUMENTS`

Refactor the selected implementation incrementally. Preserve declared behaviour and contracts, apply approved design and standards, and route unresolved meaning or design questions back to the owning hardening stage.

## Load before acting

1. Read `${CLAUDE_SKILL_DIR}/references/shared-protocol.md`.
2. Read `${CLAUDE_SKILL_DIR}/references/refactoring-method.md`.
3. Resolve the effective scope from `$scope` or the hardening manifest.
4. Read all repository and scope files required by the shared protocol.
5. Read every approved wiki, design, code-standard, handoff, baseline, finding, and exception relevant to the paths being changed.

## Entry checks

Normally require wiki, design, and code-docs tracks to be `passed`. Proceed earlier only when `scope.yaml` explicitly permits limited refactoring and tests protect the change.

Before editing, confirm:

- included, excluded, and shared-code paths;
- baseline commit or current behavioural baseline;
- preserved capabilities and known defects;
- approved frontend/backend/UXUI design;
- applicable code standards and exceptions;
- required verification commands.

## Workflow

1. Mark the refactoring track `in-progress`.
2. Add or strengthen characterisation tests where behaviour is not adequately protected.
3. Write a small ordered plan. For each step state purpose, affected files, invariants, decisions/standards applied, checks, risks, and rollback boundary.
4. Refactor in slices: introduce a seam or target interface, adapt current code, migrate one caller or vertical slice, verify, then continue.
5. Apply approved Claude Design/UXUI output through the permanent design documents and implementation map—not from screenshots alone.
6. Apply backend, data, integration, security, error, logging, and other approved design decisions only where scoped.
7. Add approved automated enforcement.
8. Run targeted checks after meaningful slices and broader checks before completion.
9. Review the diff for accidental capability, contract, persistence, dependency, or scope changes.
10. Record findings for unclear business meaning, design conflict, standard ambiguity, guide impact, shared-code impact, new features, and accepted deviations.
11. Reopen earlier tracks when implementation evidence invalidates their assumptions.
12. Update verification and cycle state honestly; never mark a check passed when it was not run.

## Stop and route back when

- a behaviour change is required but not approved;
- an approved design is contradictory or infeasible;
- a code standard is ambiguous;
- business meaning is unclear;
- shared-code impact materially widens the scope;
- a UX/UI proposal conflicts with accessibility, contracts, or frontend engineering architecture.

## Do not

- perform a broad rewrite when incremental migration is possible;
- add deferred functionality;
- change business rules to simplify code;
- silently rewrite design or standards to match existing code;
- treat visual similarity as complete frontend conformance.

## Completion

Report implementation areas changed, preserved capabilities, decisions and standards applied, tests/checks and results, deviations, findings, guide impact, remaining risk, and whether the scope is `ready-to-close`, requires `another-cycle`, is `blocked`, or has `failed` verification.
