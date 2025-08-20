%let root=C:/_github/cdisc-org/COSMoS;
%include "&root/utilities/config.sas";

%let _debug=0;

%create_template(type=BC_ISSUE, out=work.all_issues_bc);


/*
%let package=20221026;
%let folder=20221026;
%let excel_file=&root/curation/package01/BC_Package_2022_10_26.xlsx;
%let TargetFolder=&root/yaml/&folder/bc;

%generate_yaml_from_bc(excel_file=&excel_file, type=vs, package=20221026, out_folder=&TargetFolder, range=Conceptual VS BC);
%generate_yaml_from_bc(excel_file=&excel_file, type=lb, package=20221026, out_folder=&TargetFolder, range=%str(Conceptual LB (Common) BC));



%let package=20230213;
%let folder=20230213;
%let excel_file=&root/curation/package02/BC_Package_2023_02_13.xlsx;
%let TargetFolder=&root/yaml/&package/bc;

%generate_yaml_from_bc(excel_file=&excel_file, type=lb_1, package=&package, out_folder=&TargetFolder, range=%str(BC LB (Common)));
%generate_yaml_from_bc(excel_file=&excel_file, type=lb_2, package=&package, out_folder=&TargetFolder, range=%str(BC LB (TIG Biomarkers)));


%let package=20230331;
%let folder=20230331;
%let excel_file=&root/curation/package03/BC_Package_2023_03_31.xlsx;
%let TargetFolder=&root/yaml/&folder/bc;

%generate_yaml_from_bc(excel_file=&excel_file, type=dm, package=&package, out_folder=&TargetFolder, range=%str(BC_DM));
%generate_yaml_from_bc(excel_file=&excel_file, type=vs, package=&package, out_folder=&TargetFolder, range=%str(BC_VS));
%generate_yaml_from_bc(excel_file=&excel_file, type=lb, package=&package, out_folder=&TargetFolder, range=%str(BC_LB));
%generate_yaml_from_bc(excel_file=&excel_file, type=mb, package=&package, out_folder=&TargetFolder, range=%str(BC_MB));
%generate_yaml_from_bc(excel_file=&excel_file, type=ae, package=&package, out_folder=&TargetFolder, range=%str(BC_AE));
%generate_yaml_from_bc(excel_file=&excel_file, type=mh, package=&package, out_folder=&TargetFolder, range=%str(BC_MH));
%generate_yaml_from_bc(excel_file=&excel_file, type=cm, package=&package, out_folder=&TargetFolder, range=%str(BC_CM));
%generate_yaml_from_bc(excel_file=&excel_file, type=re, package=&package, out_folder=&TargetFolder, range=%str(BC_RE));
%generate_yaml_from_bc(excel_file=&excel_file, type=pr, package=&package, out_folder=&TargetFolder, range=%str(BC_PR));
%generate_yaml_from_bc(excel_file=&excel_file, type=be, package=&package, out_folder=&TargetFolder, range=%str(BC_BE));
%generate_yaml_from_bc(excel_file=&excel_file, type=eg, package=&package, out_folder=&TargetFolder, range=%str(BC_EG));
%generate_yaml_from_bc(excel_file=&excel_file, type=ds, package=&package, out_folder=&TargetFolder, range=%str(BC_DS));

*/


/*
%let package=20230706;
%let folder=20230706_oncology;
%let excel_file=&root/curation/package04/BC_Package_R4_Oncology_RECIST11_2023_07_06.xlsx;
%let TargetFolder=&root/yaml/&folder/bc;

%generate_yaml_from_bc(excel_file=&excel_file, type=recist, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(BC TU_TR_RS));

%let package=20230706;
%let folder=20230706_nononco;
%let excel_file=&root/curation/package04/BC_Package_R4_2023_07_06.xlsx;
%let TargetFolder=&root/yaml/&folder/bc;

%generate_yaml_from_bc(excel_file=&excel_file, type=ae, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(BC_AE));
%generate_yaml_from_bc(excel_file=&excel_file, type=be, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(BC_BE));
%generate_yaml_from_bc(excel_file=&excel_file, type=be_edits, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(BC_BE_EDITS));
%generate_yaml_from_bc(excel_file=&excel_file, type=ds, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(BC_DS));
%generate_yaml_from_bc(excel_file=&excel_file, type=eg, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(BC_EG));
%generate_yaml_from_bc(excel_file=&excel_file, type=eg_edits, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(BC_EG_EDITS));
%generate_yaml_from_bc(excel_file=&excel_file, type=lb, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(BC_LB_(TIG)_Biomarkers));
%generate_yaml_from_bc(excel_file=&excel_file, type=lb_edits, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(BC_LB_EDITS));
%generate_yaml_from_bc(excel_file=&excel_file, type=mh, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(BC_MH));
%generate_yaml_from_bc(excel_file=&excel_file, type=pr_edits, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(BC_PR_EDITS));
%generate_yaml_from_bc(excel_file=&excel_file, type=vs_edits, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(BC_VS_EDITS));
*/

/*
%let package=20231003;
%let folder=20231003_r5;
%let excel_file=&root/curation/package05/BC_Package_R5_LZZT.xlsx;
%let TargetFolder=&root/yaml/&folder/bc;

%generate_yaml_from_bc(excel_file=&excel_file, type=ae_edits, package=&package, override_package_date=%str(2023-10-03), out_folder=&TargetFolder, range=%str(BC_AE_EDITS));
%generate_yaml_from_bc(excel_file=&excel_file, type=cm_edits, package=&package, override_package_date=%str(2023-10-03), out_folder=&TargetFolder, range=%str(BC_CM_EDITS));
%generate_yaml_from_bc(excel_file=&excel_file, type=ds_edits, package=&package, override_package_date=%str(2023-10-03), out_folder=&TargetFolder, range=%str(BC_DS_EDITS));
%generate_yaml_from_bc(excel_file=&excel_file, type=ec, package=&package, override_package_date=%str(2023-10-03), out_folder=&TargetFolder, range=%str(BC_EC));
%generate_yaml_from_bc(excel_file=&excel_file, type=lb, package=&package, override_package_date=%str(2023-10-03), out_folder=&TargetFolder, range=%str(BC_LB));
%generate_yaml_from_bc(excel_file=&excel_file, type=lb_edits, package=&package, override_package_date=%str(2023-10-03), out_folder=&TargetFolder, range=%str(BC_LB_EDITS));
%generate_yaml_from_bc(excel_file=&excel_file, type=mb, package=&package, override_package_date=%str(2023-10-03), out_folder=&TargetFolder, range=%str(BC_MB));
%generate_yaml_from_bc(excel_file=&excel_file, type=mh_edits, package=&package, override_package_date=%str(2023-10-03), out_folder=&TargetFolder, range=%str(BC_MH_EDITS));
%generate_yaml_from_bc(excel_file=&excel_file, type=pr_edits, package=&package, override_package_date=%str(2023-10-03), out_folder=&TargetFolder, range=%str(BC_PR_EDITS));
*/

/*
%let package=20231212;
%let folder=20231212_r6;
%let excel_file=&root/curation/package06/BC_Package_R6_LZZT.xlsx;
%let TargetFolder=&root/yaml/&folder/bc;

%generate_yaml_from_bc(excel_file=&excel_file, type=cm_edits, package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, range=%str(BC_CM_EDITS));
%generate_yaml_from_bc(excel_file=&excel_file, type=ds,       package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, range=%str(BC_DS));
%generate_yaml_from_bc(excel_file=&excel_file, type=eg_edits, package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, range=%str(BC_EG_EDITS));
%generate_yaml_from_bc(excel_file=&excel_file, type=ex,       package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, range=%str(BC_EX));
%generate_yaml_from_bc(excel_file=&excel_file, type=ie,       package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, range=%str(BC_IE));
%generate_yaml_from_bc(excel_file=&excel_file, type=lb,       package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, range=%str(BC_LB));
%generate_yaml_from_bc(excel_file=&excel_file, type=lb_edits, package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, range=%str(BC_LB_EDITS));
%generate_yaml_from_bc(excel_file=&excel_file, type=mh_edits, package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, range=%str(BC_MH_EDITS));
%generate_yaml_from_bc(excel_file=&excel_file, type=pr,       package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, range=%str(BC_PR));
%generate_yaml_from_bc(excel_file=&excel_file, type=qs,       package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, range=%str(BC_QS));
%generate_yaml_from_bc(excel_file=&excel_file, type=sc,       package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, range=%str(BC_SC));
%generate_yaml_from_bc(excel_file=&excel_file, type=su,       package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, range=%str(BC_SU));
%generate_yaml_from_bc(excel_file=&excel_file, type=vs_edits, package=&package, override_package_date=%str(2023-12-12), out_folder=&TargetFolder, range=%str(BC_VS_EDITS));
*/

/*
%let package=20240402;
%let folder=20240402_r7;
%let TargetFolder=&root/yaml/&folder/bc;
%let OverrideDate=%str(2024-04-02);

%let excel_file=&root/curation/package07/BC_Package_R7_GF.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=bc_gf, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_GF));

%let excel_file=&root/curation/package07/BC_Package_R7_FACV.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=bc_facv, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_FACV));

%let excel_file=&root/curation/package07/BC_Package_R7_DD.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=bc_dd, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_DD));

%let excel_file=&root/curation/package07/BC_Package_R7_BC_updates.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=bc_updates, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(Biomedical Concepts));
*/

/*
%let package=20240627;
%let folder=20240627_r8;
%let TargetFolder=&root/yaml/&folder/bc;
%let OverrideDate=%str(2024-06-27);

%let excel_file=&root/curation/package08/BC_Package_R8_LUGANO_RS.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=rs_lugano, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_RS));

%let excel_file=&root/curation/package08/BC_Package_R8_RANO_RS.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=rs_rano, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_RS));

%let excel_file=&root/curation/package08/BC_Package_R8_BC_updates.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=updates1, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_Onco_Corrections));
%generate_yaml_from_bc(excel_file=&excel_file, type=updates2, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_New));
*/

/*
%let release=9;
%let package=20241216;
%let folder=20241216_r9;
%let TargetFolder=&root/yaml/&folder/bc;
%let OverrideDate=%str(2024-12-16);

%let excel_file=&root/curation/package09/BC_Package_R9_public_review_updates.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=pr_updates, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_Corrections));
*/

/*
%let release=10;
%let package=20241217;
%let folder=20241217_r10;
%let TargetFolder=&root/yaml/&folder/bc;
%let OverrideDate=%str(2024-12-17);

%let excel_file=&root/curation/package10/BC_Package_R10.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=rp, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_RP));
%generate_yaml_from_bc(excel_file=&excel_file, type=sr, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_SR));

%let excel_file=&root/curation/package10/BC_Package_R10_Breast_Cancer.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=mi, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_MI));
%generate_yaml_from_bc(excel_file=&excel_file, type=pr, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_PR));

%let excel_file=&root/curation/package10/BC_Package_R10_ECG.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=eg, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_EG));
*/

/*
%let release=11;
%let package=20250401;
%let folder=20250401_r11;
%let TargetFolder=&root/yaml/&folder/bc;
%let OverrideDate=%str(2025-04-01);

%let excel_file=&root/curation/package11/BC_Package_R11_BC_Lindus Health.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=bc, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_Breast_Cancer));

%let excel_file=&root/curation/package11/BC_Package_R11_UR.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=ur, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_UR));

%let excel_file=&root/curation/package11/BC_Package_R11_LB_GF_Edits.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=lb, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_LB));
%generate_yaml_from_bc(excel_file=&excel_file, type=gf, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_GF));

%let excel_file=&root/curation/package11/BC_Package_R11_DM.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=dm, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_DM));

%let excel_file=&root/curation/package11/BC_Package_R11_MK.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=mk, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_MK));
*/


/*
%let release=12;
%let package=20250701;
%let folder=20250701_r12;
%let TargetFolder=&root/yaml/&folder/bc;
%let OverrideDate=%str(2025-07-01);

%let excel_file=&root/curation/package12/R12_BC_SDTM_QRS_6MWT.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=6mwt, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_6MWT));

%let excel_file=&root/curation/package12/R12_BC_New.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=bc, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_Test_Occurrence));
%generate_yaml_from_bc(excel_file=&excel_file, type=bc, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_BRTHDTC));

%let excel_file=&root/curation/package12/R12_BC_Edits.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=bc_edits, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_EDITS));
%generate_yaml_from_bc(excel_file=&excel_file, type=bc_edits, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_EDITS2));

%let excel_file=&root/curation/package12/R12_BC_IE.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=ie, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_IE));

%let excel_file=&root/curation/package12/R12_LB.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=lb, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_LB_EDITS));

%let excel_file=&root/curation/package12/R12_TS.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=ts, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_TS));

%let excel_file=&root/curation/package12/R12_BC_SDTM_QRS_ADAS-Cog.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=adas, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_ADAS-Cog));

%let excel_file=&root/curation/package12/R12_BC_Event_Occurrence.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=occ, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_Indicators));

%let excel_file=&root/curation/package12/R12_BC_SDTM_LB_Japan_Group.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=lb, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(NEW_BC_LAB_2025.04.24));

%let excel_file=&root/curation/package12/R12_BC_SDTM_MK_Part2.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=mk, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_MK));
%generate_yaml_from_bc(excel_file=&excel_file, type=mk, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_MK_Edits));

%let excel_file=&root/curation/package12/R12_BC_SDTM_QRS_APACHE.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=apache, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_APACHE II));

%let excel_file=&root/curation/package12/R12_BC_SDTM_QRS_AIMS.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=aims, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_AIMS));

%let excel_file=&root/curation/package12/R12_BC_SDTM_MH_AE_CM_SU.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=various, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_MH_AE_CM_SU));

%let excel_file=&root/curation/package12/R12_BC_SDTM_GF.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=gf, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_GF));

%let excel_file=&root/curation/package12/R12_BC_SDTM_QRS_ATLAS.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=atlas, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_ATLAS));

%let excel_file=&root/curation/package12/R12_BC_SDTM_QRS_HAM-A.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=ham-a, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_HAM-A));

%let excel_file=&root/curation/package12/R12_BC_QRS.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=qrs, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_QRS));

%let excel_file=&root/curation/package12/R12_BC_SDTM_QRS_KFSS.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=kfss, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_KFSS));

%let excel_file=&root/curation/package12/R12_BC_SDTM_QRS_EQ5D.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=eq5d, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_EQ5D5L));

%let excel_file=&root/curation/package12/R12_BC_SDTM_DILI.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=lb_dili, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_DILI_EDITS_NEW));

%let excel_file=&root/curation/package12/R12_BC_SDTM_QRS_KPS.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=kps, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_KPS));
*/

%let release=13;
%let package=20250923;
%let folder=20250923_r13;
%let TargetFolder=&root/yaml/&folder/bc;
%let OverrideDate=%str(2025-09-23);

%let excel_file=&root/curation/draft/package13/R13_BC_SDTM_Edits.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_NEW));
%generate_yaml_from_bc(excel_file=&excel_file, type=, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_EDITS));

%let excel_file=&root/curation/draft/package13/R13_BC_SDTM_QRS_ADAS-Cog_FT.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_ADAS-Cog TotalScore));

%let excel_file=&root/curation/draft/package13/R13_BC_QRS_CGI.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_CGI));

%let excel_file=&root/curation/draft/package13/R13_BC_QRS_PGI.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_PGI));

%let excel_file=&root/curation/draft/package13/R13_BC_SDTM_QRS_CES.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_CES));

%let excel_file=&root/curation/draft/package13/R13_BC_SDTM_QRS_ECOG.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_ECOG));

%let excel_file=&root/curation/draft/package13/R13_BC_SDTM_QRS_rutgeerts.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_RUTGEERTS));


/************************************************************************************************************************/

ods listing close;
ods html5 file="&root/utilities/reports/convert_bc_xlsx2yaml_issues_R&release._&todays..html";
ods excel options(sheet_name="BC_&package" flow="tables" autofilter = 'all') file="&root/utilities/reports/convert_bc_xlsx2yaml_issues_R&release._&todays..xlsx";

proc print data=all_issues_bc;
  title "BC Issues - &todays";
  var _excel_file_ _tab_ package_date severity BC_ID short_name dec_id dec_label issue_type expected_value actual_value comment;
run;

ods listing;
ods html5 close;
ods excel close;

proc delete data=work.all_issues_bc;
run;
