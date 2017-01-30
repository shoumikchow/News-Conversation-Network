import csv

in_file = open('newfile_final).csv', 'rb')
output = open('test.csv', 'wb')
writer = csv.writer(output)
for row in csv.reader(in_file):
    if any(row):
        writer.writerow(row)
in_file.close()
output.close()