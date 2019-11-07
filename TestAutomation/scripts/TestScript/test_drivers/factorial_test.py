from sugar_methods import functions
from sugar_methods import rational
from util import utilities

def run_factorial_test(test_case):

    print(test_case["test_discription"])
    test_id = test_case["id"]
    test_name = test_case["test_name"]
    description = test_case["test_discription"]
    oracle = test_case["oracle"]
    inputs = test_case["input"]
    n = test_case["input"][0]

    # type casting
    if "." in n:
        n = float(n)
    else:
        n = int(n)

    # test
    try:
        output = str(functions.factorial(n))
    except:
        if(n < 0):
            output = "Factorial(x) is only defined for integers x>=0"
        if type(n) not in (int, int):
            output = "Factorial only defined for integers"

    if(output == oracle):
        print("Test Passed {} = {}".format(oracle, output))
        inputs = ('%s' % n)
        utilities.outputToFile(str(test_id), test_name, description, inputs, oracle, output, 'Passed', '../../temp/results.txt')

    else:
        inputs = ('%s' % n)
        print("Test Failed {} = {}".format(oracle, output))
        utilities.outputToFile(str(test_id), test_name, description, inputs, oracle, output, 'Failed', '../../temp/results.txt')

    print("\n \n")
