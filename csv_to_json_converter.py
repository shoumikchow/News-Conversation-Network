import csv
import json

csvfile = open('./Scraped data/network_direct_improvised.csv', 'r')
jsonfile = open('output.json', 'w')

#fieldnames = ("subject","object")
count = 1
# with open("./Scraped data/network_direct_improvised.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print (row[2])
#         arr = [row[2],row[4]]
#         json.dump(arr, jsonfile)
#         jsonfile.write(',\n')
#         count += 1
#         if count == 4:
#             break
reader = csv.DictReader( csvfile)
for row in reader:
    print (row)
    arr = {"source":row["subject"],"target":row["object"]}
    print (row["subject"])
    json.dump(arr, jsonfile)
    jsonfile.write(',\n')
    count += 1
    if count == 4:
        break


# with open('./Scraped data/quotations_and_speeches_v2.0.csv', mode='r') as infile:
#     reader = csv.reader(infile)
#     with open('coors_new.csv', mode='w') as outfile:
#         writer = csv.writer(outfile)
#         mydict = {rows[0]:rows[1] for rows in reader}