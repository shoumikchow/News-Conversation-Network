import csv
import json

csvfile = open('./Scraped data/network_direct_improvised.csv', 'r')
jsonfile = open('../output_two_hops.json', 'w')

def find_edges(reader,subject):
    print (subject)
    coun = 0
    for row in reader:
        #print (row["subject"])
        if coun == 10:
            break
    
        if row["subject"] == subject:
            print ("got subject")
            arr = {"source":row["subject"],"target":row["object"]}
            #list_of_objects.append(row["object"])
            json.dump(arr, jsonfile)
            jsonfile.write(',\n')
    
            coun += 1

count = 0
keywords = ["Dhaka", "Bangladesh", "India", "Chittagong", "Pakistan", "Myanmar", "Narayanganj", "Malaysia", "Gazipur", "Sylhet", "China", "Barisal", "Khulna",
"BNP", "Dhaka Tribune", "Awami League", "Jamaat", "RAB", "EC", "BGB", "Election Commission", "High Court", "Chhatra League", "Jatiya Party", "ACC", "Shibir", "JMB", "DMP",
"Sheikh Hasina", "Khaleda Zia", "Ershad", "Fakhrul", "Monirul", "Tarique Rahman", "Muhith", "Nuzami", "Bangabandhu", "Ziaur Rahman", "Modi"]

reader = csv.DictReader(csvfile)
for row in reader:
    if count == 10:
        break
    
    if row["subject"] == "Sheikh Hasina" and row["object"] in keywords:

        arr = {"source":row["subject"],"target":row["object"]}
        find_edges(reader,row["object"])
        #list_of_objects.append(row["object"])
        json.dump(arr, jsonfile)
        jsonfile.write(',\n')
        count += 1




# Dhaka, Bangladesh, India, Chittagong, Pakistan, Myanmar, Narayanganj, Malaysia, Gazipur, Sylhet, China, Barisal, Khulna
# BNP, Dhaka Tribune, Awami League, Jamaat, RAB, EC, BGB, Election Commission, High Court, Chhatra League, Jatiya Party, ACC, Shibir, JMB, DMP
# Sheikh Hasina, Khaleda Zia, Ershad, Fakhrul, Monirul, Tarique Rahman, Muhith, Nuzami, Bangabandhu, Ziaur Rahman, Modi