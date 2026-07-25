# Repository Hardening Skills and Documentation Architecture

**Status:** Proposed
**Version:** 0.1
**Purpose:** Define the documentation architecture, repository-hardening workflow, scope-management model, and responsibilities of the skills used to convert vibe-coded software into intentionally designed and maintainable software.

---

# 1. Overview

The development lifecycle consists of two broad stages:

## Stage 1: Functional Vibe Coding

The objective of Stage 1 is to make the software work.

The developer:

1. Defines a desired capability.
2. Breaks it into implementable pieces.
3. Uses an AI coding agent to plan and build.
4. Tests the result.
5. Records issues and missing behaviour.
6. Repeats until the software reaches a functional checkpoint.

Stage 1 prioritises:

- Functional progress
- Rapid iteration
- Exploration
- User feedback
- Discovering the real requirements
- Reaching a usable implementation

The resulting software may work correctly while still lacking:

- Explicit concepts
- Coherent architecture
- Consistent coding standards
- Reliable documentation
- Reusable design decisions
- Clear module boundaries
- Enforced development constraints

## Stage 2: Repository Hardening

The objective of Stage 2 is to make the working software intentional, understandable, maintainable, and constrained by explicit documentation.

Stage 2 does not primarily add functionality. It:

- Extracts and clarifies knowledge
- Makes design decisions explicit
- Defines implementation standards
- Refactors the code to conform
- Preserves existing capabilities
- Creates constraints for future development
- Reduces repeated AI reasoning and token usage

The hardening cycle is:

```text
Scope
  ↓
Wiki documentation hardening
  ↓
Design documentation hardening
  ↓
Code documentation hardening
  ↓
Code refactoring
  ↓
Verification
  ↓
Repeat where necessary
```

This is a cycle rather than a strictly one-way pipeline. Findings discovered during refactoring may require a design decision to be reconsidered. A design exercise may reveal unclear concepts that must return to wiki hardening.

---

# 2. Documentation Architecture

The repository uses the following top-level documentation structure:

```text
docs/
├── README.md
├── wiki/
├── design/
├── code/
├── guide/
└── hardening/
```

Each folder has a distinct purpose.

## 2.1 `docs/wiki`

The wiki contains knowledge about the system and its problem domain.

It answers questions such as:

- What is this?
- What does this term mean?
- How does this concept relate to another concept?
- What business rule exists?
- What external system are we integrating with?
- What background knowledge is necessary to understand the software?

The wiki is primarily descriptive rather than prescriptive.

Typical contents include:

```text
docs/wiki/
├── README.md
├── glossary/
├── concepts/
├── domains/
├── capabilities/
├── workflows/
├── integrations/
└── reference/
```

Examples:

- What an Import Job represents
- The difference between a validation error and a warning
- The lifecycle of an order
- Terminology used by an external API
- Business rules governing approval
- The relationship between a product, offering, and specification

Wiki documents should generally remain useful even if the implementation technology changes.

The wiki must not become:

- A copy of the source code
- A coding standards manual
- A collection of architectural decisions
- A user manual
- A dumping ground for unclassified notes

---

## 2.2 `docs/design`

The design folder contains deliberate decisions that constrain the implementation.

It answers questions such as:

- How should the system be structured?
- Which direction should dependencies flow?
- Where should responsibilities reside?
- Which UX/UI system must the frontend follow?
- Which architectural patterns have been selected?
- What alternatives were rejected?
- What constraints must future implementations respect?

The design folder is prescriptive.

A suggested structure is:

```text
docs/design/
├── README.md
├── shared/
├── frontend/
│   ├── architecture/
│   ├── uxui/
│   │   ├── foundations/
│   │   ├── tokens/
│   │   ├── components/
│   │   ├── patterns/
│   │   ├── accessibility/
│   │   ├── responsive/
│   │   └── modules/
│   └── decisions/
├── backend/
│   ├── architecture/
│   ├── domain/
│   ├── data/
│   ├── integrations/
│   ├── security/
│   └── decisions/
└── decisions/
```

Repository-wide decisions belong in shared or general decision documents.

Module-specific applications of those decisions may be stored beneath frontend or backend module folders.

Examples:

- Use feature-oriented frontend modules
- Use semantic design tokens rather than raw colour values
- Keep business validation outside React components
- Use a service boundary between the application and persistence layers
- Represent errors using a defined error hierarchy
- Use asynchronous job processing for long-running imports

Design documentation should explain:

1. The context
2. The selected direction
3. Alternatives considered
4. Consequences
5. Scope
6. Enforcement
7. Known exceptions

Design documentation must not merely describe what the current code happens to do.

---

## 2.3 `docs/code`

The code folder contains standards for implementing the approved design.

It answers questions such as:

- How must code be written?
- Which patterns are permitted?
- Which patterns are prohibited?
- How should a component, service, test, or migration be structured?
- What naming and folder conventions apply?
- How are design decisions expressed in code?
- How is compliance verified?

The code folder is prescriptive and implementation-oriented.

A suggested structure is:

```text
docs/code/
├── README.md
├── shared/
│   ├── naming.md
│   ├── errors.md
│   ├── logging.md
│   ├── configuration.md
│   └── documentation.md
├── frontend/
│   ├── components.md
│   ├── state.md
│   ├── forms.md
│   ├── data-fetching.md
│   ├── styling.md
│   ├── accessibility.md
│   └── testing.md
├── backend/
│   ├── modules.md
│   ├── services.md
│   ├── validation.md
│   ├── persistence.md
│   ├── APIs.md
│   ├── errors.md
│   └── testing.md
├── database/
├── tooling/
└── examples/
```

Examples:

- React components must not perform direct database or persistence operations
- Business validation must be implemented through a defined validation interface
- Raw colours must not appear outside the design-token package
- Public service methods must return a defined result type
- Unit tests must follow a specific naming convention
- Database migrations must be reversible where technically possible

Code documentation should contain concrete examples where they improve clarity.

A code standard should ideally be enforceable through one or more of:

- Types
- Tests
- Linters
- Architecture tests
- CI checks
- Generators
- Templates
- Code review
- Claude instructions

The code folder should not contain generic programming advice unless the repository has deliberately adopted it as a standard.

---

## 2.4 `docs/guide`

The guide contains user-facing instructions.

It answers questions such as:

- How do I use this feature?
- How do I complete this workflow?
- What should I do when an error occurs?
- How does an administrator configure the application?
- What does a user see or experience?

A suggested structure is:

```text
docs/guide/
├── README.md
├── user/
├── administrator/
├── operations/
├── troubleshooting/
└── release-notes/
```

The guide describes the supported product, not the internal implementation.

Guide hardening is not included in the initial four-skill model. However, every hardening scope must assess whether its changes affect user-facing documentation.

A future `guide-docs-hardening` skill may be introduced when the guide becomes substantial enough to justify a dedicated workflow.

---

## 2.5 `docs/hardening`

The hardening folder controls the hardening process.

It contains:

- Active scopes
- Functional baselines
- Cycle status
- Findings
- Cross-skill handoffs
- Verification results
- Deferred work
- Historical hardening records

It is not part of the product knowledge hierarchy. It is the process and coordination layer.

A suggested structure is:

```text
docs/hardening/
├── README.md
├── manifest.yaml
├── scopes/
│   ├── HD-2026-001-import-module/
│   │   ├── scope.yaml
│   │   ├── baseline.md
│   │   ├── inventory.md
│   │   ├── findings.md
│   │   ├── open-questions.md
│   │   ├── deferred.md
│   │   ├── cycle.yaml
│   │   ├── verification.md
│   │   └── handoffs/
│   └── HD-2026-002-error-handling/
└── archive/
```

---

# 3. Documentation Authority

The documentation categories have different forms of authority.

## Wiki authority

The wiki is authoritative for:

- Terminology
- Confirmed business concepts
- Domain knowledge
- Business rules
- External-system knowledge
- Capability descriptions

It explains what the system means.

## Design authority

Design documentation is authoritative for:

- Architecture
- Boundaries
- Responsibility allocation
- UX/UI direction
- Technical decisions
- Structural constraints

It explains how the system is intended to be designed.

## Code-documentation authority

Code documentation is authoritative for:

- Implementation conventions
- Coding patterns
- Testing standards
- Naming standards
- Code-level constraints

It explains how the design must be implemented consistently.

## Codebase authority

The codebase is the executable implementation.

It provides evidence about current behaviour, but existing code is not automatically the correct design.

An existing implementation may be:

- Correct and intentional
- Functionally correct but poorly structured
- Inconsistent with current standards
- Legacy code
- Accidental behaviour
- A known defect

## Guide authority

The guide is authoritative for supported user-facing procedures.

It must remain aligned with the implemented and verified product.

---

# 4. Dependency Direction

The primary dependency direction is:

```text
Confirmed product behaviour and business facts
                    ↓
                  Wiki
                    ↓
                 Design
                    ↓
             Code standards
                    ↓
               Implementation
                    ↓
                  Guide
```

This does not mean every wiki page must produce a design document or every design decision must produce a coding standard.

Documentation should be created only where it provides durable value.

Examples:

- A business term may need only a wiki entry.
- A one-off implementation detail may need no repository-wide code standard.
- A major dependency rule should have both a design decision and a coding standard.
- A new user workflow may require updates to the wiki, design, code, implementation, and guide.

---

# 5. Proportional Hardening

Every hardening cycle must operate within a declared scope.

The skills must not attempt to exhaustively harden the entire repository unless the scope explicitly requires it.

## 5.1 Scope levels

A scope should use one of the following levels:

### Patch

A narrow problem involving a small number of files.

Examples:

- Standardise error handling in one service
- Replace raw colours in one component
- Clarify one domain concept

### Component

A cohesive UI component, backend service, or small subsystem.

Examples:

- File upload component
- Authentication middleware
- Validation service

### Module

A complete functional module.

Examples:

- Import module
- Catalogue module
- User-management module

### Cross-cutting

A concern shared across several modules.

Examples:

- Logging
- Error handling
- Authentication
- Design tokens
- API response structures

### System

A broad architectural initiative affecting most of the repository.

Examples:

- Migrating to a modular architecture
- Introducing a full design system
- Replacing the persistence approach

System-level hardening should be exceptional and should usually be broken into linked module or cross-cutting scopes.

---

## 5.2 Proportionality rules

The skills must apply the following rules:

1. Do not document every function or file.
2. Add wiki content only for knowledge likely to be reused.
3. Add design documents only for consequential decisions.
4. Add code standards only when the rule should apply repeatedly.
5. Do not create an abstraction solely to make the design appear cleaner.
6. Do not refactor code outside the scope without recording and approving the expansion.
7. Treat changes to shared code as a cross-cutting impact.
8. Prefer a linked follow-up scope over silently expanding the current scope.
9. Match the depth of diagrams, examples, and analysis to the scope level.
10. Preserve traceability without creating documentation bureaucracy.

---

# 6. Hardening Scope Contract

Every hardening initiative must have a scope folder.

The primary machine-readable file is:

```text
docs/hardening/scopes/<scope-id>/scope.yaml
```

A recommended structure is:

```yaml
id: HD-2026-001-import-module
title: Import module hardening
status: active
scope_level: module

baseline_commit: abc123

modules:
  - import

include:
  source:
    - src/features/import/**
    - src/server/import/**
  documentation:
    - docs/wiki/import/**
    - docs/design/frontend/modules/import/**
    - docs/design/backend/modules/import/**
    - docs/code/frontend/**
    - docs/code/backend/**

shared_code:
  - src/ui/**
  - src/errors/**

exclude:
  - src/features/export/**
  - new file-format support
  - performance redesign

capability_freeze:
  preserve:
    - Upload CSV files
    - Preview imported rows
    - Display validation findings
    - Save valid records
  known_defects:
    - Import cancellation may leave temporary data
  deferred_features:
    - JSON import
    - Saved import templates

tracks:
  wiki:
    required: true
    status: pending
  design:
    required: true
    status: pending
  code_docs:
    required: true
    status: pending
  refactoring:
    required: true
    status: blocked
  guide:
    impact_assessment: pending

frontend:
  included: true
  claude_design:
    required: true
    status: not-prepared

backend:
  included: true

acceptance:
  - Existing capability baseline remains operational
  - Relevant concepts are documented
  - Frontend and backend design decisions are explicit
  - Applicable coding standards are documented
  - Code conforms to approved design and standards
  - Tests, type checks and builds pass
```

---

# 7. Hardening Manifest

The repository-level manifest records active and historical scopes.

Example:

```yaml
active_scopes:
  - HD-2026-001-import-module

scopes:
  HD-2026-001-import-module:
    title: Import module hardening
    level: module
    status: active
    current_track: design
    iteration: 2
    path: docs/hardening/scopes/HD-2026-001-import-module

  HD-2026-002-error-handling:
    title: Shared error-handling standard
    level: cross-cutting
    status: planned
    current_track: wiki
    iteration: 0
    path: docs/hardening/scopes/HD-2026-002-error-handling
```

When only one scope is active, a skill may select it automatically.

When multiple scopes are active, the skill must identify the intended scope before making changes.

A skill must never assume that “harden the project” means the entire repository.

---

# 8. Cycle State

Each scope maintains a `cycle.yaml`.

Example:

```yaml
scope_id: HD-2026-001-import-module
iteration: 2
current_track: design
status: in-progress

tracks:
  wiki:
    status: passed
    completed_iteration: 1
  design:
    status: in-progress
  code_docs:
    status: blocked
    blocked_by:
      - design
  refactoring:
    status: blocked
    blocked_by:
      - design
      - code_docs
  verification:
    status: pending

blockers:
  - IDENTITY-004

next_recommended_skill: design-docs-hardening
```

Supported track states are:

```text
not-required
pending
in-progress
blocked
awaiting-input
awaiting-handoff
review-required
passed
failed
drifted
```

A passed track may later become drifted if a downstream activity exposes an inconsistency.

---

# 9. Shared Skill Protocol

All four skills must follow the same repository protocol.

Before acting, each skill must read:

1. Root `CLAUDE.md`
2. `docs/README.md`
3. `docs/hardening/README.md`
4. `docs/hardening/manifest.yaml`
5. The selected scope’s `scope.yaml`
6. The selected scope’s `cycle.yaml`
7. The README belonging to the skill’s documentation area
8. Existing findings and open questions
9. The relevant implementation and documentation paths

Each skill must then:

1. Confirm the effective scope.
2. Identify relevant inclusions and exclusions.
3. Respect the capability freeze.
4. Work only within its owned responsibility.
5. Record cross-domain findings rather than silently resolving them.
6. Update the hardening record.
7. Recommend the next appropriate skill or checkpoint.
8. Avoid adding new functionality.
9. Avoid silently widening the scope.
10. Preserve traceability between findings, decisions, standards, and code changes.

---

# 10. Skill 1: Wiki Docs Hardening

## Name

```text
wiki-docs-hardening
```

## Purpose

Harden the knowledge documentation relevant to a declared repository scope.

The skill improves `docs/wiki` by extracting, reconciling, structuring, and validating knowledge from:

- Existing wiki documents
- The codebase
- Product behaviour
- Tests
- Existing design documents
- User-provided domain knowledge
- Relevant external specifications already available in the repository

## Owned area

```text
docs/wiki/**
```

The skill may also update:

```text
docs/hardening/scopes/<scope-id>/**
```

It must not make architectural decisions on behalf of design hardening.

## Inputs

- Active hardening scope
- Relevant source code
- Relevant tests
- Existing wiki documentation
- Root and wiki-specific Claude instructions
- Existing hardening findings
- Confirmed user input

## Outputs

- Improved wiki structure
- New or corrected concept documents
- Glossary updates
- Capability and workflow knowledge
- Identified inconsistencies
- Open questions
- Findings assigned to design, code documentation, or refactoring

## Primary activities

1. Inventory relevant knowledge.
2. Extract concepts and terminology.
3. Distinguish concepts from implementation details.
4. Reconcile duplicate or conflicting definitions.
5. Document business rules and invariants.
6. Identify unclear or overloaded terminology.
7. Add links between related knowledge.
8. Remove or flag stale knowledge.
9. Record unresolved questions.
10. Verify conformance with `docs/wiki/README.md`.

## Prohibited activities

The skill must not:

- Select architecture patterns
- Define coding standards
- Refactor production code
- Invent business rules
- Treat current code as unquestionable product truth
- Move implementation details into the wiki merely because they exist

## Completion criteria

Wiki hardening passes when:

- Relevant concepts are understandable
- Terminology is consistent
- Important business rules are documented
- Knowledge is separated from design and code standards
- Uncertainties are explicitly recorded
- Design hardening has enough conceptual context to proceed

---

# 11. Skill 2: Design Docs Hardening

## Name

```text
design-docs-hardening
```

## Purpose

Harden the design documentation relevant to a declared scope by making architectural, structural, frontend, backend, and UX/UI decisions explicit.

## Owned area

```text
docs/design/**
```

The skill may also update:

```text
docs/hardening/scopes/<scope-id>/**
```

## Inputs

- Active hardening scope
- Hardened wiki content
- Existing design documentation
- Current codebase
- Tests and behavioural baseline
- Existing technical constraints
- Claude Design handoffs where applicable
- Root and design-specific Claude instructions

## Outputs

- Explicit design decisions
- Frontend and backend architecture
- Responsibility and module boundaries
- UX/UI design-system documentation
- ADRs or equivalent decision records
- Design constraints
- Identified implementation gaps
- Required coding standards
- Refactoring implications

## Primary activities

1. Model the relevant current implementation.
2. Identify design pressures and inconsistencies.
3. Separate accidental implementation from deliberate design.
4. Define target frontend and backend direction.
5. Record consequential decisions and rationale.
6. Define boundaries and dependency directions.
7. Define UX/UI principles and system constraints.
8. Identify design rules that require code standards.
9. Record implementation implications without refactoring the code.
10. Verify conformance with `docs/design/README.md`.

## Frontend and backend separation

Design hardening must analyse frontend and backend independently where both are included.

### Frontend design concerns

- UX flows
- Information architecture
- Interaction design
- Visual system
- Design tokens
- Components and patterns
- Accessibility
- Responsive behaviour
- Frontend module boundaries
- State ownership
- Data-fetching boundaries

### Backend design concerns

- Domain boundaries
- Application services
- API contracts
- Data ownership
- Persistence boundaries
- Validation
- Error semantics
- Security
- Observability
- Integration boundaries
- Concurrency and idempotency

---

# 12. Claude Design Handoff

Claude Design integration belongs to `design-docs-hardening`.

A separate Claude Design skill should not initially be created unless the workflow becomes independently large enough to justify one.

## 12.1 Outbound handoff

When a frontend scope requires substantial UX/UI design, the skill prepares:

```text
docs/hardening/scopes/<scope-id>/handoffs/claude-design/outbound/
├── README.md
├── initial-prompt.md
├── product-context.md
├── capability-matrix.md
├── user-journeys.md
├── screen-inventory.md
├── interaction-states.md
├── technical-context.md
├── existing-components.md
├── constraints.md
├── screenshots/
└── assets/
```

The handoff must make the capability freeze clear.

Claude Design may improve:

- Usability
- Visual hierarchy
- Layout
- Accessibility
- Interaction design
- Component consistency
- Design-system reuse

It must not silently introduce new product functionality.

Once the outbound handoff is prepared, the design track moves to:

```text
awaiting-handoff
```

## 12.2 Human design iteration

The developer iterates in Claude Design until the design is acceptable.

This human-controlled checkpoint is intentional.

The repository-hardening skill should not assume that the first generated design is approved.

## 12.3 Inbound handoff

The returned handoff is placed under:

```text
docs/hardening/scopes/<scope-id>/handoffs/claude-design/inbound/
```

The design-hardening skill then performs an intake review.

Each proposal is classified as:

```text
adopt
adapt
existing
promote-to-design-system
module-specific
defer-as-feature
reject
clarify
```

The approved design is normalised into:

```text
docs/design/frontend/uxui/**
```

The raw handoff remains in `docs/hardening` for traceability. It is not automatically the permanent source of truth.

---

# 13. Skill 3: Code Docs Hardening

## Name

```text
code-docs-hardening
```

## Purpose

Harden the implementation standards under `docs/code` so that approved design decisions can be implemented consistently.

## Owned area

```text
docs/code/**
```

The skill may also update:

```text
docs/hardening/scopes/<scope-id>/**
```

## Inputs

- Active hardening scope
- Relevant wiki content
- Approved design documentation
- Existing code standards
- Current codebase
- Existing tests and tooling
- Root and code-specific Claude instructions

## Outputs

- Coding standards
- Naming conventions
- Implementation patterns
- Prohibited patterns
- Testing standards
- Examples
- Enforcement recommendations
- Refactoring requirements
- Traceability from design decisions to code rules

## Primary activities

1. Identify design decisions requiring implementation rules.
2. Review current coding practices.
3. Separate intentional patterns from accidental inconsistency.
4. Define repository or scope-specific standards.
5. Provide concise examples where useful.
6. Identify enforceable rules.
7. Recommend lint, type, test, or CI enforcement.
8. Define exceptions where necessary.
9. Identify code that currently violates the standards.
10. Verify conformance with `docs/code/README.md`.

## Standard quality test

A code standard should answer:

- What is required?
- Where does it apply?
- Why does it exist?
- What does compliant code look like?
- What is prohibited?
- How is compliance checked?
- What exceptions are permitted?

## Prohibited activities

The skill must not:

- Refactor the production code
- Contradict an approved design decision
- Introduce generic advice without repository value
- Turn one unusual implementation into a global standard
- Copy large portions of code into documentation unnecessarily

## Completion criteria

Code-docs hardening passes when:

- Required implementation rules are explicit
- Frontend and backend standards are separated where appropriate
- Standards trace back to design decisions
- Useful compliant examples exist
- Enforcement opportunities are identified
- Code refactoring has an actionable target

---

# 14. Skill 4: Code Refactoring

## Name

```text
code-refactoring
```

## Purpose

Refactor the actual codebase so that it conforms to approved wiki knowledge, design decisions, and coding standards while preserving the frozen capabilities.

## Owned area

The source paths declared in the hardening scope.

The skill may also update:

```text
tests/**
docs/hardening/scopes/<scope-id>/**
```

It may make small documentation corrections where the implementation exposes an obvious factual error, but it must not silently redesign the system.

## Entry conditions

Code refactoring may begin when:

- The scope is explicit
- The capability baseline is documented
- Required wiki hardening has passed
- Required design hardening has passed
- Required code-docs hardening has passed
- High-severity design questions are resolved

A scope may permit limited refactoring before all tracks pass, but this must be explicitly recorded.

## Inputs

- Active scope
- Behavioural baseline
- Approved wiki content
- Approved design documentation
- Approved coding standards
- Existing implementation
- Tests and build tooling
- Findings and deferred work

## Outputs

- Refactored code
- Added or updated tests
- Architecture and standard conformance
- Verification results
- Remaining deviations
- Newly discovered design or documentation issues
- Updated hardening status

## Primary activities

1. Establish or strengthen characterisation tests.
2. Plan incremental refactoring steps.
3. Preserve public and behavioural contracts.
4. Apply approved frontend and backend design.
5. Apply applicable coding standards.
6. Replace duplicated or inconsistent patterns.
7. Improve module boundaries.
8. Add automated enforcement where approved.
9. Run relevant tests, builds, linting, and type checks.
10. Record deviations and unresolved findings.

## Prohibited activities

The skill must not:

- Add unapproved functionality
- Widen the scope silently
- Rewrite a module unnecessarily
- Change business behaviour to simplify implementation
- Replace an approved design decision without returning to design hardening
- Treat all discovered technical debt as part of the current scope
- modify shared code without assessing affected modules

## Refactoring sequence

Prefer:

```text
Capture behaviour
  ↓
Introduce a seam or interface
  ↓
Adapt the current implementation
  ↓
Migrate one caller
  ↓
Verify
  ↓
Migrate remaining callers
  ↓
Remove obsolete code
  ↓
Verify again
```

Avoid broad rewrites without intermediate verification.

---

# 15. Findings and Routing

Every skill may discover issues outside its ownership.

These issues must be recorded rather than silently resolved.

Suggested finding types:

```text
wiki-gap
wiki-conflict
design-needed
design-conflict
code-standard-needed
code-nonconformance
behaviour-regression
known-defect
guide-impact
scope-expansion
shared-code-impact
new-feature
open-question
```

Each finding should contain:

```text
ID
Type
Severity
Status
Description
Evidence
Affected paths
Owning skill
Scope
Recommended action
Resolution
```

Example:

```markdown
## HD-IMP-014

**Type:** design-needed  
**Severity:** medium  
**Owner:** design-docs-hardening  
**Status:** open

The import form performs business validation directly inside the React
component. The wiki confirms that the same rules apply to API imports.

A design decision is required on the ownership and reuse of validation logic.

Affected paths:

- src/features/import/ImportForm.tsx
- src/server/import/validateImport.ts
```

---

# 16. Conflict Resolution

When documentation and implementation disagree, the discrepancy must be classified.

Possible classifications are:

- The wiki is stale
- The design is outdated
- The code standard is outdated
- The code is nonconforming
- The current behaviour is a defect
- The current behaviour is an undocumented requirement
- The scope is incomplete
- A human decision is required

The skill must not automatically assume that either the code or the documentation is correct.

The following precedence applies:

1. Explicit human-approved scope and capability constraints
2. Confirmed business facts and product behaviour
3. Approved design decisions
4. Approved code standards
5. Current implementation
6. Generic best practices

A generic best practice must never override an intentional repository decision without explicit reconsideration.

---

# 17. Role of `CLAUDE.md`

`CLAUDE.md` should route Claude toward the correct sources of truth.

It should not duplicate all repository documentation.

The root `CLAUDE.md` should state:

- The documentation taxonomy
- The requirement to read the active hardening scope
- The authority of wiki, design, code, and guide documentation
- The no-feature rule during hardening
- The requirement to respect scope boundaries
- The requirement to record cross-domain findings
- Links to relevant README files

Example:

```markdown
## Repository documentation

Before modifying a scoped module:

1. Read `docs/hardening/manifest.yaml`.
2. Read the selected scope under `docs/hardening/scopes/`.
3. Read relevant documents under:
   - `docs/wiki`
   - `docs/design`
   - `docs/code`
4. Preserve the capability freeze.
5. Do not widen the scope silently.
6. Record design or documentation conflicts in the scope findings.
```

Each documentation root must have its own README acting as its local constitution:

```text
docs/wiki/README.md
docs/design/README.md
docs/code/README.md
docs/guide/README.md
docs/hardening/README.md
```

These README files should define:

- Purpose
- Inclusion criteria
- Exclusion criteria
- Folder organisation
- Naming
- Document status
- Review expectations
- Ownership
- Update rules
- Relationship with other documentation areas

---

# 18. Verification

Verification occurs after refactoring and may cause earlier tracks to reopen.

The verification process must assess:

## Behavioural verification

- Existing capabilities still work
- Known contracts are preserved
- Known defects have not been accidentally reclassified as features
- No new unapproved functionality was added

## Wiki verification

- Terms used by the implementation remain consistent
- Business facts remain accurate
- New concepts have not appeared without documentation

## Design verification

- Module boundaries match the approved design
- Dependency directions are respected
- Frontend and backend responsibilities are correctly separated
- UX/UI implementation conforms to the approved system

## Code-standard verification

- Applicable standards are followed
- Exceptions are documented
- Automated enforcement is operational where required

## Documentation verification

- Links work
- Documents do not contradict one another
- Scope status is current
- Guide impact has been assessed

## Technical verification

- Tests pass
- Builds succeed
- Type checks pass
- Linters pass
- Architecture checks pass where present
- Visual regression checks pass where present

---

# 19. Definition of Done

A hardening scope may be closed when:

1. The scope and capability baseline are explicit.
2. Required wiki hardening has passed.
3. Required design hardening has passed.
4. Required code-docs hardening has passed.
5. Required refactoring is complete.
6. Relevant tests and checks pass.
7. No unresolved critical or high-severity findings remain.
8. Remaining deviations are explicitly accepted.
9. Deferred features and debt are recorded.
10. Shared-code impacts have been assessed.
11. Guide impact has been assessed.
12. The final verification report is complete.
13. The manifest records the hardened commit.
14. The scope status is set to `closed`.

Example completion data:

```yaml
status: closed
closed_at: 2026-08-15
hardened_commit: def456
final_iteration: 3

tracks:
  wiki: passed
  design: passed
  code_docs: passed
  refactoring: passed
  verification: passed

guide:
  impact_assessment: no-change-required
```

---

# 20. Skill Composition Strategy

The initial implementation should contain four independent skills:

```text
wiki-docs-hardening
design-docs-hardening
code-docs-hardening
code-refactoring
```

The repository’s `docs/hardening` protocol coordinates them.

No orchestrator skill is required initially.

This has several advantages:

- Each skill has one clear responsibility.
- Human review can occur between tracks.
- Claude Design iteration remains a deliberate checkpoint.
- Skills can be improved independently.
- Failure in one track does not obscure the others.
- Scope state persists across separate Claude sessions.
- The workflow does not depend on one long agent context.

A future skill named something like:

```text
hardening-cycle
```

may be introduced after the four individual skills are stable.

Its responsibility would be limited to:

- Selecting the scope
- Reading cycle state
- Invoking or recommending the next track
- Checking entry and exit conditions
- Producing consolidated status

It should not duplicate the specialist skills’ reasoning.

---

# 21. Example End-to-End Cycle

## Step 1: Open a scope

```text
Create a module-level hardening scope for the import module.
Freeze its existing capabilities and include its frontend and backend.
```

The result is:

```text
docs/hardening/scopes/HD-2026-001-import-module/
```

## Step 2: Harden the wiki

```text
Use wiki-docs-hardening for HD-2026-001-import-module.
```

Outputs might include:

- Import Job concept
- Import Row concept
- Validation Finding concept
- Import workflow
- Terminology corrections
- Open design questions

## Step 3: Harden the design

```text
Use design-docs-hardening for HD-2026-001-import-module.
```

The skill:

- Analyses current frontend and backend structure
- Defines backend boundaries
- Prepares a Claude Design handoff
- Pauses for human design iteration
- Ingests the approved return
- Documents the UX/UI system
- Records design decisions
- Identifies required coding standards

## Step 4: Harden code documentation

```text
Use code-docs-hardening for HD-2026-001-import-module.
```

The skill defines:

- Component rules
- Validation patterns
- Error patterns
- State-management rules
- Testing requirements
- Design-token usage
- Enforcement mechanisms

## Step 5: Refactor the code

```text
Use code-refactoring for HD-2026-001-import-module.
```

The skill:

- Adds regression tests
- Refactors incrementally
- Applies approved frontend and backend design
- Uses the approved UX/UI system
- Applies coding standards
- Records deviations

## Step 6: Verify

The refactoring skill performs technical verification.

Any unresolved documentation or design discrepancies reopen the appropriate track.

## Step 7: Close

The scope is closed and the manifest records the hardened commit.

---

# 22. Core Principles

The hardening system is governed by the following principles:

1. Functionality is frozen before structural hardening begins.
2. Every hardening action is proportional to an explicit scope.
3. Knowledge, design, coding standards, implementation, and user guidance remain separate.
4. Wiki documentation describes meaning.
5. Design documentation makes consequential decisions.
6. Code documentation defines repeatable implementation rules.
7. Refactoring makes the implementation conform.
8. Claude Design is a formal frontend design checkpoint.
9. The codebase is evidence, not automatically the intended design.
10. No skill silently expands its authority.
11. Cross-domain findings are routed, not hidden.
12. Shared code requires explicit impact analysis.
13. Future AI coding sessions must inherit hardened constraints.
14. Documentation should reduce future reasoning, not create bureaucracy.
15. Human approval remains central for consequential product and design decisions.
