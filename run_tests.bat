@echo off
REM Set PYTHONPATH for imports
set PYTHONPATH=%CD%

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Create reports folder
if not exist reports mkdir reports

REM Run pytest with JUnit XML and HTML report
python -m pytest -v --junitxml=reports/results.xml --html=reports/report.html --self-contained-html tests

REM Deactivate venv
deactivate
