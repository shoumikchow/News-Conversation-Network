import csv
from collections import Counter
import matplotlib.pyplot as plt
import datetime
import scipy.fftpack

csvfile = open('./Scraped data/DailyStar.csv', 'r')
csvreader = csv.reader(csvfile, delimiter=',')

# csvHartalFile = open('./Scraped data/data-strike-IGC.csv', 'r')
# csvHartalReader = csv.reader(csvHartalFile, delimiter=',')

keywords = ['Sheikh Hasina', 'Hasina', 'Khaleda Zia', 'Khaleda', 'Zia', 'Ershad', 'Fakhrul', 'Tarique Rahman', 'Fakhruddin Ahmed', 'Muhith', 'Nizami', 'Bangabandhu', 'Ziaur Rahman', 'Mirza Fakhrul Islam Alamgir', 'Obaidul Quader', 'Quader Molla', 'Ghulam Azam', 'Asaduzzaman Khan Kamal', 'BNP', 'Awami League', 'Jamaat', 'Jamaat-e-Islami', 'EC', 'Election Commission', 'Chhatra League', 'Jatiya Party', 'ACC', 'Shibir', 'BCL', 'Foreign Ministry', 'Jubo League', 'Chhatra Dal', 'Bangladesh Chhatra League', 'Asian Development Bank', 'Jahangirnagar University',
            'Parliament', 'Shahbagh', 'Bhola', 'Padma Bridge', 'Supreme Court Bar Association', 'University of Dhaka', 'Bangabhaban', 'Caretaker', 'Sahara Khatun', 'Shah AMS Kibria', 'President Ahmed', 'Jamaat-ul-Mujahideen', 'Jagrata Muslim Janata Bangladesh', 'Hizb-ut Tahrir', 'Motiur Rahman Nizami', 'Abul Kalam Azad', 'Ghulam Azam', 'Abdul Kader Mullah', 'Mir Quasem Ali', 'Abdus Subhan', 'Ansarullah Bangla Team', 'Shia Muslims', 'Ali Ahsan Mohammad Mujahid', 'Salahuddin Quader Chowdhury', 'atheists', 'Ahmed Rajib Haider', 'Rohingya', 'refugee']


# Check if the two entites might share a common substring
def findCommonSubstring(sub, obj):
    if sub in obj or obj in sub:
        return True
    else:
        return False


# Format date which conforms with the timestamp in indirect_network.csv
def dateFormatter(year, month, day):
    if len(month) == 1:
        month = "0" + month
    if len(day) == 1:
        day = "0" + day

    date = year + "-" + month + "-" + day
    return date


subject_objects_for_ef_idf = []

subject_objects = []

subject_objects_with_timestamps = []

# DailyStarSpecific
edgeOccurencesEachDay = []
days = []
previousDay = ''
hartalDates = []
hartalIndicator = []
# Ignore the first row
next(csvreader)

# Find out edge occurences
for row in csvreader:
    # If the subject is a political entity and the subject is not talking to himself
    if (row[2] in keywords or row[4] in keywords) and row[2] != row[4]:

        sub = (row[2])
        obj = (row[4])
        newsID = (row[0])
        """dateWithoutTime = date[:10]"""
        date = (row[1]).replace("\n", "")

        # Get only 2013 data since only 2013 hartal data is available
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
            days.append(datetime.datetime(
                int(year), int(month), int(day), 0, 0))
            previousDay = date

# Find the number of occurences of each tuple
counter = Counter(subject_objects)

# Convert the counter into a usable array
numberOfTupleOccurences = sorted(counter.items())


count = [0]
currentCount = 0
# Output


counterTimestamp = Counter(subject_objects_with_timestamps)
numberOfTupleOccurencesWithTimestamp = sorted(
    counterTimestamp.items(), key=lambda x: x[0][2])
# To get the time ranges when events occured
eventsTimeArray = []
eventsArray = []
startEdgeLength = edgeOccurencesEachDay[0]
startDate = days[0]

for x in range(len(edgeOccurencesEachDay)):
    if startEdgeLength == 0:
        # setting the threshold for edge occurences
        if edgeOccurencesEachDay[x] < 20:
            continue
        else:
            startEdgeLength = edgeOccurencesEachDay[x]
            startDate = days[x]

    if edgeOccurencesEachDay[x] <= startEdgeLength:
        dateDifference = (days[x] - startDate).days
        # setting date interval
        if dateDifference > 15:
            eventsTimeArray.append(startDate.strftime(
                "%Y-%m-%d") + " " + days[x].strftime("%Y-%m-%d") + " " + str(dateDifference))
            eventsArray.append(str(startEdgeLength) + " " +
                               str(edgeOccurencesEachDay[x]))
            if (x + 1) < len(edgeOccurencesEachDay):
                # startEdgeLength = edgeOccurencesEachDay[x+1]
                startEdgeLength = 0
                startDate = days[x + 1]

# print(len(eventsArray))

edgeOccurencesInTimeRange = {}
for i in range(len(eventsTimeArray)):
    startDate = eventsTimeArray[i].split()[0]
    endDate = eventsTimeArray[i].split()[1]
    timerange = False
    keywordsInTimeRange = []
    for x in numberOfTupleOccurencesWithTimestamp:
        if startDate in x[0][2]:
            timerange = True

        if timerange:
            keywordsInTimeRange.append(x[0][0])
            keywordsInTimeRange.append(x[0][1])

        if endDate in x[0][2]:
            break
    # print(startDate)
    # print(sorted(Counter(keywordsInTimeRange).items()))
    # print(endDate)

# dailystarspecific
plt.bar(days, height=scipy.fftpack.fft(edgeOccurencesEachDay), width=1)
# plt.plot(days,edgeOccurencesEachDay)
plt.xlabel('Year')
plt.ylabel('Total number of edges per day')


# next(csvHartalReader)
# for row in csvHartalReader:

#     year = row[0]
#     month = row[1]
#     day = row[2]

#     if int(year) < 2007:
#         continue

#     hartalDates.append(datetime.datetime(int(year), int(month), int(day), 0, 0))
#     hartalIndicator.append(20)

# plt.bar(hartalDates, height=hartalIndicator, width=1)

csvfile.close()
# csvHartalFile.close()


plt.show()
