import csv
import collections
from collections import Counter
import matplotlib.pyplot as plt
import datetime
from dateutil import parser

expiryDate = 10
csvfile = open('./Scraped data/DailyStar.csv', 'r')
csvreader = csv.reader(csvfile, delimiter=',')

keywords = ['Sheikh Hasina', 'Hasina', 'Khaleda Zia', 'Khaleda', 'Zia', 'Ershad', 'Fakhrul', 'Tarique Rahman','Fakhruddin Ahmed', 'Muhith', 'Nizami', 'Bangabandhu', 'Ziaur Rahman', 'Mirza Fakhrul Islam Alamgir', 'Obaidul Quader', 'Quader Molla', 'Ghulam Azam', 'Asaduzzaman Khan Kamal','BNP', 'Awami League', 'Jamaat','Jamaat-e-Islami', 'EC', 'Election Commission', 'Chhatra League', 'Jatiya Party', 'ACC', 'Shibir', 'BCL', 'Foreign Ministry', 'Jubo League', 'Chhatra Dal','Bangladesh Chhatra League','Asian Development Bank','Jahangirnagar University','Parliament','Shahbagh','Bhola','Padma Bridge','Supreme Court Bar Association','University of Dhaka','Bangabhaban']

def findCommonSubstring(sub, obj):
	if sub in obj:
		return True
	else:
		return False
	
#Format date which conforms with the timestamp in indirect_network.csv

subject_objects = []

subject_objects_with_timestamps = []

#DailyStarSpecific
edgeOccurencesEachDay = {}
days = []
previousDay = ''
#Ignore the first row
next(csvreader)
#Find out edge occurences
for row in csvreader:
	
	#If the subject is a political entity and the subject is not talking to himself
	if (row[2] in keywords or row[4] in keywords) and row[2] != row[4]:
		
		sub = (row[2])
		obj = (row[4])
		newsID = (row[0])
		date = (row[1])
		date = parser.parse(date)
		
		#Check whether subject object have common substring
		if findCommonSubstring(sub,obj) == True:
			continue

		#Get political edge and add it to the list
		subject_objects.append(tuple((sub,obj)))
		#Get political edge with the timestamp and add it to another list
		for i in range(1,expiryDate+1):
			subject_objects_with_timestamps.append(tuple((sub,obj,date)))
			
		#DailyStarSpecific
			if date in edgeOccurencesEachDay:
				edgeOccurencesEachDay[date] += 1

			else:
				edgeOccurencesEachDay[date] = 1
				days.append(date)
				previousDay = date
			date = date + datetime.timedelta(days=1)

	
edgeOccurencesEachDay = (collections.OrderedDict(sorted(edgeOccurencesEachDay.items())))

#Find the number of occurences of each tuple
counter = Counter(subject_objects)


#Convert the counter into a usable array
numberOfTupleOccurences = sorted(counter.items())


count = [0]
currentCount = 0

edgeOccurencesEachDay = (list(edgeOccurencesEachDay.values()))

plt.bar(days, height= edgeOccurencesEachDay, width=1, color='blue')
plt.xlabel('Number of edge occurences')
plt.ylabel('Unique edges')
plt.show()

