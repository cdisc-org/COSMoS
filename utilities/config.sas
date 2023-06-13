options sasautos = ("&root/utilities/macros", %sysfunc(compress(%sysfunc(getoption(sasautos)),%str(%(%)))));

libname macros "&root/utilities/macros";
options cmplib=macros.funcs;
options ls=max ps=max;

libname data "&root/utilities/data";

%macro add2issues_bc(condition, type, expected, actual, comment, extracode=);
  if &condition then do;
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

%macro add2issues_sdtm(condition, type, expected, actual, comment, extracode=);
  if &condition then do;
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

