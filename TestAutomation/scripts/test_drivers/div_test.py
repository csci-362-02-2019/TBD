from sugar_methods import functions
from sugar_methods import rational
from util import utilities
import re

def run_div_test(x, y, oracle):

 

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
