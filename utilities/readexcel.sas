%macro ReadExcel(file=, range=, dsout=, drop=, keep=, rename=);

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
run;

data &dsout(&drop &keep &rename);
 set &dsout;
  format _character_;
  informat _character_;
run;

%if &_Debug %then %do;
  proc contents data=&dsout varnum;
  title "ReadExcel";
  run;

  proc print data=&dsout(obs=10);
  title "ReadExcel";
  run;

%end;

%mend ReadExcel;