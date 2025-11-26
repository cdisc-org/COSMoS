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

%create_template(type=CRF_ISSUE, out=work.all_issues_crf);

%let release=xx;
%let package=20251231;
%let folder=20251231_draft;
%let TargetFolder=&root/yaml/&folder/crf;
%let OverrideDate=%str(2025-12-31);

%let excel_file=&root/curation/draft/crf/crf_specialization_AE.xlsx;
%generate_yaml_from_crf(excel_file=&excel_file, range=%str(CRF_AE), type=ae, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, debug=0);

%let excel_file=&root/curation/draft/crf/crf_specialization_CM.xlsx;
%generate_yaml_from_crf(excel_file=&excel_file, range=%str(CRF_CM), type=cm, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, debug=0);

%let excel_file=&root/curation/draft/crf/crf_specialization_DM.xlsx;
%generate_yaml_from_crf(excel_file=&excel_file, range=%str(CRF_DM), type=dm, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, debug=0);

%let excel_file=&root/curation/draft/crf/crf_specialization_DS.xlsx;
%generate_yaml_from_crf(excel_file=&excel_file, range=%str(CRF_DS), type=ds, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, debug=0);

%let excel_file=&root/curation/draft/crf/crf_specialization_EC.xlsx;
%generate_yaml_from_crf(excel_file=&excel_file, range=%str(CRF_EC), type=ec, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, debug=0);

%let excel_file=&root/curation/draft/crf/crf_specialization_EG_Local.xlsx;
%generate_yaml_from_crf(excel_file=&excel_file, range=%str(CRF_EG), type=eg, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, debug=0);

%let excel_file=&root/curation/draft/crf/crf_specialization_IE.xlsx;
%generate_yaml_from_crf(excel_file=&excel_file, range=%str(CRF_IE), type=ie, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, debug=0);

%let excel_file=&root/curation/draft/crf/crf_specialization_LB.xlsx;
%generate_yaml_from_crf(excel_file=&excel_file, range=%str(CRF_LB), type=lb, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, debug=0);

%let excel_file=&root/curation/draft/crf/crf_specialization_MB.xlsx;
%generate_yaml_from_crf(excel_file=&excel_file, range=%str(CRF_MB), type=mb, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, debug=0);

%let excel_file=&root/curation/draft/crf/crf_specialization_MH.xlsx;
%generate_yaml_from_crf(excel_file=&excel_file, range=%str(CRF_MH), type=mh, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, debug=0);

%let excel_file=&root/curation/draft/crf/crf_specialization_PR.xlsx;
%generate_yaml_from_crf(excel_file=&excel_file, range=%str(CRF_PR), type=pr, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, debug=0);

%let excel_file=&root/curation/draft/crf/crf_specialization_SC.xlsx;
%generate_yaml_from_crf(excel_file=&excel_file, range=%str(CRF_SC), type=sc, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, debug=0);

%let excel_file=&root/curation/draft/crf/crf_specialization_SU.xlsx;
%generate_yaml_from_crf(excel_file=&excel_file, range=%str(CRF_SU), type=su, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, debug=0);

%let excel_file=&root/curation/draft/crf/crf_specialization_VS.xlsx;
%generate_yaml_from_crf(excel_file=&excel_file, range=%str(CRF_VS), type=vs, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, debug=0);

%let excel_file=&root/curation/draft/crf/crf_specialization_QRS_6MWT.xlsx;
%generate_yaml_from_crf(excel_file=&excel_file, range=%str(CRF_QRS_6MWT), type=6mwt, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, debug=0);

%let excel_file=&root/curation/draft/crf/crf_specialization_QRS_ADAS_COG.xlsx;
%generate_yaml_from_crf(excel_file=&excel_file, range=%str(CRF_ADAS-COG), type=adas-cog, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, debug=0);

%let excel_file=&root/curation/draft/crf/crf_specialization_QRS_EQ5D-5L.xlsx;
%generate_yaml_from_crf(excel_file=&excel_file, range=%str(CRF_QRS_EQ5D-5L), type=eq5d-l, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, debug=0);

%let excel_file=&root/curation/draft/crf/crf_specialization_QRS_TTS.xlsx;
%generate_yaml_from_crf(excel_file=&excel_file, range=%str(CRF_QRS_TTS), type=tts, package=&package, override_package_date=&OverrideDate, out_folder=&TargetFolder, debug=0);


ods listing close;
ods html5 file="&root/utilities/reports/convert_crf_xlsx2yaml_issues_R&release._&todays..html";
ods excel options(sheet_name="Collection_&package" flow="tables" autofilter = 'all') file="&root/utilities/reports/convert_crf_xlsx2yaml_issues_R&release._&todays..xlsx";

proc print data=all_issues_crf;
  title "CRF Specialization Issues - &todays";
  var _excel_file_ _tab_ package_date severity crf_group_id crf_item issue_type expected_value actual_value comment;
run;

ods listing;
ods html5 close;
ods excel close;

proc delete data=all_issues_crf;
run;
