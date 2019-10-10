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

    O = open(outFile, "w")
    makeRow = ('<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>', id, Name, descr, inputs, oracle,output, results)
    O.write(str(makeRow))
    
    O.close()

#end outputToFile


