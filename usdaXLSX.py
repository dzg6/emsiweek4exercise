import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
import json
from pathlib import Path

def createFruit(name, price):
    return  {"name" : name, "price" : price}

def getUSDALinks():
    url = 'https://www.ers.usda.gov/data-products/fruit-and-vegetable-prices/fruit-and-vegetable-prices/#Vegetables'
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find("table", id='data_table')

    vegetable = table.find(id='Vegetables')
    tr = vegetable.find_parent("tr")

    fruits = tr.find_previous_siblings()
    vegetables = tr.find_next_siblings()

    fruitLinks = []
    vegetableLinks = []

    for row in fruits:
        if row.a:
            fruitLinks.append(row.a.get('href'))
    for row in vegetables:
        if row.a:
            vegetableLinks.append(row.a.get('href'))
            
    downloadXLSX(fruitLinks, 'fruits')
    downloadXLSX(vegetableLinks, 'vegetables')


def downloadXLSX(dataLink, location):
    for link in dataLink:
        isXLSX = link.split('.')[1].split("?")[0]

        if isXLSX == "xlsx":
            fileUrl = "https://www.ers.usda.gov" + link
            xlsx = requests.get(fileUrl)

            filename = link.split('/')[-1].split("?")[0] # this will take only -1 splitted part of the url
            filename = "data/" + location + "/" + filename

            with open(filename,'wb') as output_file:
                output_file.write(xlsx.content)


def readXLSX(folderPath = 'data'):
    outputJSON = {}
    files = Path(folderPath).rglob('*.xlsx')

    for fileLocation in files:
        product = fileLocation.name.split(".")[0]
        contents = pd.read_excel(fileLocation, nrows=5, header=1)

        isFresh = contents.iloc[1, 0]
        price = contents.iloc[1, 1]

        if isFresh == "Fresh1":
            if pd.api.types.is_number(price) and price != " ":
                price = round(price, 2)
                outputJSON[product] = createFruit(product, price)
    else:
        # return error
        pass
    return outputJSON

# getUSDALinks()
# test = readXLSX('data/vegetables')
# print(test)

