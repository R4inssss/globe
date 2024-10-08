import json
import pandas as pd
import sys
import requests

# Global Variable initiations | strange bug where only end year returns in get request using their api
start = 2010
end = 2024




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



# print(results)
df_results = pd.DataFrame(results)
print(df_results)
with open('output.txt', "a", encoding='utf-8') as f:
    f.write(str(df_results))

