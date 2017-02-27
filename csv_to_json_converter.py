from matplotlib import cm
import csv
import json
from base64 import b16encode

csvfile = open('./Scraped data/quotations_and_speeches_v3.0.csv', 'r')
jsonfile = open('output_two_hops.json', 'w')

nodes_limit = 40
center_node = "BNP"


def find_color(sentiment_value):
    sentiment_value = float(sentiment_value)
    hexColor = ""
    if(sentiment_value<=.25):
        hexColor = "#960101"
    
    elif(sentiment_value<=.45):
        hexColor = "#fc0a0a"
    
    elif(sentiment_value<=.55):
        hexColor = "#e2ff66"
    
    elif(sentiment_value<=.75):
        hexColor = "#3090ff"
    
    else:
        hexColor = "#0650a5"
    
    return hexColor


def find_second_hop_edges(subject):

    coun = 0
    csvfil = open('./Scraped data/quotations_and_speeches_v3.0.csv', 'r')
    read = csv.DictReader(csvfil)
    second_hop_objects_already_added = []
    for row in read:
        if coun == nodes_limit:
            break

    
        if row["subject"] == subject and row["object"] in keywords:
            if row["object"] not in second_hop_objects_already_added:
                # print (row["subject"]+" "+row["object"])
                second_hop_objects_already_added.append(row["object"])
                color = find_color(row["sentiment_value"])
                arr = {"source":row["subject"],"target":row["object"],"sentiment_value":color}
                json.dump(arr, jsonfile)
                jsonfile.write(',\n')
                coun += 1



count = 0
keywords = ["Dhaka", "Bangladesh", "India", "Chittagong", "Pakistan", "Myanmar", "Narayanganj", "Malaysia", "Gazipur", "Sylhet", "China", "Barisal", "Khulna",
"BNP", "Dhaka Tribune", "Awami League", "Jamaat", "RAB", "EC", "BGB", "Election Commission", "High Court", "Chhatra League", "Jatiya Party", "ACC", "Shibir", "JMB", "DMP",
"Sheikh Hasina", "Khaleda Zia", "Ershad", "Fakhrul", "Monirul", "Tarique Rahman", "Muhith", "Nuzami", "Bangabandhu", "Ziaur Rahman", "Modi"]

objects_already_added = []

reader = csv.DictReader(csvfile)
for row_number, row in enumerate(reader):

    if count == nodes_limit:
        break
    
    print (count)

    if row["subject"] == center_node and row["object"] in keywords:
        if row["object"] not in objects_already_added:

            objects_already_added.append(row["object"])
            
            # print (row["text"])
            color = find_color(row["sentiment_value"])
            arr = {"source":row["subject"],"target":row["object"],"sentiment_value":color}
            find_second_hop_edges(row["object"])
            #print ("Back!")
            json.dump(arr, jsonfile)
            jsonfile.write(',\n')
            count += 1





# Dhaka, Bangladesh, India, Chittagong, Pakistan, Myanmar, Narayanganj, Malaysia, Gazipur, Sylhet, China, Barisal, Khulna
# BNP, Dhaka Tribune, Awami League, Jamaat, RAB, EC, BGB, Election Commission, High Court, Chhatra League, Jatiya Party, ACC, Shibir, JMB, DMP
# Sheikh Hasina, Khaleda Zia, Ershad, Fakhrul, Monirul, Tarique Rahman, Muhith, Nuzami, Bangabandhu, Ziaur Rahman, Modi
