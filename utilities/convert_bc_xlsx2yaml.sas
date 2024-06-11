%let root=C:/_github/cdisc-org/COSMoS;
%include "&root/utilities/config.sas";

%let _debug=0;

%create_template(type=BC_ISSUE, out=work.all_issues_bc);


/*
%let package=20221026;
%let folder=20221026;
%let ExcelFile=&root/curation/BC_Package_2022_10_26.xlsx;
%let TargetFolder=&root/yaml/&folder/bc;

%generate_yaml_from_bc(excel_file=&ExcelFile, type=vs, package=20221026, out_folder=&TargetFolder, range=Conceptual VS BC);
%generate_yaml_from_bc(excel_file=&ExcelFile, type=lb, package=20221026, out_folder=&TargetFolder, range=%str(Conceptual LB (Common) BC));



%let package=20230213;
%let folder=20230213;
%let ExcelFile=&root/curation/BC_Package_2023_02_13.xlsx;
%let TargetFolder=&root/yaml/&package/bc;

%generate_yaml_from_bc(excel_file=&ExcelFile, type=lb_1, package=&package, out_folder=&TargetFolder, range=%str(BC LB (Common)));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=lb_2, package=&package, out_folder=&TargetFolder, range=%str(BC LB (TIG Biomarkers)));


%let package=20230331;
%let folder=20230331;
%let ExcelFile=&root/curation/BC_Package_2023_03_31.xlsx;
%let TargetFolder=&root/yaml/&folder/bc;

%generate_yaml_from_bc(excel_file=&ExcelFile, type=dm, package=&package, out_folder=&TargetFolder, range=%str(BC_DM));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=vs, package=&package, out_folder=&TargetFolder, range=%str(BC_VS));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=lb, package=&package, out_folder=&TargetFolder, range=%str(BC_LB));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=mb, package=&package, out_folder=&TargetFolder, range=%str(BC_MB));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=ae, package=&package, out_folder=&TargetFolder, range=%str(BC_AE));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=mh, package=&package, out_folder=&TargetFolder, range=%str(BC_MH));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=cm, package=&package, out_folder=&TargetFolder, range=%str(BC_CM));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=re, package=&package, out_folder=&TargetFolder, range=%str(BC_RE));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=pr, package=&package, out_folder=&TargetFolder, range=%str(BC_PR));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=be, package=&package, out_folder=&TargetFolder, range=%str(BC_BE));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=eg, package=&package, out_folder=&TargetFolder, range=%str(BC_EG));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=ds, package=&package, out_folder=&TargetFolder, range=%str(BC_DS));

*/


/*
%let package=20230706;
%let folder=20230706_oncology;
%let ExcelFile=&root/curation/BC_Package_R4_Oncology_RECIST11_2023_07_06.xlsx;
%let TargetFolder=&root/yaml/&folder/bc;

%generate_yaml_from_bc(excel_file=&ExcelFile, type=recist, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(BC TU_TR_RS));

%let package=20230706;
%let folder=20230706_nononco;
%let ExcelFile=&root/curation/BC_Package_R4_2023_07_06.xlsx;
%let TargetFolder=&root/yaml/&folder/bc;

%generate_yaml_from_bc(excel_file=&ExcelFile, type=ae, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(BC_AE));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=be, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(BC_BE));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=be_edits, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(BC_BE_EDITS));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=ds, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(BC_DS));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=eg, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(BC_EG));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=eg_edits, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(BC_EG_EDITS));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=lb, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(BC_LB_(TIG)_Biomarkers));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=lb_edits, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(BC_LB_EDITS));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=mh, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(BC_MH));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=pr_edits, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(BC_PR_EDITS));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=vs_edits, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(BC_VS_EDITS));
*/

/*
%let package=20231003;
%let folder=20231003_r5;
%let ExcelFile=&root/curation/BC_Package_R5_LZZT.xlsx;
%let TargetFolder=&root/yaml/&folder/bc;

%generate_yaml_from_bc(excel_file=&ExcelFile, type=ae_edits, package=&package, override_package_date=%str(2023-10-03), out_folder=&TargetFolder, range=%str(BC_AE_EDITS));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=cm_edits, package=&package, override_package_date=%str(2023-10-03), out_folder=&TargetFolder, range=%str(BC_CM_EDITS));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=ds_edits, package=&package, override_package_date=%str(2023-10-03), out_folder=&TargetFolder, range=%str(BC_DS_EDITS));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=ec, package=&package, override_package_date=%str(2023-10-03), out_folder=&TargetFolder, range=%str(BC_EC));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=lb, package=&package, override_package_date=%str(2023-10-03), out_folder=&TargetFolder, range=%str(BC_LB));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=lb_edits, package=&package, override_package_date=%str(2023-10-03), out_folder=&TargetFolder, range=%str(BC_LB_EDITS));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=mb, package=&package, override_package_date=%str(2023-10-03), out_folder=&TargetFolder, range=%str(BC_MB));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=mh_edits, package=&package, override_package_date=%str(2023-10-03), out_folder=&TargetFolder, range=%str(BC_MH_EDITS));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=pr_edits, package=&package, override_package_date=%str(2023-10-03), out_folder=&TargetFolder, range=%str(BC_PR_EDITS));
*/

/*
%let package=20231212;
%let folder=20231212_r6;
%let ExcelFile=&root/curation/BC_Package_R6_LZZT.xlsx;
%let TargetFolder=&root/yaml/&folder/bc;

%generate_yaml_from_bc(excel_file=&ExcelFile, type=cm_edits, package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, range=%str(BC_CM_EDITS));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=ds,       package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, range=%str(BC_DS));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=eg_edits, package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, range=%str(BC_EG_EDITS));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=ex,       package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, range=%str(BC_EX));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=ie,       package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, range=%str(BC_IE));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=lb,       package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, range=%str(BC_LB));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=lb_edits, package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, range=%str(BC_LB_EDITS));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=mh_edits, package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, range=%str(BC_MH_EDITS));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=pr,       package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, range=%str(BC_PR));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=qs,       package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, range=%str(BC_QS));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=sc,       package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, range=%str(BC_SC));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=su,       package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, range=%str(BC_SU));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=vs_edits, package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, range=%str(BC_VS_EDITS));

%let package=20240402;
%let folder=20240402_r7;
%let TargetFolder=&root/yaml/&folder/bc;
%let OverrideDate=%str(2024-04-02);

%let ExcelFile=&root/curation/BC_Package_R7_GF.xlsx;
%generate_yaml_from_bc(excel_file=&ExcelFile, type=bc_gf, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_GF));

%let ExcelFile=&root/curation/BC_Package_R7_FACV.xlsx;
%generate_yaml_from_bc(excel_file=&ExcelFile, type=bc_facv, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_FACV));

%let ExcelFile=&root/curation/BC_Package_R7_DD.xlsx;
%generate_yaml_from_bc(excel_file=&ExcelFile, type=bc_dd, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_DD));

%let ExcelFile=&root/curation/BC_Package_R7_BC_updates.xlsx;
%generate_yaml_from_bc(excel_file=&ExcelFile, type=bc_updates, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(Biomedical Concepts));
*/

%let package=20240627;
%let folder=20240627_r8;
%let TargetFolder=&root/yaml/&folder/bc;
%let OverrideDate=%str(2024-06-27);

%let ExcelFile=&root/curation/draft/BC_Package_R8_LUGANO_RS.xlsx;
%generate_yaml_from_bc(excel_file=&ExcelFile, type=rs_lugano, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_RS));

%let ExcelFile=&root/curation/draft/BC_Package_R8_RANO_RS.xlsx;
%generate_yaml_from_bc(excel_file=&ExcelFile, type=rs_rano, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_RS));

%let ExcelFile=&root/curation/draft/BC_Package_R8_BC_updates.xlsx;
%generate_yaml_from_bc(excel_file=&ExcelFile, type=updates1, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_Onco_Corrections));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=updates2, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_New));

ods listing close;
ods html5 file="&root/utilities/reports/convert_bc_xlsx2yaml_issues_&todays..html";
ods excel options(sheet_name="BC_&package" flow="tables" autofilter = 'all') file="&root/utilities/reports/convert_bc_xlsx2yaml_issues_&todays..xlsx";

proc print data=all_issues_bc;
  title "BC Issues - &todays";
  var _excel_file_ _tab_ package_date severity BC_ID short_name dec_id dec_label issue_type expected_value actual_value comment;
run;

ods listing;
ods html5 close;
ods excel close;  