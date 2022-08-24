@echo off
cd %~dp0

call ..\venv\Scripts\activate

echo.>%~dpn0.log

for /F "eol=; tokens=1 delims=" %%i IN ('dir /b /s %~dp0\sdtm\*.yaml') do @call :ValidateFile %%i

findstr /i /s "error" %~dpn0.log
goto:EOF

:ValidateFile

  set /a counter=counter+1 > nul
  echo %counter% *** %1
  echo *** %1 >> %~dpn0.log

  linkml-validate -C SDTMGroup -s ../model/cosmos_sdtm_bc_model.yaml %1 >> %~dpn0.log 2>>&1

goto :EOF
