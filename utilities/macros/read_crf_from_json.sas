%macro read_crf_from_json(json_path=, jsonlib=, maplib=work, template=, out=, include_package_dates=0);

  proc datasets library=&jsonlib kill nolist;
  quit;

  filename jsonfile "&json_path";
  filename mapfile "%sysfunc(pathname(&maplib))/specialization.map";

  libname jsonfile json map=mapfile automap=create fileref=jsonfile /* noalldata ordinalcount=none */;
  proc copy in=jsonfile out=&jsonlib;
  run;

  /*
  proc contents data=jsonfile._ALL_ varnum;
  run;  
  */
  
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

  data work.items;
    set &template %if %sysfunc(exist(&jsonlib..items)) %then &jsonlib..items;;
  run;  
  
  %if %sysfunc(exist(&jsonlib..items_prepopulatedvalue)) %then %do;    
    data work.items_prepopulatedvalue;
      set &jsonlib..items_prepopulatedvalue;
  %end;

  %if %sysfunc(exist(&jsonlib..items_valuelist)) %then %do;    
    data work.items_valuelist;
      set &jsonlib..items_valuelist end=end;
      length _value _valuedisplay $ 2048;
      retain _value _valuedisplay;
      if _n_=1 then do;
        _value="";
        _valuedisplay="";
      end;  
      _value = catx(";", _value, value);
      _valuedisplay = catx(";", _valuedisplay, displayValue);
      if end then output;
    run;
  %end;

  proc sql;
    create table &out /* (drop=ordinal_items) */
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
        , item.dataElementConceptId as dataElementConceptId length=64 label=""
      %end;
      %if not %sysfunc(exist(&jsonlib.._links_parentbiomedicalconcept)) %then %do;    
        , root.biomedicalConceptId length=64
        %if &include_package_dates %then %do; 
          , root.latest_package_date as biomedicalConceptId_PackageDate label="" length=10
        %end;
        , item.dataElementConceptId length=64
      %end;
      
      , root.standard
      , root.standardStartVersion
      , root.standardEndVersion
      , root.domain
      , root.implementationOption
      , root.scenario
      , root.crfSpecializationId
      /* , root.sdtmDatasetSpecializationId */
      , root.shortName

      %if %sysfunc(exist(&jsonlib..items)) %then %do;    
        , item.ordinal_items
        , item.name as crfItem
        /* , item.dataElementConceptId */
        , item.variableName as variable
        , item.questionText
        , item.prompt
        , item.completionInstructions
        , item.orderNumber
        , item.mandatoryVariable
        , item.dataType
        , item.length
        , item.significantDigits
        , item.displayHidden
        , item.derivedVariable
        , item.derivationDescription
        /* , item.selectionType */
      %end;

      %if %sysfunc(exist(&jsonlib..items_codelist)) %then %do;    
        , itemcl.conceptId as codelist
        , itemcl.href as codelist_href
        , itemcl.submissionValue as codelist_submission_value
      %end;
       
      %if %sysfunc(exist(&jsonlib..items_valuelist)) %then %do;    
      , itemvl._value as value_list
      , itemvl._valuedisplay as value_list_display
      %end;
          
      %if %sysfunc(exist(&jsonlib..items_prepopulatedvalue)) %then %do;  
        %if %varexist(&jsonlib..items_prepopulatedvalue, conceptId) %then %do;  
        , itempv.conceptId as prepopulated_code
        %end;
        , itempv.value as prepopulated_term
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
  %if %sysfunc(exist(&jsonlib..items)) %then %do;    
      left join work.items item 
    on (item.ordinal_root=root.ordinal_root)
  %end;  
  %if %sysfunc(exist(&jsonlib..items_codelist)) %then %do;    
      left join &jsonlib..items_codelist itemcl 
    on (itemcl.ordinal_items=item.ordinal_items)
  %end;  
  %if %sysfunc(exist(&jsonlib..items_prepopulatedvalue)) %then %do;    
      left join &jsonlib..items_prepopulatedvalue itempv 
    on (itempv.ordinal_items=item.ordinal_items)
  %end;  
  %if %sysfunc(exist(&jsonlib..items_valuelist)) %then %do;    
      left join work.items_valuelist itemvl 
    on (itemvl.ordinal_items=item.ordinal_items)
  %end;  
    order by crfSpecializationId, crfItem
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
 
%mend read_crf_from_json;
