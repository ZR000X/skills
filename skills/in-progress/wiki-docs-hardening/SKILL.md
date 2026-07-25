---
name: wiki-docs-hardening
description: Harden durable repository knowledge under docs/wiki for one declared docs/hardening scope. Use this command to extract and reconcile concepts, terminology, capabilities, workflows, business rules, invariants, integrations, and reference knowledge from code, tests, behaviour, and existing documentation without making architecture or coding-standard decisions.
argument-hint: "[scope-id]"
arguments:
  - scope
disable-model-invocation: true
---

# Wiki Docs Hardening

Requested scope: `$scope`

Harden the durable knowledge required to understand the selected scope. Keep implementation detail, architecture decisions, coding standards, and user instructions in their proper documentation areas.

## Load before acting

1. Read `${CLAUDE_SKILL_DIR}/references/shared-protocol.md`.
2. Read `${CLAUDE_SKILL_DIR}/references/wiki-method.md`.
3. Resolve the effective scope from `$scope` or `docs/hardening/manifest.yaml`.
4. Read the repository and scope files required by the shared protocol.
5. Follow `docs/wiki/README.md` as the repository-specific wiki constitution.

## Owned changes

Edit only:

- `docs/wiki/**`
- the selected `docs/hardening/scopes/<scope-id>/**` records
- small non-consequential cross-links or typo corrections outside the owned area

Route consequential design, code-standard, refactoring, and guide issues as findings.

## Workflow

1. Mark the wiki track `in-progress`.
2. Inventory relevant wiki pages, source paths, tests, observed behaviour, domain terms, APIs, integrations, and existing findings.
3. Build an evidence table separating confirmed knowledge, implementation evidence, assumptions, contradictions, defects, and unanswered questions.
4. Extract or reconcile only durable concepts, terminology, actors, capabilities, workflows, states, rules, invariants, and integration knowledge.
5. Distinguish intended business meaning from what the current implementation happens to do.
6. Consolidate duplicates and link shared knowledge rather than repeating it per module.
7. Apply repository navigation, naming, frontmatter, and Obsidian conventions defined by `docs/wiki/README.md`.
8. Record ambiguity instead of inventing a clean definition.
9. Open findings for design or code implications; do not solve them in wiki prose.
10. Run available documentation checks and verify links touched by the change.
11. Update `cycle.yaml` conservatively. Mark the wiki track `passed` only when design hardening has reliable conceptual input.

## Proportionality

For a module scope, prefer a module overview, a small set of reusable concepts, relevant workflows, glossary updates, and links to shared knowledge. Do not create one page per class, function, table, endpoint, or screen.

## Completion

Report the effective scope, pages changed, concepts clarified, conflicts resolved, open questions, routed findings, checks run, and the next command—normally `/design-docs-hardening <scope-id> analyze`.
