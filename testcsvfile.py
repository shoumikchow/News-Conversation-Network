import nltk.data
import csv
 
counter = 0
tokenizer = nltk.data.load('nltk:tokenizers/punkt/english.pickle')
 
with open('dhaka_tribune.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if counter == 1:
            break
        #print (row[0])   <--Original text
        no_slashn_text = row[0][1:].replace('\\n',' ')  #  <--converted text
        period_delimited_list = tokenizer.tokenize(no_slashn_text)  # <--delimited according to periods
 
        for sentence in period_delimited_list:
            if 'said' in sentence or 'says' in sentence or 'told' in sentence or 'tells' in sentence or 'asked' in sentence :
                with open('output.txt','a') as my_output:
                    my_output.write(sentence+"\n")

        with open('output.txt','a') as my_output:
            my_output.write("\n"+"Timestamp: "+row[4]+"\n")
            my_output.write("\n"+"Category: "+row[3][2:-2]+"\n")
            my_output.write("\n")
 
 
        counter += 1
