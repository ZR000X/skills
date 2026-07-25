#!/usr/bin/env python3
"""Create a scoped repository-hardening work package using only the standard library."""
from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path


def yaml_list(values, indent=2):
    if not values:
        return " " * indent + "[]"
    return "\n".join(" " * indent + f"- {v}" for v in values)


def next_id(scopes: Path) -> str:
    year = date.today().year
    found = []
    if scopes.exists():
        for p in scopes.iterdir():
            m = re.match(rf"HD-{year}-(\d{{3}})-", p.name)
            if m:
                found.append(int(m.group(1)))
    return f"HD-{year}-{(max(found, default=0)+1):03d}"


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug[:48] or "scope"


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("repo", nargs="?", default=".")
    p.add_argument("title")
    p.add_argument("--level", choices=["patch", "component", "module", "cross-cutting", "system"], default="module")
    p.add_argument("--module", action="append", default=[])
    p.add_argument("--include", action="append", default=[])
    p.add_argument("--exclude", action="append", default=[])
    p.add_argument("--preserve", action="append", default=[])
    p.add_argument("--frontend", choices=["yes", "no"], default="yes")
    p.add_argument("--backend", choices=["yes", "no"], default="yes")
    p.add_argument("--claude-design", choices=["yes", "no"], default="no")
    args = p.parse_args()

    repo = Path(args.repo).resolve()
    scopes = repo / "docs/hardening/scopes"
    if not (repo / "docs/hardening/manifest.yaml").exists():
        raise SystemExit("Hardening framework missing. Run docs-framework-setup first.")

    prefix = next_id(scopes)
    scope_id = f"{prefix}-{slugify(args.title)}"
    target = scopes / scope_id
    if target.exists():
        raise SystemExit(f"Scope already exists: {target}")
    (target / "handoffs").mkdir(parents=True)

    scope_yaml = f"""id: {scope_id}\ntitle: {args.title}\nstatus: active\nscope_level: {args.level}\nbaseline_commit: pending\n\nmodules:\n{yaml_list(args.module)}\n\ninclude:\n  source:\n{yaml_list(args.include, 4)}\n  documentation: []\n\nshared_code: []\n\nexclude:\n{yaml_list(args.exclude)}\n\ncapability_freeze:\n  preserve:\n{yaml_list(args.preserve, 4)}\n  known_defects: []\n  deferred_features: []\n\ntracks:\n  wiki:\n    required: true\n    status: pending\n  design:\n    required: true\n    status: pending\n  code_docs:\n    required: true\n    status: pending\n  refactoring:\n    required: true\n    status: blocked\n  guide:\n    impact_assessment: pending\n\nfrontend:\n  included: {str(args.frontend == 'yes').lower()}\n  claude_design:\n    required: {str(args.claude_design == 'yes').lower()}\n    status: not-prepared\n\nbackend:\n  included: {str(args.backend == 'yes').lower()}\n\nacceptance:\n  - Existing capability baseline remains operational\n  - Relevant knowledge, design, and coding standards are explicit\n  - Code conforms to approved design and standards\n  - Relevant tests, type checks, lint, and builds pass\n"""
    cycle_yaml = f"""scope_id: {scope_id}\niteration: 1\ncurrent_track: wiki\nstatus: in-progress\n\ntracks:\n  wiki:\n    status: pending\n  design:\n    status: blocked\n    blocked_by: [wiki]\n  code_docs:\n    status: blocked\n    blocked_by: [design]\n  refactoring:\n    status: blocked\n    blocked_by: [design, code_docs]\n  verification:\n    status: pending\n\nblockers: []\nnext_recommended_skill: wiki-docs-hardening\n"""
    files = {
        "scope.yaml": scope_yaml,
        "cycle.yaml": cycle_yaml,
        "baseline.md": "# Behavioural Baseline\n\n## Preserved capabilities\n\n## Public contracts\n\n## Known defects\n\n## Baseline verification\n",
        "inventory.md": "# Scope Inventory\n\n## Source paths\n\n## Documentation\n\n## Tests and commands\n\n## Dependencies and dependants\n",
        "findings.md": "# Findings\n",
        "open-questions.md": "# Open Questions\n",
        "deferred.md": "# Deferred Work\n",
        "verification.md": "# Verification\n\n## Behaviour\n\n## Documentation\n\n## Design\n\n## Code standards\n\n## Technical checks\n",
    }
    for name, content in files.items():
        (target / name).write_text(content, encoding="utf-8")

    manifest = repo / "docs/hardening/manifest.yaml"
    text = manifest.read_text(encoding="utf-8")
    if "active_scopes: []" in text:
        text = text.replace("active_scopes: []", f"active_scopes:\n  - {scope_id}")
    elif scope_id not in text:
        text = text.replace("active_scopes:\n", f"active_scopes:\n  - {scope_id}\n", 1)
    if "scopes: {}" in text:
        text = text.replace("scopes: {}", "scopes:")
    if f"  {scope_id}:" not in text:
        text += f"\n  {scope_id}:\n    title: {args.title}\n    level: {args.level}\n    status: active\n    current_track: wiki\n    iteration: 1\n    path: docs/hardening/scopes/{scope_id}\n"
    manifest.write_text(text, encoding="utf-8")
    print(target)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
