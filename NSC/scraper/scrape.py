#! python3
# scrapy.py - scrapes data from json file
import os
import json

data = []

with open('response.json', 'r', encoding ="utf8") as file:
    data = json.load(file)
    for airtempmonthliesAverageTempC,value in data.items():
            try:
                pring = print(airtempmonthliesAverageTempC,value)
                print(pring)
            except UnicodeDecodeError as e:
                 pass
