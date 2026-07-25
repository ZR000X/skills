# Wiki Hardening Method

## Knowledge categories

Use repository-specific organisation, but classify content conceptually as:

- glossary and terminology;
- concepts and relationships;
- actors and responsibilities;
- capabilities and supported behaviour;
- workflows and lifecycle states;
- business rules and invariants;
- integrations and external concepts;
- reference facts.

## Concept document quality

A useful concept page answers:

- What is it?
- Why does it exist?
- What is it not?
- Which rules or invariants apply?
- What are its important states or relationships?
- Which terms are synonyms, narrower, broader, or commonly confused?
- Which evidence supports the definition?
- Which questions remain unresolved?

Avoid framework, database, and UI details unless they are necessary context and clearly labelled as current implementation.

## Reconciliation table

Before changing a conflicted concept, use a compact table:

| Claim | Evidence | Authority | Classification | Action |
|---|---|---|---|---|
| ... | ... | ... | confirmed / implementation-only / uncertain / defect | keep / revise / question |

## Module proportionality

For a module scope, prefer:

- one module overview;
- a small number of reusable concept pages;
- one or more workflows when state or sequencing matters;
- glossary updates for shared terms;
- links to existing shared knowledge rather than duplication.

## Handoff to design

Design hardening is ready when it can identify:

- stable names and meanings;
- module capabilities and non-capabilities;
- business rules and invariants;
- actors and workflows;
- unresolved questions that materially constrain design.
