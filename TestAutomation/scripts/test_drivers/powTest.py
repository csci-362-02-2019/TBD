from sugar_methods import functions
from sugar_methods import rational
from util import utilities
import re

def runPowTest(x, y, oracle):


	try:
		output = str(functions.pow(x,y))
	except Exception as e:
		output = str(e)
	
	
		
	
	if (output == oracle):
		return "Passed", output

	else:
		return "Failed", output


	print("\n \n")
	
	
