: Install all required packages to virtual environment
pip install -r requirements.txt  --quiet

: Set environment variables
SET BROWSER=chrome

: Execute tests with Allure report
python -m pytest -n=%THREADS_COUNT% test\ui --alluredir %RESULTS_FOLDER%

: Generate Allure report and run it in browser
powershell -command "allure generate %RESULTS_FOLDER% -o %RESULTS_FOLDER%\generated" --clean
FOR /d /r . %%d in (".pytest_cache") do @if exist "%%d" rd /s/q "%%d"

: Open recently generated Allure report
powershell -command "allure open %RESULTS_FOLDER%\generated"