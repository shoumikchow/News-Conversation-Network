import csv
with open("/home/shoumik/Documents/Kolpokoushol/Scraped data/final v2.0.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        oid = row[0]
        is_negative = row[1]
        news_crawled_date = row[2]
        news_headline = row[3].replace("‘", "").replace("’", "").replace("“", "\"").replace("”", "\"").replace("–", "-")
        news_image_url = row[4]
        news_keyword = row[5]
        news_location = row[6]
        news_ml_tags = row[7]
        news_naive_tags = row[8]
        news_ner_tags__dates = row[9]
        news_ner_tags__dates_unique = row[10]
        news_ner_tags__locations = row[11].replace("‘", "").replace("’", "").replace("“", "\"").replace("”", "\"").replace("–", "-")
        news_ner_tags__locations_unique = row[12].replace("‘", "").replace("’", "").replace("“", "\"").replace("”", "\"").replace("–", "-")
        news_ner_tags__moneys = row[13]
        news_ner_tags__moneys_unique = row[14]
        news_ner_tags__organizations = row[15].replace("‘", "").replace("’", "").replace("“", "\"").replace("”", "\"").replace("–", "-")
        news_ner_tags__organizations_unique = row[16].replace("‘", "").replace("’", "").replace("“", "\"").replace("”", "\"").replace("–", "-")
        news_ner_tags__percent = row[17]
        news_ner_tags__percent_unique = row[18]
        news_ner_tags__persons = row[19].replace("‘", "").replace("’", "").replace("“", "\"").replace("”", "\"").replace("–", "-")
        news_ner_tags__persons_unique = row[20].replace("‘", "").replace("’", "").replace("“", "\"").replace("”", "\"").replace("–", "-")
        news_ner_tags__times = row[21]
        news_ner_tags__times_unique = row[22]
        news_original_tags = row[23]
        news_publish_date = row[24]
        news_reporters = row[25]
        news_text = row[26].replace("‘", "'").replace("’", "'").replace("“", "\"").replace("”", "\"").replace("–", "-")
        news_url = row[27]
        newspaper_name = row[28]
        news_url = row[29]

        # print(news_text)

        f = csv.writer(open("/home/shoumik/Documents/Kolpokoushol/Scraped data/final v2.1.csv", "a"))
        f.writerow([row[0], row[1], row[2], news_headline, row[4], row[5], row[6], row[7], row[8], row[9],
                    row[10], news_ner_tags__locations, news_ner_tags__locations_unique, row[13], row[14], news_ner_tags__organizations,
                    news_ner_tags__organizations_unique, row[17], row[18], news_ner_tags__persons, news_ner_tags__persons_unique,
                    row[21], row[22], row[23], row[24], row[25], news_text, row[27], row[28], row[29]])


# .replace("‚Äė", "'").replace("‚Äô","'").replace(",Äú","\"").replace("‚ÄĚ","\"").replace("‚Äô","'")
