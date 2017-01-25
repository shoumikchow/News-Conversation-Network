import nltk.data
import csv
import codecs

counter = 0
tokenizer = nltk.data.load('nltk:tokenizers/punkt/english.pickle')

with codecs.open('dhaka_tribune.csv', 'r', encoding='utf-8', errors='ignore') as f:
    reader = csv.reader(f)
    for row in reader:
        # if counter == 200:
        #    break
        # print (row[0])   <--Original text
        no_slashn_text = row[0][1:].replace('\\n', ' ')  # <--converted text
        # <--delimited according to periods
        period_delimited_list = tokenizer.tokenize(no_slashn_text)
        conversational_words = ['said', 'told', 'asked', 'speak', 'say', 'tell', 'spoke']
        for sentence in period_delimited_list:
            # if 'said' in sentence or 'told' in sentence or 'asked' in
            # sentence:
            if any(word in sentence for word in conversational_words):
                with open('output.txt', 'a') as my_output:
                    my_output.write(sentence+"\n")
        with open('output.txt', 'a') as blank_line:
            blank_line.write("\n")
        #counter += 1
