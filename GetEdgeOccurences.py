import csv
from collections import Counter

csvfile = open('../subject_objects.csv', 'r')
r = csv.DictReader(csvfile)
count = 0

subjects = ['Sheikh Hasina', 'Hasina', 'Khaleda Zia', 'Khaleda', 'Zia', 'Ershad', 'Fakhrul', 'Tarique Rahman', 'Muhith', 'Nizami', 'Bangabandhu', 'Ziaur Rahman', 'Mirza Fakhrul Islam Alamgir', 'Obaidul Quader', 'Quader Molla', 'Ghulam Azam', 'Asaduzzaman Khan Kamal']

subject_objects = []

subject_objects_with_timestamps = []

for row_number, row in enumerate(r):

	#If the subject is a political entity and the subject is not talking to himself
	if row['subject'] in subjects and row['subject'] != row['object']:
		
		sub = (row['subject'])
		obj = (row['object'])
		date = (row['timestamp'])
		#Get political edge and add it to the list
		subject_objects.append(tuple((sub,obj)))
		#Get political edge with the timestamp and add it to another list
		subject_objects_with_timestamps.append(tuple((sub,obj,date)))

		
#Find the number of occurences of each tuple
counter = Counter(subject_objects)

#Convert the counter into a usable array
numberOfTupleOccurences = sorted(counter.iteritems())
#print (numberOfTupleOccurences)

print (subject_objects_with_timestamps)