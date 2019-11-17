"""
We are team TBD and we have created a testing framework to test various methods within SugarLabs' functions.py

"""



from util import utilities
from test_drivers import div_test, factorial_test,ln_test,mod_test,powTest


def testDriver(testCase):
	test_id = testCase["id"]
	test_name = testCase["test_name"]
	description = testCase["test_discription"]
	inputs = testCase["input"]
	oracle = testCase["oracle"]
	x = testCase["input"][0]
	if(len(testCase["input"]) == 2):
		y = testCase["input"][1]

	method = testCase["test_name"]

	if(method == "div(x, y)"):
		div_test.run_div_test(testCase)
	elif (method == "mod(x,y)"):
		mod_test.run_mod_test(testCase)
	elif (method == "pow(x, y)"):
		testSuccess, output= powTest.runPowTest(x,y, oracle)
		utilities.outputToFile(str(test_id), test_name, description, inputs, oracle, output, testSuccess, '../temp/results.txt')
	elif (method == "factorial(n)"):
		factorial_test.run_factorial_test(testCase)
	elif (method == "ln(x)"):
		ln_test.run_ln_test(testCase)
	else:
		print("ERROR: Test Case not defined in testing framework")


def runAllTest():

	allTestCases = utilities.getTestCases()
	print(allTestCases)
	for testCase in allTestCases:
		testDriver(testCase)
	utilities.open_report()

def main():
	utilities.html_clean_up()
	runAllTest()

if __name__ == '__main__':
	main()
