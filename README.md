# Introduction 
This project contains test automation framework and test automation coverage for hotel registration portal

# Getting Started

## Installation

1. Install the latest version of Python 3 from `https://www.python.org/downloads/`
2. Install pip `https://pip.pypa.io/en/stable/installing/`
3. Install allure reporting tool `https://docs.qameta.io/allure/#_installing_a_commandline`
4. Clone this project and go to project root
5. Install virtualenv using `pip install virtualenv`

6. Create virtualenv within project root 

|   OS  |        Command              |
|-------|-----------------------------|
|Windows|`virtualenv venv`            |
|MacOS  |`virtualenv -p python3 venv`|

7. Activate virtualenv

|   OS  |        Command           |
|-------|--------------------------|
|Windows|`venv\scripts\activate`   |
|MacOS  |`source venv/bin/activate`|

8. Install all required packages to virtual environment `pip install -r requirements.txt`

## Test Execution from CMD (Windows)

set RESULTS_FOLDER=report
python -m pytest test/ui/ --alluredir %RESULTS_FOLDER%

## Test Execution from CMD (MacOS)

RESULTS_FOLDER=report
python -m pytest test/ui/ --alluredir $RESULTS_FOLDER

## Test Reporting

To open Allure report execute

|   OS  |        Command                |
|-------|-------------------------------|
|Windows|`allure serve %RESULTS_FOLDER%`|
|MacOS  |`allure serve $RESULTS_FOLDER` |



