%macro generate_yaml_from_bc(excel_file=, range=, type=, package=, override_package_date=, out_folder=, debug=0);

  %let type = %sysfunc(tranwrd(&type, %str(-), %str(_)));
  
  %ReadExcel(file=&excel_file, range=&range.$, dsout=bc_&type._&package, print=999);

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


  data issues(keep=_excel_file_ _tab_ package_date severity BC_ID short_name dec_id dec_label issue_type expected_value actual_value comment);
    length prev_BC_ID parent_bc_id_nci $32 concept_status $32 outname $512 value qvalue $1000 package_date qpackage_date $64 definition2 definition_nci definition_cdisc 
           short_name short_name_parent short_name_nci dec_label short_name_dec_nci short_name_parent_nci $4000
           issue_type $64 expected_value  actual_value comment $2048;
    set work.bc_&type._&package;
    retain prev_BC_ID "" count decs 0 result_scales_yn 0;

    call missing(concept_status, short_name_parent, short_name_nci, parent_bc_id_nci, short_name_dec_nci, short_name_parent_nci, definition_nci, definition_cdisc);
    
    outname=catt("&out_folder\bc_&type._", lowcase(strip(BC_ID)), ".yaml");
    file dummy filevar=outname dlm=",";

    %if %sysevalf(%superq(override_package_date)=, boolean)=0 %then package_date="&override_package_date";;

    ncit_code = kcompress(ncit_code, , 's');
    dec_id = kcompress(dec_id, , 's');
    parent_bc_id=kcompress(parent_bc_id, , 's');
    bc_id=kcompress(bc_id, , 's');
    ncit_dec_code=kcompress(ncit_dec_code, , 's');
    
    short_Name=translate(short_Name, " ", "00A0"x);
    short_Name = compress(short_Name, , 'kw');
    
    definition = strip(definition);
    definition2 = compbl (translate (definition, "", cats(collate (1, 31), collate (128, 255))));
    if definition ne definition2 then putlog / "WARNING: &type " _excel_file_ _tab_ bc_id "definition" / @5 definition / @4 definition2;

    BC_ID=strip(BC_ID);
    prev_BC_ID = lag(BC_ID);
    if not(missing(BC_ID)) and (prev_BC_ID ne BC_ID) then do;
      result_scales_yn = 0;
      count=0;
      decs = 0;
      qpackage_date = quote(strip(package_date));
      put "packageDate:" +1 qpackage_date;
      put "packageType:" +1 "bc";
      put "conceptId:" +1 BC_ID;
      %add2issues_bc(missing(ncit_code), 
                     %str(NCIT_CODE_MISSING), 
                     "", "", "");
      if not missing(ncit_code) then do;
        ncit_code=strip(ncit_code);
        put "ncitCode:" +1 ncit_code;
        put "href: &ncit_explore" ncit_code;
        %add2issues_bc(bc_id ne ncit_code, 
                       %str(BC_ID_NCIT_CODEMISMATCH), 
                       bc_id, ncit_code, "");
                       
        call get_concept_status(ncit_code, concept_status);               
        %add2issues_bc(not missing(concept_status) and (index(concept_status, "Retired") > 0), 
                       %str(BC_ID_CONCEPTSTATUS), 
                       "", concept_status, "");
      end;
      if not missing(parent_bc_id) then do;
        call get_shortname(parent_bc_id, short_name_parent);
        call get_parent_code_shortname(BC_ID, parent_bc_id_nci, short_name_parent_nci);
        %add2issues_bc(parent_bc_id ne parent_bc_id_nci, 
                       %str(PARENT_ID_MISMATCH), 
                       parent_bc_id_nci, parent_bc_id, %str(cats("parent_shortname=", short_name_parent, ", parent_shortname_nci=", short_name_parent_nci)));
        put "parentConceptId:" +1 parent_bc_id;
      end;

      if not missing(bc_categories) then do;
        put "categories:";
        countwords=countw(bc_categories, ";");
        do i=1 to countwords;
          value=strip(scan(bc_categories, i, ";"));
          value=tranwrd(value, '"', '\"');
          if index(value, '"') or index(value, ":") or index(value, "-") then value=cats('"', value, '"');
          if not missing(value) then do;
            put +2 "-" +1 value;
          end;  
        end;
      end;
      %add2issues_bc(missing(bc_categories), 
                     %str(CATEGORIES_MISSING), "", "", "");

      if not missing(short_name) then do;
        if index(short_name, '"') or index(short_name, ":") or index(short_name, "-") 
          then put "shortName:" +1 '"' short_name +(-1) '"';
          else put "shortName:" +1 short_name;
      end;
      
      call get_shortname(ncit_code, short_name_nci);
      %add2issues_bc(((short_name ne short_name_nci) and not missing(short_name_nci)) or (missing(short_name)), 
                     %str(BC_SHORTNAME_MISMATCH_OR_MISSING), short_name_nci, short_name, "");
      %add2issues_bc(((short_name ne short_name_nci)) and (missing(short_name_nci)), 
                     %str(BC_SHORTNAME_MISMATCH_OR_MISSING), short_name_nci, short_name, "", severity=NOTE);
      if not missing(synonyms) then do;
        %add2issues_bc(index(synonyms, ",") > 0, 
                       %str(SYNONYM_ISSUE_COMMA), "", synonyms, "", severity=NOTE);
        put "synonyms:";
        countwords=countw(synonyms, ";");
        do i=1 to countwords;
          value=strip(scan(synonyms, i, ";"));
          value=tranwrd(value, '"', '\"');
          value=tranwrd(value, '{', '\{');
        value=tranwrd(value, '}', '\}');
          if index(value, '"') or index(value, ":") or index(value, "-") then value=cats('"', value, '"');
          if not missing(value) then put +2 "-" +1 value;
        end;
      end;

      if not missing(result_scales) then do;
        result_scales_yn = 1;
        put "resultScales:";
        countwords=countw(result_scales, ";");
        do i=1 to countwords;
          value=strip(scan(result_scales, i, ";"));
          if not missing(value) then put +2 "-" +1 value;
        end;
      end;
      
      call get_definitions(ncit_code, definition_nci, definition_cdisc);
      /*
      definition_nci=tranwrd(definition_nci, '"', '\"');
      definition_cdisc=tranwrd(definition_cdisc, '"', '\"');
      */
      %add2issues_bc(index(definition, '"') > 0, 
                     %str(DEFINITION_QUOTE), "", definition, "");
      %add2issues_bc(((definition ne definition_nci) and not missing(definition_nci)) or (missing(definition)), 
                     %str(DEFINITION_MISMATCH_OR_MISSING), definition_nci, definition, "");
      %add2issues_bc((definition ne definition_nci) and (missing(definition_nci)), 
                     %str(DEFINITION_MISMATCH_OR_MISSING), definition_nci, definition, "", severity=NOTE);

      if not missing(definition) then do;
        definition=tranwrd(definition, '"', '\"');
        if index(definition, '"') or index(definition, ":") or index(definition, "-") 
          then definition=cats('"', definition, '"');;
        put "definition:" +1 definition;
      end;

      if not missing(system_name) then do;
        %add2issues_bc(missing(system) or missing(code), 
                       %str(BC_SYSTEM_CODE_MISSING), 
                       "", "", %str(cats("system_name=", system_name, "system=", system, "code=", code)));
      end;                 
      if not missing(system) then do;
        %add2issues_bc(missing(code), 
                       %str(BC_SYSTEM_CODE_MISSING), 
                       "", "", %str(cats("system=", system)));
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
    if (count=2 and not missing(dec_id) and decs=0) or (count=1 and not missing(dec_id)) then do; 
      
      %add2issues_bc(result_scales_yn eq 0, 
                     %str(RESULTSCALE_MISSING), "", "", "", severity=WARNING);
      %add2issues_bc(missing(dec_label), 
                     %str(DEC_SHORTNAME_MISSING), "", "", "", severity=ERROR);
      %add2issues_bc(missing(data_type), 
                     %str(DEC_DATATYPE_MISSING), "", "", "", severity=ERROR);
      
      decs + 1;
      put "dataElementConcepts:";
    end;  

    if not missing(dec_id) then do;
      
      dec_id=strip(dec_id);
      put "  - conceptId:" +1 dec_id;
      
      %add2issues_bc(missing(ncit_dec_code), 
                     %str(NCIT_DEC_CODE_MISSING), 
                     "", "", "");
      if not missing(ncit_dec_code) then do;
        put +4 "ncitCode:" +1 ncit_dec_code;
        put +4 "href: &ncit_explore" ncit_dec_code;

        call get_concept_status(ncit_dec_code, concept_status);               
        %add2issues_bc(not missing(concept_status) and (index(concept_status, "Retired") > 0), 
                       %str(DEC_ID_CONCEPTSTATUS), 
                       "", concept_status, "");

      end;
      
      %add2issues_bc(dec_id ne ncit_dec_code, 
                     %str(BC_DEC_ID_NCIT_CODEMISMATCH), 
                     dec_id, ncit_dec_code, "");

      if not missing(ncit_dec_code) then do;

        call get_shortname(ncit_dec_code, short_name_dec_nci);
        %add2issues_bc(((dec_label ne short_name_dec_nci) and not missing(short_name_dec_nci)) or (missing(dec_label)), 
                       %str(DEC_SHORTNAME MISMATCH_OR_MISSING), short_name_dec_nci, dec_label, "");
      end;
      put +4 "shortName:" +1 dec_label;
      
      if not missing(data_type) then put +4 "dataType:" +1 data_type;
      %add2issues_bc(missing(data_type), 
                     %str(BC_DEC_DATATYPE_MISSING), 
                     "", "", %str(cats("dec_label=", dec_label)));
      
      if not missing(example_set) then do;
        %add2issues_bc(index(example_set, ",") > 0, 
                       %str(EXAMPLE_SET_ISSUE_COMMA), "", example_set, %str(cats("dec_label=", dec_label)), severity=NOTE);
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
    result_scales = "";
  run;

  data all_issues_bc;
    set all_issues_bc issues;
  run;  

%mend generate_YAML_from_BC;

/*******************************************************************************/

