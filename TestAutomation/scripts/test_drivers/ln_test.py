from sugar_methods import functions
from sugar_methods import rational
from util import utilities

def run_ln_test(test_case):

    print(test_case["test_discription"])
    test_id = test_case["id"]
    test_name = test_case["test_name"]
    description = test_case["test_discription"]
    inputs = test_case["input"]
    oracle = test_case["oracle"]
    x_string = test_case["input"][0]

    if "." in x_string:
        x = float(x_string)
    else:
        x = int(x_string)

    #print(type(oracle))

    try:
        output = str(functions.ln(x))
    except:
        output = "Logarithm(x) only defined for x > 0"

    if(output == oracle):

        print("Test Passed {} = {}".format(oracle, output))
        inputs = ('%s'%(x_string))
        utilities.outputToFile(str(test_id), test_name, description, inputs, oracle, output, 'Passed', '../temp/results.txt')

    else:
        inputs = ('%s', str(x))
        print("Test Failed {} = {},".format(oracle, output))
        utilities.outputToFile(id, test_name, description, inputs, oracle, output, 'Failed', '../temp/results.txt')

    print("\n \n")
