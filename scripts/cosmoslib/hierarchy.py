"""
Generic parent-chain hierarchy builder, replacing utilities/macros/create_hierarchy.sas, and
a directory-tree lister replacing utilities/macros/util_gettree.sas. Neither has a current
caller in the SAS source (create_hierarchy.sas is never %included by a driver script, and
util_gettree.sas's only reference is its own docstring example) - both are ported as
library-only functions per the plan's architecture, with no CLI.

build_hierarchy()'s algorithm mirrors the already-working, independently-authored recursive
parent walk in scripts/create_cosmos_bc_excel.py's get_hierarchy_path()/create_bc_hierarchy()
(used for the real "BC Hierarchy" export sheet) rather than re-deriving create_hierarchy.sas's
iterative self-join from scratch - a recursive walk up the parent chain is simpler and more
idiomatic in Python, and produces the same (level, breadcrumb) shape as the SAS macro's
`_hierarchy_level_`/`_hierarchy_full_` output columns.
"""

import os


def build_hierarchy(rows, child_key, parent_key, label_key):
    """rows: an iterable of dicts, each with at least child_key/parent_key/label_key.
    Returns {child_id: (path_segments, level)} for every row with a non-blank child_key,
    where level is the ancestor-chain depth (0 for a root, i.e. no parent or an unresolved
    parent) and path_segments is an ordered list of "label (id)" strings from the topmost
    resolvable ancestor down to the row itself - join with "; " for
    create_hierarchy.sas's `_hierarchy_full_` string.

    A parent id that doesn't resolve to any row's child_key is treated as a root (matches
    the SAS macro's LEFT JOIN: an unmatched parent stops the ancestor chain there). A cycle
    is broken at the point it's detected rather than looping forever (the SAS macro has no
    such guard and would iterate until a real one existed in the data)."""
    by_child = {row[child_key]: row for row in rows if row.get(child_key)}
    cache = {}

    def path(child_id, visited):
        if child_id in cache:
            return cache[child_id]
        if child_id not in by_child or child_id in visited:
            return [], -1

        row = by_child[child_id]
        segment = f"{row.get(label_key, '')} ({child_id})"
        parent_id = row.get(parent_key)
        if not parent_id:
            result = ([segment], 0)
        else:
            parent_path, parent_level = path(parent_id, visited | {child_id})
            result = (parent_path + [segment], parent_level + 1) if parent_path else ([segment], 0)

        cache[child_id] = result
        return result

    return {child_id: path(child_id, set()) for child_id in by_child}


def hierarchy_rows(rows, child_key, parent_key, label_key):
    """Returns `rows` with two additional keys added to each dict - hierarchy_level and
    hierarchy_full - matching create_hierarchy.sas's dsout shape."""
    hierarchy = build_hierarchy(rows, child_key, parent_key, label_key)
    output = []
    for row in rows:
        path_segments, level = hierarchy.get(row.get(child_key), ([], -1))
        output.append(dict(row, hierarchy_level=level, hierarchy_full="; ".join(path_segments)))
    return output


def list_directory_tree(root):
    """Replaces util_gettree.sas's recursive directory walk with os.walk(). Returns a list
    of {dir, ext, filename, dirname, fullpath} dicts for every file and subdirectory under
    root, matching the SAS macro's output columns (dir: bool here, "0"/"1" in SAS; ext has
    no leading ".")."""
    entries = []
    for dirpath, dirnames, filenames in os.walk(root):
        for name in dirnames:
            entries.append({
                "dir": True, "ext": "", "filename": "", "dirname": dirpath + os.sep,
                "fullpath": os.path.join(dirpath, name),
            })
        for name in filenames:
            _, ext = os.path.splitext(name)
            entries.append({
                "dir": False, "ext": ext.lstrip(".").lower(), "filename": name,
                "dirname": dirpath + os.sep, "fullpath": os.path.join(dirpath, name),
            })
    return entries
