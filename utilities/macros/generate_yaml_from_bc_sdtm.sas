%macro generate_yaml_from_bc_sdtm(excel_file=, range=, type=, package=, out_folder=, subsetsDS=, debug=0);

%ReadExcel(file=&excel_file, range=&range.$, dsout=bc_sdtm_&type._&package);

  data bc_sdtm_&type._&package;
    set bc_sdtm_&type._&package(where=(not missing(vlm_group_id)));
    order=_n_;
  run;

  proc sql;
    create table bc_sdtm_&type._&package._merged
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
    proc print data=bc_sdtm_&type._&package._merged;
    run;

    ods html5 close;
    ods listing;

  %end;

  data _null_;
    length prev_vlm_group_id $32 outname $100 qpackage_date qsdtmig_start_version qsdtmig_end_version qformat $20 linking_phrase_low $512 value qvalue $100 value_list $4096;
    retain prev_vlm_group_id "" count 0;
    set work.bc_sdtm_&type._&package._merged;
    outname=catt("&out_folder\sdtm_bc_specialization_&type._", lowcase(strip(vlm_group_id)), ".yaml");
    file dummy filevar=outname dlm=",";
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
           put +4 "codelist:";
           put +6 "conceptId:" +1 codelist;
           put +6 'href: https://ncithesaurus.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=' codelist;
           if not missing(codelist_submision_value) then put +6 "submissionValue:" +1 codelist_submission_value;
        end;
        if not missing(subset_codelist) then do;
          put +4 "subsetCodelist:" +1 subset_codelist;
          if not missing(value_list) then do;
            putlog "WAR" "NING: both subset_codelist and value_list not empty. " vlm_group_id= sdtm_variable= subset_codelist= value_list=;
          end;
          if missing(value_list) and missing(subset_value_list) then do;
            putlog "WAR" "NING: both value_list and subset_value_list missing. " vlm_group_id= sdtm_variable= subset_codelist= value_list= subset_value_list=;
          end;
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
            end;
            
          end;
        end;

        if not missing(assigned_value) then do;
           put +4 "assignedTerm:";
           if not missing(assigned_term) then put +6 "conceptId:" +1 assigned_term;
           put +6 "value:" +1 assigned_value;
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
        if not missing(comparator) then put +4 "comparator:" +1 comparator;

        if upcase(vlm_target)= "Y" then put +4 "vlmTarget:" +1 vlm_target $YN.;

    end;
  run;

%mend generate_yaml_from_bc_sdtm;
