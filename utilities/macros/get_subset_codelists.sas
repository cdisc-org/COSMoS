%macro get_Subset_Codelists(file=, range=, dsout=);

%ReadExcel(file=&file, range=&range, dsout=&dsout);

proc sort data=&dsout;
  by Subset_Short_Name Submission_Value;
run;

data &dsout(keep=Parent_Codelist Subset_Short_Name subset_value_list);
  retain Parent_Codelist Subset_Short_Name subset_value_list;
  length subset_value_list $8192;
  set &dsout;
  by Subset_Short_Name Submission_Value;
  if first.Subset_Short_Name then subset_value_list="";
  subset_value_list=catx(";", subset_value_list, Submission_Value);
  if last.Subset_Short_Name then output;
run;

%mend get_Subset_Codelists;
