%macro create_template(type=, out=);

  %if %upcase(&type) eq BC %then %do;
    proc sql;
      create table &out
        (
         packageDate char(10),
         conceptId char(64),
         parentConceptId char(64),
         ncitCode char(64),
         href char(1024),
         categories char(1024),
         shortName char(256),
         synonyms char(1024),
         resultScales char(256),
         definition char(2048),
         system char(1024),
         systemname char(1024),
         code char (1024),
         dec_conceptId char(64),
         dec_href char(1024),
         dec_ncitCode char(64),
         dec_shortName char(256),
         dec_dataType char(16),
         dec_exampleSet char(32000)
        );
    quit;
  %end;


  
  %if %upcase(&type) eq SDTM %then %do;
    proc sql;
      create table &out
        (
         packageDate char(10),
         biomedicalConceptId char(64),
         dataElementConceptId char(64),
         sdtmigStartVersion char(32),
         sdtmigEndVersion char(32),
         domain char(32),
         source char(32),
         datasetSpecializationId char(64),
         shortName char(256),
         name char(32),
         isNonStandard num,
         codelist char(64),
         codelist_href char(1024),
         codelist_submission_value char(32),
         subsetCodelist char(32),
         value_list char(2048),
         assigned_term char(64),
         assigned_value char(1024),
         role char(32),
         subject char(32),
         linkingPhrase char(1024),
         predicateTerm char(128),
         object char(32),
         dataType char(16),
         length num,
         format char(32),
         significantDigits num,
         mandatoryVariable num,
         mandatoryValue num,
         originType char(32),
         originSource char(32),
         comparator char(8),
         vlmTarget num
        );
    quit;
  %end;

  %if %upcase(&type) eq BC_ISSUE %then %do;
    proc sql;
    create table &out
      (
       _excel_file_  char(128),
       _tab_  char(128),
       BC_ID char(64),
       dec_id char(64),
       issue_type char(64),
       expected_value char(2048),
       actual_value char(2048),
       comment char(2048)
      );
    quit;
  %end;
  
  %if %upcase(&type) eq SDTM_ISSUE %then %do;
    proc sql;
    create table &out
      (
       _excel_file_  char(128),
       _tab_  char(128),
       vlm_group_id char(64),
       sdtm_variable char(64),
       issue_type char(64),
       expected_value char(2048),
       actual_value char(2048),
       comment char(2048)
      );
    quit;
  %end;
  
%mend;
  