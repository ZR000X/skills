---
name: code-docs-hardening
description: Harden implementation standards under docs/code for one declared hardening scope. Use this command to translate approved frontend, backend, database, UX/UI, testing, naming, error, logging, accessibility, and tooling design into objective coding rules, examples, exceptions, and enforcement mechanisms before refactoring.
argument-hint: "[scope-id]"
arguments:
  - scope
disable-model-invocation: true
---

# Code Docs Hardening

Requested scope: `$scope`

Define repeatable implementation rules that express approved design without turning local accidents or generic advice into repository-wide policy.

## Load before acting

1. Read `${CLAUDE_SKILL_DIR}/references/shared-protocol.md`.
2. Read `${CLAUDE_SKILL_DIR}/references/code-standards-method.md`.
3. Resolve the effective scope from `$scope` or the hardening manifest.
4. Read the repository and scope files required by the shared protocol.
5. Follow `docs/code/README.md` and relevant frontend, backend, database, testing, and tooling constitutions.

## Owned changes

Edit only:

- `docs/code/**`
- the selected scope records
- small non-consequential cross-links or typo corrections

Do not refactor production code or revise approved design decisions.

## Workflow

1. Mark the code-docs track `in-progress`.
2. Confirm required wiki and design tracks have passed or that limited parallel work is explicitly authorised.
3. Trace every proposed standard to an approved design decision, repeated repository need, or concrete maintenance/conformance risk.
4. Inventory current practice and distinguish deliberate patterns from legacy, duplication, and one-off choices.
5. Select the narrowest appropriate applicability: repository, frontend, backend, database, tooling, module, or scope-local.
6. Write standards that state:
   - the rule;
   - where it applies;
   - rationale and related design;
   - compliant examples;
   - prohibited examples;
   - enforcement;
   - exceptions.
7. Keep frontend and backend standards separate when their concerns differ.
8. Prefer types, APIs, tests, architecture checks, lint, CI, generators, and templates over prose-only enforcement.
9. Record existing violations as `code-nonconformance` findings for code refactoring.
10. Validate links, examples, internal consistency, and feasibility.
11. Mark the track `passed` only when refactoring can determine conformance without inventing rules.

## Standard threshold

Do not create a repository-wide standard unless the rule recurs, consistency is worth constraining future code, approved design supports it, compliance is objective, and enforcement or review is sustainable.

## Completion

Report standards added or changed, applicability, design traceability, enforcement, violations, exceptions, checks run, and the next command—normally `/code-refactoring <scope-id>`.
