%let root=C:/_github/cdisc-org/COSMoS;

%include "&root/utilities/config.sas";

%if %sysfunc(exist(macros.funcs)) %then %do;
  proc datasets library=macros nolist;
     delete funcs;
  run;
%end;

proc fcmp outlib=macros.funcs.python;

  function get_predicateterm(linkingPhrase $) $;
    length predicateTerm $128;
    declare hash hh(dataset: "data.sdtm_linkingphrases_predterms");
    rc=hh.definedata("predicateTerm");
    rc=hh.definekey("linkingPhrase");
    rc=hh.definedone();
    rc=hh.find();
    if rc eq 0 then return(predicateTerm);
    else return ("");
  endsub;

  function exists_predicaterm_linkingphrase(linkingPhrase $, predicateTerm $);
    declare hash hh(dataset: "data.sdtm_linkingphrases_predterms");
    rc=hh.definedata("predicateTerm");
    rc=hh.definekey("linkingPhrase", "predicateTerm");
    rc=hh.definedone();
    rc=hh.find();
    if rc eq 0 then return(1);
    else return (0);
  endsub;

  function exists_predicateterm(predicateTerm $);
    declare hash hh(dataset: "data.sdtm_predicateterms");
    rc=hh.definedata("predicateTerm");
    rc=hh.definekey("predicateTerm");
    rc=hh.definedone();
    rc=hh.find();
    if rc eq 0 then return(1);
    else return (0);
  endsub;

  function get_term_code(codelist_conceptId $, codedValue $) $;
    length codedValue_conceptId $20;
    declare hash hh(dataset: "data.sdtm_latest_codelist_package");
    rc=hh.definedata("codedValue_conceptId");
    rc=hh.definekey("codelist_conceptId", "codedValue");
    rc=hh.definedone();
    rc=hh.find();
    if rc eq 0 then return(codedValue_conceptId);
    else return ("");
  endsub;

  function get_term_value(codelist_conceptId $, codedValue_conceptId $) $;
    length codedValue $200;
    declare hash hh(dataset: "data.sdtm_latest_codelist_package");
    rc=hh.definedata("codedValue");
    rc=hh.definekey("codelist_conceptId", "codedValue_conceptId");
    rc=hh.definedone();
    rc=hh.find();
    if rc eq 0 then return(codedValue);
    else return ("");
  endsub;

  function get_term_preferred_term(codelist_conceptId $, codedValue_conceptId $) $;
    length preferredTerm $200;
    declare hash hh(dataset: "data.sdtm_latest_codelist_package");
    rc=hh.definedata("preferredTerm");
    rc=hh.definekey("codelist_conceptId", "codedValue_conceptId");
    rc=hh.definedone();
    rc=hh.find();
    if rc eq 0 then return(preferredTerm);
    else return ("");
  endsub;

  function get_codelist_submissionvalue(codelist_conceptId $) $;
    length codelist_SubmissionValue $20;
    declare hash hh(dataset: "data.sdtm_latest_codelist_package");
    rc=hh.definedata("codelist_SubmissionValue");
    rc=hh.definekey("codelist_conceptId");
    rc=hh.definedone();
    rc=hh.find();
    if rc eq 0 then return(codelist_SubmissionValue);
    else return ("");
  endsub;

  function get_codelist_extensible(codelist_conceptId $) $;
    length codelist_extensible $20;
    declare hash hh(dataset: "data.sdtm_latest_codelist_package");
    rc=hh.definedata("codelist_extensible");
    rc=hh.definekey("codelist_conceptId");
    rc=hh.definedone();
    rc=hh.find();
    if rc eq 0 then return(codelist_extensible);
    else return ("");
  endsub;

  subroutine get_definitions(code $, definition $, definition_cdisc $);
    length definition cdisc_definition $400;
    outargs definition, definition_cdisc;
    declare object py1(python);
    submit into py1;
    def getDefinitions(ccode):
      """Output: conceptDefinition, conceptDefinitionCDISC"""
      import requests
      url = 'https://api-evsrest.nci.nih.gov/api/v1/concept/ncit/'+ccode+'?include=summary'
      r = requests.get(url)
      concept_info = r.json()
      conceptDefinition = ''
      conceptDefinitionCDISC = ''
      if 'definitions' in concept_info:
        for d in concept_info['definitions']:
          if d['source'] == 'CDISC' :
            conceptDefinitionCDISC = d['definition']
        for d in concept_info['definitions']:
          if d['source'] == 'NCI' :
            conceptDefinition = d['definition']
        if conceptDefinition == '':
          for d in concept_info['definitions']:
            if d['source'] == 'CDISC' :
              conceptDefinition = d['definition']
        if conceptDefinition == '':
          for d in concept_info['definitions']:
            if d['source'] == 'NCI-GLOSS' :
              conceptDefinition = d['definition']
        if conceptDefinition == '':
          for d in concept_info['definitions']:
            if d['source'] == 'CDISC-GLOSS' :
              conceptDefinition = d['definition']
      return conceptDefinition, conceptDefinitionCDISC
    endsubmit;
    rc = py1.publish();
    rc = py1.call('getDefinitions', code);
    definition = py1.results['conceptDefinition'];
    definition_cdisc = py1.results['conceptDefinitionCDISC'];
  endsub;

  subroutine get_shortname(code $, shortname $);
    length shortname $400;
    outargs shortname;
    declare object py2(python);
    submit into py2;
    def getShortName(ccode):
      """Output: conceptName"""
      import requests
      url = 'https://api-evsrest.nci.nih.gov/api/v1/concept/ncit/'+ccode+'?include=summary'
      r = requests.get(url)
      concept_info = r.json()
      try:
        shortName = concept_info['name']
      except:
        shortName = ''
      return shortName
    endsubmit;
    rc = py2.publish();
    rc = py2.call('getShortName', code);
    shortname = py2.results['conceptName'];
  endsub;

  subroutine get_parent_code_shortname(code $, parentcode $, parentshortname $);
    length parentcode parentcode_shortname $400;
    outargs parentcode, parentshortname;
    declare object py3(python);
    submit into py3;
    def getParent(ccode):
      """Output: parentCode, parentShortName"""
      import requests
      url = 'https://api-evsrest.nci.nih.gov/api/v1/concept/ncit/'+ccode+'/parents'
      r = requests.get(url)
      concept_info = r.json()
      parentCode = ''
      parentShortName = ''
      try:
          parentCode = ";".join([v['code'] for v in concept_info])
          parentShortName = ";".join([v['name'] for v in concept_info])
      except:
          parentCode = ''
          parentShortName = ''
      return parentCode, parentShortName
    endsubmit;
    rc = py3.publish();
    rc = py3.call('getParent', code);
    parentcode = py3.results['parentCode'];
    parentshortname = py3.results['parentShortName'];
  endsub;
  
  subroutine get_synonyms(code $, synonyms $);
    length synonyms $4000;
    outargs synonyms;
    declare object py4(python);
    submit into py4;
    def getSynonyms(ccode):
      """Output: synonyms"""
      import requests
      url = 'https://api-evsrest.nci.nih.gov/api/v1/concept/ncit/'+ccode+'?include=synonyms'
      r = requests.get(url)
      concept_info = r.json()
      synonyms = ''
      try:
          synonyms = [v['name'] for v in concept_info['synonyms']]
          synonyms = ";".join(list(dict.fromkeys(synonyms)))
      except:
        synonyms = ''
      return synonyms
    endsubmit;
    rc = py4.publish();
    rc = py4.call('getSynonyms', code);
    synonyms = py4.results['synonyms'];
  endsub;

  subroutine get_preferred_term(code $, preferredterm $);
    length preferredterm $400;
    outargs preferredterm;
    declare object py5(python);
    submit into py5;
    def getPreferredTerm(ccode):
        """Output: preferredTerm"""
        import requests
        url = 'https://api-evsrest.nci.nih.gov/api/v1/concept/ncit/'+ccode+'?include=synonyms'
        r = requests.get(url)
        concept_info = r.json()
        preferredTerm = ''
        if 'synonyms' in concept_info:
          for d in concept_info['synonyms']:
              if d['type'] == 'Preferred_Name':
                  preferredTerm = d['name']
                  break
        return preferredTerm
    endsubmit;
    rc = py5.publish();
    rc = py5.call('getPreferredTerm', code);
    preferredterm = py5.results['preferredTerm'];
  endsub;
  
  subroutine get_concept_status(code $, status $);
    length status $32;
    outargs status;
    declare object py6(python);
    submit into py6;
    def getConceptStatus(ccode):
        """Output: conceptStatus"""
        import requests
        url = 'https://api-evsrest.nci.nih.gov/api/v1/concept/ncit/'+ccode+'?include=minimal'
        r = requests.get(url)
        concept_info = r.json()
        try:
          conceptStatus = concept_info['conceptStatus']
        except:
          conceptStatus = ''
        return conceptStatus
    endsubmit;
    rc = py6.publish();
    rc = py6.call('getConceptStatus', code);
    status = py6.results['conceptStatus'];
  endsub;
  
  subroutine insert_image(excel_file $, excel_file_new $, image_file $, sheet_name $, anchor $, width, height);
    declare object py7(python);
    /* Create an embedded Python block to write your Python function */
    submit into py7;
    def insert_image(excel_file, excel_file_new, image_file, sheet_name, anchor, width, height):
        """Output: MyKey"""
        import os
        import openpyxl
        from openpyxl import Workbook
        from openpyxl.drawing.image import Image
        wb = openpyxl.load_workbook(excel_file)
        ws = wb[sheet_name]
        img = openpyxl.drawing.image.Image(image_file)
        img.width = width
        img.height = height
        img.anchor = anchor
        ws.add_image(img)
        wb.save(excel_file_new)
    endsubmit;
    /* Publish the code to the Python interpreter */
    rc=py7.publish();
    /* Call the Python function from SAS */
    rc = py7.call('insert_image', excel_file, excel_file_new, image_file, sheet_name, anchor, width, height);
  endsub;
  
quit;

/* Test the functions */


%macro assert_equal(val1, val2);
  if &val1 ne &val2 then putlog 'ERR' 'OR:' &val1.= " - " &val2;
%mend assert_equal;

data test;
  length ccodes $200 ccode ccode_parent $100 status shortname shortname_parent preferred_term $100 definition definition_cdisc $1000 synonyms $4000;

  * ccodes = "C103420, C117404, C117426, C117446, C124415, C124448, C49164, C94523, C94525, C94534, C94535, C96613, C96642, C96643, C96684, C96685";
  * ccodes = "C124415, C117426";
  ccodes = "C62656, C79416, C15190, C94411, C28234, C147856, C171439, C161483, C54706, NEW_1, C168688, C173522, C164634, C81328, C49672, C54706, C25298, C25299, C49676, C16358, C49680, C49677, C174446, C100948, C49678";

  do i=1 to countw(ccodes);
    call missing(status, ccode_parent, shortname, shortname_parent, definition, definition_cdisc, synonyms, preferred_term);
    ccode=scan(ccodes, i);
    call get_shortname(ccode, shortname);
    call get_definitions(ccode, definition, definition_cdisc);
    call get_parent_code_shortname(ccode, ccode_parent, shortname_parent);
    call get_synonyms(ccode, synonyms);
    call get_preferred_term(ccode, preferred_term);
    call get_concept_status(ccode, status);
    output;
  end;
run;

data codelists1;
  codelist_code="C128686";
  codelist="PKUDUG";
  _codelist_SubmValue = get_codelist_submissionvalue(codelist_code);
  term="g/mL/ug";
  term_code="C119365";
  _codedValue_conceptId = get_term_code(codelist_code, term);
  _codedValue = get_term_value(codelist_code, term_code);
  _codedValue_preferred = get_term_preferred_term(codelist_code, term_code);
  _codelist_Extensible = get_codelist_extensible(codelist_code);
  %assert_equal(_codedValue_conceptId, term_code);
  %assert_equal(_codedValue, term);
  %assert_equal(_codedValue_preferred, "Gram per Milliliter per Microgram");
  %assert_equal(_codelist_Extensible, "Yes");

  _codelist_SubmValue_qscat = get_codelist_submissionvalue("C100129");
  _codelist_Extensible_yes = get_codelist_extensible("C100129");
  %assert_equal(_codelist_SubmValue_qscat, "QSCAT");
  %assert_equal(_codelist_Extensible_yes, "Yes");

  _codelist_SubmValue_TENMW1TC = get_codelist_submissionvalue("C141657");
  _codelist_Extensible_no = get_codelist_extensible("C141657");
  %assert_equal(_codelist_SubmValue_TENMW1TC, "TENMW1TC");
  %assert_equal(_codelist_Extensible_no, "No");

  _codelist_SubmValue_APCH101OR = get_codelist_submissionvalue("C182484");
  _codelist_Extensible_no = get_codelist_extensible("C182484");
  %assert_equal(_codelist_SubmValue_APCH101OR, "APCH101OR");
  %assert_equal(_codelist_Extensible_no, "No");
  

  put (_all_) (=/) ;
  output;
  
run;


data codelists2;
  codelist="C66797";
  codelist_SubmValue="IECAT";
  _codelist_SubmValue = get_codelist_submissionvalue(codelist);
  term_code="C25532";
  term="INCLUSION";
  _codedValue = get_term_value(codelist, term_code);
  _codedValue_conceptId = get_term_code(codelist, term);
  _codedValue_preferred = get_term_preferred_term(codelist, term_code);
  _codelist_Extensible = get_codelist_extensible(codelist);

  put (_all_) (=/) ;
  output;
  
run;

data relationships;
  linkingPhrase = "is a dictionary-derived term for the value in";
  predicateTerm = "IS_DERIVED_FROM";
  _predicateTerm = get_predicateterm(linkingPhrase);
  exist = exists_predicateterm(predicateTerm);
  exist2 = exists_predicaterm_linkingphrase(linkingPhrase, predicateTerm);
  
  predicateTerm0 = get_predicateterm("is bad luck");
  existnot = exists_predicateterm("NOPE");
  existnot2 = exists_predicaterm_linkingphrase("bad luck", "NOPE");
  existnot3 = exists_predicaterm_linkingphrase("", "");

  put (_all_) (=/) ;
  output;
run;

ods listing close;
ods html5 file="&root/utilities/create_functions.html";

  proc print data=test;
    title01 "Test Functions - %sysfunc(datetime(), is8601dt.)";
    var ccode status ccode_parent shortname preferred_term shortname_parent definition definition_cdisc synonyms;
  run;

  proc print data=codelists1;
    title01 "Test Functions - codelists - %sysfunc(datetime(), is8601dt.)";
  run;

  proc print data=codelists2;
    title01 "Test Functions - codelists - %sysfunc(datetime(), is8601dt.)";
  run;

  proc print data=relationships;
    title01 "Test Functions - relationships - %sysfunc(datetime(), is8601dt.)";
  run;


ods html5 close;
ods listing;
