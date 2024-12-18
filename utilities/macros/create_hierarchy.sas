%macro create_hierarchy(dsin=, child=, parent=, label=, dsout=);
  
  %local
    _Missing
    _parent_n
    _random_
    iteration
    ;
  
    %* Check for missing parameters ;
  %let _Missing=;
  %if %sysevalf(%superq(dsin)=, boolean) %then %let _Missing = &_Missing dsin;
  %if %sysevalf(%superq(child)=, boolean) %then %let _Missing = &_Missing child;
  %if %sysevalf(%superq(parent)=, boolean) %then %let _Missing = &_Missing parent;
  %if %sysevalf(%superq(label)=, boolean) %then %let _Missing = &_Missing label;
  %if %sysevalf(%superq(dsout)=, boolean) %then %let _Missing = &_Missing dsout;

  %if %length(&_Missing) gt 0
    %then %do;
      %put ERR%str(OR): [&sysmacroname] Required macro parameter(s) missing: &_Missing;
      %goto exit_macro;
    %end;

  %let _random_=%sysfunc(putn(%sysevalf(%sysfunc(ranuni(0))*10000,floor),z4.));
  
  data ds&_random_.0(rename=&parent.=&parent._0);
    set &dsin;
  run;  

  %let iteration = 0;
  proc sql noprint;
    select count(&parent) into :_parent_n trimmed
    from &dsin
    ;
  quit;
  
  %put &=iteration &=_parent_n;
  
  %do %while (&_parent_n gt 0);
    
    proc sql noprint;
      create table ds&_random_.%eval(&iteration + 1) as
      select 
        _ds_&iteration..*,
        dsin.&parent as &parent._%eval(&iteration + 1),
        dsin.&label as &label._%eval(&iteration)
      from 
        ds&_random_.&iteration _ds_&iteration
      left join 
        &dsin dsin
      on _ds_&iteration..&parent._&iteration = dsin.&child
      ;
      select count(&parent._%eval(&iteration + 1)) into :_parent_n trimmed
      from ds&_random_.%eval(&iteration + 1)
      ;
    quit;
    
    %let iteration = %eval(&iteration + 1);
    %put &=iteration &=_parent_n;
    
    proc delete data=work.ds&_random_.%eval(&iteration - 1); 
    run;

  %end;  
  
  data &dsout(rename=&parent._0=&parent);
    length _hierarchy_level_ 8 _hierarchy_full_ $2048;
    set ds&_random_.&iteration(drop = &parent._&iteration);
    _hierarchy_level_ = 0;
    %do i = 0 %to &iteration-1;
      if not missing(&parent._&i) then _hierarchy_level_ = _hierarchy_level_ + 1;
    %end;  
    _hierarchy_full_ = catx(' ', &label, cats("(", &child, ")"));
    %do i = 0 %to &iteration-1;
      if not missing(&parent._&i) then _hierarchy_full_ = catx('; ', catx(' ', &label._&i, cats("(", &parent._&i, ")")), _hierarchy_full_);
    %end;  

    proc delete data=work.ds&_random_.&iteration; 
    run;
    
  run;  
  
  proc sort data=&dsout;
    by &label;
  run;  

  %exit_macro:

%mend create_hierarchy;
