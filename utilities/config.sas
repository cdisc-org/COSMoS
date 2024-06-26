options sasautos = ("&root/utilities/macros", %sysfunc(compress(%sysfunc(getoption(sasautos)),%str(%(%)))));

options set=MAS_PYPATH="&root/venv/Scripts/python.exe";
options set=MAS_M2PATH="%sysget(SASROOT)/tkmas/sasmisc/mas2py.py";


libname macros "&root/utilities/macros";
options cmplib=macros.funcs;
options ls=max ps=max;

libname data "&root/utilities/data";

%let today=%sysfunc(date(), is8601da.);
%let todays=%sysfunc(date(), b8601da.);
%let now=%sysfunc(datetime(), is8601dt.);

%let rest_debug=%str(OUTPUT_TEXT NO_REQUEST_HEADERS NO_REQUEST_BODY RESPONSE_HEADERS NO_RESPONSE_BODY);
%let base_url=https://library.cdisc.org/api;
%*let base_url_cosmos=https://library.cdisc.org/api/cosmos/v2;
%let base_url_cosmos=https://dev.cdisclibrary.org/api/cosmos/v2;
%* The CDISC Library API key has been set as an environment variable;
%*let api_key=%sysget(CDISC_LIBRARY_API_KEY);
%let api_key=%sysget(CDISC_LIBRARY_API_KEY_DEV);


%macro add2issues_bc(condition, type, expected, actual, comment, extracode=, severity=WARNING);
  if &condition then do;
    severity="&severity";
    issue_type = "&type";
    expected_value=&expected;
    actual_value=&actual;
    comment=&comment;

    putlog "WARN" "ING: &type " _excel_file_= _tab_= BC_ID= short_name= dec_id= 
      %if &actual NE "" %then &actual.= ;
      %if &expected NE "" %then &expected.= ;
      comment;

    &extracode;
    output;
  end;
%mend add2issues_bc;

%macro add2issues_sdtm(condition, type, expected, actual, comment, extracode=, severity=WARNING);
  if &condition then do;
    severity="&severity";
    issue_type = "&type";
    expected_value=&expected;
    actual_value=&actual;
    comment=&comment;

    putlog "WARN" "ING: &type " _excel_file_= _tab_= vlm_group_id= sdtm_variable=
      %if &actual NE "" %then &actual.= ;
      %if &expected NE "" %then &expected.= ;
      comment;

    &extracode;
    output;
  end;  
%mend add2issues_sdtm;

