%let root=C:/_github/cdisc-org/COSMoS;
%let temp=C:/temp/COSMoS;

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


%let package=20230706;
%let folder=20230706_oncology;
%let Excelfile=&root/curation/BC_Oncology_RECIST11_2023_07_06.xlsx;
%let TargetFolder=&root/yaml/&folder/sdtm;

%get_Subset_Codelists(file=&Excelfile, range=Subset Codelist Example$, dsout=subsets);

%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=recist_tu, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_TU), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=recist_tr, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_TR), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=recist_rs, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_RS), subsetsDS=subsets);



%let package=20230706;
%let folder=20230706_nononco;
%let ExcelFile=&root/curation/draft/BC_Package_R4_draft.xlsx;
%let TargetFolder=&root/yaml/&folder/sdtm;

%get_Subset_Codelists(file=&Excelfile, range=Subset Codelist Example$, dsout=subsets);

%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=ae, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_AE), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=be, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_BE), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=ds, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_DS), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=eg, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_EG), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=lb, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_LB), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=lb_edits, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_LB_EDITS), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=mb, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_MB), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=mh, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_MH), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=pr, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_PR), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=vs, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_VS), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=vs_edits, package=&package, override_package_date=%str(2023-07-06), out_folder=&TargetFolder, range=%str(SDTM_VS_EDITS), subsetsDS=subsets);



ods listing close;
ods html5 file="&root/utilities/get_bc_sdtm_issues_%sysfunc(date(), b8601da8.).html";
ods excel options(sheet_name="SDTM_&package" flow="tables" autofilter = 'all') file="&root/utilities/get_bc_sdtm_issues_%sysfunc(date(), b8601da8.).xlsx";

proc print data=all_issues_sdtm;
  var _excel_file_ _tab_ vlm_group_id sdtm_variable issue_type expected_value actual_value comment;
run;

ods listing;
ods html5 close;
ods excel close;  