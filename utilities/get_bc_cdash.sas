%let root=C:/_github/cdisc-org/COSMoS;
options sasautos = ("&root/utilities/macros", %sysfunc(compress(%sysfunc(getoption(sasautos)),%str(%(%)))));
options ls=256;
%let _debug=0;

%let package=20230131;
%let Excelfile=&root/curation/Draft_BC_Package_R2_20Dec22.xlsx;
%let TargetFolder=&root/yaml/&package/cdash;

proc format;
  value $YN
    "Y" = "true"
    "y" = "true"
    "N" = "false"
    "n" = "false"
  ;
run;

%get_Subset_Codelists(file=&Excelfile, range=Subset Codelist Example$, dsout=subsets);

%generate_yaml_from_bc_cdash(excel_file=&Excelfile, type=vs, package=20230131, out_folder=&TargetFolder, range=CDASH VS, subsetsDS=subsets);
%generate_yaml_from_bc_cdash(excel_file=&Excelfile, type=lb, package=20230131, out_folder=&TargetFolder, range=CDASH LB BC, subsetsDS=subsets);
