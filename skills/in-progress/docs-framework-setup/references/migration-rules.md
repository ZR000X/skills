# Migration Rules

## Create mode

Use when `docs/` is absent or contains no meaningful documentation.

1. Inventory repository modules and existing instruction files.
2. Create the taxonomy and root README constitutions.
3. Create the hardening manifest and empty scope/archive folders.
4. Add concise routing guidance to `CLAUDE.md` only when requested or clearly safe.
5. Validate the structure.

## Migrate mode

Use when meaningful documentation already exists.

1. Inventory every existing documentation file without moving it.
2. Classify each file by its dominant purpose: wiki, design, code, guide, hardening, generated, obsolete, mixed, or unclear.
3. Identify documents that combine multiple authorities. Propose splitting them before moving.
4. Identify broken links, duplicate concepts, conflicting decisions, and stale content.
5. Produce a migration map with source, destination, rationale, and required edits.
6. Move only approved or unambiguous groups. Preserve Git history with `git mv` when available.
7. Repair links and navigation.
8. Leave unresolved files in place and record them in the migration report.
9. Validate the resulting framework.

## Safety rules

- Never delete content merely because it does not fit the taxonomy.
- Never overwrite an existing README without first reconciling its instructions.
- Do not classify code-generated API references as design decisions.
- Do not classify user procedures as code standards.
- Do not treat current implementation descriptions as approved design without evidence.
- Keep generated documentation clearly marked and isolated according to repository preference.
