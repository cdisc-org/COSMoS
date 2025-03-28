@echo off
cd %~dp0

if /i (a%1) == (a) (REM
     set /p folder=Folder ^[folder^]:
     ) else (
     set folder=%1
)

if not exist "%~dp0\%folder%\collection\." (
    echo Folder %~dp0%folder%\collection does not exist.
    goto :EOF
    )


call ..\venv\Scripts\activate

set logfile=%~dpn0_%folder%.log
echo.>%logfile%

set counter=0
for /F "eol=; tokens=1 delims=" %%i IN ('dir /b /s %~dp0%folder%\collection\*.yaml') do @call :ValidateFile %%i

findstr /i /n /s "error" %logfile%
goto:EOF

:ValidateFile

  set /a counter=counter+1 > nul
  echo %counter% *** %1
  echo *** %1 >> %logfile%

  linkml-validate -C DataCollectionGroup -s ../model/cosmos_collection_bc_model.yaml %1 >> %logfile% 2>>&1

goto :EOF
