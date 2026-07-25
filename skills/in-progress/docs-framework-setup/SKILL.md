---
name: docs-framework-setup
description: Create, migrate, repair, validate, or extend a repository documentation framework organised as docs/wiki, docs/design, docs/code, docs/guide, and docs/hardening. Use this command to establish the framework, classify an existing docs tree, add hardening state and README constitutions, or create a new scoped hardening work package.
argument-hint: "[create|migrate|repair|validate|new-scope] [details]"
arguments:
  - action
disable-model-invocation: true
---

# Docs Framework Setup

Requested action: `$action`
Full invocation arguments: `$ARGUMENTS`

Establish or repair the repository-owned documentation and hardening framework without deleting, overwriting, or misclassifying existing knowledge.

## Load before acting

1. Read the root `CLAUDE.md` and any relevant nested `CLAUDE.md` files.
2. Read `${CLAUDE_SKILL_DIR}/references/framework-spec.md`.
3. Read `${CLAUDE_SKILL_DIR}/references/migration-rules.md`.
4. Inventory the current `docs/`, `.claude/`, source, test, and configuration structure.

## Interpret the action

- `create`: scaffold the framework when meaningful documentation does not yet exist.
- `migrate`: inventory and classify an existing documentation tree before moving anything.
- `repair`: reconcile missing constitutions, manifests, scopes, links, or authority boundaries.
- `validate`: perform read-only framework validation and report failures.
- `new-scope`: create a hardening scope after collecting its title, level, included paths, exclusions, preserved capabilities, frontend/backend inclusion, and Claude Design requirement.
- Empty or unrecognised action: inspect the repository and choose `create`, `migrate`, or `repair`; state the selected mode before changing files.

## Workflow

1. Determine the repository root and operating mode.
2. Preserve all existing documentation until its content and authority are understood.
3. Establish or reconcile:
   - `docs/README.md`
   - `docs/wiki/README.md`
   - `docs/design/README.md`
   - `docs/code/README.md`
   - `docs/guide/README.md`
   - `docs/hardening/README.md`
   - `docs/hardening/manifest.yaml`
   - `docs/hardening/scopes/`
   - `docs/hardening/archive/`
4. In migrate mode, produce a migration map with source, proposed destination, rationale, conflicts, split requirements, and review status before relocating files.
5. Keep `CLAUDE.md` concise. Add routing instructions and links, not duplicated documentation.
6. Do not create speculative deep folder trees. Create subfolders only when repository content requires them.
7. Run validation and fix framework-owned failures that are safe to fix.
8. Report created, retained, migrated, unresolved, and validation results.

## Bundled scripts

Use these scripts when they fit the repository. Inspect them before execution and preserve normal Claude Code permission prompts.

- `${CLAUDE_SKILL_DIR}/scripts/setup_docs_framework.py`
- `${CLAUDE_SKILL_DIR}/scripts/create_hardening_scope.py`
- `${CLAUDE_SKILL_DIR}/scripts/validate_docs_framework.py`

Typical invocation:

```text
python <script> <repository-path> [options]
```

On Windows, use `py` instead of `python` when required.

The setup script creates framework-owned files only and does not move legacy documents. The scope script creates a scope skeleton; review and complete the generated baseline before beginning hardening.

## Safety constraints

- Never delete documentation merely because it does not fit the taxonomy.
- Never overwrite an existing README without reconciling its instructions.
- Never move files based only on their names.
- Never treat current implementation narration as approved design automatically.
- Never create an implicit hardening scope.
- Prefer a module or cross-cutting scope over a system-wide scope.

## Completion

Leave the repository with a valid framework or a precise migration/repair plan. State the next command, usually `/wiki-docs-hardening <scope-id>` after a scope and behavioural baseline are ready.
