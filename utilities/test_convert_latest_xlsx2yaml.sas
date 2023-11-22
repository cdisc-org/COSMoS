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


%let package=latest;
%let ExcelFile=&root/utilities/reports/biomedical_concepts_2023-11-21.xlsx;
%let TargetFolder=&root/yaml/latest/bc;

%create_template(type=BC_ISSUE, out=work.all_issues_bc);
%generate_yaml_from_bc(excel_file=&ExcelFile, type=latest, package=&package, override_package_date=, out_folder=&TargetFolder, range=%str(Biomedical Concepts));

ods listing close;
ods html5 file="&root/utilities/reports/convert_latest_bc_issues_%sysfunc(date(), b8601da8.).html";
ods excel options(sheet_name="BC_&package" flow="tables" autofilter = 'all') file="&root/utilities/reports/convert_latest_bc_issues__%sysfunc(date(), b8601da8.).xlsx";

proc print data=all_issues_bc;
  title "BC Issues - %sysfunc(date(), b8601da8.)";
  var _excel_file_ _tab_ package_date severity BC_ID short_name dec_id dec_label issue_type expected_value actual_value comment;
run;

ods listing;
ods html5 close;
ods excel close;  



%let ExcelFile=&root/curation/draft/BC_Package_R6_LZZT.xlsx;
%get_Subset_Codelists(file=&Excelfile, range=Subset Codelist Example$, dsout=subsets);

%let ExcelFile=&root/utilities/reports/sdtm_dataset_specializations_2023-11-21.xlsx;
%let TargetFolder=&root/yaml/latest/sdtm;

%create_template(type=SDTM_ISSUE, out=work.all_issues_sdtm);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=latest, package=&package, override_package_date=, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM Dataset Specializations));

ods listing close;
ods html5 file="&root/utilities/reports/convert_latest_sdtm_issues_%sysfunc(date(), b8601da8.).html";
ods excel options(sheet_name="SDTM_&package" flow="tables" autofilter = 'all') file="&root/utilities/reports/convert_latest_sdtm_issues_%sysfunc(date(), b8601da8.).xlsx";

proc print data=all_issues_sdtm;
  title "SDTM Specialization Issues - %sysfunc(date(), b8601da8.)";
  var _excel_file_ _tab_ package_date severity vlm_group_id sdtm_variable issue_type expected_value actual_value comment;
run;

ods listing;
ods html5 close;
ods excel close;  

