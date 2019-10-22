from scripts.TestScript.sugar_methods import functions
from util import utilities
from test_drivers import div_test


def testDriver(testCase):

    method = testCase["test_name"]

    if(method == "div(x, y)"):
        div_test.run_div_test(testCase)

def main():

    allTestCases = utilities.getTestCases()
    print(allTestCases)
    for testCase in allTestCases:
           testDriver(testCase)

if __name__ == '__main__':
    main()