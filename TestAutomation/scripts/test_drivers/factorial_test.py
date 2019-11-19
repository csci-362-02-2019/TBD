from sugar_methods import functions
from sugar_methods import rational
from util import utilities

def run_factorial_test(n, oracle):

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
        return "Passed", output

    else:
        return "Failed", output

    print("\n \n")
