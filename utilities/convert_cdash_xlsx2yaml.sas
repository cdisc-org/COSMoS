%let root=C:/_github/cdisc-org/COSMoS;

%include "&root/utilities/config.sas";

%let _debug=0;

%let package=20230131;
%let Excelfile=&root/curation/draft/CDASH_draft.xlsx;
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
