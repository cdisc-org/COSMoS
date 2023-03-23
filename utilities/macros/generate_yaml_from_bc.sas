%macro generate_yaml_from_bc(excel_file=, package=, range=, type=, out_folder=, debug=0);

  %ReadExcel(file=&excel_file, range=&range.$, dsout=bc_&type._&package);

  data bc_&type._&package;
    set bc_&type._&package(where=(not missing(bc_id)));
    bc_id = kcompress(bc_id, , 's');
  run;


  %if &debug %then %do;

    ods listing close;
    ods html5 file="get_bc_&range..html";

    proc contents data=bc_&type._&package varnum;
    run;
    proc print data=bc_&type._&package;
    run;

    ods html5 close;
    ods listing;

  %end;


  data _null_;
    set work.bc_&type._&package;
    length prev_BC_ID $32 outname value qvalue $100 qpackage_date $20 definition2 $4000;;
    retain prev_BC_ID "" count 0;
    outname=catt("&out_folder\biomedical_concept_&type._", lowcase(strip(BC_ID)), ".yaml");
    file dummy filevar=outname dlm=",";

    short_Name=translate(short_Name, " ", "00A0"x);
    short_Name = compress(short_Name, , 'kw');
    parent_bc_id=kcompress(parent_bc_id, , 's');
    dec_id=kcompress(dec_id, , 's');
    definition=tranwrd(definition, '"', '\"');
    definition = strip(definition);
    definition2 = compbl (translate (definition, "", cats(collate (1, 31), collate (128, 255))));
    if definition ne definition2 then putlog "WARNING: &type " definition= / definition2=;

    prev_BC_ID = lag(BC_ID);
    if not(missing(BC_ID)) and (prev_BC_ID ne BC_ID) then do;
      count=0;
      qpackage_date = quote(strip(package_date));
      put "packageDate:" +1 qpackage_date;
      put "packageType:" +1 "bc";
      put "conceptId:" +1 BC_ID;
      put 'href: https://ncithesaurus.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=' bc_id;
      if not missing(parent_bc_id) then do;
        put "parentConceptId:" +1 parent_bc_id;
        * put 'parent_id_uri: https://ncithesaurus.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=' parent_bc_id;
      end;

      if not missing(bc_category) then do;
        put "category:";
        countwords=countw(bc_category, ";");
        do i=1 to countwords;
          value=strip(scan(bc_category, i, ";"));
          if not missing(value) then put +2 "-" +1 value;
        end;
      end;
      else putlog "ERROR: &type - category missing: " BC_ID "- " short_name;

      if missing(short_name) then putlog "ERROR: &type - short_name missing: " BC_ID;
      put "shortName:" +1 short_name;

      if not missing(synonym) then do;
        if index(synonym, ",") > 0 then putlog "WARNING: &type - synonym issue: " BC_ID "- " short_name "- " synonym;
        put "synonym:";
        countwords=countw(synonym, ";");
        do i=1 to countwords;
          value=strip(scan(synonym, i, ";"));
          if not missing(value) then put +2 "-" +1 value;
        end;
      end;

      if not missing(result_scale)
        then put "resultScale:" +1 Result_Scale;
        else putlog "### NOTE: &type - resultscale missing: " BC_ID "- " short_name;

      if not missing(definition) then do;
        put "definition:" +1 Definition;
      end;
      else putlog "ERROR: &type - definition missing: " BC_ID "- " short_name;

      if not missing(system) then do;
        put "coding:";
        countwords=countw(system, ";");
        do i=1 to countwords;
          value=strip(scan(code, i, ";"));
          if not missing(value) then put +2 "- code:" +1 value;
          value=strip(scan(system, i, ";"));
          if not missing(value) then put +4 "system:" +1 value;
          value=strip(scan(system_name, i, ";"));
          if not missing(value) then put +4 "systemName:" +1 value;
        end;
      end;
    end;

    count+1;
    if count=2 and not missing(dec_id) then put "dataElementConcepts:";

    if not missing(dec_id) then do;
      put "  - conceptId:" +1 dec_id;
      put +4 'href: https://ncithesaurus.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=' dec_id;
      put +4 "shortName:" +1 dec_label;
      if not missing(data_type) then put +4 "dataType:" +1 data_type;
      if not missing(example_set) then do;
        if index(example_set, ",") > 0 then putlog "WARNING: &type - example_set issue: " BC_ID "- " DEC_ID "- " dec_label"- " example_set;
        put +4 "exampleSet:";
        countwords=countw(example_set, ";");
        do i=1 to countwords;
          value=strip(scan(example_set, i, ";"));
          if not missing(value) then do;
            qvalue=quote(strip(value));
            put +6 "-" +1 qvalue;
          end;
        end;
      end;
    end;
  run;

%mend generate_YAML_from_BC;

/*******************************************************************************/

