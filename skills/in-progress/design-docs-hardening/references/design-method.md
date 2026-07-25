# Design Hardening Method

## Analyse separately

### Shared/product design

Capabilities, actors, workflows, module responsibility, contracts, and cross-cutting constraints.

### Frontend UX/UI

Information architecture, interaction flows, states, visual hierarchy, design tokens, reusable components, patterns, accessibility, responsive behaviour, and content design.

### Frontend engineering

Component boundaries, state ownership, server/client state, routing, forms, data fetching, error boundaries, rendering, performance, and test seams.

### Backend

Domain and application boundaries, service responsibilities, APIs, data ownership, persistence, validation, error semantics, security, observability, integrations, concurrency, and idempotency.

## As-is and to-be

Keep them distinct:

- **As-is:** what the current system does and how it is structured.
- **To-be:** the approved direction and constraints.
- **Migration:** behaviour-preserving steps from as-is to to-be.

## Decision record

Use this default structure, adapting to repository conventions:

```markdown
# [Decision]

**Status:** proposed | approved | superseded | rejected
**Scope:** [scope ID and affected areas]

## Context
## Decision
## Alternatives considered
## Consequences
## Enforcement direction
## Exceptions
## Migration implications
## Related knowledge and decisions
```

## Pressure-to-decision traceability

Every major decision should cite the pressure it addresses. Examples:

- duplicated validation -> define ownership and reuse boundary;
- raw UI values -> adopt semantic design tokens;
- cyclic modules -> define dependency direction;
- inconsistent errors -> define error taxonomy and propagation boundary.

## Handoff to code docs

Code-docs hardening is ready when it can derive concrete implementation rules, examples, and enforcement from approved design without guessing architecture.
