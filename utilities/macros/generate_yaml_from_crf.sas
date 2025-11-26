%macro generate_yaml_from_crf(
  excel_file=, range=, type=, package=, override_package_date=, 
  out_folder=, debug=0
  );

  %let type = %sysfunc(tranwrd(&type, %str(-), %str(_)));

  %ReadExcel(file=&excel_file, range=&range.$, dsout=bc_crf_&type._&package, drop=%str(drop=package_date));

  data bc_crf_&type._&package;
    set bc_crf_&type._&package(where=(not missing(crf_group_id)));
  run;
  proc sort;
    by crf_group_id order_number;
  run;  

  %if &debug %then %do;

    ods listing close;
    ods html5 file="get_bc_crf_&range..html";

    proc contents data=bc_crf_&type._&package varnum;
    run;
    proc print data=bc_crf_&type._&package;
    run;

    ods html5 close;
    ods listing;

  %end;

  data issues(keep=_excel_file_ _tab_ package_date severity crf_group_id crf_item issue_type expected_value actual_value comment);
    length prev_crf_group_id crf_group_id $128 outname $512 package_date qpackage_date standard crf_item $64 qstandard_start_version qstandard_end_version $20  
           codelist_submission_value_cdisc prepopulated_term_cdisc prepopulated_code_cdisc value_code_cdisc prepopulated_term_cdisc_preferd $512 
           codelist_extensible $3 lookup_term_exist 8 value qvalue $1024 categories derivation_description value_list value_display_list sdtm_annotation qsdtm_annotation $8192
           severity $10 issue_type $64 expected_value actual_value comment $2048;
    retain prev_crf_group_id "" count 0;
    set work.bc_crf_&type._&package;

    call missing(codelist_submission_value_cdisc, prepopulated_term_cdisc, prepopulated_code_cdisc, prepopulated_term_cdisc_preferd, value_code_cdisc, lookup_term_exist);
    
    outname=catt("&out_folder\crf_", lowcase(strip(crf_group_id)), ".yaml");
    file dummy filevar=outname dlm=",";
    
    %if %sysevalf(%superq(override_package_date)=, boolean)=0 %then package_date="&override_package_date";;
    
    prev_crf_group_id = strip(prev_crf_group_id);
    prev_crf_group_id = lag(crf_group_id);
    if not(missing(crf_group_id)) and (prev_crf_group_id ne crf_group_id) then do;
      count=0;
      qpackage_date = quote(strip(package_date));
      put "packageDate:" +1 qpackage_date;
      put "packageType:" +1 "crf";
      put "crfSpecializationId:" +1 crf_group_id;
      %add2issues_crf(missing(short_name), 
                     %str(MISSING_SHORT_NAME), 
                     "", "", "", severity=ERROR);
      if not missing(short_name) then do;
        if index(short_name, '"') or index(short_name, ":") or index(short_name, "-") 
          then put "shortName:" +1 '"' short_name +(-1) '"';
          else put "shortName:" +1 short_name;
      end;
      put "standard:" +1 standard;
      qstandard_start_version = quote(strip(standard_start_version));
      put "standardStartVersion:" +1 qstandard_start_version;
      qstandard_end_version = quote(strip(standard_end_version));
      put "standardEndVersion:" +1 standard_end_version;
      if not missing(implementation_option) then put "implementationOption:" +1 implementation_option;
      if not missing(scenario) then put "scenario:" +1 scenario;

      if not missing(categories) then do;
        put "categories:";
        countwords=countw(categories, ";");
        do i=1 to countwords;
          value=strip(scan(categories, i, ";"));
          value=tranwrd(value, '"', '\"');
          qvalue=quote(strip(value));
          if not missing(value) then do;
            put +2 "-" +1 qvalue;
          end;  
        end;
      end;

      put "domain:" +1 domain;
      if not missing(bc_id) then put "biomedicalConceptId:" +1 bc_id;
      if not missing(vlm_group_id) then put "sdtmDatasetSpecializationId:" +1 vlm_group_id;
      %add2issues_crf(missing(vlm_group_id), 
                     %str(MISSING_VLM_GROUP_ID), 
                     "", "", "", severity=NOTE);
    end;
    
    count+1;
    if count=1 and not missing(crf_item) then put "items:";
    if not missing(crf_item) then do;
        put +2 "- name:" +1 crf_item;
        put +4 "variableName:" +1 variable_name;
        if not missing(dec_id) then put +4 "dataElementConceptId:" +1 dec_id;
        
        %add2issues_crf(missing(question_text) and missing(prompt), 
                       %str(QUESTION_TEXT_PROMPT_BOTH_MISSING), 
                       "", "", "", severity=ERROR);

        %add2issues_crf((not missing(question_text)) and (not missing(prompt)), 
                       %str(QUESTION_TEXT_PROMPT_BOTH_NOT MISSING), 
                       "", "", %str(cats("question_text=", question_text, ", prompt=", prompt)), severity=ERROR);

        if not missing(question_text) then do;
          question_text=tranwrd(question_text, '"', '\"');
          if index(question_text, '"') or index(question_text, ":") or index(question_text, "-") 
            then question_text=cats('"', question_text, '"');
          put +4 "questionText:" +1 question_text;
        end;  
        if not missing(prompt) then do;
          prompt=tranwrd(prompt, '"', '\"');
          if index(prompt, '"') or index(prompt, ":") or index(prompt, "-") 
            then prompt=cats('"', prompt, '"');
          put +4 "prompt:" +1 prompt;
        end;  
        if not missing(completion_instructions) then do;
          completion_instructions=tranwrd(completion_instructions, '"', '\"');
          if index(completion_instructions, '"') or index(completion_instructions, ":") or index(completion_instructions, "-") 
            then completion_instructions=cats('"', completion_instructions, '"');
          put +4 "completionIinstructions:" +1 completion_instructions;
        end;  

        if not missing(order_number) then put +4 "orderNumber:" +1 order_number;
        if missing(mandatory_variable) then mandatory_variable="N";
        put +4 "mandatoryVariable:" +1 mandatory_variable $YN.;

        if not missing(data_type) then put +4 "dataType:" +1 data_type;
        if not missing(length) then put +4 "length:" +1 length;
        if not missing(significant_digits) then put +4 "significantDigits:" +1 significant_digits;
        if missing(display_hidden) then display_hidden="N";
        put +4 "displayHidden:" +1 display_hidden $YN.;
        if missing(derived_variable) then derived_variable="N";

        put +4 "derivedVariable:" +1 derived_variable $YN.;
        if not missing(derivation_description) then do;
          if index(derivation_description, '"') or index(derivation_description, ":") or index(derivation_description, "-") 
            then put +4 "derivationDescription:" +1 '"' derivation_description +(-1) '"';
            else put +4 "derivationDescription:" +1 derivation_description;
        end;


        if missing(codelist_submission_value) and not missing(codelist) then do;
             codelist_submission_value_cdisc = get_codelist_submissionvalue(codelist);
             %add2issues_crf(missing(codelist_submission_value), 
                              %str(CODELIST_SUBMISSION_VALUE_MISSING), 
                              codelist_submission_value_cdisc, "", %str(cats("codelist=", codelist)));
        end;  

        if not missing(codelist_submission_value) then do;
          
           if not missing(codelist) then do;
             codelist_submission_value_cdisc = get_codelist_submissionvalue(codelist);
             codelist_extensible = get_codelist_extensible(codelist);

             %add2issues_crf(missing(codelist_submission_value), 
                              %str(CODELIST_SUBMISSION_VALUE_MISSING), 
                              codelist_submission_value_cdisc, "", %str(cats("codelist=", codelist)));

             %add2issues_crf((codelist_submission_value ne codelist_submission_value_cdisc), 
                              %str(CODELIST_SUBMISSION_VALUE_MISMATCH), 
                              codelist_submission_value_cdisc, codelist_submission_value, %str(cats("codelist=", codelist)));

           end;
          
           put +4 "codelist:";
           put +6 "submissionValue:" +1 codelist_submission_value;
           if not missing(codelist) then put +6 "conceptId:" +1 codelist;
           put +6 "href: &ncit_explore" codelist;
        end;
        
        if not missing(value_display_list) then do;
          put +4 "valueList:";
          countwords=countw(value_display_list, ";");
          countwords2=countw(value_list, ";");

          %add2issues_crf(countwords eq 1, 
                %str(CODELIST_VALUE_LISTS_1_TERM), 
                "", "", %str(cats("value_display_list=", value_display_list, " (", countwords, ")", ", codelist=", codelist, ", codelist_submission_value=", 
                codelist_submission_value, ", value_list=", value_list, " (", countwords2, ")")));

          %add2issues_crf(countwords ne countwords2, 
                %str(CODELIST_VALUE_LISTS_TERM_COUNTS), 
                "", "", %str(cats("value_display_list=", value_display_list, " (", countwords, ")", ", codelist=", codelist, ", codelist_submission_value=", 
                codelist_submission_value, ", value_list=", value_list, " (", countwords2, ")")));

          do i=1 to countwords;
            value=strip(scan(value_display_list, i, ";"));
            if not missing(value) then do;
              qvalue=quote(strip(value));
              put +6 "- displayValue:" +1 qvalue;
              
            end;
            value=strip(scan(value_list, i, ";"));

            if not missing(value) then do;

              if not missing(codelist) then do
                value_code_cdisc = get_term_code(codelist, value);
                codelist_extensible = get_codelist_extensible(codelist);
                %add2issues_crf(missing(value_code_cdisc) and (codelist_extensible = "No"), 
                      %str(CODELIST_VALUE_LIST_TERM_CDISC_MISSING), 
                      value_code_cdisc, "", %str(cats("codelist_extensible=", codelist_extensible, ", codelist=", codelist, ", codelist_submission_value=", 
                      codelist_submission_value, ", value_list=", value_list, ", value=", value)));
              end;        

              qvalue=quote(strip(value));
              put +6 "  value:" +1 qvalue;
            end;
          end;
        end;

        %add2issues_crf(missing(selection_type) and (not missing(value_display_list)), 
              %str(VALUE_LIST_MISSING_SELECTION_TYPE), 
              "", "", %str(cats("value_display_list=", value_display_list, ", codelist=", codelist, ", codelist_submission_value=", 
              codelist_submission_value)));
              
        if not missing(selection_type) then put +4 "selectionType:" +1 selection_type;

        if not missing(prepopulated_term) then do;
          put +4 "prepopulatedValue:";
          qvalue=quote(strip(prepopulated_term));
          put +6 "value:" +1 qvalue;
          if not missing(prepopulated_code) then put +6 "conceptId:" +1 prepopulated_code;
          
          %add2issues_crf((not missing(value_list)) and (not missing(prepopulated_term)), 
                %str(BOTH_PREPOPULATED_TERM_AND_VALUE_LIST_NOT_MISSING), 
                "", value_list, 
                %str(cats("codelist=", codelist, ", codelist_submission_value=", codelist_submission_value, 
                          ", value_list=", value_list, ", prepopulated_term=", prepopulated_term, ", prepopulated_code=", prepopulated_code)));
          
          if not missing(codelist) and not missing(prepopulated_code) then do                          
            prepopulated_term_cdisc_preferd = get_term_preferred_term(codelist, prepopulated_code);
            codelist_extensible = get_codelist_extensible(codelist);
            prepopulated_code_cdisc = get_term_code(codelist, prepopulated_term);
            prepopulated_term_cdisc = get_term_value(codelist, prepopulated_code);
            
            %add2issues_crf((not missing(prepopulated_term_cdisc)) and (missing(prepopulated_term)), 
                  %str(CODELIST_TERM_VALUE_MISSING), 
                  prepopulated_term_cdisc, prepopulated_term, %str(cats("codelist_extensible=", codelist_extensible, ", codelist=", codelist, ", codelist_submission_value=", 
                  codelist_submission_value, ", prepopulated_term=", prepopulated_term)));
            
            %add2issues_crf((prepopulated_term_cdisc ne prepopulated_term) and (not missing(prepopulated_term_cdisc)) and (not missing(prepopulated_term)), 
                  %str(CODELIST_TERM_CCODE_MISMATCH), 
                  prepopulated_term_cdisc, prepopulated_term, %str(cats("codelist_extensible=", codelist_extensible, ", codelist=", codelist, ", codelist_submission_value=", 
                  codelist_submission_value, ", prepopulated_term=", prepopulated_term, ", value_code_cdisc=", value_code_cdisc)));

            %add2issues_crf(missing(prepopulated_term_cdisc) and (codelist_extensible = "No"), 
                  %str(CODELIST_TERM_CCODE_MISSING_NOTEXTENSIBLE), 
                  prepopulated_term_cdisc, prepopulated_term, %str(cats("codelist_extensible=", codelist_extensible, ", codelist=", codelist, ", codelist_submission_value=", 
                  codelist_submission_value, ", prepopulated_term=", prepopulated_term)));
            
          end;

        end;

        if (not missing(sdtm_target_variable)) or 
           (not missing(sdtm_annotation)) or 
           (not missing(sdtm_mapping)) then do;
          
          put +4 "sdtmTarget:";

          if not missing(sdtm_annotation) then do;
            qsdtm_annotation = quote(strip(sdtm_annotation));
            put +6 "sdtmAnnotation:" +1 qsdtm_annotation;
          end;  
          
          if not missing(sdtm_target_variable) then do;
            countwords=countw(sdtm_target_variable, ";");
            put +6 "sdtmVariables:";
            do i=1 to countwords;
              value=strip(scan(sdtm_target_variable, i, ";"));
              if not missing(value) then do;
                qvalue=quote(strip(value));
                put +8 "- " +1 qvalue;
                if not missing(sdtm_mapping) then put +6 "  sdtmTargetMapping:" +1 sdtm_mapping;
              end;
            end;
          end;            
          
        end;  

    end;
  run;

  data all_issues_crf;
    set all_issues_crf issues;
  run;  
  
  proc delete data=work.bc_crf_&type._&package work.issues;
  run;  

%mend generate_yaml_from_crf;
