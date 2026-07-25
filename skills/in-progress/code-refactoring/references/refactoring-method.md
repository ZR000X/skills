# Refactoring Method

## Plan unit

Each step should state:

- purpose;
- affected files or modules;
- behaviour and contracts to preserve;
- approved design and standards being applied;
- checks to run;
- risk and rollback boundary.

## Preferred sequence

```text
Capture behaviour
  -> introduce a seam or target interface
  -> adapt current implementation behind it
  -> migrate one caller or vertical slice
  -> verify
  -> migrate remaining callers
  -> remove obsolete paths
  -> verify broadly
```

## Verification layers

### Behaviour

User journeys, business rules, outputs, errors, permissions, and declared known defects.

### Contracts

Public APIs, events, schemas, persisted meaning, integrations, and backwards compatibility.

### Design

Boundaries, dependency direction, ownership, UX/UI states, design tokens, accessibility, responsive behaviour, security, and operational constraints.

### Code standards

Required patterns, prohibited patterns, tests, naming, lint, types, and recorded exceptions.

### Technical

Targeted tests, full relevant suites, build, type check, lint, architecture checks, migration checks, visual regression, and smoke tests as available.

## Frontend conformance

Verify more than appearance:

- all preserved capabilities and interaction states;
- keyboard and focus behaviour;
- semantic structure and accessibility;
- responsive behaviour;
- design-token and component reuse;
- loading, empty, error, permission, destructive, and success states;
- state and data ownership consistent with frontend engineering design.

## Backend conformance

Verify:

- domain and application boundaries;
- contracts and validation;
- transaction and persistence behaviour;
- errors, logs, security, and observability;
- concurrency and idempotency where applicable;
- integration failure behaviour.

## Completion classifications

- **ready-to-close:** all required tracks and verification pass;
- **another-cycle:** noncritical drift requires a targeted earlier track;
- **blocked:** human decision or external dependency required;
- **failed:** regression or conformance failure remains unresolved.
