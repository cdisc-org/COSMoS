%macro get_sdtm(code);

  %local code_short;
  %let code_short = &code;

  %if %length(&code) gt 24 %then %let code_short = %substr(&code, 1, 24);

  %get_api_response(
    baseurl=&base_url_cosmos,
    endpoint=/mdr/specializations/sdtm/datasetspecializations/&code,
    response_file=%sysfunc(pathname(work))/sdtm_datasetspecialization_&code..json
  );

  %read_sdtm_from_json(
    json_path=%sysfunc(pathname(work))/sdtm_datasetspecialization_&code..json, 
    jsonlib=jsontmp, 
    maplib=work, 
    template=work.sdtm__template, 
    out=work.sdtm__&code_short, 
    include_package_dates=0
    );

%mend get_sdtm;  

%let root=C:/_github/cdisc-org/COSMoS;
%include "&root/utilities/config.sas";

%let rest_debug=%str(OUTPUT_TEXT NO_REQUEST_HEADERS NO_REQUEST_BODY RESPONSE_HEADERS NO_RESPONSE_BODY);
%let base_url_cosmos=https://library.cdisc.org/api/cosmos/v2;
%* The CDISC Library API key has been set as an environment variable;
%let api_key=%sysget(CDISC_LIBRARY_API_KEY);

%create_template(type=sdtm, out=work.sdtm__template);

%get_api_response(
    baseurl=&base_url_cosmos,
    endpoint=/mdr/specializations/datasetspecializations,
    response_file=%sysfunc(pathname(work))/sdtm_datasetspecializations_latest.json
  );

%put %sysfunc(dcreate(jsontmp, %sysfunc(pathname(work))));
libname jsontmp "%sysfunc(pathname(work))/jsontmp";

filename jsfile "%sysfunc(pathname(work))/sdtm_datasetspecializations_latest.json";
filename mpfile "%sysfunc(pathname(work))/sdtm_latest.map";
libname jsfile json map=mpfile automap=create fileref=jsfile noalldata ordinalcount=none;

  data sdtm_latest(keep=datasetSpecializationId);
    length datasetSpecializationId $128 code $512;
    set jsfile.datasetSpecializations_sdtm;
    datasetSpecializationId = scan(href, -1, "/");
        code=cats('%nrstr(%get_sdtm(',
                            'code=', datasetSpecializationId,
                          ');)');
        call execute(code);
    
  run;

filename jsfile clear;
filename mpfile clear;
libname jsfile clear;


data work.sdtm_latest(
  rename=(
      packageDate = package_date
      biomedicalConceptId = bc_id
      dataElementConceptId = dec_id
      sdtmigStartVersion = sdtmig_start_version
      sdtmigEndVersion = sdtmig_end_version
      source = vlm_source
      datasetSpecializationId = vlm_group_id
      name = sdtm_variable 
      isNonStandard = nsv_flag
      subsetCodelist = subset_codelist
      linkingPhrase = linking_phrase
      predicateTerm = predicate_term
      dataType= data_type
      significantDigits = significant_digits
      mandatoryVariable = mandatory_variable
      mandatoryValue = mandatory_value
      originType = origin_type
      originSource = origin_source
      vlmTarget = vlm_target 
  )
  );
  set work.sdtm__:;
run;


proc contents data=work.sdtm_latest varnum;
run;

ods listing close;
ods excel options(sheet_name="SDTM Dataset Specializations" flow="tables" autofilter = 'all') file="&root/utilities/reports/sdtm_datasetspecializations_&today..xlsx";

  title "Latest SDTM Dataset Specializations generated on %sysfunc(datetime(), is8601dt.))";
    proc report data=work.sdtm_latest;
      columns vlm_group_id bc_id dec_id sdtmig_start_version sdtmig_end_version 
              domain vlm_source shortName sdtm_variable nsv_flag codelist_href codelist codelist_submission_value subset_codelist
              value_list assigned_term assigned_value role subject linking_phrase predicate_term object 
              data_type length format significant_digits mandatory_variable mandatory_value origin_type origin_source comparator vlm_target;
      define codelist_href / noprint; 
                 
      compute dec_id;
        if not missing(dec_id) then do;
          call define (_col_, 'url', cats('https://ncithesaurus.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=', dec_id));
          call define (_col_, "style","style={textdecoration=underline color=#0000FF}");
        end;  
      endcomp;

      compute codelist;
        if not missing(codelist) then do;
          call define (_col_, 'url', codelist_href);
          call define (_col_, "style","style={textdecoration=underline color=#0000FF}");
        end;  
      endcomp;

  run;  
  
ods excel close;
ods listing;
