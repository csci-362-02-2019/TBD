from sugar_methods import functions
from sugar_methods import rational
from util import utilities

def run_div_test(x, y, oracle):

 
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

	if (output == oracle):
		return "Passed", output

	else:
		return "Failed", output

	print("\n \n")
