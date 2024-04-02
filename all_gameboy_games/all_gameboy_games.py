import requests
import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO

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
searchterm = "HAL Laboratory"
returnsearch2 = {}
leaveloop = False

for column in column_headers:

    counter = 0
    while counter < row_length:

        value = data[column, counter]
        if value == searchterm:
            for column1 in column_headers:
                returnsearch2[column1,counter] = data[column1, counter]

        counter = counter + 1

print(f"Number of results: {len(returnsearch2)}\n Actual Results: {returnsearch2}")
