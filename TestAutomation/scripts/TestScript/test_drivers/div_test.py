from scripts.TestScript.sugar_methods import functions
from scripts.TestScript.util import utilities

def run_div_test(test_case):

    print(test_case["test_discription"])
    test_id = test_case["id"]
    test_name = test_case["test_name"]
    description = test_case["test_discription"]
    inputs = test_case["input"]
    oracle = test_case["oracle"]
    x = int(test_case["input"][0])
    y = test_case["input"][1]
    if "." in y:
        y = float(y)
    else:
        y = int(y)
    #print(type(x))
    #print(type(y))

    #print(type(oracle))
    try:
        output = str(functions.div(x, y))
    except:
        output = "Can not divide by zero"

    if(output == oracle):
        print("Test Passed {} = {}".format(oracle, output))
        inputs = ('%s, %s'%( x , y))
        utilities.outputToFile(str(test_id), test_name, description, inputs, oracle, output, 'Passed', '../temp/results.txt')

    else:
        inputs = ('%s, %s', x, y)
        print("Test Failed {} = {},".format(oracle, output))
        utilities.outputToFile(id, test_name, description, inputs, oracle, output, 'Failed', '../temp/results.txt')

    print("\n \n")
