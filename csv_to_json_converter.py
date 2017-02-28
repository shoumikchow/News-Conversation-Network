import csv
import json

csvfile = open('./Scraped data/quotations_and_speeches_v3.0.csv', 'r')
jsonfile = open('output_two_hops.json', 'w')

nodes_limit = 39
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


def find_total_sentiment_and_total_instance_count(position_in_csv, subject, object, text):
    csvf = open('./Scraped data/quotations_and_speeches_v3.0.csv', 'r')

    r = csv.DictReader(csvf)
    count = 1
    totalsentiment = 0
    # csvf.seek(position_in_csv)
    for row_number,row in enumerate(r):
        # if count >= 40:
        #     break
        if row["subject"] == subject and row["object"] == object and row["text"] != text:
            print ("In function----  "+str(row_number)+" "+row["text"])
            totalsentiment += float(row["sentiment_value"])
            count += 1

            
    return [totalsentiment,count]
        

def find_second_hop_edges(subject):

    coun = 0
    csvfil = open('./Scraped data/quotations_and_speeches_v3.0.csv', 'r')
    read = csv.DictReader(csvfil)
    second_hop_objects_already_added = []
    for row_number, row in enumerate(read):
        if coun == nodes_limit:
            break
    
        if row["subject"] == subject and row["object"] in keywords:
            if row["object"] not in second_hop_objects_already_added:
                #print (row["subject"]+" "+row["object"])
                second_hop_objects_already_added.append(row["object"])
                color = find_color(row["sentiment_value"])
                total_sentiment_and_total_instance_count = find_total_sentiment_and_total_instance_count(row_number,row["subject"], row["object"],row["text"])
                average_sentiment = (total_sentiment_and_total_instance_count[0] + float(row["sentiment_value"]))/total_sentiment_and_total_instance_count[1]
                arr = {"source":row["subject"],"target":row["object"],"sentiment_value":row["sentiment_value"], "edge_color":color, "instance_count":total_sentiment_and_total_instance_count[1]}
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
    
    if row["subject"] == center_node and row["object"] in keywords:
        if row["object"] not in objects_already_added:
            #print ("Count: "+str(count)+" "+row["subject"]+" "+row["object"])
            objects_already_added.append(row["object"])
            print (str(row_number)+" "+row["text"])
            print("---"+row["object"])
            color = find_color(row["sentiment_value"])
            total_sentiment_and_total_instance_count = find_total_sentiment_and_total_instance_count(row_number,row["subject"], row["object"],row["text"])
            average_sentiment = (total_sentiment_and_total_instance_count[0] + float(row["sentiment_value"]))/total_sentiment_and_total_instance_count[1]            
            
            #print ("---"+str(row_number)+"---")
            #print (row["text"])
            arr = {"source":row["subject"],"target":row["object"],"sentiment_value":average_sentiment,"edge_color":color,"instance_count":total_sentiment_and_total_instance_count[1]}
            find_second_hop_edges(row["object"]) 
            json.dump(arr, jsonfile)
            jsonfile.write(',\n')
            count += 1





# Dhaka, Bangladesh, India, Chittagong, Pakistan, Myanmar, Narayanganj, Malaysia, Gazipur, Sylhet, China, Barisal, Khulna
# BNP, Dhaka Tribune, Awami League, Jamaat, RAB, EC, BGB, Election Commission, High Court, Chhatra League, Jatiya Party, ACC, Shibir, JMB, DMP
# Sheikh Hasina, Khaleda Zia, Ershad, Fakhrul, Monirul, Tarique Rahman, Muhith, Nuzami, Bangabandhu, Ziaur Rahman, Modi
