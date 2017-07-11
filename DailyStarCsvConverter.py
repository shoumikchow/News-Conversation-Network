import csv
import uuid
import re
import itertools

def insertInCsv(uniqueNewsID,newsDate,line,allEntities):

    #Take combination pairs
    for instance in itertools.combinations(allEntities, 2):
        #print (instance)
        with open("DailyStar.csv", "a") as my_output:
            writer = csv.writer(my_output)
            writer.writerow([uniqueNewsID, newsDate, instance[0], getTag(instance[0]), instance[1], getTag(instance[1]), line])



def populateEntityArray(word,entityTypeArray):
    
    # if there's a word like Np/cl/ORGANIZATION, split() will give error
    [entity,tag] = word.rsplit("/",1)
    global previousTag

    #If first time encountering the tag, append to array
    if tag != previousTag:
        entityTypeArray.append(entity)

    print (entityTypeArray)
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
    count = 1
    #Read each line in the txt file
    for line in content:
        print ("Line number is "+str(count))

        uniqueNewsID = uuid.uuid4()

        if re.search(r'^\d\d\d\d-\d\d-\d\d$',line):
            newsDate = line
            count += 1
            continue

        count += 1
        #print("This is the line "+line)

        #Separate each word in the line and place them in the array
        arr = line.split()

        neatSentence = ''
        #Read each word in the line
        for index,word in enumerate(arr):

            if word == '//O' or word == '//ORGANIZATION' or word == '//PERSON' or word == '//LOCATION':
                continue

            #if the entity is an organization
            if re.search(r'[\dA-z]*\/ORGANIZATION',word):
                populateEntityArray(word, organizations)

            #if the entity is a location
            elif re.search(r'[\dA-z]*\/LOCATION',word):
                populateEntityArray(word, locations)

            #if the entity is a person
            elif re.search(r'[\dA-z]*\/PERSON',word):
                populateEntityArray(word, persons)

            elif re.search(r'[\dA-z]*\/O',word):
                previousTag = ''

            neatSentence += word.split("/")[0] + ' '
        
        allEntities = organizations + persons + locations
        insertInCsv(uniqueNewsID,newsDate,neatSentence.strip(),allEntities)
        emptyAllLists()
        """print (organizations)
        print (persons)
        print (locations)"""

          