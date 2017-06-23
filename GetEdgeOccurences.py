import csv
from collections import Counter

csvfile = open('../network_indirect.csv', 'r')
csvreader = csv.reader(csvfile, delimiter=',')

keywords = ['Sheikh Hasina', 'Hasina', 'Khaleda Zia', 'Khaleda', 'Zia', 'Ershad', 'Fakhrul', 'Tarique Rahman', 'Muhith', 'Nizami', 'Bangabandhu', 'Ziaur Rahman', 'Mirza Fakhrul Islam Alamgir', 'Obaidul Quader', 'Quader Molla', 'Ghulam Azam', 'Asaduzzaman Khan Kamal']

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
		date = (row[1])
		#Get political edge and add it to the list
		subject_objects.append(tuple((sub,obj)))
		#Get political edge with the timestamp and add it to another list
		subject_objects_with_timestamps.append(tuple((sub,obj,date)))

#Find the number of occurences of each tuple
counter = Counter(subject_objects)

#Convert the counter into a usable array
numberOfTupleOccurences = sorted(counter.iteritems())

#Output
print (numberOfTupleOccurences)
#print (subject_objects_with_timestamps)