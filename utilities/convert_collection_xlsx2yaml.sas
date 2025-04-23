%let root=C:/_github/cdisc-org/COSMoS;
%include "&root/utilities/config.sas";

%let _debug=0;

proc format;
  value $YN
    "Y" = "true"
    "y" = "true"
    "N" = "false"
    "n" = "false"
  ;
run;

%create_template(type=COLLECTION_ISSUE, out=work.all_issues_collection);

options mprint;

%let release=xx;
%let package=20251231;
%let folder=20251231_draft;
%let TargetFolder=&root/yaml/&folder/collection;
%let OverrideDate=%str(2025-12-31);

%let ExcelFile=&root/curation/draft/collection/collection_specialization_EG_Local.xlsx;
%generate_yaml_from_bc_collection(excel_file=&Excelfile, type=eg, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(Collection_EG), debug=0);

%let ExcelFile=&root/curation/draft/collection/collection_specialization_IE.xlsx;
%generate_yaml_from_bc_collection(excel_file=&Excelfile, type=ie, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(Collection_IE), debug=0);

%let ExcelFile=&root/curation/draft/collection/collection_specialization_LB_Local_Chem_Blood.xlsx;
%generate_yaml_from_bc_collection(excel_file=&Excelfile, type=lb, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(Collection_LB), debug=0);

%let ExcelFile=&root/curation/draft/collection/collection_specialization_LB_Local_Chem_Urin.xlsx;
%generate_yaml_from_bc_collection(excel_file=&Excelfile, type=lb, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(Collection_LB), debug=0);

%let ExcelFile=&root/curation/draft/collection/collection_specialization_LB_Local_Hematology.xlsx;
%generate_yaml_from_bc_collection(excel_file=&Excelfile, type=lb, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(Collection_LB), debug=0);

%let ExcelFile=&root/curation/draft/collection/collection_specialization_LB_Local_Urinalysis.xlsx;
%generate_yaml_from_bc_collection(excel_file=&Excelfile, type=lb, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(Collection_LB), debug=0);

%let ExcelFile=&root/curation/draft/collection/collection_specialization_VS.xlsx;
%generate_yaml_from_bc_collection(excel_file=&Excelfile, type=vs, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(Collection_VS), debug=0);




ods listing close;
ods html5 file="&root/utilities/reports/convert_collection_xlsx2yaml_issues_R&release._&todays..html";
ods excel options(sheet_name="Collection_&package" flow="tables" autofilter = 'all') file="&root/utilities/reports/convert_collection_xlsx2yaml_issues_R&release._&todays..xlsx";

proc print data=all_issues_collection;
  title "Collection Specialization Issues - &todays";
  var _excel_file_ _tab_ package_date severity collection_group_id collection_item issue_type expected_value actual_value comment;
run;

ods listing;
ods html5 close;
ods excel close;  
