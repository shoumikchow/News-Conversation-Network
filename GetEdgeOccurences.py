import csv
from collections import Counter
import matplotlib.pyplot as plt
import datetime
#csvfile = open('../person_count.csv', 'r')
csvfile = open('DailyStar.csv', 'r')
csvreader = csv.reader(csvfile, delimiter=',')

"""keywords = []
for row in csvreader:
	keywords.append(row[0])
print(keywords)"""

#indirect_network.csv
"""csvfile = open('../network_indirect.csv', 'r')
csvreader = csv.reader(csvfile, delimiter=',')"""

#Hartal data csv
csvHartalFile = open('../../data-strike-IGC.csv', 'r')
csvHartalReader = csv.reader(csvHartalFile, delimiter=',')

keywords = ['Sheikh Hasina', 'Hasina', 'Khaleda Zia', 'Khaleda', 'Zia', 'Ershad', 'Fakhrul', 'Tarique Rahman', 'Muhith', 'Nizami', 'Bangabandhu', 'Ziaur Rahman', 'Mirza Fakhrul Islam Alamgir', 'Obaidul Quader', 'Quader Molla', 'Ghulam Azam', 'Asaduzzaman Khan Kamal','BNP', 'Awami League', 'Jamaat', 'EC', 'Election Commission', 'Chhatra League', 'Jatiya Party', 'ACC', 'Shibir', 'BCL', 'Foreign Ministry', 'Jubo League', 'Chhatra Dal']

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

#Format date which conforms with the timestamp in indirect_network.csv
def dateFormatter(year,month,day):
	if len(month) == 1:
		month = "0"+month
	if len(day) == 1:
		day = "0"+day

	date = year+"-"+month+"-"+day
	return date

subject_objects_for_ef_idf = []

subject_objects = []

subject_objects_with_timestamps = []

#DailyStarSpecific
edgeOccurencesEachDay = []
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
		"""dateWithoutTime = date[:10]"""
		dateWithoutTime = date


		#Get only 2013 data since only 2013 hartal data is available
		"""if dateWithoutTime[:4] != "2013":
			continue"""
		
		#Check whether subject object have common substring
		if findCommonSubstring(sub,obj) == True:
			continue

		"""if tuple((sub,obj)) not in subject_objects_for_ef_idf:
			subject_objects_for_ef_idf.append(tuple((sub,obj)))"""

		#Get political edge and add it to the list
		subject_objects.append(tuple((sub,obj)))
		#Get political edge with the timestamp and add it to another list
		subject_objects_with_timestamps.append(tuple((sub,obj,date)))

		[year,month,day] = date.split("-")
		
		#DailyStarSpecific
		if date == previousDay:
			edgeOccurencesEachDay[-1] += 1

		else:
			edgeOccurencesEachDay.append(1)
			days.append(datetime.datetime(int(year),int(month),int(day),0,0))
			previousDay = date

#Print the edge occurences each day
"""for i in range(0,10):
	print(days[i]+" "+str(edgeOccurencesEachDay[i]))
"""
"""#Ignore the first row
next(csvHartalReader)

for row in csvHartalReader:
	if row[0] != 2013:
		continue

	hartalDate = dateFormatter(row[0],row[1],row[2])"""


#Find the number of occurences of each tuple
counter = Counter(subject_objects)

#Convert the counter into a usable array
numberOfTupleOccurences = sorted(counter.iteritems())

"""for i in numberOfTupleOccurences:
	print (i)"""

count = [0]
currentCount = 0
#Output

#YAxis
for x in range(1,16):
	for i in numberOfTupleOccurences:
		if i[1] == x:
			currentCount += 1
	count.append(currentCount)
	currentCount = 0


#XAxis
xAxis = range(0,16)


#Plotting magic begins here
"""plt.bar(xAxis, height= count)
plt.xlabel('Number of edge occurences')
plt.ylabel('Unique edges')
plt.yticks(range(0, max(count)+100, 1000))"""

#dailystarspecific
plt.bar(days, height= edgeOccurencesEachDay, width=1)
plt.xlabel('Number of edge occurences')
plt.ylabel('Unique edges')
plt.yticks(range(0, max(edgeOccurencesEachDay)+100, 1000))

plt.show()
#print (numberOfTupleOccurences)
#print (subject_objects_with_timestamps)

