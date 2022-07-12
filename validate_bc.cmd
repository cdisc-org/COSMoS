@echo off
call .\venv\Scripts\activate

echo.>%~dpn0.log

for /F "eol=; tokens=1 delims=" %%i IN ('dir /b /s .\yaml\bc\*.yaml') do @call :ValidateFile %%i

findstr /i /s "error" %~dpn0.txt
pause
goto:EOF

:ValidateFile

  set /a counter=counter+1 > nul
  echo %counter% *** %1
  echo *** %1 >> %~dpn0.txt
  
  linkml-validate -C BiomedicalConcept -s cosmos_bc_model.yaml %1 >> %~dpn0.txt 2>>&1
  
goto :EOF
