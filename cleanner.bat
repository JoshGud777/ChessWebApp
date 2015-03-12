if "%1" == "FULL" goto :FULL
if "%1" == "pycache" goto :pycache

:FULL
echo ### - Deleteing files ^& Removeing dirs
echo ### --- del *.coverage
echo ### --- del *.log
echo ### --- RD /S /Q coverage
echo ### --- RD /S /Q python_tests_xml
echo ### --- RD /S /Q __pycache__
echo ### --- RD /S /Q webapp\__pycache__
echo ### --- RD /S /Q webapp_tests\__pycache__

del *.coverage*
del *.log
del webapp\db17b1a5c2b2f6d370af2c59c885d5db\*journal

RD /S /Q coverage
RD /S /Q python_tests_xml

:pycache
RD /S /Q __pycache__
RD /S /Q webapp\__pycache__
RD /S /Q webapp_tests\__pycache__