@echo off
REM Set workspace root for imports
set PYTHONPATH=%CD%

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Create reports folder if missing
if not exist reports mkdir reports

REM Run pytest and generate JUnit XML and HTML reports
python -m pytest -v --junitxml=reports/results.xml --html=reports/report.html --self-contained-html

REM Deactivate environment
deactivate
