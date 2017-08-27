import json
import csv
from pprint import pprint


def flattenjson(b, delim):
    val = {}
    for i in b.keys():
        if isinstance(b[i], dict):
            get = flattenjson(b[i], delim)
            for j in get.keys():
                val[i + delim + j] = get[j]
        else:
            val[i] = b[i]

    return val


with open('./Scraped data/DailyStar2.csv', 'a') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(['_id', 'about_reporter', 'bottom_tagline', 'breadcrumb', 'category', 'content', 'date_crawled__date',
                'date_published__date', 'generated_keywords', 'generated_summary', 'id', 'image_captions', 'images',
                'ml_tags', 'ner_location', 'ner_money', 'ner_organization', 'ner_percent', 'ner_person', 'ner_time', 'ner_unique_location',
                'ner_unique_money', 'ner_unique_organization', 'ner_unique_percent', 'ner_unique_person', 'ner_unique_time',
                'news_url', 'newspaper', 'reporter', 'section', 'sentiment', 'shoulder', 'title', 'top_tagline'])


with open('./Scraped data/news_db.json', 'r+') as infile:
    counter = 0
    for row in infile:
        # pprint(flattenjson(json.loads(row), "__"))
        fj = flattenjson(json.loads(row), "__")

        _id = fj['_id__$oid']
        about_reporter = fj['about_reporter']
        bottom_tagline = fj['bottom_tagline']
        breadcrumb = fj['breadcrumb']
        category = fj['category']
        content = fj['content']
        date_crawled__date = fj['date_crawled__$date']
        date_published__date = fj['date_published__$date']
        generated_keywords = fj['generated_keywords']
        generated_summary = fj['generated_summary']
        id = fj['id']
        image_captions = fj['image_captions']
        images = fj['images']
        ml_tags = fj['ml_tags']
        ner_location = fj['ner_location']
        ner_money = fj['ner_money']
        ner_organization = fj['ner_organization']
        ner_percent = fj['ner_percent']
        ner_person = fj['ner_person']
        ner_time = fj['ner_time']
        ner_unique_location = fj['ner_unique_location']
        ner_unique_money = fj['ner_unique_money']
        ner_unique_organization = fj['ner_unique_organization']
        ner_unique_percent = fj['ner_unique_percent']
        ner_unique_person = fj['ner_unique_person']
        ner_unique_time = fj['ner_unique_time']
        news_url = fj['news_url']
        newspaper = fj['newspaper']
        reporter = fj['reporter']
        section = fj['section']
        sentiment = fj['sentiment']
        shoulder = fj['sentiment']
        title = fj['title']
        top_tagline = fj['top_tagline']

        with open('./Scraped data/DailyStar2.csv', 'a') as outfile:
            writer = csv.writer(outfile)
            writer.writerow([_id, about_reporter, bottom_tagline, breadcrumb, category, content, date_crawled__date,
                date_published__date, generated_keywords, generated_summary, id, image_captions, images,
                ml_tags, ner_location, ner_money, ner_organization, ner_percent, ner_person, ner_time, ner_unique_location,
                ner_unique_money, ner_unique_organization, ner_unique_percent, ner_unique_person, ner_unique_time,
                news_url, newspaper, reporter, section, sentiment, shoulder, title, top_tagline])

        counter += 1
        if counter == 150400:
            break
