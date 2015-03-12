@echo off
call jenkins_build.bat pep8

start pep8.log
start pylint.log