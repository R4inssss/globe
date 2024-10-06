import json
import pandas as pd


# Same load as before, but swapped to pandas

with open('response.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

keyKey = 'airtempmonthliesAverageTempC'
results = []

#print(data)

for feature in data['features']:
    properties = feature.get('properties', {})
    #print(properties)
    if keyKey in properties:
        results.append({keyKey: properties[keyKey]})#, 'location': properties['siteName']})
        # If you want to add another thing, just pass through like this:'Country': properties['countryCode']}


print(results)
