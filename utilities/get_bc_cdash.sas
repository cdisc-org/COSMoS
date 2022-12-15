%macro generate_bc_cdash(excel_file=, range=, type=, out_folder=, debug=1);

%ReadExcel(file=&excel_file, range=&range.$, dsout=bc_cdash_&type);

  data bc_cdash_&type;
    set bc_cdash_&type(where=(not missing(cdash_group_id)));
    order=_n_;
  run;

  proc sql;
    create table bc_cdash_&type._merged
    as select
      bccdash.*,
      ss.subset_value_list
    from work.bc_cdash_&type bccdash
      left join subsets ss
    on bccdash.subset_codelist = ss.subset_short_name
    order by cdash_group_id, order
    ;
  quit;

  %if &debug %then %do;

    ods listing close;
    ods html5 file="get_bc_cdash_&range..html";

    proc contents data=bc_cdash_&type varnum;
    run;
    proc print data=bc_cdash_&type._merged;
    run;

    ods html5 close;
    ods listing;

  %end;

  data _null_;
    set work.bc_cdash_&type._merged;
    retain count 0;
    length outname $100 qpackage_date qcdashig_start_version qcdashig_end_version $20 linking_phrase_low $512 value $100;
    by cdash_group_id notsorted;
    outname=catt("&out_folder\cdash_bc_specialization_&type._", lowcase(strip(cdash_group_id)), ".yaml");
    file dummy filevar=outname dlm=",";
    if first.cdash_group_id then do;
      count=0;
      qpackage_date = quote(strip(package_date));
      put "packageDate:" +1 qpackage_date;
      put "packageType:" +1 "cdash";
      put "datasetSpecializationId:" +1 cdash_group_id;
      put "domain:" +1 domain;
      put "shortName:" +1 short_name;
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
            put +6 "-" +1 value;
          end;
        end;

        if not missing(assigned_value) then put +4 "assignedValue:" +1 assigned_value;

        if not missing(data_type) then put +4 "dataType:" +1 data_type;
        if not missing(length) then put +4 "length:" +1 length;
        if not missing(significant_digits) then put +4 "significantDigits:" +1 significant_digits;

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

%mend generate_bc_cdash;

/*******************************************************************************/

%let root=C:\_github\cdisc-org\COSMoS;
options sasautos = ("&root/utilities", %sysfunc(compress(%sysfunc(getoption(sasautos)),%str(%(%)))));
options ls=256;
%let _debug=0;

%let package=2023mmdd;
%let Excelfile=Draft_BC_Package_R2_13Dec22.xlsx;

proc format;
  value $YN
    "Y" = "true"
    "y" = "true"
    "N" = "false"
    "n" = "false"
  ;
run;

%ReadExcel(file=&root/curation/&Excelfile, range=Subset Codelist Example$, dsout=subsets);

proc sort data=subsets;
  by Subset_Short_Name Submission_Value;
run;

data subsets(keep=Subset_Short_Name subset_value_list);
  length subset_value_list $8192;
  retain subset_value_list;
  set subsets;
  by Subset_Short_Name Submission_Value;
  if first.Subset_Short_Name then subset_value_list="";
  subset_value_list=catx(";", subset_value_list, Submission_Value);
  if last.Subset_Short_Name then output;
run;

%generate_bc_cdash(excel_file=&root/curation/&Excelfile, type=vs, out_folder=&root/yaml/&package/cdash, range=CDASH VS);
