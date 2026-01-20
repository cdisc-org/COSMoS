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

%create_template(type=SDTM_ISSUE, out=work.all_issues_sdtm);


%let excel_file=&root/curation/package06/BC_Package_R6_LZZT.xlsx;
%get_Subset_Codelists(file=&excel_file, range=Subset Codelist Example$, dsout=subsets);

%let release=dht;
%let package=20261231;
%let folder=dht_test;
%let TargetFolder=&root/yaml/&folder/sdtm;
%let OverrideDate=%str(2026-12-31);

%let checkrelationships=1;
%let excel_file=&root/curation/draft/dht/DHT_BC_SDTM.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=di, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_DI), debug=0, check_relationships=&checkrelationships);
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=sleep, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_Sleep), debug=0, check_relationships=&checkrelationships);
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=steps, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_Steps), debug=0, check_relationships=&checkrelationships);
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=hr, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_HR), debug=0, check_relationships=&checkrelationships);
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=scratch, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_Scratch), debug=0, check_relationships=&checkrelationships);

/************************************************************************************************************************/

ods listing close;
ods html5 file="&root/utilities/reports/convert_sdtm_xlsx2yaml_issues_R&release._&todays..html";
ods excel options(sheet_name="SDTM_&package" flow="tables" autofilter = 'all') file="&root/utilities/reports/convert_sdtm_xlsx2yaml_issues_R&release._&todays..xlsx";

proc print data=all_issues_sdtm;
  title "SDTM Specialization Issues - &todays";
  var _excel_file_ _tab_ package_date severity vlm_group_id short_name sdtm_variable issue_type expected_value actual_value comment;
run;

ods listing;
ods html5 close;
ods excel close;

proc freq data=all_issues_sdtm;
  where index(issue_type, "RELATIONSHIP") and index(actual_value, ",")=0;
  tables actual_value;
run;
proc freq data=all_issues_sdtm;
  where index(issue_type, "RELATIONSHIP") and index(actual_value, ",")>0;
  tables actual_value;
run;    

proc delete data=work.all_issues_sdtm work.subsets;
run;
