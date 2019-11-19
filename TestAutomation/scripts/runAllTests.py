"""
We are team TBD and we have created a testing framework to test various methods within SugarLabs' functions.py

"""



from util import utilities
from test_drivers import div_test, factorial_test,ln_test,mod_test,powTest
import os
import json

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
		testSuccess, output= div_test.run_div_test(x, y, oracle)
		utilities.outputToFile(str(test_id), test_name, description, inputs, oracle, output, testSuccess, '../temp/results.txt')
	elif (method == "mod(x,y)"):
		testSuccess, output= mod_test.run_mod_test(x, y, oracle)
		utilities.outputToFile(str(test_id), test_name, description, inputs, oracle, output, testSuccess, '../temp/results.txt')
	elif (method == "pow(x, y)"):
		testSuccess, output= powTest.runPowTest(x,y, oracle)
		utilities.outputToFile(str(test_id), test_name, description, inputs, oracle, output, testSuccess, '../temp/results.txt')
	elif (method == "factorial(n)"):
		testSuccess, output= factorial_test.run_factorial_test(x, oracle)
		utilities.outputToFile(str(test_id), test_name, description, inputs, oracle, output, testSuccess, '../temp/results.txt')
	elif (method == "ln(x)"):
		testSuccess, output= ln_test.run_ln_test(x, oracle)
		utilities.outputToFile(str(test_id), test_name, description, inputs, oracle, output, testSuccess, '../temp/results.txt')
	else:
		print("ERROR: Test Case not defined in testing framework")


def runAllTest():



	directory = utilities.natural_sort(os.listdir("../testCases"))
	print(directory)
	for file in directory:
		if (file != "template.json"):
			testCase = "../testCases/" + file
			with open(testCase) as jsonFile:
				jsonData = json.load(jsonFile)
			jsonFile.close()
			testDriver(jsonData)

	utilities.open_report()


def main():
	utilities.html_clean_up()
	runAllTest()

if __name__ == '__main__':
	main()
