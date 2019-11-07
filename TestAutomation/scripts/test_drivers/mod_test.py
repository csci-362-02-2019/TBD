from sugar_methods import functions
from sugar_methods import rational
from util import utilities

def run_mod_test(test_case):

    print(test_case["test_discription"])
    test_id = test_case["id"]
    test_name = test_case["test_name"]
    description = test_case["test_discription"]
    oracle = test_case["oracle"]
    inputs = test_case["input"]
    x = test_case["input"][0]
    y = test_case["input"][1]

    if "." in y:
        y = float(y)
    else:
        y = int(y)
    if "." in x:
        x = float(x)
    elif "<string>" not in x:
        x = int(y)

    try:
        output = str(functions.mod(x, y))
    except:
        output = "Can only calculate x modulo <integer>"

    if(output == oracle):
        print("Test Passed {} = {}".format(oracle, output))
        inputs = ('%s, %s'%( x , y))
        utilities.outputToFile(str(test_id), test_name, description, inputs, oracle, output, 'Passed', '../temp/results.txt')

    else:
        inputs = ('%s, %s' % (x, y))
        print("Test Failed {} = {}".format(oracle, output))
        utilities.outputToFile(str(test_id), test_name, description, inputs, oracle, output, 'Failed', '../temp/results.txt')

    print("\n \n")
