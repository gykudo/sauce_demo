# sauce_demo
# Descriptions
## Auto test for Swag labs site
    - url: https://www.saucedemo.com
# Install: 
    - Language: python 3.8  
   
# Run Parallel
## Browsers: 
    - Chrome: 
    - FireFox: 
    - Safari: 

## Execute:
    - cmd: python TestSuites/test_suite.py
    - Run by editor
    
# Guideline 
## Structure folder: 
    - Drivers: store all drivers of browser can run in this project
    - Locators: store all files which define elements of each page in site
    - Pages: store list functions/Modules in project
    - TestCases: store all TestCases (TCs) in project
    - TestData: store all type data files
    - Utils: store templates of reports
    
## Rule define name of new file in each folder:
### Follow coding style guide conventions
    - Locators: page_name_locator.py
    - Pages: page_name_page.py
    - TestCases: test_function_name.py

### 