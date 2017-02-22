import csv
import itertools
import codecs

location_tags = []
organization_tags = []
person_tags = []


def find_all_quoted_sentences(line):
    matches=re.findall(r'\"(.+?)\"',line)
    return matches

def get_sentence_without_quotations(quoted_sentences, line):
    new_line = line
    for sentence in quoted_sentences:
        new_line = new_line.replace(sentence,'')
        new_line = new_line.replace('"','')
    return new_line.strip()

def convert_tags_string_to_list(tags):
    if tags == '[]':
        return []
    else:
        #tags_list =  ((tags.replace('[','').replace(']','').replace('\'','').replace(',',' ')).split())
        tags_list =  ((tags.replace('[','').replace(']','').replace('\'','')).split(', '))
        #print (tags_list)
        return tags_list


def insert_in_csv(news_id, timestamp, line, tags, original_tags, naive_tags, keywords_from_csv):
    
    line = line.replace(","," ")
    #print (line)

        
    for instance in itertools.combinations(tags, 2):

        with open("latest_output.csv", "a", newline='') as my_output:
            writer = csv.writer(my_output)
            writer.writerow([news_id, timestamp, instance[0] , get_tag(instance[0]), instance[1], get_tag(instance[1]), line, original_tags, naive_tags, keywords_from_csv])

    return


def get_tag(word):
    if word in person_tags:
        return "PERSON"
    elif word in location_tags:
        return "LOCATION"
    elif word in organization_tags:
        return "ORGANIZATION"

def empty_all_lists():
    global location_tags,organization_tags,person_tags,subjects,objects
    location_tags = []
    organization_tags = []
    person_tags = []
    subjects = []
    objects = []
    return

counter = 0
#with open("quotations_and_speeches_v2.csv", "r") as f:
with codecs.open('quotations_and_speeches_v2.csv', 'r', encoding='utf-8', errors='ignore') as f:
	reader = csv.reader(f)
	for row in reader:
		if counter == 0:        
			counter += 1
			continue 

		if row[2] == '' or "\n" in row[2]:
			continue

		news_id = row[0]
		timestamp = row[1]
		line = row[2]
        

		location_tags = convert_tags_string_to_list(row[3])
		organization_tags = convert_tags_string_to_list(row[4])
		person_tags = convert_tags_string_to_list(row[5])
		tags = location_tags + organization_tags + person_tags
		subjects = list(set(tags))
        #print ("Here are tags")
        #print (tags)
		original_tag = row[6]
		naive_tag = row[7]
		keywords_from_csv = row[8]

		print (tags)
		print (counter)
		counter += 1
		insert_in_csv(news_id, timestamp, line, tags, original_tag,
                      naive_tag, keywords_from_csv)




