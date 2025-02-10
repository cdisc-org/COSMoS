%macro get_latest_codelist_package(package=, jsonout=, dsout=);
    
  filename response temp;
  filename map temp;

  %get_api_response(
      baseurl=&base_url,
      endpoint=/mdr/products,
      response_fileref=response,
      apikey=&api_key
    );

  libname response json map=map automap=create fileref=response;

  proc sql noprint;
    select 
      href into :_latest_ctpackage trimmed
    from response._links_packages
    where index(href, "&package") > 0
    order by href DESC
    ;
  quit;

  %put &=_latest_ctpackage;

  libname response clear;
  filename response clear;
  filename map clear;

  filename response "&jsonout";
  filename map temp;

  
  %get_api_response(
      baseurl=&base_url,
      endpoint=&_latest_ctpackage,
      response_fileref=response
    );

  libname response json map=map automap=create fileref=response;

  proc sql;
    create table &dsout
    as select
      root.name as name,
      root.version as codelist_version,
      cl.conceptId  as codelist_conceptId,
      cl.name as codelist_name,
      cl.submissionValue as codelist_submissionValue,
      case 
        when cl.extensible = "true" then "Yes"
        when cl.extensible = "false" then "No"
        else ""
      end as codelist_extensible,
      cli.submissionValue as codedValue,
      cli.conceptId as codedValue_conceptId,
      cli.preferredTerm as preferredTerm
    from response.root root 
    inner join response.codelists cl 
      on root.ordinal_root = cl.ordinal_root
    inner join response.codelists_terms cli
      on cl.ordinal_codelists = cli.ordinal_codelists
    order by codelist_version, codelist_submissionValue, codedvalue;
  quit;

  libname response clear;
  filename response clear;
  filename map clear;

%mend get_latest_codelist_package;
