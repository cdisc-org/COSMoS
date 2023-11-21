%macro get_latest_sdtm_api(dsout=);

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
        shortName = short_name
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

  proc sort data=work.sdtm_latest out=&dsout(drop=ordinal_variables);
    by domain vlm_group_id ordinal_variables;
  run;

%mend get_latest_sdtm_api;

%let root=C:/_github/cdisc-org/COSMoS;
%include "&root/utilities/config.sas";

%let rest_debug=%str(OUTPUT_TEXT NO_REQUEST_HEADERS NO_REQUEST_BODY RESPONSE_HEADERS NO_RESPONSE_BODY);
%let base_url_cosmos=https://library.cdisc.org/api/cosmos/v2;
%* The CDISC Library API key has been set as an environment variable;
%let api_key=%sysget(CDISC_LIBRARY_API_KEY);

  proc format;
    value yesno
    0 = 'N'
    1 = 'Y'
    . = " ";
  run;  

%create_template(type=sdtm, out=work.sdtm__template);
    
%*get_latest_sdtm_api(dsout=data.sdtm_latest);

proc sql;
  create table work.readme
    (
     column char(32) label="Column",
     description char(256) label="Description"
    )
    ;
  insert into work.readme
    values("package_date", "Biomedical Concept package release date indicating when the BC package was published to production")
    values("bc_id", "A unique identifier for a Biomedical Concept which will be assigned as the NCIt code if it exists or a placeholder identifier if the concept is not yet available in NCIt")
    values("dec_id", "NCI C-code for the BC Data Element Concep")
    values("sdtmig_start_version", "The earliest SDTMIG version applicable to the BC dataset specialization")
    values("sdtmig_end_version", "The last SDTMIG version that is applicable to the BC dataset specialization")
    values("domain", "Domain for the SDTM specialization group")
    values("vlm_source", "SDTM VLM Source which categorizes VLM groups by topic variable")
    values("vlm_group_id", "Identifier for SDTM Value Level Metadata group")
    values("short_name", "SDTM group short name which provides a user friendly and intuitive name for the vlm_group_id")
    values("sdtm_variable", "Variable included in the SDTM dataset specialization")
    values("nsv_flag", "Flag that indicates if the variable is a non-standard variable")
    values("codelist", "CodeList")
    values("codelist_submission_value", "CDISC submission value for the codelist")
    values("subset_codelist", "Subset codelist short name")
    values("value_list", "List of SDTM submission values used if subset codelist is not applicable")
    values("assigned_term", "C-code for assigned term in NCIt or left blank when CDISC terminology does not apply")
    values("assigned_value", "Submission value for assigned term in NCIt if it exists, or an assigned value which will be the default value")
    values("role", "SDTM variable role")
    values("subject", "Subject in a variable relationship")
    values("linking_phrase", "Variable relationship descriptive linking phrase")
    values("predicate_term", "Short variable relationship linking phrase for programming purposes")
    values("object", "Object in a variable relationship")
    values("data_type", "Variable data type")
    values("length", "Variable length")
    values("format", "Variable display format")
    values("significant_digits", "Variable significant_digits")
    values("mandatory_variable", "Indicator that variable must be present within the SDTM group")
    values("mandatory_value", "Indicator that variable must be populated within the SDTM group")
    values("origin_type", "Variable origin type (define-XML v21)")
    values("origin_source", "Variable origin source (define-XML v21)")
    values("comparator", " Comparison operator for SDTM group variables included in VLM")
    values("vlm_target", "Target variable for VLM")
    ;
quit;    

%let headerstyle1 = {background=lightgreen color=black};
options  missing= " ";

ods listing close;
ods excel options(sheet_name="ReadMe" flow="tables") file="&root/utilities/reports/sdtm_dataset_specializations_&today..xlsx";


  ods text = "This spreadsheet contains  the latest versions of CDISC SDTM Dataset Specializations as of &today.";
  
  proc report data=work.readme;
    columns column description;
  run;  

ods excel options(sheet_name="SDTM Dataset Specializations" flow="tables" autofilter = 'all');

  title "Latest SDTM Dataset Specializations generated on %sysfunc(datetime(), is8601dt.))";
    proc report data=data.sdtm_latest;
      columns package_date bc_id dec_id sdtmig_start_version sdtmig_end_version domain vlm_source vlm_group_id short_name
              sdtm_variable nsv_flag codelist_href codelist codelist_submission_value subset_codelist
              value_list assigned_term assigned_value role subject linking_phrase predicate_term object 
              data_type length format significant_digits mandatory_variable mandatory_value origin_type origin_source comparator vlm_target;
      define codelist_href / noprint; 
      
      define package_date / style(header) = &headerstyle1;
      define bc_id / style(header) = &headerstyle1;
      define dec_id / style(header) = &headerstyle1;
      define sdtmig_start_version / style(header) = &headerstyle1;
      define sdtmig_end_version / style(header) = &headerstyle1;
      define domain / style(header) = &headerstyle1;
      define vlm_source / style(header) = &headerstyle1;
      define vlm_group_id / style(header) = &headerstyle1;
      define short_name / style(header) = &headerstyle1;

      define nsv_flag / format = yesno.;
      define mandatory_variable / format = yesno.;
      define mandatory_value / format = yesno.;
      define vlm_target / format = yesno.;
                 
      compute bc_id;
        if not missing(bc_id) and index(bc_id, "NEW")=0 then do;
          call define (_col_, 'url', cats('https://ncithesaurus.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=', bc_id));
          call define (_col_, "style","style={textdecoration=underline color=#0000FF}");
        end;  
      endcomp;

      compute dec_id;
        if not missing(dec_id) and index(dec_id, "NEW")=0 then do;
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
