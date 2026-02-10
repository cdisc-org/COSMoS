%let root=C:/_github/cdisc-org/COSMoS;
%include "&root/utilities/config.sas";

filename jsfile "&root/project/bc/jsonschema/cosmos_bc_model.schema.json";
filename mpfile "%sysfunc(pathname(work))/json_schema.map";
libname jsfile json map=mpfile automap=create fileref=jsfile ordinalcount=none;

data work.linkml_enums_bc(keep=enum value);
  length enum $64 value $1024; 
  set jsfile.ALLDATA(where=(index(enum, 'Enum') and (not missing(P4))) rename=(P2=enum));
run;

filename jsfile clear;
filename mpfile clear;
libname jsfile clear;



filename jsfile "&root/project/sdtm/jsonschema/cosmos_sdtm_model.schema.json";
filename mpfile "%sysfunc(pathname(work))/json_schema.map";
libname jsfile json map=mpfile automap=create fileref=jsfile ordinalcount=none;

data work.linkml_enums_sdtm(keep=enum value);
  length enum $64 value $1024; 
  set jsfile.ALLDATA(where=(index(enum, 'Enum') and (not missing(P4))) rename=(P2=enum));
run;

filename jsfile clear;
filename mpfile clear;
libname jsfile clear;


filename jsfile "&root/project/crf/jsonschema/cosmos_crf_model.schema.json";
filename mpfile "%sysfunc(pathname(work))/json_schema.map";
libname jsfile json map=mpfile automap=create fileref=jsfile ordinalcount=none;

data work.linkml_enums_crf(keep=enum value);
  length enum $64 value $1024; 
  set jsfile.ALLDATA(where=(index(enum, 'Enum') and (not missing(P4))) rename=(P2=enum));
run;

filename jsfile clear;
filename mpfile clear;
libname jsfile clear;


data work.linkml_enums;
  set work.linkml_enums_bc
      work.linkml_enums_sdtm
      work.linkml_enums_crf
      ;
      enum = tranwrd(enum, "Enum", "");
run;  

proc sort data=work.linkml_enums out=data.linkml_enums;
  by enum value;
run;

proc print data=data.linkml_enums;
run;
    