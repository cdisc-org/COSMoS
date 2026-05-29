%let root=C:/_github/cdisc-org/COSMoS;
%include "&root/utilities/config.sas";

%let _debug=0;
%let checkrelationships=1;

proc format;
  value $YN
    "Y" = "true"
    "y" = "true"
    "N" = "false"
    "n" = "false"
  ;
run;


%let release=r17;

%macro run_latest_bc(release=);
  
  %local bc_set TargetFolder;
  %let bc_set =;
  %let TargetFolder=&root/yaml/latest/bc;

  %if %sysevalf(%superq(release)=, boolean)=0 %then %do;

    %let excel_file=&root/curation/draft/cdisc_biomedical_concepts_&release._draft.xlsx;
    %ReadExcel(file=&excel_file, range=%str(Biomedical Concepts)$, dsout=bc_new);
    
    data bc_set;
      length bc_id $128;
      set bc_new(where=(not missing(bc_id)) keep=bc_id);
    run;  
      
    proc sql noprint;
      select distinct bc_id into :bc_set separated by '","'
      from bc_new(where=(not missing(bc_id)))
      ;
    quit;
    
    %let TargetFolder=&root/yaml/latest_test/bc;
    
  %end;  
    
  %put bc_set = "&bc_set";
    
  %let ExcelFile=&root/export/cdisc_biomedical_concepts_latest.xlsx;
  
  %create_template(type=BC_ISSUE, out=work.all_issues_bc);
  %generate_yaml_from_bc(excel_file=&ExcelFile, type=latest, package=latest, override_package_date=, out_folder=&TargetFolder, 
                         range=%str(Biomedical Concepts), 
                         select=%str(bc_id not in ("&bc_set")));
  
  ods listing close;
  ods html5 file="&root/utilities/reports/convert_bc_xlsx2yaml_issues_latest_&release._%sysfunc(date(), b8601da8.).html";
  ods excel options(sheet_name="BC_latest" flow="tables" autofilter = 'all') file="&root/utilities/reports/convert_bc_xlsx2yaml_issues_latest_&release._%sysfunc(date(), b8601da8.).xlsx";
  
  proc print data=all_issues_bc;
    title "BC Issues - %sysfunc(date(), b8601da8.)";
    var _excel_file_ _tab_ package_date severity BC_ID short_name dec_id dec_label issue_type expected_value actual_value comment;
  run;
  
  ods listing;
  ods html5 close;
  ods excel close;  


%mend run_latest_bc;
/***********************************************************************************************************************/

%macro run_latest_sdtm(release=);

  %local sdtm_set TargetFolder;
  %let sdtm_set =;
  %let TargetFolder=&root/yaml/latest/sdtm;
  
  %if %sysevalf(%superq(release)=, boolean)=0 %then %do;
    
    %let excel_file=&root/curation/draft/cdisc_sdtm_dataset_specializations_&release._draft.xlsx;
    %ReadExcel(file=&excel_file, range=%str(SDTM Dataset Specializations)$, dsout=sdtm_new);
    
    data sdtm_set;
      length vlm_group_id $128;
      set sdtm_new(where=(not missing(vlm_group_id)) keep=vlm_group_id);
    run;  
      
    proc sql noprint;
      select distinct vlm_group_id into :sdtm_set separated by '","'
      from sdtm_new(where=(not missing(vlm_group_id)))
      ;
    quit;
    
    %let TargetFolder=&root/yaml/latest_test/sdtm;
    
  %end;
  
  %put sdtm_set = "&sdtm_set";
  
  %let ExcelFile=&root/curation/package06/BC_Package_R6_LZZT.xlsx;
  %get_Subset_Codelists(file=&Excelfile, range=Subset Codelist Example$, dsout=subsets1);
  
  %let ExcelFile=&root/curation/package16/R16_BC_DS_Edits.xlsx;
  %get_Subset_Codelists(file=&Excelfile, range=Subset Codelist$, dsout=subsets2);
  
  %create_template(type=SUBSET, out=work.subsets);
  
  data subsets;
    set work.subsets subsets1 subsets2;
  run;  
  
  %let ExcelFile=&root/export/cdisc_sdtm_dataset_specializations_latest.xlsx;
  
  %create_template(type=SDTM_ISSUE, out=work.all_issues_sdtm);
  %generate_yaml_from_sdtm(excel_file=&Excelfile, type=latest, package=latest, override_package_date=, out_folder=&TargetFolder, subsetsDS=subsets, 
                           range=%str(SDTM Dataset Specializations), check_relationships=&checkrelationships, 
                           select=%str(vlm_group_id not in ("&sdtm_set")));
  
  ods listing close;
  ods html5 file="&root/utilities/reports/convert_sdtm_xlsx2yaml_issues_latest_&release._%sysfunc(date(), b8601da8.).html";
  ods excel options(sheet_name="SDTM_latest" flow="tables" autofilter = 'all') file="&root/utilities/reports/convert_sdtm_xlsx2yaml_issues_latest_&release._%sysfunc(date(), b8601da8.).xlsx";
  
  proc print data=all_issues_sdtm;
    title "SDTM Specialization Issues - %sysfunc(date(), b8601da8.)";
    var _excel_file_ _tab_ package_date severity vlm_group_id sdtm_variable issue_type expected_value actual_value comment;
  run;
  
  ods listing;
  ods html5 close;
  ods excel close;  

%mend run_latest_sdtm;


%run_latest_bc(release=r17);
%run_latest_sdtm(release=r17);
