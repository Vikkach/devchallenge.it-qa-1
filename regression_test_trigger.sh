#!/usr/bin/env bash
virtualenv -p python3 venv
source venv/bin/activate

pip install --upgrade virtualenv --no-cache-dir
pip install --upgrade pip --no-cache-dir

# Install all required packages to virtual environment
pip install -r requirements.txt --no-cache-dir --quiet

export BROWSER=chrome
RESULTS_FOLDER=report

# Clear previous runs
rm -rf $RESULTS_FOLDER/*

# Execute tests with Allure report
python -m pytest tests/api/ --alluredir $RESULTS_FOLDER
