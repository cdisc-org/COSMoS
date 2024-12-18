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

  %if %sysfunc(exist(&dsout)) %then %do;
    %put WAR%str(NING): dataset &dsout already exists.;
    %goto exit_macro;
  %end;
  
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

  %exit_macro:;

%mend get_latest_sdtm_api;

%let root=C:/_github/cdisc-org/COSMoS;
%include "&root/utilities/config.sas";

%let packageDate=2024-12-17;
%let packageDateShort=%sysfunc(compress(&packageDate, %str(-)));
%let temp_location=%sysfunc(pathname(work));
%*let temp_location=&root/utilities/test;

proc format;
  value yesno
  0 = 'N'
  1 = 'Y'
  . = " ";
run;  

%create_template(type=sdtm, out=work.sdtm__template);

%global _sdtm_nobs;    
%get_latest_sdtm_api(dsout=data.sdtm_latest_&packageDateShort);

proc sql noprint;
  select count(distinct vlm_group_id) into :_sdtm_n trimmed
  from data.sdtm_latest_&packageDateShort
  ;
run;

proc sort data=data.sdtm_latest_&packageDateShort out=work.domains(keep=domain) nodupkey;
 by domain;
run; 


proc sql;
  create table work.readme
    (
     group char(32) label="Group",
     order num label="Order",
     class char(32) label="Class",
     column char(32) label="Column",
     description char(256) label="Description"
    )
    ;
  insert into work.readme
    values("SDTM Group", 1, "SDTMGroup", "package_date", "Biomedical Concept package release date indicating when the BC package was published to production")
    values("SDTM Group", 1, "SDTMGroup", "bc_id", "Biomedical Concept identifier foreign key")
    values("SDTM Group", 1, "SDTMGroup", "sdtmig_start_version", "The earliest SDTMIG version applicable to the BC dataset specialization")
    values("SDTM Group", 1, "SDTMGroup", "sdtmig_end_version", "The last SDTMIG version that is applicable to the BC dataset specialization")
    values("SDTM Group", 1, "SDTMGroup", "domain", "Domain for the SDTM specialization group")
    values("SDTM Group", 1, "SDTMGroup", "vlm_source", "SDTM VLM Source which categorizes VLM groups by topic variable")
    values("SDTM Group", 1, "SDTMGroup", "vlm_group_id", "Identifier for SDTM Value Level Metadata group")
    values("SDTM Group", 1, "SDTMGroup", "short_name", "SDTM group short name which provides a user friendly and intuitive name for the vlm_group_id")
    values("SDTM Variable", 1, "SDTMVariable", "sdtm_variable", "Variable included in the SDTM dataset specialization")
    values("SDTM Variable", 1, "SDTMVariable", "dec_id", "Biomedical Concept Data Element Concept idenfifier foreign key")
    values("SDTM Variable", 1, "SDTMVariable", "nsv_flag", "Flag that indicates if the variable is a non-standard variable")
    values("SDTM Variable", 2, "CodeList", "codelist", "C-code for a codelist in NCIt")
    values("SDTM Variable", 2, "CodeList", "codelist_submission_value", "CDISC submission value for the codelist")
    values("SDTM Variable", 3, "SDTMVariable", "subset_codelist", "Subset codelist short name")
    values("SDTM Variable", 3, "SDTMVariable", "value_list", "List of SDTM submission values used if subset codelist is not applicable")
    values("SDTM Variable", 4, "AssignedTerm", "assigned_term", "C-code for assigned term in NCIt or left blank when CDISC terminology does not apply")
    values("SDTM Variable", 4, "AssignedTerm", "assigned_value", "Submission value for assigned term in NCIt if it exists, or an assigned value which will be the default value")
    values("SDTM Variable", 5, "SDTMVariable", "role", "SDTM variable role")
    values("SDTM Variable", 6, "Relationship", "subject", "Subject in a variable relationship")
    values("SDTM Variable", 6, "Relationship", "linking_phrase", "Variable relationship descriptive linking phrase")
    values("SDTM Variable", 6, "Relationship", "predicate_term", "Short variable relationship linking phrase for programming purposes")
    values("SDTM Variable", 6, "Relationship", "object", "Object in a variable relationship")
    values("SDTM Variable", 7, "SDTMVariable", "data_type", "Variable data type")
    values("SDTM Variable", 7, "SDTMVariable", "length", "Variable length")
    values("SDTM Variable", 7, "SDTMVariable", "format", "Variable display format")
    values("SDTM Variable", 7, "SDTMVariable", "significant_digits", "Variable significant_digits")
    values("SDTM Variable", 7, "SDTMVariable", "mandatory_variable", "Indicator that variable must be present within the SDTM group")
    values("SDTM Variable", 7, "SDTMVariable", "mandatory_value", "Indicator that variable must be populated within the SDTM group")
    values("SDTM Variable", 7, "SDTMVariable", "origin_type", "Variable origin type (define-XML v21)")
    values("SDTM Variable", 7, "SDTMVariable", "origin_source", "Variable origin source (define-XML v21)")
    values("SDTM Variable", 7, "SDTMVariable", "comparator", " Comparison operator for SDTM group variables included in VLM")
    values("SDTM Variable", 7, "SDTMVariable", "vlm_target", "Target variable for VLM")
    ;
quit;    

%let headerstyle1 = {background=lightgreen color=black};
options  missing= " ";

ods listing close;
ods excel options(sheet_name="ReadMe" flow="tables") file="&temp_location/cdisc_sdtm_dataset_specializations_&packageDateShort..xlsx";

  proc report data=work.readme spanrows missing;
    columns group order column description class;
    define group / order style(column)={vjust=t};
    define order / order noprint;
    define column / style(column)={vjust=t};
    define description / style(column)={vjust=t};
    define class / order style(column)={vjust=t};
    
    compute before _page_ /
      style =[font_weight=bold just=l color=black];
      line "This spreadsheet contains the latest versions of CDISC SDTM Dataset Specializations in the CDISC Library as of &packageDate..";
      line "There are currently &_sdtm_n unique CDISC SDTM Dataset Specializations in the CDISC Library.";
      line "The image on the right shows the relation between Biomedical Concepts and SDTM Dataset Specializations.";
      line "Only a few attributes are shown in the image.";
    endcomp;  
  run;  

ods excel options(sheet_name="SDTM Dataset Specializations" flow="tables" autofilter = 'all');

  title "Latest SDTM Dataset Specializations generated on &today";
    proc report data=data.sdtm_latest_&packageDateShort;
      columns package_date bc_id sdtmig_start_version sdtmig_end_version domain vlm_source vlm_group_id short_name
              sdtm_variable dec_id nsv_flag codelist_href codelist codelist_submission_value subset_codelist
              value_list assigned_term assigned_value role subject linking_phrase predicate_term object 
              data_type length format significant_digits mandatory_variable mandatory_value origin_type origin_source comparator vlm_target;
      define codelist_href / noprint; 
      
      define package_date / style(header) = &headerstyle1;
      define bc_id / style(header) = &headerstyle1;
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
          call define (_col_, 'url', cats("&ncit_explore", bc_id));
          call define (_col_, "style","style={textdecoration=underline color=#0000FF}");
        end;  
      endcomp;

      compute dec_id;
        if not missing(dec_id) and index(dec_id, "NEW")=0 then do;
          call define (_col_, 'url', cats("&ncit_explore", dec_id));
          call define (_col_, "style","style={textdecoration=underline color=#0000FF}");
        end;  
      endcomp;

      compute codelist;
        if not missing(codelist) then do;
          call define (_col_, 'url', cats("&ncit_explore", codelist));
          call define (_col_, "style","style={textdecoration=underline color=#0000FF}");
        end;  
      endcomp;

  run;  
  
ods excel options(sheet_name="Domains" flow="tables" autofilter = 'none');

  proc report data=work.domains;
    columns domain;
  run;  
  
ods excel close;
ods listing;

/* Add image to ReadMe */
data _null_;
  call insert_image(
    "&temp_location/cdisc_sdtm_dataset_specializations_&packageDateShort..xlsx",
    "&root/utilities/downloads/cdisc_sdtm_dataset_specializations_&packageDateShort..xlsx",
    "&root/utilities/images/bc-sdtm-erd-light.png",
    "ReadMe",
    "F2",
    439,
    480
  );
