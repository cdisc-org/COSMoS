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
        put "synonym:";
        countwords=countw(synonym, ";");
        do i=1 to countwords;
          value=strip(scan(synonym, i, ";"));
          put +2 "-" +1 value;    
        end;  
      end;

      if not missing(result_scale) then put "resultScale:" +1 Result_Scale;
      if not missing(definition) then do;
        qDefinition = quote(strip(definition));
        put "definition:" +1 qDefinition;
      end;

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
      put +4 "label:" +1 dec_label; 
      if not missing(data_type) then put +4 "dataType:" +1 data_type; 
      if not missing(example_set) then do;
        put +4 "exampleSets:";
        countwords=countw(example_set, ";");
        do i=1 to countwords;
          value=strip(scan(example_set, i, ";"));
          put +7 "-" +1 value;    
        end;  
      end;
    end;  
  run;

%mend generate_bc;


%let root=C:/_github/cdisc-org/COSMoS;
%let _debug=0;

options sasautos = ("&root/sas", %sysfunc(compress(%sysfunc(getoption(sasautos)),%str(%(%)))));
options ls=256;

%generate_bc(excel_file=&root\BC Curation Template.xlsx, type=vs, out_folder=&root/yaml/bc, range=Conceptual VS BC);
%generate_bc(excel_file=&root\\BC Curation Template.xlsx, type=lb, out_folder=&root/yaml/bc, range=%str(Conceptual LB (Common) BC));
