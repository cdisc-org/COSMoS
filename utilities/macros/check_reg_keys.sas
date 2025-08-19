%macro check_reg_keys();

  /* source: https://blogs.sas.com/content/sasdummy/2012/05/22/windows-reg-query-from-sas/ */

  %local os_type TypeGuessRows_ACE;

  %let os_type = &sysscp; /* or &sysscpl */
  %if "&os_type" = "WIN" %then %do;

    %let key1 = HKLM\SOFTWARE\Microsoft\Office;
    %let key2 = HKLM\SOFTWARE\WOW6432Node\Microsoft\Jet\4.0\Engines;
  
    /* Requires XCMD privileges */
    filename reg pipe
      "reg query ""&key1"" /s /f TypeGuessRows";
    
    %let TypeGuessRows_ACE = 0;
     
    data _null_;
      infile reg dsd;
      length TypeGuessRows 8;
      format TypeGuessRows 4.;
      input;
      if index(_infile_, "HKEY") then put "NOTE: " _infile_;
      if (find(_infile_,'TypeGuessRows')>0) then
        do;
          TypeGuessRows = input(trim(scan(_infile_,-1,'x')),hex2.);
          if TypeGuessRows=0 then put "NOTE: " TypeGuessRows= /;
                             else do;
                               put "WARN" "NING: " TypeGuessRows= /;
                               call symput('TypeGuessRows_ACE',TypeGuessRows);
                             end;
        end;
    run;
     
    filename reg clear;
    
    /* Requires XCMD privileges */
    filename reg pipe
      "reg query ""&key2"" /s /f TypeGuessRows";
    
    data _null_;
      infile reg dsd;
      length TypeGuessRows 8;
      format TypeGuessRows 4.;
      input;
      if index(_infile_, "HKEY") then put "NOTE: " _infile_;
      if (find(_infile_,'TypeGuessRows')>0) then
        do;
          TypeGuessRows = input(trim(scan(_infile_,-1,'x')),hex2.);
          if TypeGuessRows=0 then put "NOTE: " TypeGuessRows= /;
                             else do;
                               put "WARN" "NING: " TypeGuessRows= /;
                               call symput('TypeGuessRows_ACE',TypeGuessRows);
                             end;
        end;
    run;
     
    %put Excel (ACE) TypeGuessRows is %trim(&TypeGuessRows_ACE.);
    filename reg clear;

  %end;
  %else %do;
    %put NOTE: This SAS session is running on a non-Windows operating system (e.g., UNIX, Linux).;
  %end;
    
  
%mend check_reg_keys;  
  
