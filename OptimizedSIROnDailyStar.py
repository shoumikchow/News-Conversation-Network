import csv
from collections import Counter
import matplotlib.pyplot as plt
import datetime
import random
import time

#Setting up the parameters
simulationsLimit = 1000
expiryTimeLimit = 1
timestepLimit = 3
probabilityOfGettingInfected = 0.2

csvfile = open('DailyStar.csv', 'r')
csvreader = csv.reader(csvfile, delimiter=',')

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

def findNeighbouringNodes(subject):
	neighbouringNetwork = []
	for neighbour in networkForCurrentSimulation[subject]:
		if neighbour not in recoveredNodes:
			neighbouringNetwork.append(neighbour)
	return neighbouringNetwork

def infectNodes(node, neighbouringNodes):
	infectedNodes = []
	
	#For each node in the network, get a random number and if its above 0.5, infect the node
	for i in neighbouringNodes:
		randomNumber = random.uniform(0, 1)
		if(randomNumber > (1-probabilityOfGettingInfected)):
			if i not in infectedNodes and i not in recoveredNodes:
				infectedNodes.append(i)
				networkForCurrentSimulation[node].remove(i)
	return infectedNodes

def addToExpiryTimeDict(infectedNodes, nodesToBeDeleted, timeToBeDeleted):
	nodesToBeDeleted[timeToBeDeleted] = []
	for i in infectedNodes:
		#Update the nodesToBeDeleted dictionary to set the expiry time for the infected nodes 
		nodesToBeDeleted[timeToBeDeleted].append(i)

def recoverNodes(infectedNodes, nodesToBeDeleted, timestep):
	if timestep in nodesToBeDeleted:
		for i in nodesToBeDeleted[timestep]:
			if i not in infectedNodes:
				continue
			#remove the infected nodes
			infectedNodes.remove(i)
			#Add to recovered nodes so that these nodes are not infected again
			recoveredNodes.append(i)
	return infectedNodes

def chooseRandomNode(tuples):
	while True:
		index = random.randint(0,len(tuples))
		node = tuples[index][0]
		if node not in randomNodesAlreadyChosen:
			randomNodesAlreadyChosen.append(node)
			return node

def plotHistogram(nodeLabels,maximumFrequencyOfInfectionOfAllSimulations):
	x = range(0,len(maximumFrequencyOfInfectionOfAllSimulations))
	plt.bar(x, height= maximumFrequencyOfInfectionOfAllSimulations,align='center',width=.5)
	plt.xlabel('Simulation')
	plt.ylabel('Maximum number of infected nodes')
	#plt.xticks(x, nodeLabels,rotation='vertical');
	plt.show()

def populateNeighbouringNetworkDict(sub, obj):
	network.setdefault(sub,[]).append(obj)


subject_objects = []

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

#Find the number of occurences of each tuple
counter = Counter(subject_objects)

#Convert the counter into a usable array
numberOfTupleOccurences = sorted(counter.items())

network = {}

for i in numberOfTupleOccurences:
	populateNeighbouringNetworkDict(i[0][0],i[0][1])

##Network dictionary built


###SIR starts here

#Choose a unique random node in each loop
randomNodesAlreadyChosen = []
maximumFrequencyOfInfectionOfAllSimulations = []
xAxisOfHistogram = []

for simulation in range(1,simulationsLimit+1):
	maxInfectedNodesOfCurrentNode = 0
	#Create a copy of the network in each simulation
	networkForCurrentSimulation = network
	for expiryTime in range(1,expiryTimeLimit+1):
		seedNode = chooseRandomNode(subject_objects)
		print ('seed node is '+seedNode)
		infectedNodes = [seedNode]
		#Key is the expiry time and values are the nodes which are going to expire in the respective key timestep
		nodesToBeDeleted = {}
		#These nodes will not be added to infected nodes
		recoveredNodes = []
		#plotterLists
		yAxis = []
		xAxis = []
		for timestep in range(0,timestepLimit+1):
			if not infectedNodes:
				break
			#Remove all the infected nodes which have reached their expiry time
			infectedNodes = recoverNodes(infectedNodes, nodesToBeDeleted, timestep)
			#Label the nodes with their respective expiry times
			addToExpiryTimeDict(infectedNodes, nodesToBeDeleted, timestep+expiryTime)
			#All the neighboring nodes of the current infected nodes are added here, which will later be added to the infected nodes
			tempInfected = []
			for i in infectedNodes:
				if i in networkForCurrentSimulation:
					tempInfected += infectNodes(i,networkForCurrentSimulation[i])
			
			infectedNodes += tempInfected
			print ('current infected nodes are')
			#print (infectedNodes)
			
			
			print('after recovery')
			#print (infectedNodes)
			if len(infectedNodes) > maxInfectedNodesOfCurrentNode:
				maxInfectedNodesOfCurrentNode = len(infectedNodes)
			#Y axis will have the total number of infected nodes at the current timestep 
			yAxis.append(len(infectedNodes))

			#X axis will have the time
			xAxis.append(timestep)

		#plt.plot(xAxis,yAxis,label=expiryTime)
		#plt.plot(xAxis,yAxis)

	maximumFrequencyOfInfectionOfAllSimulations.append(maxInfectedNodesOfCurrentNode)
	xAxisOfHistogram.append(seedNode)

"""plt.title(str(simulationsLimit)+' simulations expirytime upto ' + str(expiryTimeLimit) + ' susceptibility ' + str(probabilityOfGettingInfected*100)+'%')
plt.xlabel('Time')
plt.ylabel('Number of infected nodes')"""
#plt.legend(loc='upper right')
#plt.show()
plotHistogram(xAxisOfHistogram,maximumFrequencyOfInfectionOfAllSimulations)
print(maximumFrequencyOfInfectionOfAllSimulations)