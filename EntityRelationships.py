import csv
import nltk.data
import itertools
from nltk.tag import StanfordNERTagger
from itertools import groupby



def check_sequence(org, sentence):
    # org = list(org)
    # combined = ()
    # new_word = ''
    # index = 0
    # sentence = sentence.split()
    # for word in sentence:
    #     if word in org:
    #         new_word+=word+" "
    #         for next_word_counter in range(index+1, len(sentence)):
    #             if sentence[next_word_counter] in org:

    #                 new_word+=(sentence[next_word_counter])+" "
    #                 print(new_word)
    #                 for i in range(0,len(org)):
    #                     if org[i] == sentence[next_word_counter]:
    #                         org.remove(org[i])
    #                         break

    #                 #print (new_word)
    #             else:
    #                 combined+=(new_word,)
    #                 new_word=''
    #                 break
    #     index = index + 1
    combined = ()
    for tag, chunk in groupby(org,lambda x:x[1]):
        if tag != 'O':
           chunked_entity =(" ".join(w for w, t in chunk))
           if chunked_entity is not None:
                combined+=(chunked_entity,)
    return combined


org = ("Dhaka", "Tribune", "Dhaka", "North", "City", "Corporation","Herald", "Tribune")
sentence = "When the Dhaka Tribune contacted Md Nayeb Ali living in New York, Boston, zonal executive officer at Dhaka North City Corporation (DNCC) for Mirpur and at Herald Tribune Pallabi, he said birth registration was not his responsibility"

org = [('Dhaka', 'ORGANIZATION'),
('Tribune', 'ORGANIZATION'),
('bla','O'),
('Dhaka', 'ORGANIZATION'),
('North', 'ORGANIZATION'),
('City', 'ORGANIZATION'),
('Corporation', 'ORGANIZATION'),
('bla','O'),
('New', 'ORGANIZATION'),
('York', 'ORGANIZATION'),
('Boston', 'ORGANIZATION'),
('bla','O')]

print(check_sequence(org, sentence))

"""
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

        #TODO: Make tokenizer work!
        period_delimited_list = row[0].split('.')
        #period_delimited_list = tokenizer.tokenize(row[0])

        # print('This is original info')
        # print (row[0])
        # print('This is delimited list')
        #print (period_delimited_list)
        counter = counter + 1



        for sentence in period_delimited_list:
            if 'said' in sentence:
                print (sentence)
                tagged = st.tag(sentence.split())
                org = ()
                for tags in tagged:
                    if 'PERSON' in tags or 'ORGANIZATION' in tags or 'LOCATION' in tags :
                        if tags[1] == "ORGANIZATION":
                            org += (tags[0],)
                print(check_sequence(org, sentence))
                #print(org)


        #print (row)

"""
