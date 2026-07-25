#!/usr/bin/env python3
"""Safely scaffold the repository documentation hardening framework."""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

ROOT_READMES = {
    "docs/README.md": """# Documentation\n\nThis repository separates durable knowledge, design decisions, coding standards, user guidance, and hardening process state.\n\n- [Wiki](wiki/README.md): concepts, terminology, capabilities, workflows, and reference knowledge.\n- [Design](design/README.md): approved architectural and UX/UI direction.\n- [Code](code/README.md): implementation and testing standards.\n- [Guide](guide/README.md): user, administrator, operations, and troubleshooting guidance.\n- [Hardening](hardening/README.md): scoped hardening state, findings, handoffs, and verification.\n\nRepository-specific rules belong in each root README.\n""",
    "docs/wiki/README.md": """# Wiki Documentation\n\n## Purpose\nStore durable system and domain knowledge.\n\n## Include\nTerminology, concepts, capabilities, workflows, business rules, integrations, and reference knowledge.\n\n## Exclude\nArchitectural decisions, coding standards, process records, and user manuals.\n\n## Local rules\nDefine repository-specific organisation, naming, status, ownership, review, linking, and Obsidian conventions here.\n""",
    "docs/design/README.md": """# Design Documentation\n\n## Purpose\nStore deliberate decisions that constrain implementation.\n\n## Include\nArchitecture, boundaries, frontend and backend design, UX/UI systems, data and integration direction, security, and decision records.\n\n## Exclude\nUnconfirmed concepts, generic coding advice, current-code narration without approval, and user procedures.\n\n## Decision quality\nRecord context, decision, alternatives, consequences, scope, enforcement, and exceptions.\n""",
    "docs/code/README.md": """# Code Documentation\n\n## Purpose\nStore repeatable implementation and testing standards.\n\n## Include\nRequired and prohibited patterns, naming, frontend/backend/database conventions, examples, tooling, and enforcement.\n\n## Exclude\nArchitecture rationale, domain theory, process records, and user guidance.\n\n## Standard quality\nState what is required, where it applies, why, compliant and prohibited examples, enforcement, and exceptions.\n""",
    "docs/guide/README.md": """# User Guide\n\n## Purpose\nStore supported user-facing, administrator, operations, troubleshooting, and release guidance.\n\n## Exclude\nInternal architecture, coding standards, and hardening process records.\n\n## Local rules\nDefine audiences, versioning, screenshots, terminology, review, and release alignment here.\n""",
    "docs/hardening/README.md": """# Repository Hardening\n\nHardening converts working software into intentionally documented, designed, standardised, and conforming software without silently adding features.\n\nEvery action must belong to a declared scope under `scopes/`. Read `manifest.yaml`, then the scope's `scope.yaml` and `cycle.yaml`. Record cross-domain findings rather than silently widening scope.\n\nTrack states: `not-required`, `pending`, `in-progress`, `blocked`, `awaiting-input`, `awaiting-handoff`, `review-required`, `passed`, `failed`, and `drifted`.\n""",
}

MANIFEST = """active_scopes: []\n\nscopes: {}\n"""


def classify(path: Path) -> str:
    text = (path.name + " " + str(path.parent)).lower()
    if any(k in text for k in ("user-guide", "how-to", "tutorial", "troubleshoot", "runbook")):
        return "guide"
    if any(k in text for k in ("adr", "architecture", "design", "decision", "ux", "ui")):
        return "design"
    if any(k in text for k in ("coding", "standard", "convention", "style", "testing")):
        return "code"
    if any(k in text for k in ("glossary", "concept", "domain", "workflow", "reference")):
        return "wiki"
    return "unclear"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", nargs="?", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--force", action="store_true", help="Overwrite framework-owned files only")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    docs = repo / "docs"
    existing = []
    if docs.exists():
        existing = [p for p in docs.rglob("*") if p.is_file()]

    actions = []
    for rel, content in ROOT_READMES.items():
        target = repo / rel
        if not target.exists() or args.force:
            actions.append((target, content))
    manifest = repo / "docs/hardening/manifest.yaml"
    if not manifest.exists() or args.force:
        actions.append((manifest, MANIFEST))

    for directory in (repo/"docs/hardening/scopes", repo/"docs/hardening/archive"):
        if not directory.exists():
            if args.dry_run:
                print(f"CREATE DIR {directory}")
            else:
                directory.mkdir(parents=True, exist_ok=True)

    for target, content in actions:
        print(f"WRITE {target}")
        if not args.dry_run:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")

    framework_paths = {str((repo/rel).resolve()) for rel in ROOT_READMES}
    framework_paths.add(str(manifest.resolve()))
    legacy = [p for p in existing if str(p.resolve()) not in framework_paths and "docs/hardening" not in str(p)]
    if legacy:
        report = repo / "docs/hardening/framework-migration-report.md"
        lines = [
            "# Documentation Framework Migration Report",
            "",
            f"Generated: {date.today().isoformat()}",
            "",
            "No files were moved automatically. Review these provisional classifications based on names and paths; classify by content before migration.",
            "",
            "| Existing file | Provisional destination | Review status |",
            "|---|---|---|",
        ]
        for p in sorted(legacy):
            rel = p.relative_to(repo).as_posix()
            lines.append(f"| `{rel}` | `{classify(p)}` | unresolved |")
        print(f"WRITE {report}")
        if not args.dry_run and (not report.exists() or args.force):
            report.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print("Framework scaffold complete. Existing documentation was preserved.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
