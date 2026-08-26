"""
BC/SDTM/CRF issue-record id columns, replacing the BC_ISSUE/SDTM_ISSUE/CRF_ISSUE dataset
shells defined in utilities/macros/create_template.sas. IssueLog (see issues.py) always
adds _excel_file_, _tab_, severity, issue_type, expected_value, actual_value, comment; these
lists supply the record-identifying columns that differ per domain.
"""

BC_ISSUE_ID_COLUMNS = ["BC_ID", "short_name", "dec_id"]
SDTM_ISSUE_ID_COLUMNS = ["vlm_group_id", "short_name", "sdtm_variable"]
CRF_ISSUE_ID_COLUMNS = ["crf_group_id", "short_name", "crf_item"]

# The cross-workbook validators (cosmoslib/validators/) have no dedicated SAS *_ISSUE
# template - the SAS source just prints ad hoc PROC SQL result sets per check. package_date
# and identifier (a formatted "column=value, ..." string - see validators/common.py's
# _identifier()) stand in for whatever columns each check's SQL SELECT happened to project.
VALIDATION_ISSUE_ID_COLUMNS = ["package_date", "identifier"]
