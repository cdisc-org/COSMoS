%macro get_sdtm(code);

  %get_api_response(
    baseurl=&base_url_cosmos,
    endpoint=/mdr/specializations/sdtm/datasetspecializations/&code,
    response_file=%sysfunc(pathname(work))/sdtm_specialization_&code..json
  );

  filename jsonfile "%sysfunc(pathname(work))/sdtm_specialization_&code..json";
  filename mapfile "%sysfunc(pathname(work))/sdtm.map";
  libname jsonfile json map=mapfile automap=create fileref=jsonfile noalldata;

  %if %sysfunc(exist(jsonfile.variables_relationship)) %then %do;

      data __tmp__;
        length href $512 specializationId $64 latest_package_date $10 subject	linkingPhrase	predicateTerm	object $200;
        merge jsonfile._links_parentpackage(keep=href rename=(href=href_package)) jsonfile._links_self jsonfile.variables_relationship;
        latest_package_date=scan(href_package, -2, "\/");
        specializationId = scan(href, -1, "\/");
      run;  
      
      proc sql;
        create table __tmp__ 
        as select
          t1.datasetSpecializationId as specializationId length=64,
          scan(t2.href, -2, "\/") as latest_package_date length=10,
          t3.href length=512,
          t1.domain length=8,
          t5.name as variable length=32,
          t4.subject length=32,
          t4.linkingPhrase length=256,
          t4.predicateTerm length=128,
          t4.object length=32
          
        from jsonfile.root t1,
             jsonfile._links_parentpackage t2, 
             jsonfile._links_self t3, 
             jsonfile.variables_relationship t4,
             jsonfile.variables t5
        where t4.ordinal_variables = t5.ordinal_variables
        ;
      quit;
           
      
      data _sdtm_api;
        set _sdtm_api __tmp__;
      run;  

  %end;

  filename jsonfile clear;
  libname jsonfile clear;
  filename mapfile clear;
  
%mend get_sdtm;  

/*************************************************************************************************/

%let root=C:/_github/cdisc-org/COSMoS;
%include "&root/utilities/config.sas";

data _sdtm_api;
  if 0=1;
run;  

%get_api_response(
    baseurl=&base_url_cosmos,
    apikey=&api_key,
    endpoint=/mdr/specializations/sdtm/datasetspecializations,
    response_file=%sysfunc(pathname(work))/sdtm_specializations_latest.json
  );

filename jsfile "%sysfunc(pathname(work))/sdtm_specializations_latest.json";
filename mpfile "%sysfunc(pathname(work))/sdtm_latest.map";
libname jsfile json map=mpfile automap=create fileref=jsfile noalldata ordinalcount=none;

%let _cstLRECL=%str(LRECL=2048);
filename initCode CATALOG "work._cosmos.init.source" &_cstLRECL;

data _null_;
  length code $4096 specializationId $64;
  file initcode;
  set jsfile._links_datasetSpecializations;
  specializationId = scan(href, -1, "/");
  code=cats('%get_sdtm(code=', specializationId, ');');
  * call execute (code);
  put code;
run;

%include initCode;

proc datasets nolist lib=work;
  delete _cosmos / memtype=catalog;
quit;

filename initCode clear;

proc sort data=_sdtm_api out=data.sdtm_api_relationships;
  by specializationId;
run;  

filename jsfile clear;
libname jsfile clear;
filename mpfile clear;

proc sql noprint;
  select max(latest_package_date) into :latest_package_date trimmed
  from data.sdtm_api_relationships
;
quit;
%let latest_package_date=%sysfunc(compress(&latest_package_date, %str(-)));
%put &=latest_package_date;

proc sort data=_sdtm_api(keep=subject object linkingPhrase predicateTerm) out=work.sdtm_subject_rel_object nodupkey;
  by _ALL_;
run;  
proc sort data=work.sdtm_subject_rel_object;
  by subject object linkingPhrase predicateTerm;
run;  

data data.sdtm_subject_rel_object;
  retain n 0;
  set work.sdtm_subject_rel_object;
  by subject object linkingPhrase predicateTerm;
  file "&root/utilities/text/sdtm_specializations_subject_object_phrases_terms.txt";
  if first.object then n = 1;
    put n @10 subject @20 linkingPhrase @105 predicateTerm @125 object;
    n + 1;
run; 


proc sort data=_sdtm_api;
  by linkingPhrase predicateTerm;
run;  

data _null_;
  retain n 0;
  set _sdtm_api;
  by linkingPhrase predicateTerm;
  file "&root/utilities/text/sdtm_specializations_phrases_terms.txt";
  if first.linkingPhrase then n = 1;
  if first.predicateTerm then do;
    put n linkingPhrase +(-1) "," predicateTerm;
    n + 1;
  end;  
run; 

data data.sdtm_linkingphrases_predterms(keep=linkingPhrase predicateTerm);
  set _sdtm_api;
  by linkingPhrase predicateTerm;
  file "&root/utilities/text/sdtm_specializations_phrases.txt";
  /* Temporary hard update */
  if first.linkingPhrase then do;
    put linkingPhrase;
    * output;
  end;  
  if first.predicateTerm then do;
    output;
  end;  
run;  

data data.sdtm_linkingphrases(keep=linkingPhrase);
  set _sdtm_api;
  by linkingPhrase predicateTerm;
  /* Temporary hard update */
  if first.linkingPhrase then do;
    output;
  end;  
run;  


proc sort data=_sdtm_api;
  by predicateTerm linkingPhrase;
run;  

data _null_;
  retain n 0;
  set _sdtm_api;
  by predicateTerm linkingPhrase;
  file "&root/utilities/text/sdtm_specializations_terms_phrases.txt";
  if first.predicateTerm then n = 1;
  if first.linkingPhrase then do;
    put n predicateTerm +(-1) "," linkingPhrase;
    n + 1;
  end;  
run; 

proc sort data=_sdtm_api(keep=predicateTerm linkingPhrase) out=work.sdtm_predicateTerms nodupkey;
  by _ALL_;
run;  
proc sort data=work.sdtm_predicateTerms;
  by predicateTerm linkingPhrase;
run;  

data data.sdtm_predicateTerms(keep=predicateTerm linkingPhrases);
  retain linkingPhrases 0;
  set work.sdtm_predicateTerms;
  by predicateTerm linkingPhrase;
  file "&root/utilities/text/sdtm_specializations_terms.txt";
  if first.predicateTerm then linkingPhrases = 0;
  linkingPhrases + 1;
  if last.predicateTerm then do;
    put predicateTerm +(-1) "," linkingPhrases;
    output;
  end;  
run; 

options ls=256;
ods listing close;
ods excel file="&root/utilities/reports/sdtm_specializations_relationships_&latest_package_date..xlsx";

ods excel options(sheet_name="Linking Phrases" flow="tables" autofilter = 'all');
  proc report data=data.sdtm_linkingphrases;
    column linkingPhrase;
    define linkingPhrase / width = 256;
  run;  

ods excel options(sheet_name="Predicate Terms" flow="tables" autofilter = 'all');
  proc report data=data.sdtm_predicateTerms;
    column predicateTerm linkingPhrases;
  run;  

ods excel options(sheet_name="Link. Phrases - Pred. Terms" flow="tables" autofilter = 'all');
  proc report data=data.sdtm_linkingphrases_predterms;
    column linkingPhrase predicateTerm;
    define linkingPhrase / width = 256;
  run;  

ods excel options(sheet_name="Subj Phrase/Terms Obj" flow="tables" autofilter = 'all');
  proc report data=data.sdtm_subject_rel_object;
    column Subject linkingPhrase predicateTerm Object;
    define linkingPhrase / width = 256;
  run;  

ods excel close;
ods listing;

proc sort data=_sdtm_api;
  by domain specializationId variable;
run;  

proc sql;
  create table _sdtm_api2 as
  select
    t1.specializationId as id1,
    t2.specializationId as id2,
    t1.latest_package_date as latest1,
    t2.latest_package_date as latest2,
    t1.domain length=8,
    t1.subject length=8,
    t1.predicateTerm as predicateTerm1,
    t2.predicateTerm as predicateTerm2,
    t1.linkingPhrase as linkingPhrase1,
    t2.linkingPhrase as linkingPhrase2,
    t1.object length=8
  from _sdtm_api t1, _sdtm_api t2
  where (t1.subject = t2.subject) and (t1.object = t2.object) and 
        (strip(t1.linkingPhrase) ne strip(t2.LinkingPhrase)) and 
        (t1.specializationId le t2.specializationId)
  order by t1.specializationId, t1.subject, t1.object, t1.linkingPhrase
  ;
quit;

ods listing close;
ods excel file="&root/utilities/reports/relationships_issues_&latest_package_date..xlsx"
    options(sheet_name="Potential issues" flow="tables" autofilter = 'all');

  proc report data=_sdtm_api;
    where (variable ne subject) or (variable eq object) or (substr(subject, 1, 2) ne substr(object, 1, 2));
    column latest_package_date domain specializationId variable subject linkingPhrase predicateTerm object;
    define linkingPhrase / width = 120;
  run;

ods excel options(sheet_name="Link. Phrases - Pred. Terms" flow="tables" autofilter = 'all');

  proc report data=_sdtm_api2;
    column id1 id2 latest1 latest2 domain subject predicateTerm1 predicateTerm2 linkingPhrase1 linkingPhrase2 object;
    define linkingPhrase1 / width = 120;
    define linkingPhrase2 / width = 120;
  run;

ods excel close;
ods listing;
