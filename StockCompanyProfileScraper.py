

import requests #Request sender/reciever import
from bs4 import BeautifulSoup # pip install beautlfulsoup4 #Information scraper import
import pandas as pd # pip install pandas #Reading HTML markup table import
import win32com.client as win32 #Exporting data to excel sheet

df = pd.DataFrame({'A': [10, 20], 'B': [39, 49]})
df.size

excelNames = ['goog', 'fb', 'aapl', 'tsla', 'amzn', 'msft', 'mrna','nvda','amd','nflx','zm','adbe','abnb','sbux','tmus','pep','intc','cmcsa','pypl','txn','cost'] #Company names
headers= {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0'}


excelApplication= win32.Dispatch('Excel.Application')
excelApplication.Visible = True #Launches a visible instance of Excel spreadsheet 
wb = excelApplication.Workbooks.Add()

for excelName in excelNames:
    url = "https://www.marketwatch.com/investing/stock/{0}/company-profile".format(excelName) #URL that will be used in scraper properly formatted
    response = requests.get(url, headers=headers) #Send GET Response to our URL respond 200 if successful
    soup = BeautifulSoup(response.content, 'html.parser') #Parses our response using BeautifulSoup

    profileInfo = {}

    eleTables = soup.select("div[class='element element--table']") #Scans through HTML and selects all contents with specified tag. Note: Using select because find would only read the first word in element element--tables
    for eleTable in eleTables: #Loops through every instance of the element table and strips the area we are looking for
        valuationType = eleTable.h2.text.strip() #Specific location of the data we want to extra stripped downed and formatted
        df = pd.read_html(str(eleTable))[0] #Insert tables using the Pandas import by reading the html and converting the element to a string. 
        profileInfo[valuationType] = df #Passing information using the title to profileInf

    """
    Export data to Excel spreadsheets properly formatted
    """
    ws = wb.Worksheets.Add()
    ws.name = excelName

    row_spacing = 2
    
    for table in profileInfo.items():
        lastrow = ws.Cells(ws.rows.count, 1).End(-4162).row 
        ws.cells(lastrow+row_spacing, 1).value = table[0]
        ws.cells(lastrow+row_spacing, 1).font.bold = True

        ws.Range(
            ws.cells(lastrow+row_spacing+1, 1),
            ws.cells(lastrow+table[1].shape[0]+row_spacing, table[1].shape[1])
        ).value = table[1].values
    
    ws.Rows('1:' + str(row_spacing)).delete
    ws.columns(1).columnwidth = 30
    ws.columns(2).columnwidth = 15
        
