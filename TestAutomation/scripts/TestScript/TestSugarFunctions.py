import functions
import json
import os
import outputWriter

def _getTestCases():

    allTestCasesJson = []
    directory = os.listdir("../../testCases")
    for file in directory:
        if (file != "template.json"):
            testCase = "../../testCases/" + file
            #print(testCase)
            allTestCasesJson.append(_loadJsonData(testCase))
   #print(allTestCasesJson[0])
    return allTestCasesJson

def _loadJsonData(testCaseJson):

    with open(testCaseJson) as jsonFile:
        jsonData = json.load(jsonFile)
        #print(json.dumps(jsonData, indent=4, sort_keys=True))
    jsonFile.close()
    return (jsonData)

def testDriver(testCase):

    method = testCase["test_name"]

    if(method == "div(x, y)"):
        _runDivTest(testCase)

def _runDivTest(testCase):

    print(testCase["test_discription"])
    test_id = testCase["id"]
    test_name = testCase["test_name"]
    description = testCase["test_discription"]
    inputs = testCase["input"]
    oracle = testCase["oracle"]
    x = int(testCase["input"][0])
    y = testCase["input"][1]
    if "." in y:
        y = float(y)
    else:
        y = int(y)
    #print(type(x))
    #print(type(y))

    #print(type(oracle))
    try:
        output = str(functions.div(x,y))
    except:
        output = "Can not divide by zero"

    if(output == oracle):
        print("Test Passed {} = {}".format(oracle, output))
        inputs = ('%s, %s'%( x , y))
        outputWriter.outputToFile(str(test_id), test_name, description, inputs, oracle, output, 'Passed', 'results.txt')

    else:
        inputs = ('%s, %s', x, y)
        print("Test Failed {} = {},".format(oracle, output))
        outputWriter.outputToFile(id, test_name, description, inputs, oracle, output, 'Failed', 'results.txt')

    print("\n \n")

def main():

    allTestCases = _getTestCases()
    #print(allTestCases[0])
    for testCase in allTestCases:
            testDriver(testCase)

if __name__ == '__main__':
    main()