%macro get_latest_codelist_package(package=, jsonout=, dsout=);

  %local api_key;
    
  %let api_key=%sysget(CDISC_LIBRARY_API_KEY);

  filename response temp;
  filename map temp;

  %get_api_response(
      baseurl=&base_url,
      endpoint=/mdr/products,
      response_fileref=response
    );

  libname response json map=map automap=create fileref=response;

  proc sql noprint;
    select 
      href into :_latest_sdtm_ctpackage trimmed
    from response._links_packages
    where index(href, "&package") > 0
    order by href DESC
    ;
  quit;

  %put &=_latest_sdtm_ctpackage;

  libname response clear;
  filename response clear;
  filename map clear;

  filename response "&jsonout";
  filename map temp;

  
  %if %sysfunc(fileexist(&jsonout)) %then %do;
    %put;
    %put WAR%str(NING): [&sysmacroname] The file &jsonout already exist. ;
    %put;
  %end;    
  %else %do;
 
    %get_api_response(
        baseurl=&base_url,
        endpoint=&_latest_sdtm_ctpackage,
        response_fileref=response
      );

  %end;

  libname response json map=map automap=create fileref=response;


  %if not %sysfunc(exist(&dsout)) %then %do;
    proc sql;
      create table &dsout
      as select
        root.name as name,
        root.version as codelist_version,
        cl.conceptId  as codelist_conceptId,
        cl.name as codelist_Name,
        cl.extensible,
        cl.submissionValue as codelist_submissionValue,
        cli.conceptId,
        cli.submissionValue as codedValue,
        cli.conceptId as codedValue_conceptId
      from response.root root 
      inner join response.codelists cl 
        on root.ordinal_root = cl.ordinal_root
      inner join response.codelists_terms cli
        on cl.ordinal_codelists = cli.ordinal_codelists
      order by codelist_version, codelist_submissionValue, codedvalue;
    quit;
  %end;

  libname response clear;
  filename response clear;
  filename map clear;

%mend get_latest_codelist_package;
