%macro read_bc_from_json(json_path=, jsonlib=, template=, out=, include_package_dates=0, clean=1);

  filename jsonfile "&json_path";
  filename mapfile "%sysfunc(pathname(work))/bc.map";

  libname jsonfile json map=mapfile automap=create fileref=jsonfile /* noalldata ordinalcount=none */;
  proc copy in=jsonfile out=&jsonlib;
  run;

  data work.root;
    set &template &jsonlib..root;
  run;  

  %if %sysfunc(exist(&jsonlib..dataelementconcepts_exampleset)) %then %do;    
    data work.dataelementconcepts_exampleset(drop=exampleSet:);
      set &jsonlib..dataelementconcepts_exampleset;
      length _exampleSets $ 1024; 
      array exampleSets_{*} $ 32 exampleSet:;
      _exampleSets = catx(";", OF exampleSets_{*});
    run;
  %end;
    
  %if %sysfunc(exist(&jsonlib..category)) %then %do;    
    data work.category;
      set &jsonlib..category;
      length _category $ 1024; 
      array category_{*} $ 32 category:;
      _category = catx(";", OF category_{*});
    run;
  %end;

  %if %sysfunc(exist(&jsonlib..synonym)) %then %do;    
    data work.synonym;
      set &jsonlib..synonym;
      length _synonym $ 1024; 
      array synonym_{*} $ 32 synonym:;
      _synonym = catx(";", OF synonym_{*});
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
      %end;
      
      %if %sysfunc(exist(&jsonlib..category)) %then %do;    
        , catd._category as category
      %end;
      
      , root.href
      
      , root.shortName
      %if %sysfunc(exist(&jsonlib..synonym)) %then %do;      
        , synd._synonym as synonym
      %end;
      , root.resultScale
      , root.Definition
      %if %sysfunc(exist(&jsonlib..coding)) %then %do;      
        , cd._system as system
        , cd._systemName as systemName
        , cd._code as code
      %end;  
      %if %sysfunc(exist(&jsonlib..dataelementconcepts)) %then %do;
        , dec.conceptId as dec_conceptId
        , dec.href as dec_href
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
  %if %sysfunc(exist(&jsonlib..synonym)) %then %do;      
      left join work.synonym synd 
    on (synonym.ordinal_root=root.ordinal_root)
  %end;
  %if %sysfunc(exist(&jsonlib..category)) %then %do;    
      left join work.category catd 
    on (category.ordinal_root=root.ordinal_root)
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

  filename jsonfile clear;
  filename mapfile clear;

  data &out;
    set &template &out;
  run;   

  %if &clean %then %do;
    proc datasets library=&jsonlib kill nolist;
    quit;
    run;
  %end;  

%mend read_bc_from_json;
