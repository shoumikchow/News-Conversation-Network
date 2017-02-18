import csv
import ast
with open("/home/shoumik/Documents/Kolpokoushol/Scraped data/quotations and speeches v1.1.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    with open("/home/shoumik/Documents/Kolpokoushol/Scraped data/quotations and speeches v1.1.csv", "a") as out:
        writer = csv.writer(out)
        writer.writerow(["original_id", "timestamp", "text", "locations", "organizations", "persons", "original_tag", "naive_tag", "keywords"])

    article = []
    text = ""
    conversational_words = ['said', 'told', 'asked', 'speak', 'say', 'tell', 'spoke', 'add', 'alleged', 'declare']
    for row in reader:

        loc = ast.literal_eval(row[3])
        org = ast.literal_eval(row[4])
        per = ast.literal_eval(row[5])
        new_loc = []
        new_org = []
        new_per = []
        if "\n" in row[2]:
            article = row[2].split("\n")
            # print(article)
            for i in article:
                if "\"" in i or any(word in i for word in conversational_words):
                    text = i
                    for j in loc:
                        if j in i:
                            new_loc.append(j)
                    for k in org:
                        if k in i:
                            new_org.append(k)
                    for l in per:
                        if l in i:
                            new_per.append(l)

            with open("/home/shoumik/Documents/Kolpokoushol/Scraped data/quotations and speeches v1.2.csv", "a") as out:
                writer = csv.writer(out)
                if len(new_loc + new_org + new_per) >= 2:
                    writer.writerow([row[0], row[1], text, new_loc, new_org, new_per, row[6], row[7], row[8]])
        else:
            with open("/home/shoumik/Documents/Kolpokoushol/Scraped data/quotations and speeches v1.2.csv", "a") as out:
                writer = csv.writer(out)
                writer.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]])
