import csv
from collections import Counter
import matplotlib.pyplot as plt
import datetime
import random

csvfile = open('DailyStar.csv', 'r')
csvreader = csv.reader(csvfile, delimiter=',')

#Hartal data csv
csvHartalFile = open('../../data-strike-IGC.csv', 'r')
csvHartalReader = csv.reader(csvHartalFile, delimiter=',')

keywords = ['Sheikh Hasina', 'Hasina', 'Khaleda Zia', 'Khaleda', 'Zia', 'Ershad', 'Fakhrul', 'Tarique Rahman','Fakhruddin Ahmed', 'Muhith', 'Nizami', 'Bangabandhu', 'Ziaur Rahman', 'Mirza Fakhrul Islam Alamgir', 'Obaidul Quader', 'Quader Molla', 'Ghulam Azam', 'Asaduzzaman Khan Kamal','BNP', 'Awami League', 'Jamaat','Jamaat-e-Islami', 'EC', 'Election Commission', 'Chhatra League', 'Jatiya Party', 'ACC', 'Shibir', 'BCL', 'Foreign Ministry', 'Jubo League', 'Chhatra Dal','Bangladesh Chhatra League','Asian Development Bank','Jahangirnagar University','Parliament','Shahbagh','Bhola','Padma Bridge','Supreme Court Bar Association','University of Dhaka','Bangabhaban']

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

def findNeighbouringNodes(tuples, subject, recoveredNodes):
	neighbouringNodes = []
	
	for i in tuples:
		sub = i[0]
		obj = i[1]
		if sub == subject:
			if obj not in neighbouringNodes and obj not in recoveredNodes and obj != sub:
				neighbouringNodes.append(obj)
		elif obj == subject:
			if sub not in neighbouringNodes and sub not in recoveredNodes and obj != sub:
				neighbouringNodes.append(sub)

	return neighbouringNodes

def infectNodes(node, neighbouringNodes):
	infectedNodes = []
	
	#For each node in the network, get a random number and if its above 0.5, infect the node
	for i in neighbouringNodes:
		randomNumber = random.uniform(0, 1)
		if(randomNumber > 0.5):
			infectedNodes.append(i)
	return infectedNodes

def addToDict(infectedNodes, nodesToBeDeleted, timeToBeDeleted):
	nodesToBeDeleted[timeToBeDeleted] = []
	for i in infectedNodes:
		nodesToBeDeleted[timeToBeDeleted].append(i)

def recoverNodes(infectedNodes, nodesToBeDeleted, timestep):
	if timestep in nodesToBeDeleted:
		for i in nodesToBeDeleted[timestep]:
			if i not in infectedNodes:
				continue
			infectedNodes.remove(i)
			recoveredNodes.append(i)
	return infectedNodes

subject_objects = []

subject_objects_with_timestamps = []

#DailyStarSpecific
edgeOccurencesEachDay = []
days = []
previousDay = ''

hartalDates = []
hartalIndicator = []


#Ignore the first row
next(csvreader)

#Find out edge occurences
for row in csvreader:
	
	#If the subject is a political entity and the subject is not talking to himself
	if row[2] != row[4]:
		
		sub = (row[2])
		obj = (row[4])
		newsID = (row[0])
		date = (row[1])
		
		#Check whether subject object have common substring
		if findCommonSubstring(sub,obj) == True:
			continue

		#Get political edge and add it to the list
		subject_objects.append(tuple((sub,obj)))

		#Get political edge with the timestamp and add it to another list
		subject_objects_with_timestamps.append(tuple((sub,obj,date)))

#Find the number of occurences of each tuple
counter = Counter(subject_objects)

#Convert the counter into a usable array
numberOfTupleOccurences = sorted(counter.iteritems())




#SIR starts here

print( "Seed node of simulation?")
seedNode = raw_input()


for expiryTime in range(7,10):

	#plotterLists
	yAxis = []
	xAxis = []

	#key will be the timestep at which the values/nodes will be recovered
	nodesToBeDeleted = {}

	#The list which will contain all the recovered nodes that will not be processed further
	recoveredNodes = []

	infectedNodes = [seedNode]

	neighbouringNodes = findNeighbouringNodes(subject_objects,seedNode,recoveredNodes)

	currentNode = seedNode
	previousNode = seedNode

	#The timer
	for timestep in range (1,1000):

		if not infectedNodes:
			break

		if not neighbouringNodes:
			for i in range (1,len(infectedNodes)):
				arr = findNeighbouringNodes(subject_objects,currentNode,recoveredNodes)
				if arr:
					currentNode = infectedNodes[i]
					break
		else:
			currentNode = infectedNodes[0]


		if currentNode != previousNode:
			#Find the network of the current node
			neighbouringNodes = findNeighbouringNodes(subject_objects,currentNode,recoveredNodes)
			previousNode = currentNode

		#Update the infected nodes list by infecting the neighbouring nodes of the current node
		infectedNodes += infectNodes(currentNode,neighbouringNodes)

		neighbouringNodes = [x for x in neighbouringNodes if x not in infectedNodes]

		addToDict(infectedNodes, nodesToBeDeleted, timestep+expiryTime)

		infectedNodes = recoverNodes(infectedNodes, nodesToBeDeleted, timestep)
		yAxis.append(len(infectedNodes))
		xAxis.append(timestep)
		print (timestep)
		print (infectedNodes)
		print (neighbouringNodes)
		print ('----------------------------------------------------')
		print ('----------------------------------------------------')
		print ('----------------------------------------------------')
		print ('----------------------------------------------------')
		print ('----------------------------------------------------')
		print ('----------------------------------------------------')
		print ('----------------------------------------------------')
		print ("\n")
		print ("\n")
		print ("\n")
		print ("above expiry time was "+str(expiryTime))
		


	#print ("after "+str(len(infectedNodes)))

	plt.plot(xAxis,yAxis,label=expiryTime)

plt.title('Seed node '+seedNode)
plt.xlabel('Time')
plt.ylabel('Number of infected nodes')
plt.legend(loc='upper right')
plt.show()







