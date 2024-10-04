/**  
  @file util_gettree.sas
  @brief Create a dataset with directory information.

  @details
  credit: https://communities.sas.com/t5/SAS-Programming/listing-all-files-of-all-types-from-all-subdirectories/m-p/334113/highlight/true#M75419

  Example usage:
  
      %util_gettree(
        dir=&project_folder/json_out/sdtm, 
        outds=work.dirtree_sdtm, 
        where=%str(ext="json" and dir=0)
      );

  @author Lex Jansen

  @param[in] dir= The starting directory
  @param[out] outds= (work.dirtree) Output dataset
  @param[in] where= Filter records
  @param[in] keep=  Variables to keep in output dataset
  @param[in] drop= (ext) Variables to drop in output dataset

**/
%macro util_gettree(
  dir=, 
  outds=work.dirtree, 
  where=,
  keep=,
  drop=ext
  ) / des = 'Create a dataset with directory information';

  /*
  credit:
   Tom:
   https://communities.sas.com/t5/SAS-Programming/listing-all-files-of-all-types-from-all-subdirectories/m-p/334113/highlight/true#M75419
  */
  
  data &outds ;
    length dir 8 ext filename dirname $256 fullpath $512;
    call missing(of _all_);
    fullpath = "&dir";
  run;
  
  data &outds;
    modify &outds ;
    sep='/';
    if "&sysscp"="WIN" or "&sysscp"="DNTHOST" then sep='\';
    rc=filename('tmp',fullpath);
    dir_id=dopen('tmp');
    dir = (dir_id ne 0);
    if dir then dirname=cats(fullpath,sep);
    else do;
      filename=scan(fullpath,-1,sep);
      dirname =substrn(fullpath,1,length(fullpath)-length(filename));
      if index(filename,'.')>1 then ext=scan(filename,-1,'.');
    end;
    replace;
    if dir then do;
      do i=1 to dnum(dir_id);
        fullpath=cats(dirname,dread(dir_id,i));
        output;
      end;
      rc=dclose(dir_id);
    end;
    rc=filename('tmp');
  run;
  
  data &outds(%if %sysevalf(%superq(keep)=, boolean)=0 %then keep=&keep;
              %if %sysevalf(%superq(drop)=, boolean)=0 %then drop=&drop;
              );
    set &outds %if %sysevalf(%superq(where)=, boolean)=0 %then (where=(&where));;
  run;  

  
%mend util_gettree ;
