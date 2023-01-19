%let root=C:/_github/cdisc-org/COSMoS;
options sasautos = ("&root/utilities/macros", %sysfunc(compress(%sysfunc(getoption(sasautos)),%str(%(%)))));
options ls=256;
%let _debug=0;

/*
%let package=20221026;
%let ExcelFile=&root/curation/BC_Package_2022_10_26.xlsx;
%let TargetFolder=&root/yaml/&package/bc;

%generate_yaml_from_bc(excel_file=&ExcelFile, type=vs, package=20221026, out_folder=&TargetFolder, range=Conceptual VS BC);
%generate_yaml_from_bc(excel_file=&ExcelFile, type=lb, package=20221026, out_folder=&TargetFolder, range=%str(Conceptual LB (Common) BC));
*/

%let package=20230213;
%let ExcelFile=&root/curation/BC_Package_2023_02_13.xlsx;
%let TargetFolder=&root/yaml/&package/bc;

%generate_yaml_from_bc(excel_file=&ExcelFile, type=lb_1, package=&package, out_folder=&TargetFolder, range=%str(BC LB (Common)));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=lb_2, package=&package, out_folder=&TargetFolder, range=%str(BC LB (TIG Biomarkers)));
