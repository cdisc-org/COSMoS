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
    length codedValue_conceptId $20;
    declare hash hh(dataset: "data.sdtm_latest_codelist_package");
    rc=hh.definedata("codelist_SubmissionValue");
    rc=hh.definekey("codelist_conceptId");
    rc=hh.definedone();
    rc=hh.find();
    if rc eq 0 then return(codelist_SubmissionValue);
    else return ("");
  endsub;

  function get_codelist_extensible(codelist_conceptId $) $;
    length codedValue_conceptId $20;
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
      if 'definitions' in concept_info:
        conceptDefinition = ''
        conceptDefinitionCDISC = ''
        for d in concept_info['definitions']:
          if d['source'] == 'NCI' :
            conceptDefinition = d['definition']
          if d['source'] == 'CDISC' :
            conceptDefinitionCDISC = d['definition']
      else:
        conceptDefinition = ''
        conceptDefinitionCDISC = ''
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
  
  subroutine insert_image(excel_file $, excel_file_new $, image_file $, sheet_name $, anchor $, width, height);
    declare object py5(python);
    /* Create an embedded Python block to write your Python function */
    submit into py5;
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
    rc=py5.publish();
    /* Call the Python function from SAS */
    rc = py5.call('insert_image', excel_file, excel_file_new, image_file, sheet_name, anchor, width, height);
  endsub;
  
run;

/* Test the functions */

data test;
  length ccodes $200 ccode ccode_parent $100 shortname shortname_parent $100 definition definition_cdisc $1000 synonyms $4000;

  * ccodes = "C103420, C117404, C117426, C117446, C124415, C124448, C49164, C94523, C94525, C94534, C94535, C96613, C96642, C96643, C96684, C96685";
  * ccodes = "C124415, C117426";
  ccodes = "C147856, C171439, C161483, C54706, NEW_1, C168688, C173522, C164634, C81328, C49672, C54706, C25298, C25299, C49676, C16358, C49680, C49677, C174446, C100948, C49678";

  do i=1 to countw(ccodes);
    call missing(ccode_parent, shortname, shortname_parent, definition, definition_cdisc, synonyms);
    ccode=scan(ccodes, i);
    call get_shortname(ccode, shortname);
    call get_definitions(ccode, definition, definition_cdisc);
    call get_parent_code_shortname(ccode, ccode_parent, shortname_parent);
    call get_synonyms(ccode, synonyms);
    output;
  end;
run;

ods listing close;
ods html5 file="&root/utilities/create_functions.html";

  proc print data=test;
    title01 "Test Functions - %sysfunc(datetime(), is8601dt.)";
    var ccode ccode_parent shortname shortname_parent definition definition_cdisc synonyms;
  run;

ods html5 close;
ods listing;


data codelists;
  exp_codelist_SubmissionValue="PKUDUG";
  exp_term="C119365";
  codedValue_conceptId = get_term_code("C128686", "g/mL/ug");
  codedValue_preferred = get_term_preferred_term("C128686", "C119365");
  codelist_SubmValue = get_codelist_submissionvalue("C128686");
  codelist_Extensible = get_codelist_extensible("C128686");

  codelist_SubmValue_qscat = get_codelist_submissionvalue("C100129");
  codelist_Extensible_yes = get_codelist_extensible("C100129");

  codelist_SubmValue_TENMW1TC = get_codelist_submissionvalue("C141657");
  codelist_Extensible_no = get_codelist_extensible("C141657");

  put (_all_) (=/) ;
run;

data relationships;
  linkingPhrase = "is a dictionary-derived term for the value in";
  predicateTerm = get_predicateterm(linkingPhrase);
  exist = exists_predicateterm(predicateTerm);
  exist2 = exists_predicaterm_linkingphrase(linkingPhrase, predicateTerm);
  
  predicateTerm0 = get_predicateterm("is bad luck");
  existnot = exists_predicateterm("NOPE");
  existnot2 = exists_predicaterm_linkingphrase("bad luck", "NOPE");
  existnot3 = exists_predicaterm_linkingphrase("", "");

  put (_all_) (=/) ;
run;
