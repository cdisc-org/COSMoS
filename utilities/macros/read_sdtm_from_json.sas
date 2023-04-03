%macro read_sdtm_from_json(json_path=, jsonlib=, maplib=work, template=, out=, include_package_dates=0);

  proc datasets library=&jsonlib kill nolist;
  quit;

  filename jsonfile "&json_path";
  filename mapfile "%sysfunc(pathname(&maplib))/specialization.map";

  libname jsonfile json map=mapfile automap=create fileref=jsonfile /* noalldata ordinalcount=none */;
  proc copy in=jsonfile out=&jsonlib;
  run;

  %if &SYSERR %then %do;
    %put ### &_package - &specialization;
    %goto exit_get_json;
  %end;

  data work.root;
    set &template &jsonlib..root;
  run;  
  
  %if not %sysfunc(exist(&jsonlib..._links_parentbiomedicalconcept)) and &include_package_dates %then %do;    

    data work.root;
      merge work.root(in=in1) data.latest_bc(keep=biomedicalConceptId latest_package_date);
      by biomedicalConceptId;
      if in1;
    run;  

  %end;

  data work.variables;
    set &template %if %sysfunc(exist(&jsonlib..variables)) %then &jsonlib..variables;;
  run;  
  
  %if %sysfunc(exist(&jsonlib..variables_valuelist)) %then %do;    
    data work.variables_valuelist(drop=valueList:);
      set &jsonlib..variables_valuelist;
      length _valueList $ 2048;
      array valueList_{*} $ 1024 valueList:;
      _valueList = catx(";", OF valueList_{*});
    run;
  %end;

  proc sql;
    create table &out(drop=ordinal_variables)
    as select 
      %if %sysfunc(exist(&jsonlib.._links_parentpackage)) %then %do;    
        scan(pp.title, -1, " ") as packageDate length=10
      %end;
      %if not %sysfunc(exist(&jsonlib.._links_parentpackage)) %then %do;    
        root.packageDate length=10
      %end;
      
      %if &include_package_dates %then %do;
        %if %sysfunc(exist(&jsonlib.._links_self)) %then %do;    
          , scan(self.href, -3, "\/") as sdtmSpecializationId_PackageDate length=10
        %end;
        %if not %sysfunc(exist(&jsonlib.._links_self)) %then %do;    
          , root.packageDate as sdtmSpecializationId_PackageDate length=10
        %end;
      %end;

      %if %sysfunc(exist(&jsonlib.._links_parentbiomedicalconcept)) %then %do;    
        , scan(pbc.href, -1, "\/") as biomedicalConceptId length=64
        %if &include_package_dates %then %do; 
          , scan(pbc.href, -3, "\/") as biomedicalConceptId_PackageDate length=10 
        %end;
        , var.dateElementConceptId as dataElementConceptId length=64 label=""
      %end;
      %if not %sysfunc(exist(&jsonlib.._links_parentbiomedicalconcept)) %then %do;    
        , root.biomedicalConceptId length=64
        %if &include_package_dates %then %do; 
          , root.latest_package_date as biomedicalConceptId_PackageDate label="" length=10
        %end;
        , var.dataElementConceptId length=64
      %end;
      
      , root.sdtmigStartVersion
      , root.sdtmigEndVersion
      , root.domain
      , root.source
      , root.datasetSpecializationId
      
      , root.shortName

      %if %sysfunc(exist(&jsonlib..variables)) %then %do;    
        , var.ordinal_variables
        , var.name
        /* , var.dataElementConceptId */
        , var.isNonStandard
        , var.subsetCodelist
        , var.role
        , var.dataType
        , var.length
        , var.format
        , var.significantDigits
        , var.mandatoryVariable
        , var.mandatoryValue
        , var.originType
        , var.originSource
        , var.comparator
        , var.vlmTarget
      %end;
       
      %if %sysfunc(exist(&jsonlib..variables_codelist)) %then %do;    
        , varcl.conceptId as codelist
        , varcl.href as codelist_href
        , varcl.submissionValue as codelist_submission_value
      %end;
       
      %if %sysfunc(exist(&jsonlib..variables_valuelist)) %then %do;    
      , varvl._valueList as value_list
      %end;
          
      %if %sysfunc(exist(&jsonlib..variables_assignedterm)) %then %do;    
        , varat.conceptId as assigned_term
        , varat.value as assigned_value
      %end;
            
      %if %sysfunc(exist(&jsonlib..variables_relationship)) %then %do;    
        , varrel.subject
        , varrel.linkingPhrase
        , varrel.predicateTerm
        , varrel.object
      %end;
    from
      work.root root
  %if %sysfunc(exist(&jsonlib.._links_self)) %then %do;    
      left join &jsonlib.._links_self self 
    on (self.ordinal_self=root.ordinal_root)
  %end;  
  %if %sysfunc(exist(&jsonlib.._links_parentpackage)) %then %do;    
      left join &jsonlib.._links_parentpackage pp 
    on (pp.ordinal_parentpackage=root.ordinal_root)
  %end;  
  %if %sysfunc(exist(&jsonlib.._links_parentbiomedicalconcept)) %then %do;    
      left join &jsonlib.._links_parentbiomedicalconcept pbc 
    on (pbc.ordinal_parentbiomedicalconcept=root.ordinal_root)
  %end;  
  %if %sysfunc(exist(&jsonlib..variables)) %then %do;    
      left join work.variables var 
    on (var.ordinal_root=root.ordinal_root)
  %end;  
  %if %sysfunc(exist(&jsonlib..variables_codelist)) %then %do;    
      left join &jsonlib..variables_codelist varcl 
    on (varcl.ordinal_variables=var.ordinal_variables)
  %end;  
  %if %sysfunc(exist(&jsonlib..variables_assignedterm)) %then %do;    
      left join &jsonlib..variables_assignedterm varat 
    on (varat.ordinal_variables=var.ordinal_variables)
  %end;  
  %if %sysfunc(exist(&jsonlib..variables_valuelist)) %then %do;    
      left join work.variables_valuelist varvl 
    on (varvl.ordinal_variables=var.ordinal_variables)
  %end;  
  %if %sysfunc(exist(&jsonlib..variables_relationship)) %then %do;    
      left join &jsonlib..variables_relationship varrel 
    on (varrel.ordinal_variables=var.ordinal_variables)
  %end;
    order by datasetSpecializationId, name
      ;
    ;
  quit;  

  data &out;
    set &template &out;
  run;   

  %****************************;
  %*  Handle any errors here  *;
  %****************************;
  %exit_get_json:

  filename jsonfile clear;
  filename mapfile clear;
 
%mend read_sdtm_from_json;
