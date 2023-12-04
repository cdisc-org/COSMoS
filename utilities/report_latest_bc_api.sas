%macro get_latest_bc_api(dsout=);

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

  %if %sysfunc(exist(&dsout)) %then %do;
    %put WAR%str(NING): dataset &dsout already exists.;
    %goto exit_macro;
  %end;
  
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

  data &dsout(
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

  %exit_macro:;

%mend get_latest_bc_api;

%let root=C:/_github/cdisc-org/COSMoS;
%include "&root/utilities/config.sas";
%let packageDate=2023-12-12;
%let packageDateShort=20231212;


%let rest_debug=%str(OUTPUT_TEXT NO_REQUEST_HEADERS NO_REQUEST_BODY RESPONSE_HEADERS NO_RESPONSE_BODY);
%let base_url_cosmos=https://library.cdisc.org/api/cosmos/v2;
%* The CDISC Library API key has been set as an environment variable;
%let api_key=%sysget(CDISC_LIBRARY_API_KEY);

%create_template(type=bc, out=work.bc__template);

%get_latest_bc_api(dsout=data.bc_latest);

data work.categories(keep=category);
  length category $1024;
  set data.bc_latest(keep=bc_categories);
  countwords=countw(bc_categories, ";");
  do i=1 to countwords;
    category=strip(scan(bc_categories, i, ";"));
    output;
  end;
 run;
 
 proc sort data=work.categories nodupkey;
   by category;
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
    values("Biomedical Concept", 1, "BiomedicalConcept", "package_date", "Biomedical Concept package release date indicating when the BC package was published to production")
    values("Biomedical Concept", 1, "BiomedicalConcept", "short_name", "NCI Preferred Name for the concept; provisional name will be used if concept is not available in NCIt")
    values("Biomedical Concept", 1, "BiomedicalConcept", "bc_id", "A unique identifier for a Biomedical Concept which will be assigned as the NCIt code if it exists or a placeholder identifier if the concept is not yet available in NCIt")
    values("Biomedical Concept", 1, "BiomedicalConcept", "ncit_code", "NCIt C-code for the Biomedical Concept")
    values("Biomedical Concept", 1, "BiomedicalConcept", "parent_bc_id", "C-code for the parent concept in the NCIt hiearchy; blank if concept is not available in NCIt")
    values("Biomedical Concept", 1, "BiomedicalConcept", "bc_categories", "Biomedical Concept category for the faciliation of API search and extract")
    values("Biomedical Concept", 1, "BiomedicalConcept", "synonyms", "Biomedical Concept synonym equivalent to BC short name for the facilitation of API search and extraction")
    values("Biomedical Concept", 1, "BiomedicalConcept", "result_scales", "Scale of measurement for the Biomedical Concept result")
    values("Biomedical Concept", 1, "BiomedicalConcept", "definition", "NCIt definition for the Biomedical Concept; provisional defintion if concept is not available in NCIt")
    values("Biomedical Concept", 1, "Coding", "system", "Identifies the code system for the synonym concept. The URL of the code system should be used if it exists")
    values("Biomedical Concept", 1, "Coding", "system_name", "Human-readable name for the code system")
    values("Biomedical Concept", 1, "Coding", "code", "Synonym concept for the Biomedical Concept as defined in a code system")
    values("Data Element Concept (DEC)", 2, "DataElementConcept", "dec_id", "An identifier for a Data Element Concept (DEC) which will be assigned as the NCIt code if it exists or a placeholder identifier if the concept is not yet available in NCIt")
    values("Data Element Concept (DEC)", 2, "DataElementConcept", "ncit_dec_code", "NCI C-code for the BC Data Element Concept")
    values("Data Element Concept (DEC)", 2, "DataElementConcept", "dec_label", "NCI Preferred Name for the concept; provisional name will be used if concept is not available in NCIt")
    values("Data Element Concept (DEC)", 2, "DataElementConcept", "data_type", "Data Type for the Data Element Concept")
    values("Data Element Concept (DEC)", 2, "DataElementConcept", "example_set", "Example values for the Data Element Concept")
    ;
quit;    
     
%let headerstyle1 = {background=lightgreen color=black};

ods listing close;
ods excel options(sheet_name="ReadMe" flow="tables") file="%sysfunc(pathname(work))/cdisc_biomedical_concepts_&packageDateShort..xlsx";

  proc report data=work.readme spanrows missing;
    columns group order column description class;
    define group / order style(column)={vjust=t};
    define order / order noprint;
    define column / style(column)={vjust=t};
    define description / style(column)={vjust=t};
    define class / order style(column)={vjust=t};
    
    compute before _page_ /
      style =[font_weight=bold just=l color=black];
      line "This spreadsheet contains the latest versions of CDISC Biomedical Concepts in the CDISC Library as of &packageDate..";
      line "The picture on the right shows the relation between Biomedical Concepts and SDTM Dataset Specializations.";
      line "Only a limited number of attributes are shown.";
    endcomp;  
  run;  

ods excel options(sheet_name="Biomedical Concepts" flow="tables" autofilter = 'all');

  title "Latest Biomedical Concepts as of &packageDate";
  proc report data=data.bc_latest;
    columns package_date short_name href bc_id ncit_code parent_bc_id bc_categories synonyms result_scales definition system system_name code
             dec_href dec_id ncit_dec_code dec_label data_type example_set;
    
    define package_date /  style(header) = &headerstyle1;
    define bc_categories /  style(header) = &headerstyle1;
    define bc_id /  style(header) = &headerstyle1;
    define ncit_code /  style(header) = &headerstyle1;
    define parent_bc_id /  style(header) = &headerstyle1;
    define short_name /  style(header) = &headerstyle1;
    define synonyms /  style(header) = &headerstyle1;
    define result_scales /  style(header) = &headerstyle1;
    define definition /  style(header) = &headerstyle1;
    define system /  style(header) = &headerstyle1;
    define system_name /  style(header) = &headerstyle1;
    define code/  style(header) = &headerstyle1;
    
    define href / noprint; 
    define dec_href / noprint;
               
    compute bc_id;
      if not missing(bc_id) and index(bc_id, "NEW")=0 then do;
        call define (_col_, 'url', href);
        call define (_col_, "style","style={textdecoration=underline color=#0000FF}");
      end;  
    endcomp;

    compute ncit_code;
      if not missing(ncit_code) then do;
        call define (_col_, 'url', href);
        call define (_col_, "style","style={textdecoration=underline color=#0000FF}");
      end;  
    endcomp;

    compute parent_bc_id;
      if not missing(parent_bc_id) then do;
        call define (_col_, 'url', cats('https://ncithesaurus.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=', parent_bc_id));
        call define (_col_, "style","style={textdecoration=underline color=#0000FF}");
      end;  
    endcomp;

    compute ncit_dec_code;
      if not missing(ncit_dec_code) then do;
        call define (_col_, 'url', dec_href);
        call define (_col_, "style","style={textdecoration=underline color=#0000FF}");
      end;  
    endcomp;

  run;  

ods excel options(sheet_name="Categories" flow="tables" autofilter = 'none');

  proc report data=work.categories;
    columns category;
  run;  
  
ods excel close;
ods listing;

data _null_;
  call insert_image(
    "%sysfunc(pathname(work))/cdisc_biomedical_concepts_&packageDateShort..xlsx",
    "&root/utilities/reports/cdisc_biomedical_concepts_&packageDateShort..xlsx",
    "&root/utilities/images/bc-sdtm-erd-light.png",
    "ReadMe",
    "F2",
    439,
    480
  );
run;
