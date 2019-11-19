from sugar_methods import functions
from sugar_methods import rational
from util import utilities
import re

def run_ln_test(x, oracle):


    #if "." in x:
     #   x = float(x)
    #elif(re.search('[a-zA-Z]',x)):
    #    x = x
    #else:
       # x = int()

    try:
        output = str(functions.ln(x))
    except:
        output = "Logarithm(x) only defined for x > 0"

    if(output == oracle):

        return "Passed", output

    else:
        return "Failed", output

    print("\n \n")
