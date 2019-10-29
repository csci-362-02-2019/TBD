
import json
import os
import webbrowser

def outputToFile(ID, Name, descr, inputs, oracle, output, results, outFile):
    """
    This function accepts the following parameters:
    ID: test case number,
    Name: name of the method being tested
    descr: description of the method being tested
    inputs: all inputs that are passed to the method
    oracle: expected output from the function
    output: actual output of the function
    results: if the test case passed
    outFile: name of the file where the data where be written
    From here the function will wrap the output in HTML tags for later display
    in a browser
    """

    O = open(outFile, "a+")
    makeRow = ('<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>\n' % (
    ID, Name, descr, inputs, oracle, output, results))
    O.write(str(makeRow))

    O.close()


# end outputToFile


def getTestCases():
    # This function parses the directory of test cases for all the testcase Jsons
    allTestCasesJson = []
    directory = os.listdir("../../testCases")
    for file in directory:
        if (file != "template.json"):
            testCase = "../../testCases/" + file

            allTestCasesJson.append(_loadJsonData(testCase))

    return allTestCasesJson


# end getTestCases()

def _loadJsonData(testCaseJson):
    # This function accepts the testcase Json file, opens it, and obtains the data from it
    with open(testCaseJson) as jsonFile:
        jsonData = json.load(jsonFile)

    jsonFile.close()
    return (jsonData)


# end _loadJsonData


def createHTML():
    # This function creates the HTML representation using the html template and the gathered output

    result = open("../../temp/results.txt","r")
    template = open("../../project/resultstemplate.html","r")
    display = open("../../project/display.html","w")
    lineCT = 0
    tableStart = 35  # line number for where table data to be inserted
    for templateLine in template:

        if (lineCT < tableStart):  # beginning of table
            display.write(templateLine)
            pass
        elif (lineCT == tableStart):
            for resultLine in result:
                display.write(resultLine)
        else:
            display.write(templateLine)
        lineCT += 1

    template.close()
    result.close()
    display.close()


# end createHTML
def html_clean_up():

	O = open("../../temp/results.txt", "w")
	O.close()


def open_report():

	createHTML()
	page_name = '../../project/display.html'
	#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

	# opens page

	webbrowser.open_new_tab(page_name)


