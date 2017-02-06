import csv
import codecs

with codecs.open('test_penultimate.csv', 'r', encoding='utf-8', errors='ignore') as infile:
    reader = csv.reader(infile)

    for row in reader:
    	with open('final.csv','a') as outfile:
    		outfile.write(row[0]+","+row[1]+":00,"+row[2]+","+row[3]+","+row[4]+","+row[5]+","+row[6]+"\n")

