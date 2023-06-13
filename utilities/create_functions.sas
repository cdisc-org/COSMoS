%let root=C:/_github/cdisc-org/COSMoS;

%include "&root/utilities/config.sas";
  
proc datasets library=macros nolist;
   delete funcs;
run;

proc fcmp outlib=macros.funcs.python;
  
  function get_term_code(codelist_conceptId $, codedValue $) $;    
    attrib codedValue_conceptId length=$20;
    declare hash hh(dataset: "data.codelist_package_sdtm");    
    rc=hh.definedata("codedValue_conceptId");    
    rc=hh.definekey("codelist_conceptId", "codedValue");    
    rc=hh.definedone();    
    rc=hh.find();    
    if rc eq 0 then return(codedValue_conceptId);    
    else return ("");    
  endsub; 
  
  function get_codelist_submissionvalue(codelist_conceptId $) $;    
    attrib codedValue_conceptId length=$20;
    declare hash hh(dataset: "data.codelist_package_sdtm");    
    rc=hh.definedata("codelist_SubmissionValue");    
    rc=hh.definekey("codelist_conceptId");    
    rc=hh.definedone();    
    rc=hh.find();    
    if rc eq 0 then return(codelist_SubmissionValue);    
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
      try:
          parentCode = concept_info[0]['code']
          parentShortName = concept_info[0]['name']
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
run;

data test;
  length ccodes $200 ccode ccode_parent $10 shortname shortname_parent $100 definition definition_cdisc $1000;
  
  * ccodes = "C103420, C117404, C117426, C117446, C124415, C124448, C49164, C94523, C94525, C94534, C94535, C96613, C96642, C96643, C96684, C96685";
  * ccodes = "C124415, C117426";
  ccodes = "C161483, C54706, NEW_1, C168688, C173522, C164634, C81328, C49672, C54706, C25298, C25299, C49676, C16358, C49680, C49677, C174446, C100948, C49678";
  
  do i=1 to countw(ccodes);
    call missing(ccode_parent, shortname, shortname_parent, definition, definition_cdisc);
    ccode=scan(ccodes, i);
    call get_shortname(ccode, shortname);
    call get_definitions(ccode, definition, definition_cdisc);
    * call get_definition_cdisc(ccode, definition_cdisc);
    call get_parent_code_shortname(ccode, ccode_parent, shortname_parent);
    output;
  end;
run;

ods listing close;
ods html5 file="create_functions.html";

  proc print data=test;
    title01 "Test Functions - %sysfunc(datetime(), is8601dt.)";
    var ccode ccode_parent shortname shortname_parent definition definition_cdisc;
  run;  

ods html5 close;
ods listing;

data new;   
  exp_codelist_SubmissionValue="PKUDUG";
  exp_term="C119365";
  codedValue_conceptId = get_term_code("C128686", "g/mL/ug");
  codelist_SubmissionValue = get_codelist_submissionvalue("C128686");
  put (_all_) (=/) ;
run; 

