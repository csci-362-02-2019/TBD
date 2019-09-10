#This program parses the top level directories of its folder and pushes a full list of them to an html page

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
    t1 ="""<html>
    <style>
        .cofc{
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
    
        body{
            background:#660000;
        }
        
        table, td {
            border: 2px solid #858585;
               
        }
        th{
            text-align: center;
            text-transform: uppercase;
            font-size: 20px;
            color: #ffffff; 
        }
        tr:nth-child(odd){
            background:#383838;
            color: #ffffff;          
        }  
        tr:nth-child(even){
            background:#000000;
            color: #ffffff ;
            
        }  
    </style>
	<head><img src="cofc.png" class="cofc"></head>
	<body>
		<table>
			<tr>
				<th>Contents of the Top Level Directory</th>
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

    # to use chrome on macs
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
