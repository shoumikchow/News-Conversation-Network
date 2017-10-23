import csv
from collections import Counter
import matplotlib.pyplot as plt
import datetime
import scipy.fftpack
from matplotlib.backends.backend_pdf import PdfPages
from FunctionsAndLists import *

# csvfile = open('../SortedIndirectNetwork.csv', 'r')
# csvfile = open('../network_indirect.csv', 'r')
csvfile = open('./Scraped data/DailyStar.csv', 'r')
csvreader = csv.reader(csvfile, delimiter=',')

# Hartal data csv
# csvHartalFile = open('.Scraped data/data-strike-IGC.csv', 'r')
# csvHartalReader = csv.reader(csvHartalFile, delimiter=',')

# Ignore the first row
next(csvreader)

startYear = 2007
endYear = 2008
pp = PdfPages('fft_out_granular.pdf')


for i in range(7):

    subject_objects = []
    subject_objects_with_timestamps = []

    # DailyStarSpecific
    edgeOccurencesEachDay = []
    days = []
    previousDay = ''

    hartalDates = []
    hartalIndicator = []

    # Find out edge occurences
    for row in csvreader:
        sub = (row[2])
        obj = (row[4])
        # If the subject is a political entity and the subject is not talking to himself
        # if ((row[2] in allHartals) or (row[4] in allHartals)) and row[2] != row[4]:
        if (sub in previousKeywords or obj in previousKeywords):
            # print (row)
            newsID = (row[0])
            date = (row[1]).replace("\n", "")
            if int(date[:4]) < int(startYear):
                continue

            if(int(date[:4]) == endYear):
                break
            # Check whether subject object have common substring
            if findCommonSubstring(sub, obj):
                continue

            """if tuple((sub,obj)) not in subject_objects_for_ef_idf:
                subject_objects_for_ef_idf.append(tuple((sub,obj)))"""

            # Get political edge and add it to the list
            subject_objects.append(tuple((sub, obj)))
            # Get political edge with the timestamp and add it to another list
            subject_objects_with_timestamps.append(tuple((sub, obj, date)))

            [year, month, day] = date.split("-")

            # DailyStarSpecific
            if date == previousDay:
                edgeOccurencesEachDay[-1] += 1

            else:
                edgeOccurencesEachDay.append(1)
                days.append(datetime(int(year), int(month), int(day), 0, 0))
                previousDay = date

    # Find the number of occurences of each tuple
    counter = Counter(subject_objects)

    # Convert the counter into a usable array
    numberOfTupleOccurences = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    # pprint(numberOfTupleOccurences)
    count = [0]
    currentCount = 0
    # Output

    plt.bar(days, height=scipy.fftpack.fft(edgeOccurencesEachDay), width=1)
    plt.xlabel('Year')
    plt.ylabel('Total number of edges per day')
    plt.title(startYear)

    # print (edgeOccurencesEachDay)
    # next(csvHartalReader)
    # for row in csvHartalReader:

    #     year = row[0]
    #     month = row[1]
    #     day = row[2]

    #     if int(year) < startYear:
    #         continue

    #     if int(year) >= endYear:
    #         break

    #     hartalDates.append(datetime(int(year),int(month),int(day),0,0))
    #     hartalIndicator.append(50)

    # csvHartalFile.seek(0)

    # if hartalDates:
    #     plt.bar(hartalDates, height= hartalIndicator, width=1)

    plt.xticks(rotation='45', size='small')
    pp.savefig()
    plt.clf()

    pp.savefig()
    # plt.show()
    startYear += 1
    endYear += 1

pp.close()
csvfile.close()
# csvHartalFile.close()
