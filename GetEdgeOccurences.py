import csv
from collections import Counter

csvfile = open('../network_indirect.csv', 'r')
csvreader = csv.reader(csvfile, delimiter=',')

keywords = ['Sheikh Hasina', 'Hasina', 'Khaleda Zia', 'Khaleda', 'Zia', 'Ershad', 'Fakhrul', 'Tarique Rahman', 'Muhith', 'Nizami', 'Bangabandhu', 'Ziaur Rahman', 'Mirza Fakhrul Islam Alamgir', 'Obaidul Quader', 'Quader Molla', 'Ghulam Azam', 'Asaduzzaman Khan Kamal','BNP', 'Awami League', 'Jamaat', 'EC', 'Election Commission', 'Chhatra League', 'Jatiya Party', 'ACC', 'Shibir', 'BCL', 'Foreign Ministry', 'Jubo League', 'Chhatra Dal']

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
		if len(shortString)>3:
			return True
		else:
			return False
	else:
		return False

subject_objects_for_ef_idf = []

subject_objects = []

subject_objects_with_timestamps = []

count = 0

for row in csvreader:

	#Ignore the first row
	if count == 0:
		count += 1
		continue

	#If the subject is a political entity and the subject is not talking to himself
	if (row[2] in keywords or row[4] in keywords) and row[2] != row[4]:
		
		sub = (row[2])
		obj = (row[4])
		newsID = (row[0])
		date = (row[1])

		if findCommonSubstring(sub,obj) == True:
			continue

		if tuple((sub,obj)) not in subject_objects_for_ef_idf:
			subject_objects_for_ef_idf.append(tuple((sub,obj)))

		#Get political edge and add it to the list
		subject_objects.append(tuple((sub,obj)))
		#Get political edge with the timestamp and add it to another list
		subject_objects_with_timestamps.append(tuple((sub,obj,date)))

#Find the number of occurences of each tuple
counter = Counter(subject_objects)

#Convert the counter into a usable array
numberOfTupleOccurences = sorted(counter.iteritems())

#Output
for i in numberOfTupleOccurences:
	if i[1] >= 10:
		print i
#print (numberOfTupleOccurences)
#print (subject_objects_with_timestamps)