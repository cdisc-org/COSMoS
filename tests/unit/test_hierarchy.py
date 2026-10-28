from cosmoslib.hierarchy import build_hierarchy, hierarchy_rows, list_directory_tree


def test_multi_level_chain_builds_outermost_first_breadcrumb():
    rows = [
        {"bc_id": "C1", "parent_bc_id": None, "short_name": "Grandparent"},
        {"bc_id": "C2", "parent_bc_id": "C1", "short_name": "Parent"},
        {"bc_id": "C3", "parent_bc_id": "C2", "short_name": "Child"},
    ]
    hierarchy = build_hierarchy(rows, "bc_id", "parent_bc_id", "short_name")

    assert hierarchy["C1"] == (["Grandparent (C1)"], 0)
    assert hierarchy["C2"] == (["Grandparent (C1)", "Parent (C2)"], 1)
    assert hierarchy["C3"] == (["Grandparent (C1)", "Parent (C2)", "Child (C3)"], 2)


def test_unresolvable_parent_is_treated_as_a_root():
    rows = [{"bc_id": "C2", "parent_bc_id": "MISSING", "short_name": "Orphan"}]
    hierarchy = build_hierarchy(rows, "bc_id", "parent_bc_id", "short_name")
    assert hierarchy["C2"] == (["Orphan (C2)"], 0)


def test_cycle_is_broken_rather_than_looping_forever():
    rows = [
        {"bc_id": "C1", "parent_bc_id": "C2", "short_name": "A"},
        {"bc_id": "C2", "parent_bc_id": "C1", "short_name": "B"},
    ]
    hierarchy = build_hierarchy(rows, "bc_id", "parent_bc_id", "short_name")
    # Whichever of the two is resolved first breaks the cycle and becomes a pseudo-root;
    # the other's chain then completes through it. Neither loops forever (this assertion
    # completing at all is the real test).
    assert hierarchy["C1"][1] in (0, 1)
    assert hierarchy["C2"][1] in (0, 1)


def test_rows_without_a_child_key_are_excluded():
    rows = [
        {"bc_id": "C1", "parent_bc_id": None, "short_name": "A"},
        {"bc_id": None, "parent_bc_id": None, "short_name": "No id"},
    ]
    hierarchy = build_hierarchy(rows, "bc_id", "parent_bc_id", "short_name")
    assert list(hierarchy.keys()) == ["C1"]


def test_hierarchy_rows_adds_level_and_full_columns_without_mutating_input():
    rows = [
        {"bc_id": "C1", "parent_bc_id": None, "short_name": "Parent"},
        {"bc_id": "C2", "parent_bc_id": "C1", "short_name": "Child"},
    ]
    augmented = hierarchy_rows(rows, "bc_id", "parent_bc_id", "short_name")

    by_id = {r["bc_id"]: r for r in augmented}
    assert by_id["C1"]["hierarchy_level"] == 0
    assert by_id["C1"]["hierarchy_full"] == "Parent (C1)"
    assert by_id["C2"]["hierarchy_level"] == 1
    assert by_id["C2"]["hierarchy_full"] == "Parent (C1); Child (C2)"

    assert "hierarchy_level" not in rows[0]  # original dicts untouched


def test_list_directory_tree_lists_files_and_subdirectories(tmp_path):
    (tmp_path / "sub").mkdir()
    (tmp_path / "sub" / "a.yaml").write_text("x: 1\n")
    (tmp_path / "b.txt").write_text("hello\n")

    entries = list_directory_tree(str(tmp_path))
    by_fullpath = {e["fullpath"]: e for e in entries}

    sub_dir = str(tmp_path / "sub")
    yaml_file = str(tmp_path / "sub" / "a.yaml")
    txt_file = str(tmp_path / "b.txt")

    assert by_fullpath[sub_dir]["dir"] is True
    assert by_fullpath[yaml_file]["dir"] is False
    assert by_fullpath[yaml_file]["ext"] == "yaml"
    assert by_fullpath[txt_file]["ext"] == "txt"
