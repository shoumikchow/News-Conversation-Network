import networkx as nx
import matplotlib.pyplot as plt
import community
import csv
from collections import Counter
from pprint import pprint
import operator

keywords = ['Sheikh Hasina', 'Hasina', 'Khaleda Zia', 'Khaleda', 'Zia', 'Ershad', 'Fakhrul', 'Tarique Rahman','Fakhruddin Ahmed', 'Muhith', 'Nizami', 'Bangabandhu', 'Ziaur Rahman', 'Mirza Fakhrul Islam Alamgir', 'Obaidul Quader', 'Quader Molla', 'Ghulam Azam', 'Asaduzzaman Khan Kamal','BNP', 'Awami League', 'Jamaat','Jamaat-e-Islami', 'EC', 'Election Commission', 'Chhatra League', 'Jatiya Party', 'ACC', 'Shibir', 'BCL', 'Foreign Ministry', 'Jubo League', 'Chhatra Dal','Bangladesh Chhatra League','Asian Development Bank','Jahangirnagar University','Parliament','Shahbagh','Bhola','Padma Bridge','Supreme Court Bar Association','University of Dhaka','Bangabhaban','Caretaker','Sahara Khatun','Shah AMS Kibria','President Ahmed','Jamaat-ul-Mujahideen','Jagrata Muslim Janata Bangladesh','Hizb-ut Tahrir','Motiur Rahman Nizami','Abul Kalam Azad','Ghulam Azam','Abdul Kader Mullah','Mir Quasem Ali','Abdus Subhan','Ansarullah Bangla Team','Shia Muslims','Ali Ahsan Mohammad Mujahid','Salahuddin Quader Chowdhury','atheists','Ahmed Rajib Haider','Rohingya','refugee']

comunity = {}
#def getCommunity(partition):
    #max_value = max(partition.values())  # maximum value
    #max_keys = [k for k, v in partition.items() if v == max_value] # getting all keys containing the `maximum`
    #print(max_value, max_keys)
    #for communityNo in range(0,115):
        #for i in 
        #network.setdefault(sub,[]).append(obj)

"""def populateNeighbouringNetworkDict(sub, obj):
    comunity.setdefault(sub,[]).append(obj)"""

def getComm(community):
    for com in set(community.values()) :
        list_nodes = [nodes for nodes in community.keys() if community[nodes] == com]
        comunity[com] = list_nodes
    for i in comunity:
        print(str(i) + " " + str(comunity[i]))
    

def getCommunities(G):

    partition = community.best_partition(G)
    """for i in partition:
        print(str(i)+" : "+str(partition[i]))"""
    getComm(partition)
    return

def getBetweenessCentrality(G):
    bc = nx.betweenness_centrality(G)
    sorted_bc = sorted(bc.items(), key=operator.itemgetter(1),reverse=True)
    pprint(sorted_bc)

def getPagerankNodes(G):
    pr = nx.pagerank(G, alpha=0.9)
    sorted_x = sorted(pr.items(), key=operator.itemgetter(1),reverse=True)
    pprint(sorted_x)
   
#Check if the two entites might share a common substring
def findCommonSubstring(sub, obj):
    shortString = ""
    longString = ""
    if len(sub)<len(obj):
        shortString = sub
        longString = obj
    else:
        shortString = obj
        longString = sub
    if shortString in longString:
        #Making the assumption of 3 since the shortest name possible in the dataset is Zia
        if len(shortString)>3:
            return True
        else:
            return False
    else:
        return False
csvfile = open('DailyStar.csv', 'r')
csvreader = csv.reader(csvfile, delimiter=',')
subject_objects = []
G=nx.Graph()
#Ignore the first row
next(csvreader)
count = 1
#Find out edge occurences
for row in csvreader:
    
    """if count == 7000:
        break"""
    #If the subject is a political entity and the subject is not talking to himself
    if (row[2] in keywords or row[4] in keywords) and (row[2] != row[4]):
        
        sub = (row[2])
        obj = (row[4])
        newsID = (row[0])
        date = (row[1])
        
        #Check whether subject object have common substring
        if findCommonSubstring(sub,obj) == True:
            continue
        #G.add_edge(sub,obj)
        #Get political edge and add it to the list
        subject_objects.append(tuple((sub,obj)))
        count += 1

csvfile.close()
#Find the number of occurences of each tuple
counter = Counter(subject_objects)
#Convert the counter into a usable array
numberOfTupleOccurences = sorted(counter.items())
#pprint(numberOfTupleOccurences)
#print(numberOfTupleOccurences)
#print(len(numberOfTupleOccurences))
for i in numberOfTupleOccurences:
    G.add_edge(i[0][0],i[0][1])

getCommunities(G)
#getPagerankNodes(G)
#getBetweenessCentrality(G)



