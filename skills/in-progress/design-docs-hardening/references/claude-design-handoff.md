# Claude Design Handoff

Use this only when the active frontend scope declares Claude Design required or substantial UX/UI redesign clearly warrants it.

## Outbound package

Create under `docs/hardening/scopes/<scope-id>/handoffs/claude-design/outbound/`:

- `README.md`
- `initial-prompt.md`
- `product-context.md`
- `capability-matrix.md`
- `user-journeys.md`
- `screen-inventory.md`
- `interaction-states.md`
- `technical-context.md`
- `existing-components.md`
- `constraints.md`
- `screenshots/` and `assets/` when available

Cover happy, empty, loading, error, permission, destructive, success, large-data, narrow-viewport, keyboard, and accessibility states where relevant. State that new functionality is deferred.

## Human checkpoint

Set the track to `awaiting-handoff`. Do not approve the first generated design automatically. The human iterates in Claude Design and returns an approved or candidate handoff.

## Inbound intake

Store raw output under `.../claude-design/inbound/`. Classify each proposal:

- adopt;
- adapt;
- existing;
- promote-to-design-system;
- module-specific;
- defer-as-feature;
- reject;
- clarify.

Compare against capability freeze, existing shell and components, technical constraints, accessibility, backend contracts, and current approved design.

Normalise approved reusable decisions into `docs/design/frontend/uxui/`; keep module-specific designs in the repository's chosen module structure. Preserve the raw handoff only for traceability.

## Two representations

Maintain agreement between:

- the design representation humans and Claude Design consume; and
- the engineering representation: tokens, component APIs, composition rules, accessibility contracts, linting, examples, and visual tests.
