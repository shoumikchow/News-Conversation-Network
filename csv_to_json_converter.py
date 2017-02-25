import csv
import json

csvfile = open('./Scraped data/network_direct_improvised.csv', 'r')
jsonfile = open('output.json', 'w')


count = 1

reader = csv.DictReader(csvfile)
for row in reader:
    if count == 20:
        break
    arr = {"source":row["subject"],"target":row["object"]}
    json.dump(arr, jsonfile)
    jsonfile.write(',\n')
    count += 1



