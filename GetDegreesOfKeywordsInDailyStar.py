import csv
import matplotlib.pyplot as plt
import operator

csvfile = open('../DailyStar.csv', 'r')
csvreader = csv.reader(csvfile, delimiter=',')

keywords = ['Sheikh Hasina', 'Hasina', 'Khaleda Zia', 'Khaleda', 'Zia', 'Ershad', 'Fakhrul', 'Tarique Rahman','Fakhruddin Ahmed', 'Muhith', 'Nizami', 'Bangabandhu', 'Ziaur Rahman', 'Mirza Fakhrul Islam Alamgir', 'Obaidul Quader', 'Quader Molla', 'Ghulam Azam', 'Asaduzzaman Khan Kamal','BNP', 'Awami League', 'Jamaat','Jamaat-e-Islami', 'EC', 'Election Commission', 'Chhatra League', 'Jatiya Party', 'ACC', 'Shibir', 'BCL', 'Foreign Ministry', 'Jubo League', 'Chhatra Dal','Bangladesh Chhatra League','Asian Development Bank','Jahangirnagar University','Parliament','Shahbagh','Bhola','Padma Bridge','Supreme Court Bar Association','University of Dhaka','Bangabhaban']

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

keywordInDict = []
frequencyOfKeyword  = []

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

keywordDegree = sorted(keywordDegree.items(), key=operator.itemgetter(1), reverse=True)

for i in keywordDegree:
	#print (i+": "+str(keywordDegree[i]))
	print(i)
	keywordInDict.append(i[0])
	frequencyOfKeyword.append(i[1])

#keywordInDict = range(0,42)
#print (len(keywordInDict))
"""plt.bar(keywordInDict, height= frequencyOfKeyword, width=1)
plt.xlabel('Keywords')
plt.ylabel('Frequency')
plt.set_xticklabels(keywordInDict, rotation='vertical', fontsize=18) 
plt.yticks(range(0, max(frequencyOfKeyword), 1000))"""

plt.bar(range(len(frequencyOfKeyword)), frequencyOfKeyword, align='center',width=1)
plt.xticks(range(len(frequencyOfKeyword)), keywordInDict, size='small',rotation='vertical')
plt.show()

