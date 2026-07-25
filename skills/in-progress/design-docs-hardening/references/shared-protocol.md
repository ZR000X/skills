# Shared Hardening Protocol

Use this protocol for every hardening skill. Repository instructions override defaults in this file.

## Required repository reads

Before changing anything, read in this order when present:

1. Root `CLAUDE.md` and any nested `CLAUDE.md` that governs the scoped paths.
2. `docs/README.md`.
3. `docs/hardening/README.md`.
4. `docs/hardening/manifest.yaml`.
5. The selected scope's `scope.yaml` and `cycle.yaml`.
6. The selected scope's `baseline.md`, `findings.md`, `open-questions.md`, and `deferred.md`.
7. The README for the owned documentation area.
8. Relevant wiki, design, code, guide, source, and test files.

If the framework files are absent, stop destructive work and recommend running `docs-framework-setup` first. Do not invent an implicit scope.

## Scope selection

- Use the scope named by the user.
- If no scope is named and exactly one active scope exists, use it.
- If several active scopes exist, identify the intended scope before editing. When interaction is not possible, perform a read-only assessment and state the ambiguity.
- Respect `include`, `exclude`, `shared_code`, module, frontend, backend, and capability-freeze declarations.
- Treat changes to undeclared shared code as `shared-code-impact`, not as permission to widen the scope.

Supported scope levels are `patch`, `component`, `module`, `cross-cutting`, and `system`.

## Capability freeze

During hardening, preserve declared user capabilities, business behaviour, public contracts, persisted meaning, and integration behaviour. Do not implement deferred features.

A behaviour may change only when it is explicitly classified as:

- a confirmed defect to fix in this scope;
- an approved design migration with accepted compatibility impact; or
- an explicitly approved scope change.

## Ownership boundaries

Each skill edits only its owned area plus the active scope records. Record findings for other areas rather than silently changing them.

Small factual cross-links or typo fixes are acceptable when they cannot alter policy or design meaning. Anything consequential must be routed to the owning skill.

## Finding format

Record findings in `findings.md` with:

```markdown
## [Scope prefix]-NNN

**Type:** wiki-gap | wiki-conflict | design-needed | design-conflict | code-standard-needed | code-nonconformance | behaviour-regression | known-defect | guide-impact | scope-expansion | shared-code-impact | new-feature | open-question
**Severity:** critical | high | medium | low
**Owner:** skill-name
**Status:** open | resolved | accepted | deferred

[Description]

**Evidence**
- `path:line` or command/test output

**Recommended action**
[Action]
```

Never fabricate line references. Use exact paths and evidence available in the repository.

## Cycle updates

Update `cycle.yaml` conservatively:

- Mark the owned track `in-progress` when work starts.
- Mark it `awaiting-input`, `awaiting-handoff`, `review-required`, `blocked`, `passed`, `failed`, or `drifted` based on evidence.
- Do not mark another skill's track passed.
- Set `next_recommended_skill` to the most logical next action.
- Increment the iteration only when beginning a genuinely new pass through the cycle, not for every edit.

If repository YAML conventions differ, follow the repository's existing format.

## Proportionality

- Do not document every function or file.
- Create wiki pages for durable knowledge.
- Create design records for consequential choices.
- Create code standards for repeatable implementation rules.
- Prefer local/module documentation over repository-wide policy when evidence is narrow.
- Prefer a follow-up scope over silent expansion.
- Avoid speculative abstractions and generic best-practice dumps.

## Conflict handling

When code and documentation disagree, classify the discrepancy. Do not automatically assume either is correct.

Use this precedence for decisions:

1. Explicit human-approved scope and capability constraints.
2. Confirmed business facts and product behaviour.
3. Approved design decisions.
4. Approved code standards.
5. Current implementation.
6. Generic best practices.

## Completion response

Report:

1. Effective scope.
2. Files changed.
3. Material decisions or knowledge added.
4. Findings opened, resolved, or deferred.
5. Verification performed.
6. Remaining blockers.
7. Next recommended skill or checkpoint.
