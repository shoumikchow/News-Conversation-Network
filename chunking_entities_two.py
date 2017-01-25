import re
import itertools

PERSON = []
LOCATION = []
ORGANIZATION = []
ALLENTITIES = []
TAGSINSENTENCE = {}

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

def insert_in_cv(formatted_line,sline):

    if len(ALLENTITIES)<2:
       return

    if len(ALLENTITIES) == 2:
        
        with open("newfile_final.csv", "a") as my_output:
            my_output.write(sline[0][:-2]+","+sline[1][:-2]+" "+sline[2][:-2]+","+ALLENTITIES[0]+","+get_tag(ALLENTITIES[0])+","+ALLENTITIES[1]+","+get_tag(ALLENTITIES[1])+","+formatted_line+"\n")
        return

    else:
        for subset in itertools.combinations(ALLENTITIES, 2):
            with open("newfile_final.csv", "a") as my_output:
                my_output.write(sline[0][:-2]+","+sline[1][:-2]+" "+sline[2][:-2]+","+subset[0]+","+get_tag(subset[0])+","+subset[1]+","+get_tag(subset[1])+","+formatted_line+"\n")
        return

def get_tag(word):
    if word in PERSON:
        return "PERSON"
    elif word in LOCATION:
        return "LOCATION"
    elif word in ORGANIZATION:
        return "ORGANIZATION"
    

def clear_prev_tag():
    global prev_tag
    prev_tag = ''
    return
    
with open('tagged_1.txt', 'r') as f:
    
    #count = 0
    for line in f.readlines():
        #print(count)
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
        formatted_line = ' '.join(map(str,formatted_line.split(' ', 3)[3:]))
        insert_in_cv(formatted_line, sline)

        ALLENTITIES = []
        PERSON = []
        ORGANIZATION = []
        LOCATION = []
        #count += 1
        

                
            

remove_duplicate_elements()  #If there are duplicate elements in the list, they will be removed. However the order will change too.

#print(PERSON)
#print(LOCATION)
#print(ORGANIZATION)        
                        
                
                    
                        
