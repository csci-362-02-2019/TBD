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
    O.write("<tr><td>" + id + "</td><td>" + Name  + "</td><td>" + descr + "</td><td>" +
            inputs + "</td><td>" + oracle + "</td><td>" + output + "</td><td>" + results + "</td><td>" +
            outFile + "</td></tr>")
    
    O.close()

#end outputToFile


