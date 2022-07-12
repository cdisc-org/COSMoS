@echo off
call .\venv\Scripts\activate

echo.>%~dpn0.log

for /F "eol=; tokens=1 delims=" %%i IN ('dir /b /s .\yaml\sdtm\*.yaml') do @call :ValidateFile %%i

findstr /i /s "error" %~dpn0.log

pause
goto:EOF

:ValidateFile

  set /a counter=counter+1 > nul
  echo %counter% *** %1
  echo *** %1 >> %~dpn0.log
  
  linkml-validate -C SDTMGroup -s cosmos_sdtm_bc_model.yaml %1 >> %~dpn0.log 2>>&1
  
goto :EOF
