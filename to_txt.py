import nltk.data
import csv
import codecs

# counter = 0
tokenizer = nltk.data.load('nltk:tokenizers/punkt/english.pickle')

with codecs.open('indexed_dhaka_tribune.csv', 'r', encoding='utf-8', errors='ignore') as f:
    reader = csv.reader(f)
    for row in reader:
        # if counter == 10000:
        #    break
        no_slashn_text = row[1][1:].replace('\\n', ' ')  # <--converted text
        period_delimited_list = tokenizer.tokenize(no_slashn_text)
        conversational_words = ['said', 'told', 'asked', 'speak', 'say', 'tell', 'spoke']
        for sentence in period_delimited_list:
            if any(word in sentence for word in conversational_words):
                with open('output.txt', 'a') as my_output:
                    my_output.write(row[0]+" "+row[5][:11]+row[5][12:]+" "+sentence+"\n")
        with open('output.txt', 'a') as blank_line:
            blank_line.write("\n")
        # counter += 1
