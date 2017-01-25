import re
import itertools

PERSON = []
LOCATION = []
ORGANIZATION = []
ALLENTITIES = []

prev_tag = ''

def append_to_array(word,tag):
    if tag=='PERSON':
        PERSON.append(word)
    if tag=='LOCATION':
        LOCATION.append(word)
    if tag=='ORGANIZATION':
        ORGANIZATION.append(word)
    return

def append_to_last_element(word,tag):
    #print("INSIDE METHOD")

    if tag=='PERSON':
        #print (word)
        newWord = PERSON.pop()+" "+word
        PERSON.append(newWord)
        #print (PERSON)
    if tag=='LOCATION':
        newWord = LOCATION.pop()+" "+word
        LOCATION.append(newWord)
    if tag=='ORGANIZATION':
        newWord = ORGANIZATION.pop()+" "+word
        ORGANIZATION.append(newWord)
    return

def remove_duplicate_elements():
    global PERSON,LOCATION,ORGANIZATION
    PERSON = list(set(PERSON))
    LOCATION = list(set(LOCATION))
    ORGANIZATION = list(set(ORGANIZATION))

def insert_in_cv(formatted_line):
   # print (formatted_line)
   # for subset in itertools.combinations(PERSON, 2):
   #     print (subset)
   # global PERSON
   # PERSON = []
    if len(ALLENTITIES)<2:
       return

    if len(ALLENTITIES) == 2:

        with open("newfile.csv", "a") as my_output:
            my_output.write(ALLENTITIES[0]+"\t"+ALLENTITIES[1]+"\t"+formatted_line+"\n")
        return

    else:
        for subset in itertools.combinations(ALLENTITIES, 2):
            with open("newfile.csv", "a") as my_output:
                my_output.write(subset[0]+"\t"+subset[1]+"\t"+formatted_line+"\n")
        return




def clear_prev_tag():
    global prev_tag
    prev_tag = ''
    return

with open('taggednew.txt', 'r') as f:

    for line in f.readlines():
        #print (line)
        sline = line.split()
        #print(sline)
        for word in sline: #iterate through the words in a sentence
            matched_obj = re.match(r'^(.*)/(.*)$',word)
            current_word = matched_obj.group(1)
            current_tag = matched_obj.group(2)
            #print(current_word)


            if re.match(r'[!#$%&()*+,-./:;<=>?@[\]^_`{|}~]',current_word[len(current_word)-1]):
                if current_tag == prev_tag:  #If the word has an attached punctuation and the word before it has same tag, they are chunked
                    append_to_last_element(current_word[:-1],current_tag)
                else: #else they are appended as separate elements in separate lists
                    append_to_array(current_word[:-1],current_tag)

                clear_prev_tag()
                continue


            if re.match(r'^.*/(ORGANIZATION|LOCATION|PERSON)$',word):#If tag is any of these 3

                #print (word)
                if prev_tag == '':  #If no previous word had the above three tags
                    append_to_array(current_word,current_tag)
                    prev_tag = current_tag
                    #print (PERSON)
                    continue

                else:
                    if current_tag == prev_tag:
                        append_to_last_element(current_word,current_tag)
                        #print (PERSON)
                        continue

                    else:

                       append_to_array(current_word,current_tag)
                       clear_prev_tag()
                       continue

            else:
                if prev_tag != '':
                    clear_prev_tag()
                    continue

        remove_duplicate_elements()
        ALLENTITIES.extend(PERSON)
        ALLENTITIES.extend(ORGANIZATION)
        ALLENTITIES.extend(LOCATION)

        formatted_line = (line.replace("/ORGANIZATION","").replace("/PERSON","").replace("/LOCATION","").replace("/O","").replace(",",""))
        insert_in_cv(formatted_line)

        ALLENTITIES = []
        PERSON = []
        ORGANIZATION = []
        LOCATION = []




remove_duplicate_elements()  #If there are duplicate elements in the list, they will be removed. However the order will change too.

#print(PERSON)
#print(LOCATION)
#print(ORGANIZATION)




