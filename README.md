# Team TBD

John-Tyler Cooper, Austin Purtell, Thomas Setzler

## Framework Directory Structure:

/TestAutomation

​		/project 

​	​	/scripts

​		/testCases

​	​	/testCaseExcutables

​	​	​/tmp

​	​	​/oracles

​	​	​/docs
		
		/reports

#Framework

#Test Cases

Test cases are located in the testCases directory within TestAutomation.  Within this directory, each test case is assumed to be properly formatted, as a JSON, based on the test case template file.  The template file is located within the testCases directory.  Each testCase file should follow the naming scheme of "testCase" immediately followed by the number of the test case.

#How to use Framework
In order to execute the test cases, first ensure that at least one test case is created within the testCase files for an existing driver.  Then run /TestAutomation/scripts/TestScripts/TestSugarFunctions.py.  The output will be sent to an HTML file and then opened in the browser. 


