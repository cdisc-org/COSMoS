"""
Hand-rolled, ordered YAML line emitter, replacing the `put` statements in
utilities/macros/generate_yaml_from_{bc,sdtm,crf}.sas.

The BC/SDTM/CRF yaml/**/*.yaml files have a fixed, non-alphabetical field order and a
conditional quoting rule (quote a scalar only if it contains '"', ':', or '-') that
yaml.safe_dump cannot reproduce without a fully custom Dumper. Using an explicit line
emitter keeps the "assemble ordered lines" model the SAS macros already use, and lets
callers opt individual fields (packageDate, version strings, valueList/exampleSet
terms) into always-quoted output where the source data requires it.
"""

_QUOTE_TRIGGER_CHARS = ('"', ':', '-')


def needs_quoting(value):
    if value is None:
        return False
    text = str(value)
    return any(char in text for char in _QUOTE_TRIGGER_CHARS)


def escape_and_quote(value):
    text = str(value).replace('"', '\\"')
    return f'"{text}"'


class YamlWriter:
    def __init__(self, fh):
        self.fh = fh

    def _write(self, line):
        self.fh.write(line + "\n")

    def raw(self, key, value, indent=0):
        """Write "key: value" with no quoting at all and no omit-if-blank guard, matching a
        bare `put "key:" +1 value;` call in the SAS macros - one with no surrounding
        index('"')/index(':')/index('-') check, so a value that contains a trigger
        character (an ncit explore URL always contains ':', and a curated DEC label like
        "Not-Done Reason" contains '-') is written as-is. Some call sites (the ncit "href:"
        line) are only ever reached from inside the caller's own `if not missing(...)`
        guard; others (the DEC-level "shortName:") have none in the SAS source and so must
        always write the line, even blank - callers, not this method, are responsible for
        matching whichever behavior the source macro has at that call site."""
        text = "" if value is None else str(value)
        self._write(f"{' ' * indent}{key}: {text}")

    def scalar(self, key, value, indent=0):
        """Write "key: value", quoting only if the value needs it. Omits the line
        entirely if value is None or empty, matching the SAS "if not missing(x)" guards."""
        if value is None or value == "":
            return
        text = str(value)
        if needs_quoting(text):
            text = escape_and_quote(text)
        self._write(f"{' ' * indent}{key}: {text}")

    def scalar_always_quoted(self, key, value, indent=0):
        """Write "key: \"value\"" unconditionally, including an empty "" when value is
        blank (e.g. packageDate, sdtmigStartVersion/EndVersion)."""
        text = "" if value is None else str(value)
        self._write(f"{' ' * indent}{key}: {escape_and_quote(text)}")

    def block_key(self, key, indent=0):
        """Write "key:" with no value, heading a nested map or list."""
        self._write(f"{' ' * indent}{key}:")

    def list_scalar(self, value, indent=0):
        """Write "- value" (a list item), quoting only if the value needs it."""
        text = str(value)
        if needs_quoting(text):
            text = escape_and_quote(text)
        self._write(f"{' ' * indent}- {text}")

    def list_quoted(self, value, indent=0):
        """Write "- \"value\"" (a list item) unconditionally quoted, matching fields
        like valueList/exampleSet whose terms are always quoted regardless of content."""
        self._write(f"{' ' * indent}- {escape_and_quote(value)}")
