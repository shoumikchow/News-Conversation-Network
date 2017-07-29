import networkx as nx
import matplotlib.pyplot as plt
import community
import csv
from collections import Counter

keywords = ['Sheikh Hasina', 'Hasina', 'Khaleda Zia', 'Khaleda', 'Zia', 'Ershad', 'Fakhrul', 'Tarique Rahman','Fakhruddin Ahmed', 'Muhith', 'Nizami', 'Bangabandhu', 'Ziaur Rahman', 'Mirza Fakhrul Islam Alamgir', 'Obaidul Quader', 'Quader Molla', 'Ghulam Azam', 'Asaduzzaman Khan Kamal','BNP', 'Awami League', 'Jamaat','Jamaat-e-Islami', 'EC', 'Election Commission', 'Chhatra League', 'Jatiya Party', 'ACC', 'Shibir', 'BCL', 'Foreign Ministry', 'Jubo League', 'Chhatra Dal','Bangladesh Chhatra League','Asian Development Bank','Jahangirnagar University','Parliament','Shahbagh','Bhola','Padma Bridge','Supreme Court Bar Association','University of Dhaka','Bangabhaban']


def plotGraph(G):
	part = community.best_partition(G)
	values = [part.get(node) for node in G.nodes()]
	nx.draw_spring(G, cmap = plt.get_cmap('jet'), node_color = values, node_size=15, with_labels=False)
	plt.show()

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
	if (row[2] in keywords or row[4] in keywords) and row[2] != row[4]:
		
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

#Find the number of occurences of each tuple
counter = Counter(subject_objects)

#Convert the counter into a usable array
numberOfTupleOccurences = sorted(counter.items())

print(len(numberOfTupleOccurences))

for i in numberOfTupleOccurences:
	G.add_edge(i[0],i[1])

plotGraph(G)

"""for i in numberOfTupleOccurences:
	G.add_edge(i[0],i[1])"""



