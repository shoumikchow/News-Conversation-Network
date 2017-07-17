import csv
import operator

csvfile = open('../DailyStar.csv', 'r')
csvreader = csv.reader(csvfile, delimiter=',')

keywordDegree = {}

next(csvreader)

for row in csvreader:
	
	sub = (row[2])
	obj = (row[4])
	
	if sub in keywordDegree:
		keywordDegree[sub] += 1
	elif sub not in keywordDegree:
		keywordDegree[sub] = 1

	if obj in keywordDegree:
		keywordDegree[obj] += 1
	elif obj not in keywordDegree:
		keywordDegree[obj] = 1

sortedKeywordDegree = sorted(keywordDegree.items(), key=operator.itemgetter(1), reverse=True)

#print (sortedKeywordDegree)

for i in sortedKeywordDegree:
	print (i)