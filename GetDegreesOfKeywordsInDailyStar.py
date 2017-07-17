import csv

csvfile = open('../DailyStar.csv', 'r')
csvreader = csv.reader(csvfile, delimiter=',')

keywords = ['Sheikh Hasina', 'Hasina', 'Khaleda Zia', 'Khaleda', 'Zia', 'Ershad', 'Fakhrul', 'Tarique Rahman', 'Muhith', 'Nizami', 'Bangabandhu', 'Ziaur Rahman', 'Mirza Fakhrul Islam Alamgir', 'Obaidul Quader', 'Quader Molla', 'Ghulam Azam', 'Asaduzzaman Khan Kamal','BNP', 'Awami League', 'Jamaat', 'EC', 'Election Commission', 'Chhatra League', 'Jatiya Party', 'ACC', 'Shibir', 'BCL', 'Foreign Ministry', 'Jubo League', 'Chhatra Dal']

keywordDegree = {}

def initializeKeywordDegree():
	for i in keywords:
		keywordDegree[i] = 1

def incrementDegreeOfKeyword(keyword):
	keywordDegree[keyword] += 1

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


initializeKeywordDegree()
#Skip first line
next(csvreader)

for row in csvreader:
	
	if (row[2] in keywords or row[4] in keywords) and row[2] != row[4]:
		
		sub = (row[2])
		obj = (row[4])

		if findCommonSubstring(sub,obj) == True:
			continue

		if sub in keywords:
			incrementDegreeOfKeyword(sub)

		elif obj in keywords:
			incrementDegreeOfKeyword(obj)

for i in keywordDegree:
	print (i+": "+str(keywordDegree[i]))

