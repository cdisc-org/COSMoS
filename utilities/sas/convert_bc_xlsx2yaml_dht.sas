%let root=C:/_github/cdisc-org/COSMoS;
%include "&root/utilities/config.sas";

%let _debug=0;

%create_template(type=BC_ISSUE, out=work.all_issues_bc);


%let release=dht;
%let package=20261231;
%let folder=dht_test;
%let TargetFolder=&root/yaml/&folder/bc;
%let OverrideDate=%str(2026-12-31);

%let excel_file=&root/curation/draft/dht/DHT_BC_SDTM.xlsx;
%generate_yaml_from_bc(excel_file=&excel_file, type=di, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_DI));
%generate_yaml_from_bc(excel_file=&excel_file, type=sleep, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_Sleep));
%generate_yaml_from_bc(excel_file=&excel_file, type=mk, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_MK));
%generate_yaml_from_bc(excel_file=&excel_file, type=hr, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, range=%str(BC_HR));

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
