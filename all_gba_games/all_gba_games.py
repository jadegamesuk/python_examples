import requests
import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO

r = requests.get('https://en.wikipedia.org/wiki/List_of_Game_Boy_Advance_games')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
wiki_table = soup.select("table", class_="wikitable sortable jquery-tablesorter", style="width:98%; margin-right:0")

html_list = wiki_table[2]
list = wiki_table[2].getText()
tables = pd.read_html(StringIO(str(html_list)))

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
    print("\n\tType in a Gameboy Advance game, and I'll return some information about it")
    print("\tType 'q' to exit")

    searchterm = input("What Gameboy Advance game would you like to know more about? ")
    if searchterm == 'q':
        break
    #searchterm = f"{searchterm}*"
    #print(f"Searching for {searchterm}")
    returnsearch = {}
    #leaveloop = False

    for column in column_headers:

        counter = 0
        while counter < row_length:

            value = data[column, counter]
            if value == searchterm:
                for column1 in column_headers:
                    returnsearch[column1,counter] = data[column1, counter]

            counter = counter + 1

    print(f"Number of results: {len(returnsearch)}\n\n\n Actual Results: {returnsearch}")
