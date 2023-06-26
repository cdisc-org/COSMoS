%macro read_bc_from_json(json_path=, jsonlib=, maplib=work, template=, out=, include_package_dates=0);

  proc datasets library=&jsonlib kill nolist;
  quit;

  filename jsonfile "&json_path";
  filename mapfile "%sysfunc(pathname(&maplib))/bc.map";

  libname jsonfile json map=mapfile automap=create fileref=jsonfile /* noalldata ordinalcount=none */;
  proc copy in=jsonfile out=&jsonlib;
  run;

  %if &SYSERR %then %do;
    %put ### &_package - &bc;
    %goto exit_get_json;
  %end;

  data work.root;
    set &template &jsonlib..root;
  run;  

  %if not %sysfunc(exist(&jsonlib..._links_parentbiomedicalconcept)) and &include_package_dates %then %do;    

    data work.root;
      merge work.root(in=in1) data.latest_bc(keep=biomedicalConceptId latest_package_date rename=(biomedicalConceptId=parentConceptId) );
      by parentConceptId;
      if in1;
    run;  

  %end;


  %if %sysfunc(exist(&jsonlib..dataelementconcepts_exampleset)) %then %do;    
    data work.dataelementconcepts_exampleset(drop=exampleSet:);
      set &jsonlib..dataelementconcepts_exampleset;
      length _exampleSets $ 32000; 
      array exampleSets_{*} $ 32 exampleSet:;
      _exampleSets = catx(";", OF exampleSets_{*});
    run;
  %end;
    
  %if %sysfunc(exist(&jsonlib..categories)) %then %do;    
    data work.categories;
      set &jsonlib..categories;
      length _categories $ 4096; 
      array categories_{*} $ 32 categories:;
      _categories = catx(";", OF categories_{*});
    run;
  %end;

  %if %sysfunc(exist(&jsonlib..synonyms)) %then %do;    
    data work.synonyms;
      set &jsonlib..synonyms;
      length _synonyms $ 1024; 
      array synonyms_{*} $ 32 synonyms:;
      _synonyms = catx(";", OF synonyms_{*});
    run;
  %end;

  %if %sysfunc(exist(&jsonlib..resultscales)) %then %do;    
    data work.resultscales;
      set &jsonlib..resultscales;
      length _resultscales $ 256; 
      array resultscales_{*} $ 32 resultscales:;
      _resultscales = catx(";", OF resultscales_{*});
    run;
  %end;

  %if %sysfunc(exist(&jsonlib..coding)) %then %do;    
    data work.coding;
      set &jsonlib..coding end=end;
      length _code _system _systemname $ 1000; 
      retain _code _system _systemname; 
      if _n_=1 then do
        _code="";
        _system="";
        _systemName="";
      end ; 
      _code = catx(";", _code, code);
      _system = catx(";", _system, system);
      _systemname = catx(";", _systemname, systemname);
      if end then output;
    run;
  %end;

  proc sql;
    create table &out
    as select
      %if %sysfunc(exist(&jsonlib.._links_parentpackage)) %then %do;    
        scan(pp.title, -1, " ") as packageDate length=10
      %end;
      %if not %sysfunc(exist(&jsonlib.._links_parentpackage)) %then %do;    
        root.packageDate length=10
      %end;
      
      %if &include_package_dates %then %do;
        %if %sysfunc(exist(&jsonlib.._links_self)) %then %do;    
          , scan(self.href, -3, "\/") as ConceptId_PackageDate length=10
        %end;
        %if not %sysfunc(exist(out._links_self)) %then %do;    
          , root.packageDate as ConceptId_PackageDate length=10
        %end;
      %end;

      , root.conceptId

      %if %sysfunc(exist(&jsonlib.._links_parentbiomedicalconcept)) %then %do;    
        , scan(pbc.href, -1, "\/") as parentConceptId length=64
        %if &include_package_dates %then %do; 
          , scan(pbc.href, -3, "\/") as parentConceptId_PackageDate length=10 
        %end;
      %end;
      %if not %sysfunc(exist(&jsonlib.._links_parentbiomedicalconcept)) %then %do;    
        , root.parentConceptId length=64
        %if &include_package_dates %then %do; 
          , root.latest_package_date as parentConceptId_PackageDate length=10
        %end;
      %end;
      
      %if %sysfunc(exist(&jsonlib..categories)) %then %do;    
        , catd._categories as categories
      %end;
      
      , root.href
      , root.ncitCode as ncitCode
      
      , root.shortName
      %if %sysfunc(exist(&jsonlib..synonyms)) %then %do;      
        , synd._synonyms as synonyms
      %end;
      %if %sysfunc(exist(&jsonlib..resultscales)) %then %do;      
        , res._resultscales as resultscales
      %end;
      , root.Definition
      %if %sysfunc(exist(&jsonlib..coding)) %then %do;      
        , cd._system as system
        , cd._systemName as systemName
        , cd._code as code
      %end;  
      %if %sysfunc(exist(&jsonlib..dataelementconcepts)) %then %do;
        , dec.conceptId as dec_conceptId
        , dec.href as dec_href
        , dec.ncitCode as dec_ncitCode
        , dec.shortName as dec_shortName
        , dec.dataType as dec_dataType
      %end;
      %if %sysfunc(exist(&jsonlib..dataelementconcepts_exampleset)) %then %do;    
        , decex._exampleSets as dec_exampleSet
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
  %if %sysfunc(exist(&jsonlib..coding)) %then %do;  
      left join work.coding cd 
    on (coding.ordinal_root=root.ordinal_root)
  %end;
  %if %sysfunc(exist(&jsonlib..synonyms)) %then %do;      
      left join work.synonyms synd 
    on (synonyms.ordinal_root=root.ordinal_root)
  %end;
  %if %sysfunc(exist(&jsonlib..resultscales)) %then %do;      
      left join work.resultscales res 
    on (res.ordinal_root=root.ordinal_root)
  %end;
  %if %sysfunc(exist(&jsonlib..categories)) %then %do;    
      left join work.categories catd 
    on (categories.ordinal_root=root.ordinal_root)
  %end;
  %if %sysfunc(exist(&jsonlib..dataelementconcepts)) %then %do;
        left join &jsonlib..dataelementconcepts dec 
    on (dec.ordinal_root=root.ordinal_root)
  %end;
  %if %sysfunc(exist(&jsonlib..dataelementconcepts_exampleset)) %then %do;    
      left join work.dataelementconcepts_exampleset decex 
    on (decex.ordinal_dataelementconcepts=dec.ordinal_dataelementconcepts)
  %end;
    order by conceptId %if %sysfunc(exist(&jsonlib..dataelementconcepts)) %then, dec.ordinal_dataElementConcepts, dec_ConceptId;;
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

%mend read_bc_from_json;
