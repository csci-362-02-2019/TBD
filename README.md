# Team TBD

John-Tyler Cooper, Austin Purtell, Thomas Setzler

## Framework Directory Structure:

![directory framework](https://raw.githubusercontent.com/csci-362-02-2019/TBD/master/directoryStructure.jpg?token=ALEZGXNEIAH7USMKKCVIF6S5XBUQO)

#Repositories
Project: Contains files for presentation of data and formatting of data\n
Scripts: Contains all test scripts and related directories
TestScript: Contains TestSugarFunctions.py and relates directories
sugar_methods: Contains all files from sugar necessary for running test cases
test_drivers: Contains all drivers specific to individual methods
util: contains utility functions and files
testCases: Contains the test case template and each test case JSON
testCase Executables: Will contain the master executable for the testing framework
temp: contains temporary files, such as output from the testing framework
oracles: empty because oracles are specified in the test case JSON
docs: contains documentation on the framework
reports: contains all reports relating to the project

#Test Cases

Test cases are located in the testCases directory within TestAutomation.  Within this directory, each test case is assumed to be properly formatted, as a JSON, based on the test case template file.  The template file is located within the testCases directory.  Each testCase file should follow the naming scheme of "testCase" immediately followed by the number of the test case.

#How to use Framework
In order to execute the test cases, first ensure that at least one test case is created within the testCase files for an existing driver.  Then run /TestAutomation/scripts/TestScripts/TestSugarFunctions.py.  The output will be sent to an HTML file and then opened in the browser. 


