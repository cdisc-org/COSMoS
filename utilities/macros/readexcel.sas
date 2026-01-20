%macro ReadExcel(file=, range=, dsout=, where=, drop=, keep=, rename=, print=20);

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
     scantext = yes;
     usedate = yes;
     scantime = yes;
     textsize = 32767;
run;

data &dsout(
  %if %sysevalf(%superq(where)=, boolean) eq 0 %then where = (&where);
  %if %sysevalf(%superq(drop)=, boolean) eq 0 %then drop = &drop;
  %if %sysevalf(%superq(keep)=, boolean) eq 0 %then keep = &keep;
  %if %sysevalf(%superq(rename)=, boolean) eq 0 %then rename = (&rename);
  );
  length _tab_ _excel_file_ $100 _record_ 8;
  retain _tab_;
  set &dsout;
  format _character_;
  informat _character_;
  _tab_ = compress("&range", "$");
  _excel_file_ = scan("&file", -1, "\/");
  _record_ = _n_;
run;

%if &_Debug ge 1 %then %do;
  proc contents data=&dsout varnum;
  title01 "ReadExcel - %sysfunc(datetime(), is8601dt.)";
  run;

  proc print data=&dsout(obs=&print);
  title01 "ReadExcel - %sysfunc(datetime(), is8601dt.)";
  run;

%end;

%mend ReadExcel;