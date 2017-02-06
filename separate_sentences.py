import csv, nltk.data, re, ast

tokenizer = nltk.data.load('nltk:tokenizers/punkt/english.pickle')

def find_quotes(text):
    regx = re.compile('(?!\Z)'
                  '[. \n\r]*'
                  '('
                    '(?:[^."]*"[^"]*")+'
                    '[^."]*'
                    '(?:\.|\Z)'
                  ')')

    conversational_words = ['said', 'told', 'asked', 'speak', 'say', 'tell', 'spoke', 'add']
    for el in regx.findall(text):
        if any(n in el for n in conversational_words):
            return el

def entities_in_text(just_text, loc, org, pers):
    entities = [[],[],[],[]]
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


    if entities is not None:
        return just_text, entities



# entity[0] is location, entity[1] is org, entity[2] is pers, entity[3] is text

with open("/home/shoumik/Documents/Kolpokoushol/Scraped datas/new_scraped_without_weird_symbols.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:

        oid = row[0]
        time = row[24]
        locations = row[12]
        organizations = row[16]
        persons = row[20]
        news_text = row[26]

        o_tags = row[23]
        naive_tags = row[8]
        keywords = row[5]

        o_tags = ast.literal_eval(o_tags)
        naive_tags = ast.literal_eval(naive_tags)
        keywords = ast.literal_eval(keywords)

        quotes = find_quotes(news_text)
        entities = [[],[],[]]
        text = ""
        if quotes is not None:
            text, entities = entities_in_text(quotes, locations, organizations, persons)


            #print (entities)

# entity[0] is location, entity[1] is org, entity[2] is pers

        if entities is not None and len(entities[0]+entities[1]+entities[2])>=2:
            with open ("/home/shoumik/Documents/Kolpokoushol/Scraped datas/quotations and speeches.csv","a") as out:
                            writer = csv.writer(out)
                            writer.writerow([oid, text, entities[0], entities[1], entities[2], o_tags, naive_tags, keywords])

            #print(quotes, entities[0], entities[1], entities[2])

        period_delimited_list = tokenizer.tokenize(news_text)
        conversational_words = ['said', 'told', 'asked', 'speak', 'say', 'tell', 'spoke', 'add']
        for sentence in period_delimited_list:
            if any(word in sentence for word in conversational_words):
                if quotes is not None:
                    sentence, entities = entities_in_text(sentence, locations, organizations, persons)
                    if sentence not in quotes and entities is not None and len(entities[0]+entities[1]+entities[2])>=2:
                        with open ("/home/shoumik/Documents/Kolpokoushol/Scraped datas/quotations and speeches.csv","a") as out:
                            writer = csv.writer(out)
                            writer.writerow([oid, sentence, entities[0], entities[1], entities[2], o_tags, naive_tags, keywords])





