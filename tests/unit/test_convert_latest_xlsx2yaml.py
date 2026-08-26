from convert_latest_xlsx2yaml import already_produced_ids


def test_already_produced_ids_reads_top_level_field_only(tmp_path):
    (tmp_path / "bc__c1.yaml").write_text(
        "packageDate: \"2026-01-01\"\n"
        "packageType: bc\n"
        "conceptId: C1\n"
        "dataElementConcepts:\n"
        "  - conceptId: C99\n"  # indented DEC conceptId - must NOT be picked up
        "    shortName: Foo\n"
    )
    (tmp_path / "bc__c2.yaml").write_text("packageDate: \"2026-01-01\"\nconceptId: C2\n")
    (tmp_path / "not-yaml.txt").write_text("conceptId: C999\n")

    ids = already_produced_ids(str(tmp_path), "conceptId")
    assert ids == ["C1", "C2"]


def test_already_produced_ids_returns_empty_list_for_missing_folder(tmp_path):
    assert already_produced_ids(str(tmp_path / "does_not_exist"), "conceptId") == []


def test_already_produced_ids_skips_file_with_no_matching_field(tmp_path):
    (tmp_path / "bc__c1.yaml").write_text("packageDate: \"2026-01-01\"\n")
    assert already_produced_ids(str(tmp_path), "conceptId") == []
