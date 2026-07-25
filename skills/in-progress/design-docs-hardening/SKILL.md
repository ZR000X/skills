---
name: design-docs-hardening
description: Harden scoped design documentation under docs/design. Use this command to analyse a working frontend, backend, or full-stack module; make architecture, boundary, data, integration, security, UX/UI, accessibility, and design-system decisions explicit; prepare or ingest a Claude Design handoff; record ADRs; and produce an approved design target before coding standards or refactoring.
argument-hint: "[scope-id] [analyze|prepare-handoff|ingest-handoff|finalize]"
arguments:
  - scope
  - phase
disable-model-invocation: true
---

# Design Docs Hardening

Requested scope: `$scope`
Requested phase: `$phase`

Convert accidental working structure into explicit, consequential, scoped design direction. Keep the as-is model separate from the approved to-be design.

## Load before acting

1. Read `${CLAUDE_SKILL_DIR}/references/shared-protocol.md`.
2. Read `${CLAUDE_SKILL_DIR}/references/design-method.md`.
3. Read `${CLAUDE_SKILL_DIR}/references/claude-design-handoff.md` when frontend UX/UI is included.
4. Resolve the effective scope and phase.
5. Read all repository and scope files required by the shared protocol.
6. Follow `docs/design/README.md` and relevant frontend/backend constitutions.

## Phases

### `analyze`

1. Mark the design track `in-progress`.
2. Confirm the capability freeze, behavioural baseline, wiki status, frontend/backend inclusion, and unresolved questions.
3. Model the as-is frontend, backend, data, integration, and cross-cutting structure without endorsing it.
4. Identify design pressures using concrete repository evidence.
5. Decide only what is consequential for the current scope.
6. Record context, decision, alternatives, consequences, scope, enforcement direction, exceptions, and migration implications.
7. Open `code-standard-needed` and implementation findings instead of writing detailed code rules or refactoring code.

### `prepare-handoff`

Use when substantial frontend UX/UI work should be explored in Claude Design.

1. Create the outbound bundle under `docs/hardening/scopes/<scope-id>/handoffs/claude-design/outbound/`.
2. Include product context, capability matrix, journeys, screen inventory, interaction states, technical context, existing components, constraints, screenshots/assets inventory, and a ready-to-paste initial prompt.
3. Make preserved capabilities and prohibited new functionality explicit.
4. Set the design track and Claude Design state to `awaiting-handoff`.
5. Stop before implementing or treating the first generated design as approved.

### `ingest-handoff`

1. Read the returned material under `handoffs/claude-design/inbound/`.
2. Compare it with capability, accessibility, existing shell, backend contracts, frontend engineering constraints, and approved design.
3. Classify proposals as `adopt`, `adapt`, `existing`, `promote-to-design-system`, `module-specific`, `defer-as-feature`, `reject`, or `clarify`.
4. Write an intake report and implementation map.
5. Keep raw exports in the scope handoff folder; do not make them the sole permanent source of truth.

### `finalize`

1. Normalise approved decisions into `docs/design/**`.
2. Separate reusable design-system rules from module-specific design.
3. Verify frontend engineering, backend architecture, and UX/UI decisions are mutually compatible.
4. Mark the track `review-required` or `passed` based on unresolved consequential decisions.

If `$phase` is empty, inspect state and perform the next valid design phase without skipping a human Claude Design checkpoint.

## Owned changes

Edit `docs/design/**` and selected scope records/handoffs. Do not refactor production code or define detailed coding standards that belong in `docs/code`.

## Decision quality

Reject architecture theatre. A decision must be evidenced, scoped, coherent, compatible with frozen capabilities, and specific enough to constrain implementation.

## Completion

Report design documents and ADRs changed, decisions made, handoff status, findings routed to code docs or refactoring, unresolved decisions, and the next command—normally `/code-docs-hardening <scope-id>` after design approval.
