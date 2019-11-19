from sugar_methods import functions
from sugar_methods import rational
from util import utilities

def runPowTest(x, y, oracle):
	"""
	print(test_case["test_discription"])
	test_id = test_case["id"]
	test_name = test_case["test_name"]
	description = test_case["test_discription"]
	inputs = test_case["input"]
	oracle = test_case["oracle"]
	x = test_case["input"][0]
	y = test_case["input"][1]
	"""
	try:
		output = str(functions.pow(x,y))
	except Exception as e:
		output = str(e)
	
	
		
	
	if (output == oracle):
		return "Passed", output

	else:
		return "Failed", output


	print("\n \n")
	
	
