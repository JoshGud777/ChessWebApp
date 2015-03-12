:A
@echo off
echo.
echo ##### START OF BUILD #####
echo.

echo ### Running cleanner.bat
call cleanner.bat FULL 1> out.log 2> error.log
echo Done!
echo.

echo ### Adding Python and Python\Scripts to PATH
echo ### - set PATH^=%%PATH%%^;C:\Python34\^;C:\Python34\Scripts
echo. 
set PATH=%PATH%;C:\Python34\;C:\Python34\Scripts

Echo ### Set the Project Dir to 'd'
echo ### - set d^=www_app
echo.
set dir=webapp

if "%1" == "pep8" goto :pep8

echo ### Each test must be in wwwTests and have test in its name
echo ### - set E=0
echo ### - set dir=wwwTests
echo ### - FOR /R wwwTests %%F in (*test*.py) do (
echo ### - coverage run -p -m %dir%.%%~nF
echo ### - if %ERRORLEVEL% GTR 0 set E=1
echo ### - )
echo.
echo +++++++++++++++++++ RUN  TESTS +++++++++++++++++++
echo.

set E=0

set dir=webapp_tests

FOR /R %dir% %%F in (*test*.py) do (coverage run -p -m %dir%.%%~nF)
if %ERRORLEVEL% GTR 0 set E=1
)


echo.
echo.
echo ++++++++++++++++++ END OF TESTS ++++++++++++++++++
echo.
if "%1" == "runtests" goto :end

echo ### Coverage Reports
echo ### - coverage combine
echo ### ----- Combines all the reports made from tests
echo ### - coverage html -d coverage
echo ### ----- Makes a folder with HTML resualts under coverage.
echo ### - coverage xml -o coverage/coverage.xml
echo ### ----- Saves a XML to the coverage dir with name coverage.xml
echo Creating coverage directory if non...
mkdir coverage 1>> out.log 2>> error.log
echo Combinng and outputing...
coverage combine 
coverage html -d coverage
coverage xml -o coverage/coverage.xml
echo Done!
echo.

:pep8

echo ### Files to run pep8 and pyflakes on.
echo ### - set lintfiles^=wwwApp
set lintfiles0=webapp\ webapp_tests\

echo.

echo ### Running and Saving Pep8 data.
echo ### - pep8 --config=pep8.cfg %%lintfiles%% ^> pep8.log
pep8 --config=pep8.cfg %lintfiles0% > pep8.log
echo Done!
echo.

echo ### Running and Saving Pylint data.
echo ### - pyflakes --rcfile=pylint.cfg %%lintfiles%% ^> pylint.log
pylint --rcfile=pylint.cfg %lintfiles0% > pylint.log
echo Done!
echo.

if "%1" == "pep8" EXIT /B 

:end
echo ###Cleaning __pycache__ from workspace
call cleanner.bat pycache 1> out.log 2> error.log

echo ##### END OF BUILD #####
if %E% == 0 (
    echo PASS %E%
) else (
    echo FAILED %E%
)


pause
echo.
EXIT /B %E%


