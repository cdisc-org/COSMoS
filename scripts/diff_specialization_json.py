#!/usr/bin/env python3
"""Summarize differences between two SDTM dataset specialization JSON files.

Variables are matched by ``name`` (not array position); ``_links`` is ignored
by default because it only carries package-date noise.

Usage:
    python scripts/diff_specialization_json.py OLD.json NEW.json [--include-links]
"""
import argparse
import json
import sys


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def diff_values(old, new, path=""):
    """Yield (path, old, new) for every leaf-level difference between two JSON values."""
    if isinstance(old, dict) and isinstance(new, dict):
        for key in sorted(set(old) | set(new)):
            sub = f"{path}.{key}" if path else key
            if key not in old:
                yield sub, None, new[key]
            elif key not in new:
                yield sub, old[key], None
            else:
                yield from diff_values(old[key], new[key], sub)
    elif old != new:
        yield path, old, new


def fmt(value):
    return "<absent>" if value is None else json.dumps(value, ensure_ascii=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("old")
    parser.add_argument("new")
    parser.add_argument("--include-links", action="store_true", help="also diff the _links block")
    args = parser.parse_args()

    old, new = load(args.old), load(args.new)
    old_vars = {v["name"]: v for v in old.pop("variables", [])}
    new_vars = {v["name"]: v for v in new.pop("variables", [])}
    if not args.include_links:
        old.pop("_links", None)
        new.pop("_links", None)

    changed = False

    top = list(diff_values(old, new))
    if top:
        changed = True
        print("== Top-level changes ==")
        for path, o, n in top:
            print(f"  {path}: {fmt(o)} -> {fmt(n)}")

    added = [n for n in new_vars if n not in old_vars]
    removed = [n for n in old_vars if n not in new_vars]
    if added:
        changed = True
        print(f"\n== Variables added ({len(added)}) ==")
        for name in added:
            print(f"  + {name} ({new_vars[name].get('role')})")
    if removed:
        changed = True
        print(f"\n== Variables removed ({len(removed)}) ==")
        for name in removed:
            print(f"  - {name} ({old_vars[name].get('role')})")

    var_changes = []
    for name in old_vars:
        if name in new_vars:
            diffs = list(diff_values(old_vars[name], new_vars[name]))
            if diffs:
                var_changes.append((name, diffs))
    if var_changes:
        changed = True
        print(f"\n== Variables changed ({len(var_changes)}) ==")
        for name, diffs in var_changes:
            print(f"  ~ {name}")
            for path, o, n in diffs:
                print(f"      {path}: {fmt(o)} -> {fmt(n)}")

    if not changed:
        print("No differences.")
    return 1 if changed else 0


if __name__ == "__main__":
    sys.exit(main())
