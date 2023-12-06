%macro excel_enhance(open_workbook=,
                     insert_workbook=,
                     insert_sheet=,
                     copydata_from_to=,
                     move_table=,
                     insert_image=,
                     filter=,
                     autofit=,
                     autofit_row=,
                     table_style=,
                     mouseover=,
                     create_workbook=,
                     password=,
                     file_format=);

 %local open_workbook insert_sheet insert_image create_workbook file_format password filter autofit table_style  mouseover copydata_from_to;
 %let script_loc=%sysfunc(getoption(WORK))\enhancex.vbs;
 
 %if %sysevalf(%superq(open_workbook)=, boolean)=0 %then 
   %let open_workbook = %sysfunc(translate(&open_workbook, %str(\), %str(/)));
 %if %sysevalf(%superq(insert_workbook)=, boolean)=0 %then 
   %let insert_workbook = %sysfunc(translate(&insert_workbook, %str(\), %str(/)));
 %if %sysevalf(%superq(insert_image)=, boolean)=0 %then 
   %let insert_image = %sysfunc(translate(&insert_image, %str(\), %str(/)));
 %if %sysevalf(%superq(create_workbook)=, boolean)=0 %then 
   %let create_workbook = %sysfunc(translate(&create_workbook, %str(\), %str(/)));

data _null_;
  length sheet_name range_field $256 image_loc $1024;
  file "&script_loc";
  put "Set objExcel = CreateObject(""Excel.Application"") ";
  put "objExcel.Visible = False";
  put "objExcel.DisplayAlerts=False";
  put "Set objWorkbook1= objExcel.Workbooks.Open(""&open_workbook"")";

  %if %length(&insert_image) ne 0 %then %do;
    %let pic_count=%sysfunc(countc(&insert_image,","));
    %if %sysfunc(countc(&insert_image,","))=0 %then %do;
      %let sheet_name=%sysfunc(scan(&insert_image,2,"#"));
      %let range_field=%sysfunc(scan(&insert_image,2,"!"));
      %let image_loc=%sysfunc(scan("&insert_image",1,"#"));
      sheet_name=quote(scan("&sheet_name",1,"!"));
      range_field=quote("&range_field");
      image_loc=quote("&image_loc");
      put "Set Xlsheet1 = objWorkbook1.Worksheets(" sheet_name ")";
      put "Xlsheet1.Range(" range_field ").Activate";
      put "Xlsheet1.Pictures.Insert(" image_loc ")";
    %end;
    %else %do;
      %let image_count=%sysfunc(countc(&insert_image,","));
      %let image_count=%eval(&image_count+1);
      %do j=1 %to &image_count;
        %let insert_image&j=%sysfunc(scan(&&insert_image,&j,","));
        %let sheet_name&j=%sysfunc(scan(&&insert_image&j,2,"#"));
        %let sheet_name&j=%quote(%str(%")%sysfunc(scan(&&sheet_name&j,1,"!"))%str(%"));
        %let range_field&j=%quote(%str(%")%sysfunc(scan(&&insert_image&j,2,"!"))%str(%"));
        %let image_loc&j=%quote(%str(%")%sysfunc(scan("&&insert_image&j",1,"#"))%str(%"));
        sheet_name=quote(scan("&&sheet_name&j",1,"!"));
        range_field=quote("&&range_field&j");
        image_loc=quote("&&image_loc&j");
        put;
        put "Set Xlsheet&j = objWorkbook1.Worksheets( &&sheet_name&j)";
        put "objWorkbook1.Sheets(""&&sheet_name&j"").select";
        put "Xlsheet&j.Range(&&range_field&j).Activate";
        put "Xlsheet&j.Pictures.Insert(&&image_loc&j)";
      %end;
    %end;
  %end;

  %if %length(&insert_workbook) ne 0 %then %do;
      put;
      put "set objWorkbook2=objExcel.Workbooks.Open(""&insert_workbook"")";
      %let sheet_count=%sysfunc(countc(&insert_sheet,","));
      %let sheet_count=%eval(&sheet_count+1);
      %do i=1 %to &sheet_count;
        %let x=%sysfunc(scan(&insert_sheet,&i));
        %if &i=1
        %then %let s&i=%sysfunc(quote(&x));
        %else %let s&i=&s%eval(&i-1),%sysfunc(quote(&x)) ;
        %let list=%nrbquote(&&s&i);
      %end;
      put "set sheetsToCopy=objWorkbook2.Sheets(Array(%quote(&list))) ";
      put "sheetsToCopy.Copy objWorkbook1.Sheets(1) ";

      /* Copy data to specific sheet */
      /* Copy data sheet to template sheet */
     

     %if %length(&copydata_from_to) ne 0 %then %do;
        %let data_list=%sysfunc(scan(&copydata_from_to,1,%str(|)));
        %let data_find=%sysfunc(index(%quote(&data_list),%str(,)));
        %let data_sheet=%sysfunc(substr(%quote(&data_list),1,%eval(&data_find-1)));
        %let data_range=%sysfunc(substr(%quote(&data_list),%eval(&data_find)+1));

        %put "data_list: " &data_list;
        %put "data_find: " &data_find;
        %put "data_sheet:" &data_sheet;
        %put "data_range:" &data_range;

        put "objWorkbook.Worksheets(""&data_Sheet"").Range(""&data_range"").Copy";

        %let template_list=%sysfunc(scan(&copydata_from_to,2,%str(|)));
        %let template_find=%sysfunc(index(%quote(&template_list),%str(,)));
        %let template_sheet=%sysfunc(substr(%quote(&template_list),1,%eval(&template_find-1)));
        %let template_range=%sysfunc(substr(%quote(&template_list),%eval(&template_find)+1));

        %put "template_list: " &template_list;
        %put "template_find: " &template_find;
        %put "template_sheet:" &template_sheet;
        %put "template_range:" &template_range;

        put "objWorkbook1.Worksheets(""&template_sheet"").Range(""&template_range"").PasteSpecial";
        put "objWorkbook1.Worksheets(""&template_sheet"").Activate";
     %end;
  %end;

  %if %length(&move_table) ne 0 %then %do;
    %if %sysfunc(countc(&move_table,",")) = 0 %then %do;
      %let move_range=%sysfunc(scan(&move_table,1,"!"));
      %let paste_location=%sysfunc(scan(&move_table,2,"!"));
      %put &move_range &paste_location;
      put;
      put "Set objWorksheet = objWorkbook1.Worksheets(1)";
      put "objWorksheet.Activate";
      put "Set objRange = objWorkSheet.Range(""&move_range"")";
      put "objRange.Copy";
      put "Set objRange = objWorkSheet.Range(""&paste_location"")";
      put "objWorksheet.Paste(objRange)";
      put "Set objRange1 = objWorkSheet.Range(""&move_range"")";
      put "objRange1.Delete";
    %end;
    %else %do;
      %let countx=%sysfunc(countc(&move_table,","));
      %let countx=%eval(&countx+1);
      put "Set objWorksheet = objWorkbook1.Worksheets(1)";
      put "objWorksheet.Activate";
      %do j=1 %to &countx;
        %let move_range&j=%sysfunc(scan(&move_table,&j,","));
        %let move_range_only&j=%sysfunc(scan(&&move_range&j,1,"!"));
        %let paste_location&j=%sysfunc(scan(&&move_range&j,2,"!"));
        %put  'move=' &&move_range&j 'paste_location' &&paste_location&j;
        put;
        put "Set objRange = objWorkSheet.Range(""&&move_range_only&j"")";
        put "objRange.Copy";
        put "Set objRange = objWorkSheet.Range(""&&paste_location&j"")";
        put "objWorksheet.Paste(objRange)";
        put "Set objRange1 = objWorkSheet.Range(""&&move_range_only&j"")";
        put "objRange1.Delete";
      %end;
    %end;
  %end;


 /* Add Filters */                                              
 

  %if %length(&filter) ne 0 %then %do;
     %if %sysfunc(count(&filter,%str(|))) > 0 %then %do;
        %let filter_sheet=%sysfunc(count(&filter,%str(|)));
        %let filter_sheet=%eval(&filter_sheet+1);
           /*%put "filter sheet"   &filter_sheet;*/
           %do i=1 %to &filter_sheet;
              %let filter&i=%sysfunc(scan(&filter,&i,%str(|)));
              %put &&filter&i;

              %let sheet_val&i=%sysfunc(scan(%quote(&&filter&i),1,%str(,)));
              %let sheet_column&i=%sysfunc(scan(%quote(&&filter&i),2,%str(,)));
              %let sheet_condition&i=%sysfunc(scan(%quote(&&filter&i),3,%str(,)));

              %let numvar&i=%eval( %sysfunc(verify(&&sheet_condition&i,-0123456789)));
              %if &&numvar&i=1 %then %do;
                  put "objWorkbook1.Sheets(""&&sheet_val&i"").Range(""A1"").AutoFilter &&sheet_column&i,""&&sheet_condition&i""";
              %end;
              %else %do;
                  put "objWorkbook1.Sheets(""&&sheet_val&i"").Range(""A1"").AutoFilter &&sheet_column&i,&&sheet_condition&i";
              %end;
       %end;
     %end;
     %else %do;
     %let filter_list=%sysfunc(count(&filter,%str(,)));
     %let filter_list=%eval(&filter_list+1);
       %do i=1 %to &filter_list;
           %let filter_param&i=%sysfunc(scan(&filter,&i));
           %let numvar=%eval( %sysfunc(verify(&&sheet_condition&i,-0123456789)));
       %end;
     %end;
      %if &numvar=1 %then %do;
           put "objWorkbook1.Sheets(""&filter_param1"").Range(""A1"").AutoFilter &filter_param2,""&filter_param3""";
      %end;
      %else %do;
       put "objWorkbook1.Sheets(""&filter_param1"").Range(""A1"").AutoFilter &filter_param2,&filter_param3";
     %end;
  %end;

  /* AutoFit columns within the table */

  
   %if %length(&autofit) ne 0 %then %do;
      %let autofit_sheet=&autofit;
      %let autofit_count=%sysfunc(count(&autofit_sheet,%str(,)));
      %put "autofit_count" &autofit_count;

      %if &autofit_count=0 %then %do;
         put "objWorkbook1.Worksheets(""&autofit_sheet"").Cells.EntireColumn.AutoFit";
      %end;
      %else %do;
         put "objWorkbook1.Worksheets(""&autofit_sheet"").Columns(""&autofit_range"").EntireColumn.AutoFit";
      %end;
   %end;

   
   
 %if %length(&table_style) > 0 %then %do;
    %let file=&open_workbook;
    %let filename=%sysfunc(reverse(&file));
    %let file_loc=%sysfunc(index(&filename,%str(.)));
    %let file_endloc=%eval(%sysfunc(index(&filename,%str(\))));
    %let name=%sysfunc(substr(&filename,&file_loc+1,&file_endloc-&file_loc-1));
    %let export_workbook=%sysfunc(reverse(&name));

    put "Set Object=objWorkbook1.Sheets(""&export_workbook"").ListObjects.add()";

    %let object_count=1;
    %do %while(%scan(&table_style,&object_count) ne);
       %let temp_list=%scan(&table_style,&object_count);
          put "object.&temp_list";
       %let object_count=%eval(&object_count+1);
      %end;
   %end;


  %if %length(&file_format) ne 0 %then %do;
    %if &file_format=xlsx %then %let file_formatn=51;
    %else %if &file_format=xls %then %let file_formatn=1;
    %else %if &file_format=csv %then %let file_formatn=16;
  %end;

  %if %length(&create_workbook) ne 0 %then %do;
    %if %length(&file_format) ne 0 and %length(&password)=0 %then %do;
       %let save="objWorkbook1.saveAs ""&create_workbook"",&file_formatn";
    %end;
    %else %if %length(&file_format) ne 0 and %length(&password) ne 0 %then %do;
       %let save="objWorkbook1.saveAs ""&create_workbook"",&file_formatn,""&password""";
    %end;
    %else %do;
       %let save="objWorkbook1.saveAs(""&create_workbook"")";
    %end;
    put &save;
  %end;
  %else %do;
    %let name=%sysfunc(scan(%sysfunc(reverse(%sysfunc(scan(%sysfunc(reverse(&open_workbook)),2)))),1,"."))_update.&file_format;
    %put &name;

    %if %length(&file_format) ne 0
    %then %let save="objWorkbook1.saveAs ""&name"",&file_formatn";
    %else %let save="objWorkbook1.saveAs(""&name"")";
    put &save;
  %end;

   put "objWorkbook1.close";
   put "objExcel.DisplayAlerts=True";
   put "set objExcel=nothing";

run;

x "'&script_loc\'";

%mend excel_enhance;


  