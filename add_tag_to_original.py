import csv
import codecs

with codecs.open('dhaka_tribune.csv', 'r', encoding='utf-8', errors='ignore') as input, open('indexed_dhaka_tribune.csv', 'w') as output:
    reader = csv.reader(input, delimiter=',')
    writer = csv.writer(output, delimiter=',')

    all = []
    row = reader
    # row.insert(0, 'ID')
    #all.append(row)
    for k, row in enumerate(reader):
        all.append([str(k)] + row)
    writer.writerows(all)
