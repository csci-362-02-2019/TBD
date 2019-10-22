import functions
import json
import os
from util import utilities



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
        utilities.outputToFile(str(test_id), test_name, description, inputs, oracle, output, 'Passed', 'results.txt')

    else:
        inputs = ('%s, %s', x, y)
        print("Test Failed {} = {},".format(oracle, output))
        utilities.outputToFile(id, test_name, description, inputs, oracle, output, 'Failed', 'results.txt')

    print("\n \n")

def main():

    allTestCases = utilities.getTestCases()
    print(allTestCases)
    for testCase in allTestCases:
           testDriver(testCase)

if __name__ == '__main__':
    main()