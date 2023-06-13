%macro generate_yaml_from_bc_cdash(excel_file=, range=, type=, package=, override_package_date=, out_folder=, subsetsDS=, debug=0);

%ReadExcel(file=&excel_file, range=&range.$, dsout=bc_cdash_&type._&package);

  data bc_cdash_&type._&package;
    set bc_cdash_&type._&package(where=(not missing(cdash_group_id)));
    order=_n_;
  run;

  proc sql;
    create table bc_cdash_&type._&package._merged
    as select
      bccdash.*,
      ss.subset_value_list
    from work.bc_cdash_&type._&package bccdash
      left join &subsetsDS ss
    on bccdash.subset_codelist = ss.subset_short_name
    order by cdash_group_id, scenario, order
    ;
  quit;

  %if &debug %then %do;

    ods listing close;
    ods html5 file="get_bc_cdash_&range..html";

    proc contents data=bc_cdash_&type._&package varnum;
    run;
    proc print data=bc_cdash_&type._&package._merged;
    run;

    ods html5 close;
    ods listing;

  %end;

  data _null_;
    length prev_cdash_group_id $32 prev_scenario $40 outname $100 qpackage_date qcdashig_start_version qcdashig_end_version $20 linking_phrase_low $512 value $100 value_list $4096;
    retain prev_cdash_group_id prev_scenario "" count 0;
    set work.bc_cdash_&type._&package._merged;
    if missing(scenario) then
      outname=catt("&out_folder\cdash_bc_specialization_&type._", lowcase(strip(cdash_group_id)), ".yaml");
    else
      outname=catt("&out_folder\cdash_bc_specialization_&type._", lowcase(strip(cdash_group_id)), "_", lowcase(strip(scenario)), ".yaml");
    file dummy filevar=outname dlm=",";
    prev_cdash_group_id = lag(cdash_group_id);
    prev_scenario = lag(scenario);
    if not(missing(cdash_group_id)) and ((prev_cdash_group_id ne cdash_group_id) or (prev_scenario ne scenario)) then do;
      count=0;
      %if %sysevalf(%superq(override_package_date)=, boolean)=0 %then package_date="&override_package_date";;
      qpackage_date = quote(strip(package_date));
      put "packageDate:" +1 qpackage_date;
      put "packageType:" +1 "cdash";
      put "datasetSpecializationId:" +1 cdash_group_id;
      put "domain:" +1 domain;
      put "shortName:" +1 short_name;
      if not missing(scenario) then put "scenario:" +1 scenario;
      qcdashig_start_version = quote(strip(cdashig_start_version));
      put "cdashigStartVersion:" +1 qcdashig_start_version;
      qcdashig_end_version = quote(strip(cdashig_end_version));
      put "cdashigEndVersion:" +1 qcdashig_end_version;
      if not missing(bc_id) then put "biomedicalConceptId:" +1 bc_id;
    end;
    count+1;
    if count=1 and not missing(cdash_variable) then put "variables:";
    if not missing(cdash_variable) then do;
        put +2 "- name:" +1 cdash_variable;
        if not missing(dec_id) then put +4 "dataElementConceptId:" +1 dec_id;
        if not missing(question_text) then put +4 "questionText:" +1 question_text;
        if not missing(prompt) then put +4 "prompt:" +1 prompt;
        if not missing(codelist) then do;
           put +4 "codelist:";
           put +6 "conceptId:" +1 codelist;
           put +6 'href: https://ncithesaurus.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=' codelist;
           if not missing(codelist_submision_value) then put +6 "submissionValue:" +1 codelist_submision_value;
        end;
        if not missing(subset_codelist) then do;
          put +4 "subsetCodelist:" +1 subset_codelist;
          if not missing(value_list) then do;
            putlog "WAR" "NING: both subset_codelist and value_list not empty. " cdash_group_id= cdash_variable= subset_codelist= value_list=;
          end;
          if missing(value_list) and missing(subset_value_list) then do;
            putlog "WAR" "NING: both value_list and subset_value_list missing. " cdash_group_id= cdash_variable= subset_codelist= value_list= subset_value_list=;
          end;
          value_list = subset_value_list;
        end;

        if not missing(value_list) then do;
          value_list=compress(value_list, "", "s");
          put +4 "valueList:";
          countwords=countw(value_list, ";");
          do i=1 to countwords;
            value=strip(scan(value_list, i, ";"));
            if not missing(value) then put +6 "-" +1 value;
          end;
        end;

        if not missing(prepopulated_value) then put +4 "prepopulatedValue:" +1 prepopulated_value;

        if not missing(data_type) then put +4 "dataType:" +1 data_type;
        if not missing(length) then put +4 "length:" +1 length;
        if not missing(significant_digits) then put +4 "significantDigits:" +1 significant_digits;
        if not missing(cdashig_core) then put +4 "cdashigCore:" +1 cdashig_core;

        if not missing(subject) then do;
          object=tranwrd(object, '93'x, '"');
          object=tranwrd(object, '94'x, '"');
          linking_phrase_low = lowcase(linking_phrase);
          put +4 "relationship:";
          put +6 "subject:" +1 subject;
          put +6 "linkingPhrase:" +1 linking_phrase_low;
          put +6 "predicateTerm:" +1 predicate_term;
          put +6 "object:" +1 object;
        end;

        if not missing(sdtm_target_variable) then do;
          put +4 "sdtmTarget:";
          put +6 "sdtmTargetVariable:" +1 sdtm_target_variable;
          put +6 "sdtmTargetMapping:" +1 sdtm_target_mapping;
          put +6 "sdtmTargetGroup:" +1 sdtm_target_group;
        end;

    end;
  run;

%mend generate_yaml_from_bc_cdash;
