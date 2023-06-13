%macro get_api_response(
    baseurl=,
    endpoint=,
    response_file=,
    response_fileref=,
    apikey=&api_key,
    accept=application/json
  );

  %if %sysevalf(%superq(response_file)=, boolean)=0 %then
    filename response "&response_file";;

  proc http
      url="&baseurl.&endpoint"
      %if %sysevalf(%superq(response_file)=, boolean)=0 %then
        out=response;
      %else 
        out=&response_fileref;
      ;      
      headers
        "api-key"="&apikey"
        "Accept"="&accept"
        ;
      debug &rest_debug;
  run;
  %prochttp_check_return(200);
  
  %if %sysevalf(%superq(response_file)=, boolean)=0 %then
    filename response clear;;

%mend get_api_response;
