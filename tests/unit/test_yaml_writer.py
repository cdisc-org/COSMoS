import io

from cosmoslib.yaml_writer import YamlWriter, needs_quoting


def test_needs_quoting_true_for_special_chars():
    assert needs_quoting('has "quote"')
    assert needs_quoting("has:colon")
    assert needs_quoting("has-dash")


def test_needs_quoting_false_for_plain_text():
    assert not needs_quoting("Subject Characteristics")
    assert not needs_quoting("")
    assert not needs_quoting(None)


def test_scalar_omits_blank_values():
    fh = io.StringIO()
    writer = YamlWriter(fh)
    writer.scalar("ncitCode", "")
    writer.scalar("ncitCode", None)
    assert fh.getvalue() == ""


def test_scalar_quotes_only_when_needed():
    fh = io.StringIO()
    writer = YamlWriter(fh)
    writer.scalar("shortName", "Entry Date from Country")
    writer.scalar("shortName", "PASI Fredriksson Version - Head: Desquamation/Scaling")
    lines = fh.getvalue().splitlines()
    assert lines[0] == "shortName: Entry Date from Country"
    assert lines[1] == 'shortName: "PASI Fredriksson Version - Head: Desquamation/Scaling"'


def test_scalar_always_quoted_writes_empty_string():
    fh = io.StringIO()
    writer = YamlWriter(fh)
    writer.scalar_always_quoted("sdtmigEndVersion", "")
    writer.scalar_always_quoted("packageDate", "2026-07-14")
    lines = fh.getvalue().splitlines()
    assert lines[0] == 'sdtmigEndVersion: ""'
    assert lines[1] == 'packageDate: "2026-07-14"'


def test_block_key_and_indent():
    fh = io.StringIO()
    writer = YamlWriter(fh)
    writer.block_key("categories")
    writer.list_scalar("Subject Characteristics", indent=2)
    assert fh.getvalue().splitlines() == ["categories:", "  - Subject Characteristics"]


def test_list_scalar_quotes_only_when_needed():
    fh = io.StringIO()
    writer = YamlWriter(fh)
    writer.list_scalar("Temporal", indent=2)
    writer.list_scalar("has-dash", indent=2)
    assert fh.getvalue().splitlines() == ["  - Temporal", '  - "has-dash"']


def test_list_quoted_always_quotes():
    fh = io.StringIO()
    writer = YamlWriter(fh)
    writer.list_quoted("0", indent=6)
    writer.list_quoted("NONE", indent=6)
    assert fh.getvalue().splitlines() == ['      - "0"', '      - "NONE"']


def test_escaping_embedded_quotes():
    fh = io.StringIO()
    writer = YamlWriter(fh)
    writer.scalar("shortName", 'has "embedded" quotes')
    assert fh.getvalue().splitlines() == ['shortName: "has \\"embedded\\" quotes"']


def test_raw_never_quotes_even_with_trigger_characters():
    fh = io.StringIO()
    writer = YamlWriter(fh)
    writer.raw("href", "https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/C1", indent=4)
    writer.raw("shortName", "Not-Done Reason", indent=4)
    assert fh.getvalue().splitlines() == [
        "    href: https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/C1",
        "    shortName: Not-Done Reason",
    ]


def test_raw_writes_blank_value_instead_of_omitting():
    fh = io.StringIO()
    writer = YamlWriter(fh)
    writer.raw("shortName", "", indent=4)
    writer.raw("shortName", None, indent=4)
    assert fh.getvalue().splitlines() == ["    shortName: ", "    shortName: "]
