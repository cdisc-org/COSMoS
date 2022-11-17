@echo off
cd %~dp0

if /i (a%1) == (a) (REM
     set /p package=Package ^[yyyymmdd^]: 
     ) else (
     set package=%1
)

if not exist "%~dp0\%package%\sdtm\." (
    echo Folder %~dp0%package%\sdtm does not exist.
    goto :EOF
    )


call ..\venv\Scripts\activate

set logfile=%~dpn0_%package%.log
echo.>%logfile%

set counter=0
for /F "eol=; tokens=1 delims=" %%i IN ('dir /b /s %~dp0%package%\sdtm\*.yaml') do @call :ValidateFile %%i

findstr /i /s "error" %logfile%
goto:EOF

:ValidateFile

  set /a counter=counter+1 > nul
  echo %counter% *** %1
  echo *** %1 >> %logfile%

  linkml-validate -C SDTMGroup -s ../model/cosmos_sdtm_bc_model.yaml %1 >> %logfile% 2>>&1

goto :EOF
