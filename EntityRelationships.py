import csv
import nltk.data
from nltk.tag import StanfordNERTagger



tokenizer = nltk.data.load('nltk:tokenizers/punkt/english.pickle')
st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz')
with open('dhaka_tribune.csv', 'r') as f:
    reader = csv.reader(f)
    counter = 0
    rownum = 0
    for row in reader:
        if counter == 1:
            break

        #First cell value of each row/article
    

        #period_delimited_list = row[0].split('.')
        period_delimited_list = tokenizer.tokenize(row[0])

        print('This is original info')
        print (row[0])
        print('This is delimited list')
        print (period_delimited_list)
        counter = counter + 1
        end()


        for sentence in period_delimited_list:
            if 'said' in sentence:
                print (sentence)
                tagged = st.tag(sentence.split())
                for tags in tagged:
                    if 'PERSON' in tags or 'ORGANIZATION' in tags or 'LOCATION' in tags :
                        print (tags)

                    
        #print (row)
        
