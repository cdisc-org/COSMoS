%macro generate_bc(excel_file=, range=, type=, out_folder=, debug=1);

  %ReadExcel(file=&excel_file, range=&range.$, dsout=bc_&type);

  data bc__&type;
    set bc_&type(where=(not missing(bc_id)));
  run;

  %if &debug %then %do;

    ods listing close;
    ods html5 file="get_bc_&range..html";

    proc contents data=bc_&type varnum;
    run;
    proc print data=bc_&type;
    run;

    ods html5 close;
    ods listing;

  %end;

  data _null_;
    set work.bc_&type;
    retain count 0;
    length outname value $100 qpackage_date $20 qDefinition $1024;
    by BC_ID notsorted;
    outname=catt("&out_folder\biomedical_concept_&type._", lowcase(strip(BC_ID)), ".yaml");
    file dummy filevar=outname dlm=",";
    if first.bc_id and not(missing(bc_id)) then do;
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
          put +2 "-" +1 value;
        end;
      end;

      put "shortName:" +1 short_name;

      if not missing(synonym) then do;
        if index(synonym, ",") > 0 then putlog 'WARNING: ' BC_ID 'Synonym issue: '  synonym;
        put "synonym:";
        countwords=countw(synonym, ";");
        do i=1 to countwords;
          value=strip(scan(synonym, i, ";"));
          put +2 "-" +1 value;
        end;
      end;

      if not missing(result_scale)
        then put "resultScale:" +1 Result_Scale;
        else putlog 'WARNING: ' BC_ID short_name 'no resultscale';

      if not missing(definition) then do;
        qDefinition = quote(strip(definition));
        put "definition:" +1 qDefinition;
      end;
      else putlog 'WARNING: ' BC_ID short_name 'no definition';

      if not missing(system) then do;
        put "coding:";
        countwords=countw(system, ";");
        do i=1 to countwords;
          value=strip(scan(code, i, ";"));
          put +2 "- code:" +1 value;
          value=strip(scan(system, i, ";"));
          put +4 "system:" +1 value;
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
        put +4 "exampleSet:";
        countwords=countw(example_set, ";");
        do i=1 to countwords;
          value=strip(scan(example_set, i, ";"));
          put +6 "-" +1 value;
        end;
      end;
    end;
  run;

%mend generate_bc;

/*******************************************************************************/

%let root=C:\_github\cdisc-org\COSMoS;
options sasautos = ("&root/utilities", %sysfunc(compress(%sysfunc(getoption(sasautos)),%str(%(%)))));
options ls=256;
%let _debug=0;

%let package=20221026;
%let Excelfile=BC_Package_2022_10_26.xlsx;

%generate_bc(excel_file=&root/curation/&Excelfile, type=vs, out_folder=&root/yaml/&package/bc, range=Conceptual VS BC);
%generate_bc(excel_file=&root/curation/&Excelfile, type=lb, out_folder=&root/yaml/&package/bc, range=%str(Conceptual LB (Common) BC));