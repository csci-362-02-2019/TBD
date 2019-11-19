
import json
import os
import webbrowser
import re

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
    inputs = [str(r) for r in inputs]
    color = " style=\"color:#ffffff\" "
    if(results == "Passed"):
        color = " style=\"color:#00ff00\" "
    elif (results == "Failed"):
        color = " style=\"color:#ff0000\" "

    O = open(outFile, "a+")
    makeRow = ('        <tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td%s>%s</td></tr>\n' % (
    ID, "functions." + Name, descr, inputs, oracle, output, color, results))
    O.write(str(makeRow))

    O.close()


# end outputToFile


def getTestCases():
    # This function parses the directory of test cases for all the testcase Jsons
    allTestCasesJson = []
    directory = natural_sort(os.listdir("../testCases"))
    print(directory)
    for file in directory:
        if (file != "template.json"):
            testCase = "../testCases/" + file

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

    result = open("../temp/results.txt","r")
    template = open("../project/resultstemplate.html","r")
    display = open("../project/display.html","w")
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

	O = open("../temp/results.txt", "w")
	O.close()


def open_report():

	createHTML()
	page_name = '../project/display.html'
	#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

	# opens page

	webbrowser.open_new_tab(page_name)


def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)


