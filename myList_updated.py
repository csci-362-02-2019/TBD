import webbrowser
import os


def main():
    arr = listTopLevelContents()
    create_webpage(arr)

# austin's part
def create_webpage(arr):
    # name of web page
    page_name = 'index.html'
    f = open(page_name, 'w')

    # first half of formatted web page
    t1 = """<html>
	<head></head>
	<body>
		<table style="margin:auto;padding:20px;border:1px solid black;text-align:center">
			<tr>
				<th style="border-bottom: 1px solid black">Contents of the Top Level Directory</th>
			</tr>"""

    # second half of web page
    t2 = """	</table>
	</body>
	</html>"""

    # inserts strings from list
    table_in = ""
    for ob in arr:
        table_in += "\n		<tr>\n			<td>" + ob + "</td>\n		</tr>\n"

    # writes to file
    f.write(t1 + table_in + t2)
    f.close()
    """
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

    # opens page

    webbrowser.get(chrome_path).open('index.html')
    """
    webbrowser.open_new_tab(page_name)

    
def listTopLevelContents():
    listOfContents = []
    for path, subdirs, files in os.walk(os.path.dirname(os.path.realpath(__file__))):
        for name in files:
            content = os.path.join(path, name)
            listOfContents.append(content)
    return listOfContents


main()