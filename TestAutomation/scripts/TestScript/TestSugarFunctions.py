from util import utilities
from test_drivers import div_test


def testDriver(testCase):

    method = testCase["test_name"]

    if(method == "div(x, y)"):
        div_test.run_div_test(testCase)

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