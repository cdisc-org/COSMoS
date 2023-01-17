%let root=C:/_github/cdisc-org/COSMoS;
%let _debug=0;

options sasautos = ("&root/utilities/macros", %sysfunc(compress(%sysfunc(getoption(sasautos)),%str(%(%)))));
options ls=max;

%let excel_file=&root/curation/BC_Package_2022_10_26.xlsx;
%ReadExcel(file=&excel_file, range=Conceptual VS BC$, dsout=bc3);
%ReadExcel(file=&excel_file, range=%str(Conceptual LB (Common) BC)$, dsout=bc4);
%ReadExcel(file=&excel_file, range=SDTM VS BC$, dsout=sdtm3);
%ReadExcel(file=&excel_file, range=%str(SDTM LB BC)$, dsout=sdtm4);

%let excel_file=&root/curation/BC_Package_2023_02_13_draft2.xlsx;
%ReadExcel(file=&excel_file, range=%str(BC LB (Common))$, dsout=bc1);
%ReadExcel(file=&excel_file, range=%str(BC LB (TIG Biomarkers))$, dsout=bc2);
%ReadExcel(file=&excel_file, range=%str(SDTM LB)$, dsout=sdtm1);
%ReadExcel(file=&excel_file, range=%str(SDTM LB (TIG Biomarkers))$, dsout=sdtm2);


data bc;
  length order 8 parent_bc_id bc_id dec_id $32 bc_category $5124 short_name synonym dec_label $256;
  set 
      bc1(where=(not missing(bc_id))) 
      bc2(where=(not missing(bc_id)))
      bc3(where=(not missing(bc_id))) 
      bc4(where=(not missing(bc_id)))
      ;
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

data sdtm;
  length order 8 bc_id dec_id $32 vlm_group_id $64 short_name value_list assigned_value predicate_term format vlm_target $256 linking_phrase $512;
  set 
      sdtm1(where=(not missing(vlm_group_id)))
      sdtm2(where=(not missing(vlm_group_id)))
      sdtm3(where=(not missing(vlm_group_id)))
      sdtm4(where=(not missing(vlm_group_id)))
      ;
  order=_n_;
run;  

%if &_debug=1 %then %do;
  proc freq data=sdtm;
    tables vlm_group_id;
  run;  
%end;  

%get_Subset_Codelists(file=&excel_file, range=Subset Codelists$, dsout=subsets);

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
   