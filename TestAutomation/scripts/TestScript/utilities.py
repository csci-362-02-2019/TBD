import json
import os

def outputToFile(ID, Name, descr, inputs, oracle, output, results, outFile):
    """
    This function accepts the following parameters:
    ID: test case number,
    Name: name of the method being tested
    descr: description of the method being tested
    inputs: all inputs that are passed to the method
    oracle: expected output from the function
    output: actual output of the function
    results: if the test case passed
    outFile: name of the file where the data where be written
    From here the function will wrap the output in HTML tags for later display
    in a browser
    """

    O = open(outFile, "a+")
    makeRow = ('<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>\n' % (ID, Name, descr, inputs, oracle,output, results))
    O.write(str(makeRow))
    
    O.close()

#end outputToFile

    
def _getTestCases():
#This function parses the directory of test cases for all the testcase Jsons
    allTestCasesJson = []
    directory = os.listdir("../../testCases")
    for file in directory:
        if (file != "template.json"):
            testCase = "../../testCases/" + file
            
            allTestCasesJson.append(_loadJsonData(testCase))
   
    return allTestCasesJson
#end _getTestCases()

def _loadJsonData(testCaseJson):
#This function accepts the testcase Json file, opens it, and obtains the data from it
    with open(testCaseJson) as jsonFile:
        jsonData = json.load(jsonFile)
        
    jsonFile.close()
    return (jsonData)
#end _loadJsonData

