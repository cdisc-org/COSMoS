%let root=C:/_github/cdisc-org/COSMoS;

%include "&root/utilities/config.sas";

%let rest_debug=%str(OUTPUT_TEXT REQUEST_HEADERS NO_REQUEST_BODY RESPONSE_HEADERS NO_RESPONSE_BODY);
%let base_url=https://library.cdisc.org/api;

%get_latest_codelist_package(
  package=sdtmct, 
  jsonout=&root/utilities/data/sdtm_latest_codelist_package.json, 
  dsout=data.sdtm_latest_codelist_package
);