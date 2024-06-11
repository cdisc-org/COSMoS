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


/*
%let package=20221026;
%let folder=20221026;
%let Excelfile=&root/curation/BC_Package_2022_10_26.xlsx;
%let TargetFolder=&root/yaml/&folder/sdtm;

%get_Subset_Codelists(file=&Excelfile, range=Subset Codelist Example$, dsout=subsets);

%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=vs, package=20221026, out_folder=&TargetFolder, range=SDTM VS BC, subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=lb, package=20221026, out_folder=&TargetFolder, range=%str(SDTM LB BC), subsetsDS=subsets);



%let package=20230213;
%let folder=20230213;
%let Excelfile=&root/curation/BC_Package_2023_02_13.xlsx;
%let TargetFolder=&root/yaml/&folder/sdtm;

%get_Subset_Codelists(file=&Excelfile, range=Subset Codelists$, dsout=subsets);

%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=lb_1, package=&package, out_folder=&TargetFolder, range=%str(SDTM LB), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=lb_2, package=&package, out_folder=&TargetFolder, range=%str(SDTM LB (TIG Biomarkers)), subsetsDS=subsets);
*/


/*
%let package=20230706;
%let folder=20230706_oncology;
%let Excelfile=&root/curation/BC_Package_R4_Oncology_RECIST11_2023_07_06.xlsx;
%let TargetFolder=&root/yaml/&folder/sdtm;

%get_Subset_Codelists(file=&Excelfile, range=Subset Codelist Example$, dsout=subsets);

%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=recist_tu, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_TU), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=recist_tr, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_TR), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=recist_rs, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_RS), subsetsDS=subsets);



%let package=20230706;
%let folder=20230706_nononco;
%let ExcelFile=&root/curation/BC_Package_R4_2023_07_06.xlsx;
%let TargetFolder=&root/yaml/&folder/sdtm;

%get_Subset_Codelists(file=&Excelfile, range=Subset Codelist Example$, dsout=subsets);

%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=ae, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_AE), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=be, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_BE), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=ds, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_DS), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=eg, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_EG), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=lb, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_LB), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=lb_edits, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_LB_EDITS), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=lb_edits2, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_LB_EDITS_2), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=mb, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_MB), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=mh, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_MH), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=pr, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_PR), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=vs, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_VS), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=vs_edits, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_VS_EDITS), subsetsDS=subsets);

%let package=20231003;
%let folder=20231003_r5;
%let ExcelFile=&root/curation/BC_Package_R5_LZZT.xlsx;
%let TargetFolder=&root/yaml/&folder/sdtm;

%get_Subset_Codelists(file=&Excelfile, range=Subset Codelist Example$, dsout=subsets);

%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=ae_edits, package=&package, override_package_date=%str(2023-10-03), out_folder=&TargetFolder, range=%str(SDTM_AE_EDITS), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=cm, package=&package, override_package_date=%str(2023-10-03), out_folder=&TargetFolder, range=%str(SDTM_CM), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=ds_edits, package=&package, override_package_date=%str(2023-10-03), out_folder=&TargetFolder, range=%str(SDTM_DS_EDITS), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=ec, package=&package, override_package_date=%str(2023-10-03), out_folder=&TargetFolder, range=%str(SDTM_EC), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=lb, package=&package, override_package_date=%str(2023-10-03), out_folder=&TargetFolder, range=%str(SDTM_LB), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=lb_edits, package=&package, override_package_date=%str(2023-10-03), out_folder=&TargetFolder, range=%str(SDTM_LB_EDITS), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=mb, package=&package, override_package_date=%str(2023-10-03), out_folder=&TargetFolder, range=%str(SDTM_MB), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=mh, package=&package, override_package_date=%str(2023-10-03), out_folder=&TargetFolder, range=%str(SDTM_MH), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=pr_edits, package=&package, override_package_date=%str(2023-10-03), out_folder=&TargetFolder, range=%str(SDTM_PR_EDITS), subsetsDS=subsets);

%let package=20231212;
%let folder=20231212_r6;
%let ExcelFile=&root/curation/BC_Package_R6_LZZT.xlsx;
%let TargetFolder=&root/yaml/&folder/sdtm;

%get_Subset_Codelists(file=&Excelfile, range=Subset Codelist Example$, dsout=subsets);

%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=cm_edits, package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_CM_EDITS));
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=ds,       package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_DS));
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=eg_edits, package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_EG_EDITS));
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=ex,       package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_EX));
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=ie,       package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_IE));
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=lb,       package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_LB));
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=lb_edits, package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_LB_EDITS));
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=mh,       package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_MH));
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=pr,       package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_PR));
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=qs,       package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_QS));
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=sc,       package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_SC));
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=su,       package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_SU));
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=vs_edits, package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_VS_EDITS));
*/

/*
%let ExcelFile=&root/curation/BC_Package_R6_LZZT.xlsx;
%get_Subset_Codelists(file=&Excelfile, range=Subset Codelist Example$, dsout=subsets);

%let package=20240402;
%let folder=20240402_r7;
%let TargetFolder=&root/yaml/&folder/sdtm;
%let OverrideDate=%str(2024-04-02);

%let checkrelationships=0;
%let ExcelFile=&root/curation/BC_Package_R7_GF.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=sdtm_gf, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_GF), debug=0, check_relationships=&checkrelationships);

%let checkrelationships=0;
%let ExcelFile=&root/curation/BC_Package_R7_FACV.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=sdtm_facv, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_FACV), debug=0, check_relationships=&checkrelationships);

%let checkrelationships=1;
%let ExcelFile=&root/curation/BC_Package_R7_DD.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=sdtm_dd, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_DD), debug=0, check_relationships=&checkrelationships);

%let checkrelationships=0;
%let ExcelFile=&root/curation/BC_Package_R7_SDTM_updates.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=sdtm_updates, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM Dataset Specializations), debug=0, check_relationships=&checkrelationships);
*/

%let ExcelFile=&root/curation/BC_Package_R6_LZZT.xlsx;
%get_Subset_Codelists(file=&Excelfile, range=Subset Codelist Example$, dsout=subsets);

%let package=20240627;
%let folder=20240627_r8;
%let TargetFolder=&root/yaml/&folder/sdtm;
%let OverrideDate=%str(2024-06-27);

%let checkrelationships=1;
%let ExcelFile=&root/curation/draft/BC_Package_R8_LUGANO_RS.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=rs_lugano, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_RS), debug=0, check_relationships=&checkrelationships);

%let checkrelationships=1;
%let ExcelFile=&root/curation/draft/BC_Package_R8_RANO_RS.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=rs_rano, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_RS), debug=0, check_relationships=&checkrelationships);

%let checkrelationships=1;
%let ExcelFile=&root/curation/draft/BC_Package_R8_SDTM_updates.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=updates1, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_Corrections), debug=0, check_relationships=&checkrelationships);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=updates2, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_Corrections_1), debug=0, check_relationships=&checkrelationships);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=updates3, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_Corrections_2), debug=0, check_relationships=&checkrelationships);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=updates4, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_New), debug=0, check_relationships=&checkrelationships);


ods listing close;
ods html5 file="&root/utilities/reports/convert_sdtm_xlsx2yaml_issues_&todays..html";
ods excel options(sheet_name="SDTM_&package" flow="tables" autofilter = 'all') file="&root/utilities/reports/convert_sdtm_xlsx2yaml_issues_&todays..xlsx";

proc print data=all_issues_sdtm;
  title "SDTM Specialization Issues - &todays";
  var _excel_file_ _tab_ package_date severity vlm_group_id sdtm_variable issue_type expected_value actual_value comment;
run;

ods listing;
ods html5 close;
ods excel close;  
