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

%let excel_file=&root/curation/draft/collection/collection_specialization_AE.xlsx;
%generate_yaml_from_bc_collection(excel_file=&excel_file, type=ae, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(Collection_AE), debug=0);

%let excel_file=&root/curation/draft/collection/collection_specialization_DM.xlsx;
%generate_yaml_from_bc_collection(excel_file=&excel_file, type=dm, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(Collection_DM), debug=0);

%let excel_file=&root/curation/draft/collection/collection_specialization_EG_Local.xlsx;
%generate_yaml_from_bc_collection(excel_file=&excel_file, type=eg, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(Collection_EG), debug=0);

%let excel_file=&root/curation/draft/collection/collection_specialization_QRS_6MWT.xlsx;
%generate_yaml_from_bc_collection(excel_file=&excel_file, type=6mwt, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(Collection_QRS_6MWT), debug=0);

%let excel_file=&root/curation/draft/collection/collection_specialization_IE.xlsx;
%generate_yaml_from_bc_collection(excel_file=&excel_file, type=ie, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(Collection_IE), debug=0);

%let excel_file=&root/curation/draft/collection/collection_specialization_LB_Local_Chem_Blood.xlsx;
%generate_yaml_from_bc_collection(excel_file=&excel_file, type=lb, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(Collection_LB), debug=0);

%let excel_file=&root/curation/draft/collection/collection_specialization_LB_Local_Chem_Urin.xlsx;
%generate_yaml_from_bc_collection(excel_file=&excel_file, type=lb, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(Collection_LB), debug=0);

%let excel_file=&root/curation/draft/collection/collection_specialization_LB_Local_Hematology.xlsx;
%generate_yaml_from_bc_collection(excel_file=&excel_file, type=lb, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(Collection_LB), debug=0);

%let excel_file=&root/curation/draft/collection/collection_specialization_LB_Local_Urinalysis.xlsx;
%generate_yaml_from_bc_collection(excel_file=&excel_file, type=lb, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(Collection_LB), debug=0);

%let excel_file=&root/curation/draft/collection/collection_specialization_LBPERF_generic.xlsx;
%generate_yaml_from_bc_collection(excel_file=&excel_file, type=lb, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(Collection_LB_Perf), debug=0);

%let excel_file=&root/curation/draft/collection/collection_specialization_VS.xlsx;
%generate_yaml_from_bc_collection(excel_file=&excel_file, type=vs, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(Collection_VS), debug=0);

%let excel_file=&root/curation/draft/collection/collection_specialization_MH.xlsx;
%generate_yaml_from_bc_collection(excel_file=&excel_file, type=mh, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(Collection_MH), debug=0);

%let excel_file=&root/curation/draft/collection/collection_specialization_QRS_EQ5D-5L.xlsx;
%generate_yaml_from_bc_collection(excel_file=&excel_file, type=eq5d-l, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(Collection_QRS_EQ5D-5L), debug=0);

%let excel_file=&root/curation/draft/collection/collection_specialization_ADAS_COG.xlsx;
%generate_yaml_from_bc_collection(excel_file=&excel_file, type=adas-cog, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(Collection_ADAS-COG), debug=0);

%let excel_file=&root/curation/draft/collection/collection_specialization_SC.xlsx;
%generate_yaml_from_bc_collection(excel_file=&excel_file, type=sc, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(Collection_SC), debug=0);

%let excel_file=&root/curation/draft/collection/collection_specialization_SU.xlsx;
%generate_yaml_from_bc_collection(excel_file=&excel_file, type=su, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(Collection_SU), debug=0);

%let excel_file=&root/curation/draft/collection/collection_specialization_PR.xlsx;
%generate_yaml_from_bc_collection(excel_file=&excel_file, type=pr, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(Collection_PR), debug=0);

%let excel_file=&root/curation/draft/collection/collection_specialization_EC.xlsx;
%generate_yaml_from_bc_collection(excel_file=&excel_file, type=ec, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(Collection_EC), debug=0);

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

proc delete data=all_issues_collection;
run;
