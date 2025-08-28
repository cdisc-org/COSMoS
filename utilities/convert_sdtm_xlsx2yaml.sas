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
%let excel_file=&root/curation/package01/BC_Package_2022_10_26.xlsx;
%let TargetFolder=&root/yaml/&folder/sdtm;

%get_Subset_Codelists(file=&excel_file, range=Subset Codelist Example$, dsout=subsets);

%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=vs, package=20221026, out_folder=&TargetFolder, range=SDTM VS BC, subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=lb, package=20221026, out_folder=&TargetFolder, range=%str(SDTM LB BC), subsetsDS=subsets);



%let package=20230213;
%let folder=20230213;
%let excel_file=&root/curation/package02/BC_Package_2023_02_13.xlsx;
%let TargetFolder=&root/yaml/&folder/sdtm;

%get_Subset_Codelists(file=&excel_file, range=Subset Codelists$, dsout=subsets);

%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=lb_1, package=&package, out_folder=&TargetFolder, range=%str(SDTM LB), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=lb_2, package=&package, out_folder=&TargetFolder, range=%str(SDTM LB (TIG Biomarkers)), subsetsDS=subsets);
*/


/*
%let package=20230706;
%let folder=20230706_oncology;
%let excel_file=&root/curation/package04/BC_Package_R4_Oncology_RECIST11_2023_07_06.xlsx;
%let TargetFolder=&root/yaml/&folder/sdtm;

%get_Subset_Codelists(file=&excel_file, range=Subset Codelist Example$, dsout=subsets);

%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=recist_tu, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_TU), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=recist_tr, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_TR), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=recist_rs, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_RS), subsetsDS=subsets);



%let package=20230706;
%let folder=20230706_nononco;
%let excel_file=&root/curation/package04/BC_Package_R4_2023_07_06.xlsx;
%let TargetFolder=&root/yaml/&folder/sdtm;

%get_Subset_Codelists(file=&excel_file, range=Subset Codelist Example$, dsout=subsets);

%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=ae, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_AE), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=be, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_BE), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=ds, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_DS), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=eg, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_EG), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=lb, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_LB), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=lb_edits, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_LB_EDITS), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=lb_edits2, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_LB_EDITS_2), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=mb, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_MB), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=mh, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_MH), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=pr, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_PR), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=vs, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_VS), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=vs_edits, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_VS_EDITS), subsetsDS=subsets);

%let package=20231003;
%let folder=20231003_r5;
%let excel_file=&root/curation/package05/BC_Package_R5_LZZT.xlsx;
%let TargetFolder=&root/yaml/&folder/sdtm;

%get_Subset_Codelists(file=&excel_file, range=Subset Codelist Example$, dsout=subsets);

%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=ae_edits, package=&package, override_package_date=%str(2023-10-03), out_folder=&TargetFolder, range=%str(SDTM_AE_EDITS), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=cm, package=&package, override_package_date=%str(2023-10-03), out_folder=&TargetFolder, range=%str(SDTM_CM), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=ds_edits, package=&package, override_package_date=%str(2023-10-03), out_folder=&TargetFolder, range=%str(SDTM_DS_EDITS), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=ec, package=&package, override_package_date=%str(2023-10-03), out_folder=&TargetFolder, range=%str(SDTM_EC), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=lb, package=&package, override_package_date=%str(2023-10-03), out_folder=&TargetFolder, range=%str(SDTM_LB), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=lb_edits, package=&package, override_package_date=%str(2023-10-03), out_folder=&TargetFolder, range=%str(SDTM_LB_EDITS), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=mb, package=&package, override_package_date=%str(2023-10-03), out_folder=&TargetFolder, range=%str(SDTM_MB), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=mh, package=&package, override_package_date=%str(2023-10-03), out_folder=&TargetFolder, range=%str(SDTM_MH), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=pr_edits, package=&package, override_package_date=%str(2023-10-03), out_folder=&TargetFolder, range=%str(SDTM_PR_EDITS), subsetsDS=subsets);

%let package=20231212;
%let folder=20231212_r6;
%let excel_file=&root/curation/package06/BC_Package_R6_LZZT.xlsx;
%let TargetFolder=&root/yaml/&folder/sdtm;

%get_Subset_Codelists(file=&excel_file, range=Subset Codelist Example$, dsout=subsets);

%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=cm_edits, package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_CM_EDITS));
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=ds,       package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_DS));
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=eg_edits, package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_EG_EDITS));
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=ex,       package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_EX));
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=ie,       package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_IE));
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=lb,       package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_LB));
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=lb_edits, package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_LB_EDITS));
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=mh,       package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_MH));
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=pr,       package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_PR));
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=qs,       package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_QS));
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=sc,       package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_SC));
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=su,       package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_SU));
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=vs_edits, package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_VS_EDITS));
*/

/*
%let excel_file=&root/curation/package06/BC_Package_R6_LZZT.xlsx;
%get_Subset_Codelists(file=&excel_file, range=Subset Codelist Example$, dsout=subsets);

%let package=20240402;
%let folder=20240402_r7;
%let TargetFolder=&root/yaml/&folder/sdtm;
%let OverrideDate=%str(2024-04-02);

%let checkrelationships=0;
%let excel_file=&root/curation/package07/BC_Package_R7_GF.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=sdtm_gf, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_GF), debug=0, check_relationships=&checkrelationships);

%let checkrelationships=0;
%let excel_file=&root/curation/package07/BC_Package_R7_FACV.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=sdtm_facv, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_FACV), debug=0, check_relationships=&checkrelationships);

%let checkrelationships=1;
%let excel_file=&root/curation/package07/BC_Package_R7_DD.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=sdtm_dd, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_DD), debug=0, check_relationships=&checkrelationships);

%let checkrelationships=0;
%let excel_file=&root/curation/package07/BC_Package_R7_SDTM_updates.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=sdtm_updates, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM Dataset Specializations), debug=0, check_relationships=&checkrelationships);
*/

/*
%let excel_file=&root/curation/package06/BC_Package_R6_LZZT.xlsx;
%get_Subset_Codelists(file=&excel_file, range=Subset Codelist Example$, dsout=subsets);

%let package=20240627;
%let folder=20240627_r8;
%let TargetFolder=&root/yaml/&folder/sdtm;
%let OverrideDate=%str(2024-06-27);

%let checkrelationships=1;
%let excel_file=&root/curation/package08/BC_Package_R8_LUGANO_RS.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=rs_lugano, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_RS), debug=0, check_relationships=&checkrelationships);

%let checkrelationships=1;
%let excel_file=&root/curation/package08/BC_Package_R8_RANO_RS.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=rs_rano, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_RS), debug=0, check_relationships=&checkrelationships);

%let checkrelationships=1;
%let excel_file=&root/curation/package08/BC_Package_R8_SDTM_updates.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=updates1, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_Corrections), debug=0, check_relationships=&checkrelationships);
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=updates2, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_Corrections_1), debug=0, check_relationships=&checkrelationships);
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=updates3, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_Corrections_2), debug=0, check_relationships=&checkrelationships);
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=updates4, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_New), debug=0, check_relationships=&checkrelationships);
*/

/*
%let excel_file=&root/curation/package06/BC_Package_R6_LZZT.xlsx;
%get_Subset_Codelists(file=&excel_file, range=Subset Codelist Example$, dsout=subsets);

%let release=9;
%let package=20241216;
%let folder=20241216_r9;
%let TargetFolder=&root/yaml/&folder/sdtm;
%let OverrideDate=%str(2024-12-16);

%let checkrelationships=0;
%let excel_file=&root/curation/package09/BC_Package_R9_public_review_updates.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=pr_updates, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_Corrections), debug=0, check_relationships=&checkrelationships);
*/

/*
%let excel_file=&root/curation/package06/BC_Package_R6_LZZT.xlsx;
%get_Subset_Codelists(file=&excel_file, range=Subset Codelist Example$, dsout=subsets);

%let release=10;
%let package=20241217;
%let folder=20241217_r10;
%let TargetFolder=&root/yaml/&folder/sdtm;
%let OverrideDate=%str(2024-12-17);

%let checkrelationships=0;
%let excel_file=&root/curation/package10/BC_Package_R10.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=rp, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_RP), debug=0, check_relationships=&checkrelationships);
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=sr, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_SR), debug=0, check_relationships=&checkrelationships);

%let excel_file=&root/curation/package10/BC_Package_R10_Breast_Cancer.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=mi, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_MI), debug=0, check_relationships=&checkrelationships);
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=pr, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_PR), debug=0, check_relationships=&checkrelationships);
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=cm, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_CM), debug=0, check_relationships=&checkrelationships);

%let excel_file=&root/curation/package10/BC_Package_R10_ECG_SDTM.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=eg, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_EG), debug=1, check_relationships=&checkrelationships);
*/

/*
%let excel_file=&root/curation/package06/BC_Package_R6_LZZT.xlsx;
%get_Subset_Codelists(file=&excel_file, range=Subset Codelist Example$, dsout=subsets);

%let release=11;
%let package=20250401;
%let folder=20250401_r11;
%let TargetFolder=&root/yaml/&folder/sdtm;
%let OverrideDate=%str(2025-04-01);

%let checkrelationships=1;

%let excel_file=&root/curation/package11/BC_Package_R11_UR.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=ur, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_UR), debug=0, check_relationships=&checkrelationships);

%let excel_file=&root/curation/package11/BC_Package_R11_LB_GF_Edits.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=lb, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_LB), debug=0, check_relationships=&checkrelationships);
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=gf, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_GF), debug=0, check_relationships=&checkrelationships);

%let excel_file=&root/curation/package11/BC_Package_R11_DM.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=dm, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_DM), debug=0, check_relationships=&checkrelationships);

%let excel_file=&root/curation/package11/BC_Package_R11_MK.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=mk, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_MK), debug=0, check_relationships=&checkrelationships);

%let excel_file=&root/curation/package11/BC_Package_R11_VS.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=vs, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_VS), debug=0, check_relationships=&checkrelationships);

%let excel_file=&root/curation/package11/BC_Package_R11_AE_Edit.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=ae, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_AE), debug=0, check_relationships=&checkrelationships);
*/

/*
%let excel_file=&root/curation/package06/BC_Package_R6_LZZT.xlsx;
%get_Subset_Codelists(file=&excel_file, range=Subset Codelist Example$, dsout=subsets);

%let release=12;
%let package=20250701;
%let folder=20250701_r12;
%let TargetFolder=&root/yaml/&folder/sdtm;
%let OverrideDate=%str(2025-07-01);

%let checkrelationships=1;

%let excel_file=&root/curation/package12/R12_BC_SDTM_QRS_6MWT.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=smwt, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_6MWT), debug=0, check_relationships=&checkrelationships);

%let excel_file=&root/curation/package12/R12_LB.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=lb, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_LB_EDITS), debug=0, check_relationships=&checkrelationships);

%let excel_file=&root/curation/package12/R12_SDTM_Misc.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=brth, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_brthdtc_new), debug=0, check_relationships=&checkrelationships);
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=liph, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_linking_phrase_edits), debug=0, check_relationships=&checkrelationships);
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=edits, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_Edits), debug=0, check_relationships=&checkrelationships);

%let excel_file=&root/curation/package12/R12_TS.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=ts, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_TS), debug=0, check_relationships=&checkrelationships);

%let excel_file=&root/curation/package12/R12_BC_SDTM_LB_Japan_Group.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=lb, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(NEW_SDTM_LAB_2025.04.24), debug=0, check_relationships=&checkrelationships);

%let excel_file=&root/curation/package12/R12_BC_SDTM_MK_Part2.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=mk, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_MK), debug=0, check_relationships=&checkrelationships);
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=mk, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_MK_Edits), debug=0, check_relationships=&checkrelationships);

%let excel_file=&root/curation/package12/R12_BC_SDTM_QRS_APACHE.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=apache, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_APACHE II), debug=0, check_relationships=&checkrelationships);

%let excel_file=&root/curation/package12/R12_BC_SDTM_QRS_AIMS.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=aims, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_AIMS), debug=0, check_relationships=&checkrelationships);

%let excel_file=&root/curation/package12/R12_BC_SDTM_QRS_ADAS-Cog.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=adas, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_ADAS-Cog), debug=0, check_relationships=&checkrelationships);

%let excel_file=&root/curation/package12/R12_SDTM_EC_Linking_Edits.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=ec, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_EC_EDITS), debug=0, check_relationships=&checkrelationships);

%let excel_file=&root/curation/package12/R12_BC_SDTM_MH_AE_CM_SU.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=misc, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_MH_AE_CM_SU), debug=0, check_relationships=&checkrelationships);

%let excel_file=&root/curation/package12/R12_SDTM_TU_TULOC_Linking_Edits.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=tu, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_TU), debug=0, check_relationships=&checkrelationships);

%let excel_file=&root/curation/package12/R12_BC_SDTM_GF.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=gf, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_GF), debug=0, check_relationships=&checkrelationships);

%let excel_file=&root/curation/package12/R12_BC_SDTM_QRS_ATLAS.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=atlas, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_ATLAS), debug=0, check_relationships=&checkrelationships);

%let excel_file=&root/curation/package12/R12_BC_SDTM_QRS_HAM-A.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=ham-a, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_HAM-A), debug=0, check_relationships=&checkrelationships);

%let excel_file=&root/curation/package12/R12_BC_SDTM_QRS_KFSS.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=kfss, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_KFSS), debug=0, check_relationships=&checkrelationships);

%let excel_file=&root/curation/package12/R12_BC_SDTM_QRS_EQ5D.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=eq5d, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_EQ5D5L), debug=0, check_relationships=&checkrelationships);

%let excel_file=&root/curation/package12/R12_BC_SDTM_DILI.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=lb_dili, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_DILI_NEW), debug=0, check_relationships=&checkrelationships);

%let excel_file=&root/curation/package12/R12_BC_SDTM_QRS_KPS.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=kps, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_KPS), debug=0, check_relationships=&checkrelationships);
*/

%let excel_file=&root/curation/package06/BC_Package_R6_LZZT.xlsx;
%get_Subset_Codelists(file=&excel_file, range=Subset Codelist Example$, dsout=subsets);

%let release=13;
%let package=20250923;
%let folder=20250923_r13;
%let TargetFolder=&root/yaml/&folder/sdtm;
%let OverrideDate=%str(2025-09-23);

%let checkrelationships=1;

%let excel_file=&root/curation/draft/package13/R13_BC_SDTM_Edits.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_SC_EDITS), debug=0, check_relationships=&checkrelationships);

%let excel_file=&root/curation/draft/package13/R13_BC_SDTM_QRS_ADAS-Cog_FT.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_ADAS-Cog), debug=0, check_relationships=&checkrelationships);

%let excel_file=&root/curation/draft/package13/R13_BC_SDTM_QRS_CES.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_CES), debug=0, check_relationships=&checkrelationships);

%let excel_file=&root/curation/draft/package13/R13_BC_SDTM_QRS_ECOG.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_ECOG), debug=0, check_relationships=&checkrelationships);

%let excel_file=&root/curation/draft/package13/R13_BC_SDTM_QRS_rutgeerts.xlsx;
%generate_yaml_from_bc_sdtm(excel_file=&excel_file, type=, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, subsetsDS=subsets, range=%str(SDTM_RUTGEERTS), debug=0, check_relationships=&checkrelationships);

/************************************************************************************************************************/

ods listing close;
ods html5 file="&root/utilities/reports/convert_sdtm_xlsx2yaml_issues_R&release._&todays..html";
ods excel options(sheet_name="SDTM_&package" flow="tables" autofilter = 'all') file="&root/utilities/reports/convert_sdtm_xlsx2yaml_issues_R&release._&todays..xlsx";

proc print data=all_issues_sdtm;
  title "SDTM Specialization Issues - &todays";
  var _excel_file_ _tab_ package_date severity vlm_group_id sdtm_variable issue_type expected_value actual_value comment;
run;

ods listing;
ods html5 close;
ods excel close;

proc delete data=work.all_issues_sdtm work.subsets;
run;
