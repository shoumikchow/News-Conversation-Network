import re
import csv
import itertools


location_tags = []
organization_tags = []
person_tags = []
subjects = []
objects = []


def find_all_quoted_sentences(line):
    matches = re.findall(r'\"(.+?)\"', line)
    return matches


def get_sentence_without_quotations(quoted_sentences, line):
    new_line = line
    for sentence in quoted_sentences:
        new_line = new_line.replace(sentence, '')
        new_line = new_line.replace('"', '')
    return new_line.strip()


def convert_tags_string_to_list(tags):
    if tags == '[]':
        return []
    else:
        # tags_list =  ((tags.replace('[','').replace(']','').replace('\'','').replace(',',' ')).split())
        tags_list = ((tags.replace('[', '').replace(']', '').replace('\'', '')).split(', '))
        # print (tags_list)
        return tags_list


def remove_duplicate_elements():
    global subjects, objects
    subjects = list(set(subjects))
    objects = list(set(objects))


def insert_in_csv(news_id, timestamp, line, original_tags, naive_tags, keywords_from_csv, subjects, objects):

    line = line.replace(",", " ")
    # print(subjects)
    # print (line)

    if len(subjects) >= 1 and len(objects) >= 1:

        for instance in itertools.product(subjects, objects):

            with open("./Scraped data/network_direct_improvised.csv", "a", newline='') as my_output:
                writer = csv.writer(my_output)
                writer.writerow([news_id, timestamp, instance[0], get_tag(instance[0]), instance[1], get_tag(instance[1]), line, original_tags, naive_tags, keywords_from_csv])

    return


def get_tag(word):
    if word in person_tags:
        return "PERSON"
    elif word in location_tags:
        return "LOCATION"
    elif word in organization_tags:
        return "ORGANIZATION"


def empty_all_lists():
    global location_tags, organization_tags, person_tags, subjects, objects
    location_tags = []
    organization_tags = []
    person_tags = []
    subjects = []
    objects = []
    return


keywords = ['said', 'told', 'asked', 'speak', 'say', 'tell', 'spoke', 'added', 'alleged', 'declare']
counter = 0
rowCounter = 2
# with open("quotations_and_speeches_v2.csv", "r") as f:
with open("./Scraped data/quotations_and_speeches_v2.0.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)

    with open("./Scraped data/network_direct_improvised.csv", "a", newline='') as my_output:
        writer = csv.writer(my_output)
        writer.writerow(["original_id", "timestamp", "subject", "subject_tag", "object", "object_tag", "text", "original_tags", "naive_tags", "keywords"])

    for row in reader:
        if counter == 0:
            counter += 1
            continue

        if row[2] == '' or "\n" in row[2]:
            continue

        if re.search(r'[\'\"].[\'\"]', row[3]) or re.search(r'[\'\"].[\'\"]', row[4]) or re.search(r'[\'\"].[\'\"]', row[5]):
            continue

        news_id = row[0]
        timestamp = row[1]
        line = row[2]

        location_tags = convert_tags_string_to_list(row[3])
        organization_tags = convert_tags_string_to_list(row[4])
        person_tags = convert_tags_string_to_list(row[5])
        tags = location_tags + organization_tags + person_tags
        # print ("Here are tags")
        # print (tags)
        original_tag = row[6]
        naive_tag = row[7]
        keywords_from_csv = row[8]

        # print(original_tag)

        # For sentences with quotations
        if find_all_quoted_sentences(line):

            quoted_sentences = (find_all_quoted_sentences(line))
            new_line = ' '.join(quoted_sentences)
            for word in tags:
                if word in new_line:
                    objects.append(word)
            # print("Here are objects")
            # print (objects)

            sentence_without_quotations = (get_sentence_without_quotations(quoted_sentences, line))
            # print (sentence_without_quotations)
            for word in tags:
                if word in sentence_without_quotations:
                    subjects.append(word)
            # print ("quotation program line ended")

        # For sentences without quotations
        else:
            sline = line.split()

            for word in keywords:
                if word in sline:
                    lim = sline.index(word)
                    left = ' '.join(sline[:lim])
                    right = ' '.join(sline[lim + 1:])
                    if len(left) <= len(right):

                        for word in tags:
                            if word in left:
                                subjects.append(word)
                            if word in right:
                                objects.append(word)
                    else:
                        for word in tags:
                            if word in right:
                                subjects.append(word)
                            if word in left:
                                objects.append(word)

        # print ("here are subjects and objects")
        # print (subjects)
        # print (objects)
        remove_duplicate_elements()
        insert_in_csv(news_id, timestamp, line, original_tag,
                      naive_tag, keywords_from_csv, subjects, objects)

        empty_all_lists()

        # print(rowCounter)
        rowCounter += 1


# Wrote code for checking quoted, non-quoted statements
# The code for unquoted statements is not accurate. We are assuming the part with the lower word count has the subject. Need to find alternatives
# The tags in the csv file are in string representation. Needed to write code to convert them to list representations and then merge them into a new tags list.
