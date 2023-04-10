%let root=C:/_github/cdisc-org/COSMoS;
options sasautos = ("&root/utilities/macros", %sysfunc(compress(%sysfunc(getoption(sasautos)),%str(%(%)))));
options ls=256;
%let _debug=0;

proc format;
  value $YN
    "Y" = "true"
    "y" = "true"
    "N" = "false"
    "n" = "false"
  ;
run;


%let package=20221026;
%let Excelfile=&root/curation/BC_Package_2022_10_26.xlsx;
%let TargetFolder=&root/yaml/&package/sdtm;

%get_Subset_Codelists(file=&Excelfile, range=Subset Codelist Example$, dsout=subsets);

%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=vs, package=20221026, out_folder=&TargetFolder, range=SDTM VS BC, subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=lb, package=20221026, out_folder=&TargetFolder, range=%str(SDTM LB BC), subsetsDS=subsets);


%let package=20230213;
%let Excelfile=&root/curation/BC_Package_2023_02_13.xlsx;
%let TargetFolder=&root/yaml/&package/sdtm;

%get_Subset_Codelists(file=&Excelfile, range=Subset Codelists$, dsout=subsets);

%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=lb_1, package=&package, out_folder=&TargetFolder, range=%str(SDTM LB), subsetsDS=subsets);
%generate_yaml_from_bc_sdtm(excel_file=&Excelfile, type=lb_2, package=&package, out_folder=&TargetFolder, range=%str(SDTM LB (TIG Biomarkers)), subsetsDS=subsets);
