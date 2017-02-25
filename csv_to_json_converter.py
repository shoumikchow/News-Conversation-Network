import csv
import json

csvfile = open('./Scraped data/network_direct_improvised.csv', 'r')
jsonfile = open('output_two_hops.json', 'w')

def find_second_hop_edges(subject):

    coun = 0
    csvfil = open('./Scraped data/network_direct_improvised.csv', 'r')
    read = csv.DictReader(csvfil)
    second_hop_objects_already_added = []
    for row in read:
        if coun == 10:
            break
    
        if row["subject"] == subject and row["object"] in keywords:
            if row["object"] not in second_hop_objects_already_added:
                #print (row["subject"]+" "+row["object"])
                second_hop_objects_already_added.append(row["object"])
                arr = {"source":row["subject"],"target":row["object"]}
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

    if count == 10:
        break
    
    if row["subject"] == "Sheikh Hasina" and row["object"] in keywords:
        if row["object"] not in objects_already_added:
            #print ("Count: "+str(count)+" "+row["subject"]+" "+row["object"])
            objects_already_added.append(row["object"])
            #print ("---"+str(row_number)+"---")
            #print (row["text"])
            arr = {"source":row["subject"],"target":row["object"]}
            find_second_hop_edges(row["object"])
            #print ("Back!")
            json.dump(arr, jsonfile)
            jsonfile.write(',\n')
            count += 1





# Dhaka, Bangladesh, India, Chittagong, Pakistan, Myanmar, Narayanganj, Malaysia, Gazipur, Sylhet, China, Barisal, Khulna
# BNP, Dhaka Tribune, Awami League, Jamaat, RAB, EC, BGB, Election Commission, High Court, Chhatra League, Jatiya Party, ACC, Shibir, JMB, DMP
# Sheikh Hasina, Khaleda Zia, Ershad, Fakhrul, Monirul, Tarique Rahman, Muhith, Nuzami, Bangabandhu, Ziaur Rahman, Modi
