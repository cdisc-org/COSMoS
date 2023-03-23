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

/*
%let package=20230213;
%let ExcelFile=&root/curation/BC_Package_2023_02_13.xlsx;
%let TargetFolder=&root/yaml/&package/bc;

%generate_yaml_from_bc(excel_file=&ExcelFile, type=lb_1, package=&package, out_folder=&TargetFolder, range=%str(BC LB (Common)));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=lb_2, package=&package, out_folder=&TargetFolder, range=%str(BC LB (TIG Biomarkers)));
*/

%let package=20230331;
%let ExcelFile=&root/curation/BC_Package_2023_03_31.xlsx;
%let TargetFolder=&root/yaml/&package/bc;

%generate_yaml_from_bc(excel_file=&ExcelFile, type=dm, package=&package, out_folder=&TargetFolder, range=%str(BC_DM));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=vs, package=&package, out_folder=&TargetFolder, range=%str(BC_VS));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=lb, package=&package, out_folder=&TargetFolder, range=%str(BC_LB));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=mb, package=&package, out_folder=&TargetFolder, range=%str(BC_MB));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=ae, package=&package, out_folder=&TargetFolder, range=%str(BC_AE));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=cm, package=&package, out_folder=&TargetFolder, range=%str(BC_CM));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=re, package=&package, out_folder=&TargetFolder, range=%str(BC_RE));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=pr, package=&package, out_folder=&TargetFolder, range=%str(BC_PR));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=be, package=&package, out_folder=&TargetFolder, range=%str(BC_BE));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=eg, package=&package, out_folder=&TargetFolder, range=%str(BC_EG));
%generate_yaml_from_bc(excel_file=&ExcelFile, type=ds, package=&package, out_folder=&TargetFolder, range=%str(BC_DS));
