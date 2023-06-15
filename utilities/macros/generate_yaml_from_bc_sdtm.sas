%macro generate_yaml_from_bc_sdtm(excel_file=, range=, type=, package=, override_package_date=, out_folder=, subsetsDS=, debug=0);

%ReadExcel(file=&excel_file, range=&range.$, dsout=bc_sdtm_&type._&package);

  data bc_sdtm_&type._&package;
    set bc_sdtm_&type._&package(where=(not missing(vlm_group_id)));
    order=_n_;
  run;

  proc sql;
    create table bc_sdtm_&type._&package._mrgd
    as select
      bcsdtm.*,
      ss.subset_value_list
    from work.bc_sdtm_&type._&package bcsdtm
      left join &subsetsDS ss
    on bcsdtm.subset_codelist = ss.subset_short_name
    order by vlm_group_id, order
    ;
  quit;

  %if &debug %then %do;

    ods listing close;
    ods html5 file="get_bc_sdtm_&range..html";

    proc contents data=bc_sdtm_&type._&package varnum;
    run;
    proc print data=bc_sdtm_&type._&package._mrgd;
    run;

    ods html5 close;
    ods listing;

  %end;

  data issues(keep=_excel_file_ _tab_ vlm_group_id sdtm_variable issue_type expected_value actual_value comment);
    length prev_vlm_group_id $32 outname $512 package_date qpackage_date $64 qsdtmig_start_version qsdtmig_end_version qformat $20  
           codelist_submission_value_cdisc assigned_term_cdisc value_code_cdisc linking_phrase_low $512 value qvalue $100 value_list $4096
           issue_type $64 expected_value  actual_value comment $2048;
    retain prev_vlm_group_id "" count 0;
    set work.bc_sdtm_&type._&package._mrgd;

    call missing(codelist_submission_value_cdisc, assigned_term_cdisc, value_code_cdisc);
    
    outname=catt("&out_folder\sdtm_bc_specialization_&type._", lowcase(strip(vlm_group_id)), ".yaml");
    file dummy filevar=outname dlm=",";
    
    %if %sysevalf(%superq(override_package_date)=, boolean)=0 %then package_date="&override_package_date";;
    
    prev_vlm_group_id = strip(prev_vlm_group_id);
    prev_vlm_group_id = lag(vlm_group_id);
    if not(missing(vlm_group_id)) and (prev_vlm_group_id ne vlm_group_id) then do;
      count=0;
      qpackage_date = quote(strip(package_date));
      put "packageDate:" +1 qpackage_date;
      put "packageType:" +1 "sdtm";
      put "datasetSpecializationId:" +1 vlm_group_id;
      put "domain:" +1 domain;
      put "shortName:" +1 short_name;
      put "source:" +1 vlm_source;
      qsdtmig_start_version = quote(strip(sdtmig_start_version));
      put "sdtmigStartVersion:" +1 qsdtmig_start_version;
      qsdtmig_end_version = quote(strip(sdtmig_end_version));
      put "sdtmigEndVersion:" +1 qsdtmig_end_version;
      if not missing(bc_id) then put "biomedicalConceptId:" +1 bc_id;
    end;
    count+1;
    if count=1 and not missing(sdtm_variable) then put "variables:";
    if not missing(sdtm_variable) then do;
        put +2 "- name:" +1 sdtm_variable;
        if not missing(dec_id) then put +4 "dataElementConceptId:" +1 dec_id;
        if missing(nsv_flag) then nsv_flag="N";
        put +4 "isNonStandard:" +1 nsv_flag $YN.;
        if not missing(codelist) then do;
          
           codelist_submission_value_cdisc = get_codelist_submissionvalue(codelist);

           %add2issues_sdtm(missing(codelist_submission_value), 
                            %str(CODELIST_SUBMISSION_VALUE_MISSING), 
                            codelist_submission_value_cdisc, "", %str(cats("codelist=", codelist)));

           %add2issues_sdtm(codelist_submission_value ne codelist_submission_value_cdisc, 
                            %str(CODELIST_SUBMISSION_VALUE_MISMATCH), 
                            codelist_submission_value_cdisc, codelist_submission_value, %str(cats("codelist=", codelist)));

           put +4 "codelist:";
           put +6 "conceptId:" +1 codelist;
           put +6 'href: https://ncithesaurus.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=' codelist;
           if not missing(codelist_submission_value) then put +6 "submissionValue:" +1 codelist_submission_value;
        end;
        if not missing(subset_codelist) then do;
          put +4 "subsetCodelist:" +1 subset_codelist;
          %add2issues_sdtm(not missing(value_list), 
                %str(SUBSETCODELIST_VALUE_LIST_NOT_MISSING), 
                "", value_list, 
                %str(cats("codelist=", codelist, ", codelist_submission_value=", codelist_submission_value, 
                          ", subset_codelist=", subset_codelist, ", value_list=", value_list)));
          %add2issues_sdtm(missing(value_list) and missing(subset_value_list), 
                %str(SUBSET_VALUE_LIST_VALUE_LIST_MISSING), 
                "", value_list, 
                %str(cats("codelist=", codelist, ", codelist_submission_value=", codelist_submission_value, 
                          ", subset_codelist=", subset_codelist, ", subset_value_list=", subset_value_list, ", value_list=", value_list)));
          value_list = subset_value_list;
        end;

        if not missing(value_list) then do;
          put +4 "valueList:";
          countwords=countw(value_list, ";");
          do i=1 to countwords;
            value=strip(scan(value_list, i, ";"));
            if not missing(value) then do;
              qvalue=quote(strip(value));
              put +6 "-" +1 qvalue;
              
              value_code_cdisc = get_term_code(codelist, value);
              %add2issues_sdtm(missing(value_code_cdisc), 
                    %str(CODELIST_VALUE_LIST_TERM_CDISC_MISSING), 
                    value_code_cdisc, "", %str(cats("codelist=", codelist, ", codelist_submission_value=", codelist_submission_value, ", value_list=", value_list, ", value=", value)));
            end;
          end;
        end;

        if not missing(assigned_value) then do;
          put +4 "assignedTerm:";
          if not missing(assigned_term) then put +6 "conceptId:" +1 assigned_term;
          put +6 "value:" +1 assigned_value;
          %add2issues_sdtm((not missing(value_list)) and (not missing(assigned_value)), 
                %str(ASSIGNED_VALUE_AND_VALUE_LIST_NOT_MISSING), 
                "", value_list, 
                %str(cats("codelist=", codelist, ", codelist_submission_value=", codelist_submission_value, 
                          ", value_list=", value_list, ", assigned_value=", assigned_value)));
          assigned_term_cdisc = get_term_code(codelist, assigned_value);
          %add2issues_sdtm((assigned_term_cdisc ne assigned_term) and (missing(assigned_term_cdisc)), 
                %str(CODELIST_TERM_CCODE_MISSING), 
                assigned_term_cdisc, assigned_term, %str(cats("codelist=", codelist, ", codelist_submission_value=", codelist_submission_value, ", assigned_value=", assigned_value)));
          %add2issues_sdtm((assigned_term_cdisc ne assigned_term) and (not missing(assigned_term_cdisc)), 
                %str(CODELIST_TERM_CCODE_MISMATCH), 
                assigned_term_cdisc, assigned_term, %str(cats("codelist=", codelist, ", codelist_submission_value=", codelist_submission_value, ", assigned_value=", assigned_value)));


        end;
        if not missing(role) then put +4 "role:" +1 role;

        if not missing(data_type) then put +4 "dataType:" +1 data_type;
        if not missing(length) then put +4 "length:" +1 length;
        qformat=quote(strip(format));
        if not missing(format) then put +4 "format:" +1 qformat;
        if not missing(significant_digits) then put +4 "significantDigits:" +1 significant_digits;

        if not missing(subject) then do;
          linking_phrase_low = lowcase(linking_phrase);
          put +4 "relationship:";
          put +6 "subject:" +1 subject;
          put +6 "linkingPhrase:" +1 linking_phrase_low;
          put +6 "predicateTerm:" +1 predicate_term;
          put +6 "object:" +1 object;
        end;

        if missing(mandatory_variable) then mandatory_variable="N";
        put +4 "mandatoryVariable:" +1 mandatory_variable $YN.;
        if missing(mandatory_value) then mandatory_value="N";
        put +4 "mandatoryValue:" +1 mandatory_value $YN.;

        if not missing(origin_type) then put +4 "originType:" +1 origin_type;
        if not missing(origin_source) then put +4 "originSource:" +1 origin_source;

        /* xxTEST variables shoukd not be used in the whereclauses */
        %add2issues_sdtm(length(sdtm_variable) >= 4 and substr(sdtm_variable, length(sdtm_variable)-3, 4) = "TEST" and (not missing(comparator)),
              %str(XXTEST_IN_WHERECLAUSE), 
              "", comparator, %str(cats("comparator=", comparator, ", assigned_value=", assigned_value, ", comparator will be set to missing")),
              extracode=%str(comparator="") 
              );
        
        /* Variables should only be used in an EQ whereclause when they have an asssigned_value */
        %add2issues_sdtm((not missing(comparator)) and comparator = "EQ" and missing(assigned_value),
              %str(COMPARATOR_ASSIGNED_VALUE_MISSING), 
              "", comparator, %str(cats("comparator=", comparator, ", value_list=", value_list, ", assigned_value=", assigned_value)));
        
        /* Variables should only be used in an IN whereclause when they have an value_list */
        %add2issues_sdtm((not missing(comparator)) and comparator = "IN" and missing(value_list),
              %str(COMPARATOR_VALUE_LIST_MISSING), 
              "", comparator, %str(cats("comparator=", comparator, ", value_list=", value_list, ", assigned_value=", assigned_value)));

        /* Variables should be used either in a whereclause or be a VLM target */
        %add2issues_sdtm((not missing(comparator)) and (not missing(vlm_target)),
              %str(COMPARATOR_AND_VLM_TARGET_NOT_MISSING), 
              "", "", %str(cats("comparator=", comparator, ", vlm_target=", vlm_target)));

        if not missing(comparator) then put +4 "comparator:" +1 comparator;

        if upcase(vlm_target)= "Y" then put +4 "vlmTarget:" +1 vlm_target $YN.;

    end;
  run;

  data all_issues_sdtm;
    set all_issues_sdtm issues;
  run;  

%mend generate_yaml_from_bc_sdtm;
