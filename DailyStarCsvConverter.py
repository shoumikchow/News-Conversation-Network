import csv
import uuid
import re
import itertools

def insertInCsv(uniqueNewsID,newsDate,line,allEntities):

    #Take combination pairs
    for instance in itertools.combinations(allEntities, 2):
        print (instance)
        with open("DailyStar.csv", "a") as my_output:
            writer = csv.writer(my_output)
            writer.writerow([uniqueNewsID, newsDate, instance[0], getTag(instance[0]), instance[1], getTag(instance[1]), line])



def populateEntityArray(word,entityTypeArray):
    
    [entity,tag] = word.split("/")
    global previousTag

    #If first time encountering the tag, append to array
    if previousTag == '':
        entityTypeArray.append(entity)

    #If previous word also had the same tag, assume current entity and previous one are same
    if previousTag == tag:
        entityTypeArray[-1] = entityTypeArray[-1]+" "+entity
    
    previousTag = tag



def getTag(word):
    if word in persons:
        return "PERSON"
    elif word in locations:
        return "LOCATION"
    elif word in organizations:
        return "ORGANIZATION"



def emptyAllLists():
    global locations, organizations, persons, allEntities
    locations = []
    organizations = []
    persons = []
    allEntities = []
    return



persons = []
organizations = []
locations = []
allEntities = []

previousTag = ''
newsDate = ''
uniqueNewsID = ''

#Open raw dailyStar news text
with open('DailyStar.txt') as f:
    content = f.readlines()
    count = 0
    #Read each line in the txt file
    for line in content:
        uniqueNewsID = uuid.uuid4()
        if count == 20:
            break

        uniqueNewsID = uuid.uuid4()

        if re.search(r'^\d\d\d\d-\d\d-\d\d$',line):
            newsDate = line
            
            continue

        count += 1
        print("This is the line "+line)
        #Separate each word in the line and place them in the array
        arr = line.split()

        #Read each word in the line
        for word in arr:

            #if the entity is an organization
            if re.search(r'[\dA-z]*\/ORGANIZATION',word):
                populateEntityArray(word, organizations)

            elif re.search(r'[\dA-z]*\/LOCATION',word):
                populateEntityArray(word, locations)

            elif re.search(r'[\dA-z]*\/PERSON',word):
                populateEntityArray(word, persons)

            elif re.search(r'[\dA-z]*\/O',word):
                previousTag = ''
        
        allEntities = organizations + persons + locations
        insertInCsv(uniqueNewsID,newsDate,line,allEntities)
        emptyAllLists()
        """print (organizations)
        print (persons)
        print (locations)"""

          