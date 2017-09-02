import csv
from collections import Counter
import matplotlib.pyplot as plt
import datetime
from matplotlib.backends.backend_pdf import PdfPages
from pprint import pprint
import numpy as np
from FunctionsAndLists import *

# csvfile = open('../SortedIndirectNetwork.csv', 'r')
# csvfile = open('../network_indirect.csv', 'r')
csvfile = open('DailyStar.csv', 'r')
csvreader = csv.reader(csvfile, delimiter=',')

#Hartal data csv
csvHartalFile = open('../../data-strike-IGC.csv', 'r')
csvHartalReader = csv.reader(csvHartalFile, delimiter=',')


# 'Sheikh Hasina', 'Begum Khaleda Zia', 'Hasina', 'Mirza Fakrul Islam Alamgir', 'Tarek Rahman', 'Election Commission', 'CEC', 'Party Alliance', 'Jamaat', 'Savar Jubo League', 'Awami League','Jamaat-Islami', 'caretaker government', 'BNP', 'Dhaka Metropolitan AL', 'Dhaka'


#Ignore the first row
next(csvreader)

startYear = 2007
endYear = 2008
#pp = PdfPages('DailyStarAwamiLeagueEdges.pdf')


for i in range(7):

    subject_objects_for_ef_idf = []

    subject_objects = []

    subject_objects_with_timestamps = []

    #DailyStarSpecific
    edgeOccurencesEachDay = []
    days = []
    previousDay = ''

    hartalDates = []
    hartalIndicator = []

    

    # Find out edge occurences
    for row in csvreader:
        
        sub = (row[2])
        obj = (row[4])
        #If the subject is a political entity and the subject is not talking to himself
        # if ((row[2] in allHartals) or (row[4] in allHartals)) and row[2] != row[4]:
        if (sub in AwamiLeagueMembers or obj in AwamiLeagueMembers):
            
            """if (row[2] in keywords or row[4] in keywords):
                continue"""
            # print (row[6])
            print (row)
            newsID = (row[0])

            date = (row[1]).replace("\n","")
            #date = (row[1][:10]).replace("\n","")
            """if (date[:4]) == "2012" and (date[5:7]) == 12:
                print (date)
                print (row[2]+" "+row[4])"""
            # print(date)
            #print(date)
            #Get only 2013 data since only 2013 hartal data is available
            """if dateWithoutTime[:4] != "2013":
                continue"""
            
            if int(date[:4]) < int(startYear):
                continue

            if(int(date[:4]) == endYear):
                break


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
                days.append(datetime(int(year),int(month),int(day),0,0))
                previousDay = date


    #Find the number of occurences of each tuple
    counter = Counter(subject_objects)

    #Convert the counter into a usable array
    numberOfTupleOccurences = sorted(counter.iteritems(), key=lambda x: x[1], reverse = True)
    pprint(numberOfTupleOccurences)
    # for i in numberOfTupleOccurences:
    #     print (i)
    #print(subject_objects[:1000])

    count = [0]
    currentCount = 0
    #Output

    plt.bar(days, height= edgeOccurencesEachDay, width=1)
    #plt.plot(days,edgeOccurencesEachDay)
    plt.xlabel('Year')
    plt.ylabel('Total number of edges per day')
    plt.title(startYear)
    #plt.yticks(range(0, max(edgeOccurencesEachDay)+100, 1000))
    #plt.gcf().autofmt_xdate()

    #print (edgeOccurencesEachDay)
    next(csvHartalReader)
    for row in csvHartalReader:
        
        year = row[0]
        month = row[1]
        day = row[2]

        if int(year) < startYear:
            continue

        if int(year) >= endYear:
            break

        hartalDates.append(datetime(int(year),int(month),int(day),0,0))
        hartalIndicator.append(50)

    csvHartalFile.seek(0)

    if hartalDates:
        plt.bar(hartalDates, height= hartalIndicator, width=1)

    plt.xticks(rotation='45',size='small')
    #pp.savefig()
    #plt.clf()
    plt.show()
    startYear += 1
    endYear += 1


#pp.close()

#print (numberOfTupleOccurences)
#print (subject_objects_with_timestamps)

