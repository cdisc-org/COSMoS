%macro get_bc(code);

  %get_api_response(
    baseurl=&base_url_cosmos,
    endpoint=/mdr/bc/biomedicalconcepts/&code,
    response_file=%sysfunc(pathname(work))/biomedicalconcept_&code..json
  );

  %read_bc_from_json(
    json_path=%sysfunc(pathname(work))/biomedicalconcept_&code..json, 
    jsonlib=jsontmp, 
    maplib=work, 
    template=work.bc__template, 
    out=work.bc__&code, 
    include_package_dates=0
    );

%mend get_bc;  

%let root=C:/_github/cdisc-org/COSMoS;
%include "&root/utilities/config.sas";

%let rest_debug=%str(OUTPUT_TEXT NO_REQUEST_HEADERS NO_REQUEST_BODY RESPONSE_HEADERS NO_RESPONSE_BODY);
%let base_url_cosmos=https://library.cdisc.org/api/cosmos/v2;
%* The CDISC Library API key has been set as an environment variable;
%let api_key=%sysget(CDISC_LIBRARY_API_KEY);

%create_template(type=bc, out=work.bc__template);

%get_api_response(
    baseurl=&base_url_cosmos,
    endpoint=/mdr/bc/biomedicalconcepts,
    response_file=%sysfunc(pathname(work))/biomedicalconcept_latest.json
  );

%put %sysfunc(dcreate(jsontmp, %sysfunc(pathname(work))));
libname jsontmp "%sysfunc(pathname(work))/jsontmp";

filename jsfile "%sysfunc(pathname(work))/biomedicalconcept_latest.json";
filename mpfile "%sysfunc(pathname(work))/bc_latest.map";
libname jsfile json map=mpfile automap=create fileref=jsfile noalldata ordinalcount=none;

  data bc_latest(keep=biomedicalConceptId);
    length biomedicalConceptId $64 code $512;
    set jsfile._links_biomedicalconcepts;
    biomedicalConceptId = scan(href, -1, "/");
        code=cats('%nrstr(%get_bc(',
                            'code=', biomedicalConceptId,
                          ');)');
        call execute(code);
    
  run;

filename jsfile clear;
filename mpfile clear;
libname jsfile clear;

data work.bc_latest(
  rename=(
      packageDate = package_date
      conceptId = bc_id
      categories = bc_categories
      ncitCode = ncit_code
      parentConceptId = parent_bc_id
      shortName = short_name
      resultScales = result_scales
      systemName = system_name
      dec_ConceptId = dec_id
      dec_ncitCode = ncit_dec_code
      dec_ShortName = dec_label
      dec_dataType = data_type
      dec_exampleSet = example_set
  )
  );
  set work.bc__:;
run;

ods listing close;
ods excel options(sheet_name="BiomedicalConcepts" flow="tables" autofilter = 'all') file="&root/utilities/reports/biomedical_concepts_&today..xlsx";

  title "Latest Biomedical Concepts generated on %sysfunc(datetime(), is8601dt.))";
  proc report data=work.bc_latest;
    columns package_date bc_categories href bc_id ncit_code parent_bc_id short_name synonyms result_scales definition system system_name code
             dec_href dec_id ncit_dec_code dec_label data_type example_set;
    
    define href / noprint; 
    define dec_href / noprint;
               
    compute ncit_code;
      if not missing(ncit_code) then do;
        call define (_col_, 'url', href);
        call define (_col_, "style","style={textdecoration=underline color=#0000FF}");
      end;  
    endcomp;

    compute ncit_dec_code;
      if not missing(ncit_dec_code) then do;
        call define (_col_, 'url', dec_href);
        call define (_col_, "style","style={textdecoration=underline color=#0000FF}");
      end;  
    endcomp;

    compute parent_bc_id;
      if not missing(parent_bc_id) then do;
        call define (_col_, 'url', cats('https://ncithesaurus.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=', parent_bc_id));
        call define (_col_, "style","style={textdecoration=underline color=#0000FF}");
      end;  
    endcomp;

  run;  
  
ods excel close;
ods listing;
