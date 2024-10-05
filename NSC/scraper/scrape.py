#! python3
# scrapy.py - scrapes data from json file
import os
import json

data = []

with open('response.json', 'r', encoding ="utf8") as file:
    data = json.load(file)
    for airtempmonthliesAverageTempC,value in data.items():
            try:
                print(airtempmonthliesAverageTempC,value)

            except UnicodeDecodeError as e:
                 pass
