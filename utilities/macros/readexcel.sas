%macro ReadExcel(file=, range=, dsout=, drop=, keep=, rename=, print=20);

/*
Problem Note 46472: Character strings can be truncated at 255 or 1024 characters when importing Excel files into SAS
http://support.sas.com/kb/46/472.html
*/

proc import out=&dsout 
            datafile= "&file" 
            dbms=excelcs replace;
  %if %length(&range) %then %do;
     range="&range"; 
  %end;
     scantext=yes;
     usedate=yes;
     scantime=yes;
     textsize=32767;
run;

data &dsout(&drop &keep &rename);
  length _tab_ _excel_file_ $100;
  retain _tab_;
  set &dsout;
  format _character_;
  informat _character_;
  _tab_ = compress("&range", "$");
  _excel_file_ = scan("&file", -1, "\/");
run;

%if &_Debug %then %do;
  proc contents data=&dsout varnum;
  title01 "ReadExcel - %sysfunc(datetime(), is8601dt.)";
  run;

  proc print data=&dsout(obs=&print);
  title01 "ReadExcel - %sysfunc(datetime(), is8601dt.)";
  run;

%end;

%mend ReadExcel;