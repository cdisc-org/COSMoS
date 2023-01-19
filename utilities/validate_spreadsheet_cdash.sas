%let root=C:\_github\cdisc-org\COSMoS;
%let _debug=0;

options sasautos = ("&root/utilities", %sysfunc(compress(%sysfunc(getoption(sasautos)),%str(%(%)))));
options ls=256 formchar='|_ _ ||||||+=|-/\<>*';

/******************************************************************************/
/* Read BCs                                                                   */
/******************************************************************************/
%let excel_file=&root/curation/BC_Package_2022_10_26.xlsx;

%ReadExcel(file=&excel_file, range=Conceptual VS BC$, dsout=bc_vs);
%ReadExcel(file=&excel_file, range=%str(Conceptual LB (Common) BC)$, dsout=bc_lb);

data bc_vs;
  set bc_vs(where=(not missing(bc_id)));
run;  
data bc_lb;
  set bc_lb(where=(not missing(bc_id)));
run;  

data bc;
  length order 8 parent_bc_id bc_id dec_id $32 bc_category $64 short_name synonym dec_label $256;
  set bc_vs bc_lb;
  order=_n_;
  parent_bc_id=strip(parent_bc_id);
  bc_id=strip(bc_id);
  dec_id=strip(dec_id);
run;  

ods listing close;
ods html5 file="get_bc.html";

  proc print data=bc;
  run;

ods html5 close;
ods listing;

/******************************************************************************/
/* Read CDASH specializations                                                 */
/******************************************************************************/

%let excel_file=&root/curation/Draft_BC_Package_R2_20Dec22.xlsx;

%ReadExcel(file=&excel_file, range=CDASH VS$, dsout=cdash_vs);
%ReadExcel(file=&excel_file, range=%str(CDASH LB BC)$, dsout=cdash_lb);

data cdash_vs;
  set cdash_vs(where=(not missing(cdash_group_id)));
run;  
data cdash_lb;
  set cdash_lb(where=(not missing(cdash_group_id)));
run;  

data cdash;
  length order 8 bc_id dec_id $32 cdash_group_id sdtm_target_group $64 scenario short_name value_list prepopulated_value predicate_term $256 linking_phrase $512;
  set cdash_vs(drop=significant_digits) cdash_lb(drop=significant_digits);
  order=_n_;
  bc_id=strip(bc_id);
  dec_id=strip(dec_id);
  cdash_group_id=strip(cdash_group_id);
  scenario=strip(scenario);
run;  

/*
proc freq data=cdash;
  tables cdash_group_id * scenario / norow nocol nopercent;
run;  
*/
  
/******************************************************************************/
/* Read subsets                                                               */
/******************************************************************************/
%ReadExcel(file=&excel_file, range=Subset Codelist Example$, dsout=subsets);

proc sort data=subsets;
  by Subset_Short_Name Submission_Value;
run;  

data subsets(keep=Subset_Short_Name subset_value_list);
  length subset_value_list $8192;
  retain subset_value_list;
  set subsets;
  by Subset_Short_Name Submission_Value;
  if first.Subset_Short_Name then subset_value_list="";
  subset_value_list=catx(";", subset_value_list, Submission_Value);
  if last.Subset_Short_Name then output;
run;    

proc sql;
  create table cdash_merged
  as select
    cdash.*,
    ss.subset_value_list
  from work.cdash cdash
    left join subsets ss
  on cdash.subset_codelist = ss.subset_short_name
  order by cdash_group_id, order
  ;
quit;     

ods listing close;
ods html5 file="get_bc_cdash.html";

  proc print data=cdash_merged;
  run;

ods html5 close;
ods listing;



/* Unresolved BC Parent BCs */
proc sql;
  title01 "Missing BC parent_bc_id link to BC bc_id";
  title02 "Source: &excel_file";
/*  create table parent_bc_missing as*/
    select bc_category, bc_id, parent_bc_id
    from bc
    where 
      parent_bc_id not in (select bc_id from bc)
      and not missing(parent_bc_id)
    order by bc_category, bc_id
    ;
quit;

/*
proc print data=parent_bc_missing;
  title01 "Missing BC parent_bc_id link to BC bc_id";
  title02 "Source: &excel_file";
run;  
*/


/* Unresolved cdash BCs */
proc sql;
  title01 "Missing CDASH bc_id link to BC bc_id";
  title02 "Source: &excel_file";
/*  create table cdash_bc_missing as*/
    select cdash_group_id, scenario, cdash_variable, cd.bc_id
    from cdash_merged cd
    where 
      cd.bc_id not in (select bc_id from bc)
    order by cdash_group_id, scenario, cdash_variable
    ;
quit;

/*
proc print data=cdash_bc_missing;
  title01 "Missing cdash bc_id link to BC bc_id";
  title02 "Source: &excel_file";
run;  
*/


/* Unresolved cdash BCs/DECs */
proc sql;
  title01 "Missing CDASH bc_id/dec_id link to BC bc_id/dec_id";
  title02 "Source: &excel_file";
  create table cdash_bc_dec as
    select unique catx('-', bc_id, dec_id) as bc_dec
    from cdash_merged
    where not missing(dec_id);

/*  create table cdash_bc_dec_missing as*/
    select cbdi.cdash_group_id, cbdi.scenario, cbdi.cdash_variable, cbdi.bc_id, cbdi.dec_id 
    from cdash_bc_dec cbd, cdash_merged cbdi
    where 
      cbd.bc_dec not in (select unique catx('-', bc_id, dec_id) from bc) and
      catx('-', cbdi.bc_id, cbdi.dec_id) = cbd.bc_dec
    order by cdash_group_id, cdash_variable
    ;
quit;

/*
proc print data=cdash_bc_dec_missing;
  title01 "Missing cdash bc_id/dec_id link to BC bc_id/dec_id";
  title02 "Source: &excel_file";
run;  
*/

/* Duplicate BC records */
proc sql;
  title01 "Dublicate BC records (bc_category bc_id short_name)";
  title02 "Source: &excel_file";
/*  create table cdash_bc_missing as*/
    select bc_category, bc_id, short_name, dec_id
    from bc
    group by bc_category, bc_id, short_name, dec_id
    having count(*) > 1
    ;
run;

/* Duplicate cdash records */
proc sql;
  title01 "Dublicate CDASH records (cdash_group_id cdash_variable)";
  title02 "Source: &excel_file";
/*  create table cdash_bc_missing as*/
    select cdash_group_id, scenario, cdash_variable
    from cdash_merged
    group by cdash_group_id, scenario, cdash_variable
    having count(*) > 1
    ;
run;
   