#!/usr/bin/env python3
"""Validate required repository documentation hardening files."""
from __future__ import annotations

import argparse
from pathlib import Path

REQUIRED = [
    "docs/README.md",
    "docs/wiki/README.md",
    "docs/design/README.md",
    "docs/code/README.md",
    "docs/guide/README.md",
    "docs/hardening/README.md",
    "docs/hardening/manifest.yaml",
    "docs/hardening/scopes",
    "docs/hardening/archive",
]
SCOPE_REQUIRED = [
    "scope.yaml", "cycle.yaml", "baseline.md", "inventory.md", "findings.md",
    "open-questions.md", "deferred.md", "verification.md", "handoffs",
]


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("repo", nargs="?", default=".")
    args = p.parse_args()
    repo = Path(args.repo).resolve()
    errors = []
    for rel in REQUIRED:
        if not (repo / rel).exists():
            errors.append(f"Missing: {rel}")
    scopes = repo / "docs/hardening/scopes"
    if scopes.exists():
        for scope in sorted(x for x in scopes.iterdir() if x.is_dir()):
            for rel in SCOPE_REQUIRED:
                if not (scope / rel).exists():
                    errors.append(f"Missing in {scope.name}: {rel}")
    if errors:
        print("Framework validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Framework validation passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
