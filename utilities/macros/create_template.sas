%macro create_template(type=, out=);


  %if %upcase(&type) eq BC %then %do;
    proc sql;
      create table &out
        (
         packageDate char(10),
         conceptId char(64),
         parentConceptId char(64),
         href char(1024),
         category char(1024),
         shortName char(256),
         synonym char(1024),
         resultScale char(256),
         definition char(2048),
         system char(1024),
         systemname char(1024),
         code char (1024),
         dec_ConceptId char(64),
         dec_href char(1024),
         dec_ShortName char(256),
         dec_dataType char(16),
         dec_exampleSet char(2048)
        );
    quit;
  %end;


  
  %if %upcase(&type) eq SDTM %then %do;
    proc sql;
      create table &out
        (
         packageDate char(10),
         biomedicalConceptId char(64),
         sdtmigStartVersion char(16),
         sdtmigEndVersion char(16),
         domain char(8),
         source char(32),
         datasetSpecializationId char(32),
         shortName char(256),
         name char(32),
         isNonStandard num,
         codelist char(32),
         codelist_href char(1024),
         codelist_submision_value char(32),
         subsetCodelist char(32),
         value_list char(2048),
         assigned_term char(128),
         assigned_value char(1024),
         role char(32),
         subject char(32),
         linkingPhrase char(128),
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

  
%mend;
  