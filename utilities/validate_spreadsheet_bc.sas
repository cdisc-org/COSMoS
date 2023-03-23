%let root=C:/_github/cdisc-org/COSMoS;
%let _debug=1;

options sasautos = ("&root/utilities/macros", %sysfunc(compress(%sysfunc(getoption(sasautos)),%str(%(%)))));
options ls=max;

/* Package 1*/
%let excel_file=&root/curation/BC_Package_2022_10_26.xlsx;
%ReadExcel(file=&excel_file, range=Conceptual VS BC$, dsout=bc1_1);
%ReadExcel(file=&excel_file, range=%str(Conceptual LB (Common) BC)$, dsout=bc1_2);

%ReadExcel(file=&excel_file, range=SDTM VS BC$, dsout=sdtm1_1);
%ReadExcel(file=&excel_file, range=%str(SDTM LB BC)$, dsout=sdtm1_2);

/* Package 2 */
%let excel_file=&root/curation/BC_Package_2023_02_13.xlsx;
%ReadExcel(file=&excel_file, range=%str(BC LB (Common))$, dsout=bc2_1);
%ReadExcel(file=&excel_file, range=%str(BC LB (TIG Biomarkers))$, dsout=bc2_2);

%ReadExcel(file=&excel_file, range=%str(SDTM LB)$, dsout=sdtm2_1);
%ReadExcel(file=&excel_file, range=%str(SDTM LB (TIG Biomarkers))$, dsout=sdtm2_2);

%get_Subset_Codelists(file=&excel_file, range=Subset Codelists$, dsout=subsets);

/* Package 3 */
%let excel_file=&root/curation/draft/BC_Package_2023_03_31_draft.xlsx;
%ReadExcel(file=&excel_file, range=%str(BC_DM)$, dsout=bc3_1);
%ReadExcel(file=&excel_file, range=%str(BC_VS)$, dsout=bc3_2);
%ReadExcel(file=&excel_file, range=%str(BC_LB)$, dsout=bc3_3);
%ReadExcel(file=&excel_file, range=%str(BC_MB)$, dsout=bc3_4);
%ReadExcel(file=&excel_file, range=%str(BC_AE)$, dsout=bc3_5);
%ReadExcel(file=&excel_file, range=%str(BC_CM)$, dsout=bc3_6);
%ReadExcel(file=&excel_file, range=%str(BC_RE)$, dsout=bc3_7);
%ReadExcel(file=&excel_file, range=%str(BC_PR)$, dsout=bc3_8);
%ReadExcel(file=&excel_file, range=%str(BC_BE)$, dsout=bc3_9);
%ReadExcel(file=&excel_file, range=%str(BC_EG)$, dsout=bc3_10);
%ReadExcel(file=&excel_file, range=%str(BC_DS)$, dsout=bc3_12);



data bc(drop=change_history F1:);
  retain order package_date bc_id parent_bc_id bc_category short_name 
         synonym result_scale definition system system_name	code dec_id dec_label data_type example_set;
  length order 8 package_date $64 bc_id parent_bc_id $32 bc_category synonym result_scale definition 
         system	system_name	code change_history $5124 dec_id $32 short_name dec_label $512 example_set $1024;
  set 
      bc:(where=(not missing(bc_id)));
  order=_n_;
run;  

%if &_debug=1 %then %do;
  ods listing close;
  ods html5 file="validate_spreadsheet_sdtm_bc.html";

    proc print data=bc;
    run;

  ods html5 close;
  ods listing;
%end;

data sdtm(drop=change_history F3: F4:);
  retain order package_date sdtmig_start_version sdtmig_end_version bc_id domain vlm_group_id short_name vlm_source  
         sdtm_variable dec_id nsv_flag codelist codelist_submision_value assigned_term subset_codelist value_list assigned_value 
         subject linking_phrase predicate_term object format 
         vlm_target role data_type length significant_digits mandatory_variable mandatory_value origin_type origin_source comparator;
  length order 8 package_date $64 sdtmig_start_version sdtmig_end_version bc_id dec_id $32 domain vlm_group_id vlm_source sdtm_variable $64
         subset_codelist value_list assigned_value linking_phrase predicate_term 
         short_name format data_type origin_source vlm_target change_history $512;
  set sdtm:(where=(not missing(vlm_group_id)));
  order=_n_;
run;  

%if &_debug=1 %then %do;
  proc freq data=sdtm;
    tables vlm_group_id;
  run;  
%end;  

proc sql;
  create table sdtm_merged
  as select
    sdtm.*,
    ss.subset_value_list
  from work.sdtm sdtm
    left join subsets ss
  on sdtm.subset_codelist = ss.subset_short_name
  order by vlm_group_id, order
  ;
quit;     

%if &_debug=1 %then %do;
  ods listing close;
  ods html5 file="validate_spreadsheet_sdtm.html";

    proc print data=sdtm_merged;
    run;

  ods html5 close;
  ods listing;
%end;


/* Unresolved BC Parent BCs */
proc sql;
  title01 "Missing BC parent_bc_id link to BC bc_id";
  title02 "Source: &excel_file";
  create table parent_bc_missing as
    select bc_category, bc_id, short_name, parent_bc_id
    from bc
    where 
      parent_bc_id not in (select bc_id from bc)
      and not missing(parent_bc_id)
    order by bc_category, bc_id
    ;
quit;

proc print data=parent_bc_missing;
  title01 "Missing BC parent_bc_id link to BC bc_id";
  title02 "Source: &excel_file";
run;  


/* Unresolved SDTM BCs */
proc sql;
  title01 "Missing SDTM bc_id link to BC bc_id";
  title02 "Source: &excel_file";
  create table sdtm_bc_missing as
    select vlm_group_id, sdtm_variable, sd.bc_id
    from sdtm_merged sd
    where 
      sd.bc_id not in (select bc_id from bc)
    order by vlm_group_id, sdtm_variable
    ;
quit;

proc print data=sdtm_bc_missing;
  title01 "Missing SDTM bc_id link to BC bc_id";
  title02 "Source: &excel_file";
run;  



/* Unresolved SDTM BCs/DECs */
proc sql;
  title01 "Missing SDTM bc_id/dec_id link to BC bc_id/dec_id";
  title02 "Source: &excel_file";
  create table sdtm_bc_dec as
    select unique catx('-', bc_id, dec_id) as bc_dec
    from sdtm_merged
    where not missing(dec_id);

  create table sdtm_bc_dec_missing as
    select sbdi.vlm_group_id, sbdi.sdtm_variable, sbdi.bc_id, sbdi.dec_id 
    from sdtm_bc_dec sbd, sdtm_merged sbdi
    where 
      sbd.bc_dec not in (select unique catx('-', bc_id, dec_id) from bc) and
      catx('-', sbdi.bc_id, sbdi.dec_id) = sbd.bc_dec
    order by vlm_group_id, sdtm_variable
    ;
quit;

proc print data=sdtm_bc_dec_missing;
  title01 "Missing SDTM bc_id/dec_id link to BC bc_id/dec_id";
  title02 "Source: &excel_file";
run;  


/* Duplicate BC records */
proc sql;
  title01 "Duplicate BC records (bc_category bc_id short_name)";
  title02 "Source: &excel_file";
/*  create table sdtm_bc_missing as*/
    select package_date, bc_category, bc_id, short_name, dec_id
    from bc
    group by package_date, bc_category, bc_id, short_name, dec_id
    having count(*) > 1
    ;
run;

/* Duplicate SDTM records */
proc sql;
  title01 "Duplicate SDTM records (vlm_group_id sdtm_variable)";
  title02 "Source: &excel_file";
/*  create table sdtm_bc_missing as*/
    select package_date, vlm_group_id, sdtm_variable
    from sdtm_merged
    group by package_date, vlm_group_id, sdtm_variable
    having count(*) > 1
    ;
run;
   