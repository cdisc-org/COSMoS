"""
Accumulates validation issue records and writes them out, replacing the accumulated
all_issues_{bc,sdtm,crf} dataset and the ods html5/excel report dump at the end of each
utilities/convert_*_xlsx2yaml.sas driver and utilities/macros/add2issues_{bc,sdtm,crf}
(utilities/config.sas).
"""

import os

from openpyxl import Workbook


class IssueLog:
    def __init__(self, id_columns):
        self.id_columns = list(id_columns)
        self.rows = []

    def add(self, excel_file, tab, severity, issue_type, expected_value="", actual_value="", comment="", **ids):
        row = {
            "_excel_file_": excel_file,
            "_tab_": tab,
            "severity": severity,
        }
        for column in self.id_columns:
            row[column] = ids.get(column, "")
        row["issue_type"] = issue_type
        row["expected_value"] = expected_value
        row["actual_value"] = actual_value
        row["comment"] = comment
        self.rows.append(row)
        return row

    @property
    def columns(self):
        return (
            ["_excel_file_", "_tab_", "severity"]
            + self.id_columns
            + ["issue_type", "expected_value", "actual_value", "comment"]
        )

    def severity_counts(self):
        counts = {}
        for row in self.rows:
            counts[row["severity"]] = counts.get(row["severity"], 0) + 1
        return counts

    def write_csv(self, path):
        import csv

        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(fh, fieldnames=self.columns)
            writer.writeheader()
            for row in self.rows:
                writer.writerow(row)

    def write_xlsx(self, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Issues"
        sheet.append(self.columns)
        for row in self.rows:
            sheet.append([row.get(column, "") for column in self.columns])
        workbook.save(path)

    def print_summary(self):
        counts = self.severity_counts()
        if not counts:
            print("No issues found.")
            return
        print(f"Found {len(self.rows)} issue(s):")
        for severity in sorted(counts):
            print(f"  {severity}: {counts[severity]}")
