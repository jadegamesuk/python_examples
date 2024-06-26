import requests
import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO
import re
import math

r = requests.get('https://en.wikipedia.org/wiki/List_of_Game_Boy_games')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
wiki_table = soup.select('#softwarelist')

html_list = wiki_table
list = wiki_table[0].getText()
tables = pd.read_html(StringIO(str(html_list[0])))

column_headers = tables[0].columns.tolist()
row_length = len(tables[0])
col_length = len(column_headers)

data = {}

for column in column_headers:

    counter = 0
    while counter < (row_length):
        value = tables[0][column][counter]
        data[column, counter] = value
        counter = counter + 1

# Search and Return value from Table
        
while True:
    print("\tType in a Gameboy game, and I'll return some information about it")
    print("\tType 'q' to exit")

    searchterm = input("What Gameboy game would you like to know more about? ")
    if searchterm == 'q':
        break
    
    searchterm1 = r".*" + searchterm + r".*"
    returnsearch = {}
    returnsearchcounter = []

    for column in column_headers:
        counter = 0
        while counter < row_length:
            value = data[column, counter]

            try:
                if re.match(searchterm1, value, re.IGNORECASE):
                    returnsearchcounter.append(value)
                    #print(f"VALUE IS {returnsearchcounter}")
                    if not pd.isna(value):
                        pass
                    for column1 in column_headers:
                        returnsearch[column1,counter] = data[column1, counter]
            except:
                pass
            counter = counter + 1

    print(f"Actual Results: {returnsearch}\n")
    print(f"Number of returned results: {len(returnsearchcounter)}\n")
    print(f"Short results: {returnsearchcounter}\n")


