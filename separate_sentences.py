import csv
import nltk.data
import re
import ast

tokenizer = nltk.data.load('nltk:tokenizers/punkt/english.pickle')


def fix_quotes(line):
    line = line

    if "\n\n\n\n" in line:
        line = line.replace("\n\n\n", "\n")

    if "\n" in line:
        arr = line.split("\n")
        i = 0
        prev_sentence_has_double_quote = False
        while i < len(arr):
            if arr[i] == "":
                i += 2
                continue

            # if '"' in arr[i]:
            if arr[i].count("\"") == 1:
                if prev_sentence_has_double_quote is False:
                    prev_sentence_has_double_quote = True
                    i += 2
                    continue

            if arr[i][0] == '"':
                if prev_sentence_has_double_quote is True:
                    s = list(arr[i])
                    s[0] = ' '
                    arr[i] = "".join(s)
                    arr[i - 2:i + 1] = [''.join(arr[i - 2:i + 1])]
                    prev_sentence_has_double_quote = False
                    i += 2
                    continue

            if prev_sentence_has_double_quote is True:
                prev_sentence_has_double_quote = False
            i += 2

        for i in reversed(arr):
            if i == " " or i == '':
                arr.pop()
            else:
                break

        # Final output being placed in str
        str = ""
        for i in range(0, len(arr)):
            if(arr[i] == ' ' or arr[i] == ''):
                str += "\n" + "\n"
            else:
                str += arr[i]

        return(str)


def find_quotes(text):

    regx = re.compile('([^\.\?\!]*?".+?".*?[\.\?\!\)\]\}])|([^\.\?\!]*?".+?[\.\?\!\)\]\}]")')

    array = (regx.findall(text))

    quoted_sentence = []
    for elem in array:
        if elem[0] == '':
            quoted_sentence.append(elem[1].strip())
        elif elem[1] == '':
            quoted_sentence.append(elem[0].strip())

    return quoted_sentence


def entities_in_text(just_text, loc, org, pers):
    entities = [[], [], [], []]
    try:
        loc = ast.literal_eval(loc)
        org = ast.literal_eval(org)
        pers = ast.literal_eval(pers)
    except:
        pass
    if any(word in just_text for word in loc) or any(word in just_text for word in org) or any(word in just_text for word in pers):

        for i in loc:
            if i in just_text:
                entities[0].append(i)
        for j in org:
            if j in just_text:
                entities[1].append(j)
        for k in pers:
            if k in just_text:
                entities[2].append(k)

    if entities:
        return just_text, entities


# entity[0] is location, entity[1] is org, entity[2] is pers

with open("/home/shoumik/Documents/Kolpokoushol/Scraped data/final v2.1.csv", "r") as file:
    conversational_words = ['said', 'told', 'asked', 'speak', 'say', 'tell', 'spoke', 'add', 'alleged', 'declare']
    counter = 0
    reader = csv.reader(file)

    with open("/home/shoumik/Documents/Kolpokoushol/Scraped data/quotations and speeches v1.1.csv", "a") as out:
        writer = csv.writer(out)
        writer.writerow(["original_id", "timestamp", "text", "locations", "organization", "person", "original_tags", "naive_tags", "keywords"])

    for row in reader:
        counter += 1
        try:
            oid = row[0]
            time = row[24]
            locations = row[12]
            organizations = row[16]
            persons = row[20]
            news_text = ""
            if row[26]:

                news_text = fix_quotes(row[26])
                o_tags = row[23]
                naive_tags = row[8]
                keywords = row[5]

                o_tags = ast.literal_eval(o_tags)
                naive_tags = ast.literal_eval(naive_tags)
                keywords = ast.literal_eval(keywords)

                quotes = find_quotes(news_text)

                for quote in quotes:

                    entities = [[], [], []]
                    text = ""
                    if quote:
                        text, entities = entities_in_text(
                            quote, locations, organizations, persons)

        # entity[0] is location, entity[1] is org, entity[2] is pers

                    if entities and len(entities[0] + entities[1] + entities[2]) >= 2:
                        with open("/home/shoumik/Documents/Kolpokoushol/Scraped data/quotations and speeches v1.1.csv", "a") as out:
                            writer = csv.writer(out)
                            writer.writerow([oid, time, text, entities[0], entities[1], entities[2], o_tags, naive_tags, keywords])

                period_delimited_list = tokenizer.tokenize(news_text)

                for sentence in period_delimited_list:
                    if any(word in sentence for word in conversational_words):
                        if quotes:
                            sentence, entities = entities_in_text(
                                sentence, locations, organizations, persons)
                            if not any(sentence in s for s in quotes) and entities and len(entities[0] + entities[1] + entities[2]) >= 2:
                                with open("/home/shoumik/Documents/Kolpokoushol/Scraped data/quotations and speeches v1.1.csv", "a") as out:
                                    writer = csv.writer(out)
                                    writer.writerow([oid, time, sentence, entities[0], entities[1], entities[2], o_tags, naive_tags, keywords])

        except:
            print(counter, row[26])
            # pass
