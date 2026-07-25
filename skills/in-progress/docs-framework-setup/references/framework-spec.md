# Documentation Framework Specification

## Top-level taxonomy

```text
docs/
├── README.md
├── wiki/
├── design/
├── code/
├── guide/
└── hardening/
```

### `docs/wiki`

Store durable system and domain knowledge: terminology, concepts, capabilities, workflows, business rules, integrations, and reference knowledge. Describe meaning rather than implementation policy.

### `docs/design`

Store deliberate decisions that constrain implementation: architecture, boundaries, UX/UI direction, frontend and backend design, data and integration choices, security, and ADRs. Explain context, decision, alternatives, consequences, scope, enforcement, and exceptions.

### `docs/code`

Store coding and implementation standards: naming, patterns, prohibited practices, frontend and backend conventions, testing, database practices, tooling, examples, and enforcement mechanisms.

### `docs/guide`

Store user-facing, administrator, operations, troubleshooting, and release guidance. Describe supported use rather than internal structure.

### `docs/hardening`

Store process state: scopes, baselines, inventories, findings, open questions, deferred work, handoffs, verification, cycle status, and archive records.

## Authority model

- Wiki is authoritative for confirmed terminology and domain knowledge.
- Design is authoritative for approved structural and UX/UI direction.
- Code docs are authoritative for implementation standards.
- Code is executable evidence, but not automatically the intended design.
- Guide is authoritative for supported user-facing procedures.

## Dependency direction

```text
Confirmed product behaviour and facts
  -> wiki
  -> design
  -> code standards
  -> implementation
  -> guide
```

This is a reasoning direction, not a requirement that every fact create every downstream document.

## Required constitutions

Each root requires a `README.md` defining purpose, inclusion and exclusion criteria, organisation, naming, document status, review expectations, ownership, update rules, and relationships to the other roots.

## Hardening state

`docs/hardening/manifest.yaml` indexes active and historical scopes. Each scope folder contains at least:

```text
scope.yaml
cycle.yaml
baseline.md
inventory.md
findings.md
open-questions.md
deferred.md
verification.md
handoffs/
```

## Migration principle

Never bulk-move an existing docs folder based only on filenames. Inventory first, classify by content and authority, identify duplicates and conflicts, propose a mapping, then move in reviewable groups while preserving Git history where practical.
