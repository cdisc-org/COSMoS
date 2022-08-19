%macro generate_bc_sdtm(excel_file=, range=, type=, out_folder=, debug=1);

%ReadExcel(file=&excel_file, range=&range.$, dsout=bc_sdtm_&type);

  data bc_sdtm_&type;
    set bc_sdtm_&type(where=(not missing(vlm_group_id)));
  run;

  %if &debug %then %do;

    ods listing close;
    ods html5 file="get_bc_sdtm_&range..html";

    proc contents data=bc_sdtm_&type varnum;
    run;
    proc print data=bc_sdtm_&type;
    run;

    ods html5 close;
    ods listing;

  %end;

  data _null_;
    set work.bc_sdtm_&type;
    retain count 0;
    length outname $100 linking_phrase_low $512 value $100;
    by vlm_group_id notsorted;
    outname=catt("&out_folder\sdtm_bc_specialization_&type._", lowcase(strip(vlm_group_id)), ".yaml");
    file dummy filevar=outname dlm=",";
    if first.vlm_group_id then do;
      count=0;
      put "domain:" +1 domain;
      put "vlm_group_id:" +1 vlm_group_id;
      put "group_short_name:" +1 group_short_name;
      put "vlm_source:" +1 vlm_source;
      put "sdtmig_start_version:" +1 sdtmig_start_version;
      put "sdtmig_end_version:" +1 sdtmig_end_version;
      if not missing(bc_id) then put "biomedical_concept_id:" +1 bc_id;
    end;
    count+1;
    if count=1 and not missing(sdtm_variable) then put "sdtm_variable:";
    if not missing(sdtm_variable) then do;
        put +2 "- id:" +1 sdtm_variable;
        if not missing(dec_id) then put +4 "biomedical_concept_dec_id:" +1 dec_id;
        if upcase(nsv_flag)= "Y" then put +4 "nsv_flag:" +1 nsv_flag $YN.;
        if not missing(codelist) then do;
           put +4 "codelist:";
           put +6 "id:" +1 codelist;
           put +6 'id_uri: https://ncithesaurus.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=' codelist;
           if not missing(codelist_submision_value) then put +6 "submission_value:" +1 codelist_submision_value;
        end;
        if not missing(subset_codelist) then put +6 "subset_codelist:" +1 subset_codelist;

        if not missing(value_list) then do;
          put +4 "value_list:";
          countwords=countw(value_list, ";");
          do i=1 to countwords;
            value=strip(scan(value_list, i, ";"));
            put +7 "-" +1 value;
          end;
        end;


        if not missing(assigned_value) then do;
           put +4 "assigned_term:";
           if not missing(assigned_term) then put +6 "code:" +1 assigned_term;
           put +6 "value:" +1 assigned_value;
        end;
        if not missing(role) then put +4 "role:" +1 role;
        if not missing(subject) then do;
          linking_phrase_low = lowcase(linking_phrase);
          put +4 "relationship:";
          put +6 "subject:" +1 subject;
          put +6 "linking_phrase:" +1 linking_phrase_low;
          put +6 "predicate_term:" +1 predicate_term;
          put +6 "object:" +1 object;
        end;

        if not missing(data_type) then put +4 "data_type:" +1 data_type;
        if not missing(length) then put +4 "length:" +1 length;
        if not missing(format) then put +4 "format:" +1 format;
        if not missing(significant_digits) then put +4 "significant_digits:" +1 significant_digits;

        if upcase(mandatory_variable)= "Y" then put +4 "mandatory_variable:" +1 mandatory_variable $YN.;
        if upcase(mandatory_value)= "Y" then put +4 "mandatory_value:" +1 mandatory_value $YN.;

        if not missing(origin_type) then put +4 "origin_type:" +1 origin_type;
        if not missing(origin_source) then put +4 "origin_source:" +1 origin_source;
        if not missing(comparator) then put +4 "comparator:" +1 comparator;

        if upcase(vlm_target)= "Y" then put +4 "vlm_target:" +1 vlm_target $YN.;

    end;
  run;

%mend generate_bc_sdtm;

%let root=C:\_github\cdisc-org\COSMoS;
%let _debug=0;

options sasautos = ("&root/macros", %sysfunc(compress(%sysfunc(getoption(sasautos)),%str(%(%)))));
options ls=256;

proc format;
  value $YN
    "Y" = "true"
    "y" = "true"
    "N" = "false"
    "n" = "false"
  ;
run;

%generate_bc_sdtm(excel_file=&root\BC Curation Template.xlsx, type=vs, out_folder=.&root/yaml/sdtm, range=SDTM VS BC);
%generate_bc_sdtm(excel_file=&root\\BC Curation Template.xlsx, type=lb, out_folder=&root/yaml/sdtm, range=%str(SDTM LB BC));
