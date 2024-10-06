#! python3
# scrapy.py - scrapes data from json file
import os
import json

data = []

# with open('response.json', 'r', encoding ="utf8") as file:
#     data = json.load(file)
#     for key in data.keys():
#             print(key,data[])

json_data = open('response.json', 'r', encoding='utf-8')
jdata = json.loads(json_data.read())

# def recursion(dict):
#
#     for key, value in dict.items():
#
#         if type(value) == type(dict):
#             if key != "paging":
#                 for key, value in value.items():
#                     if isinstance (value,list):
#                         print key
#                         # place where I need to enter list comprehension?
#                 if type(value) == type(dict):
#                     if key == "id":
#                         print " id found " + value
#                     if key != "id":
#                         print key + " 1st level"
#                 if key == "id":
#                     print key
#         else:
#             if key == "id":
#                 print "id found " + value
#





        #     print(airtempmonthliesAverageTempC)
        # for value in airtempmonthliesAverageTempC:
        #     print(value)
        # print(key,value)
            
        #     # try:
            #     print(airtempmonthliesAverageTempC,value)

            # except UnicodeDecodeError as e:
            #      pass
