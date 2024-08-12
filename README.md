Python API Automation Framework

### Tech Stack
- Python 3.12
- Requests - HTTP Requests
- PyTest - Testing Framework
- Reporting - Allure Report, Pytest, HTML
- Test Data - CSV, Excel, JSON, Faker
- Advance API Testcase - JSON Schema
- Parallel Execution - x distribute(xdist)
 
### How to install packages
``` pip install requests pytest pytest-html faker allure-pytest jsonschema ```
### How to run your testcase parallel
``` pip install pytest-xdist ```
### How to add .gitignore file?
copy the content from this to .gitignore
https://www.toptal.com/developers/gitignore/api/pycharm

### How to run basic testcase with allure report
pytest tests/crud/test_create_booking.py --alluredir=allure_result -s
