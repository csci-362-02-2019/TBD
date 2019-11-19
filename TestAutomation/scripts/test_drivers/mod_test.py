from sugar_methods import functions
from sugar_methods import rational
from util import utilities

def run_mod_test(x, y, oracle):



    if "." in y:
        y = float(y)
    else:
        y = int(y)
    if "." in x:
        x = float(x)
    elif "string" not in x:
        x = int(x)

    try:
        output = str(functions.mod(x, y))
    except:
        output = "Can only calculate x modulo &lt;integer&gt;"

    if(output == oracle):
        return "Passed", output

    else:
        return "Failed", output

    print("\n \n")
