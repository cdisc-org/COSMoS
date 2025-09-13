%macro get_excel_sheets(excel_file=, return=_excel_sheets);
  
  filename _wbzip ZIP "&excel_file" member='xl/workbook.xml';
  filename _wb temp ;
  data _null_;
    rc=fcopy('_wbzip','_wb');
    put rc=;
  run;
  filename _wbzip clear;
  
  %*----------------------------------------------------------------------;
  %* Generate LIBNAME pointing to copy of xl/workbook.xml from XLSX file ;
  %*----------------------------------------------------------------------;
  filename _wbmap temp;
  libname _wb xmlv2 xmlmap=_wbmap automap=reuse;
  
  proc sql noprint;
    select sheet_name into :&return separated by '|' 
    from _wb.sheet
    order by sheet_name, sheet_sheetId
    ;
  quit; 
  
  filename _wbmap clear;
  filename _wb clear;
  libname _wb clear;
  
%mend get_excel_sheets;
