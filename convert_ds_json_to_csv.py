import json
import csv
from pprint import pprint

with open('./Scraped data/DailyStar2.csv', 'a') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['oid', 'about_reporter', 'bottom_tagline', 'breadcrumb', 'category', 'content', 'date_published', 'generated_keywords',
        'generated_summary', 'id', 'image_captions', 'ml_tags', 'ner_unique_location', 'ner_unique_money', 'ner_unique_organization', 'ner_unique_percent',
        'ner_unique_person', 'ner_unique_time', 'news_url', 'section', 'sentiment', 'title', 'top_tagline'])


with open("./Scraped data/news_db.json") as infile:
    counter = 1
    for row in infile:
        all_data = json.loads(row)
        oid = all_data['_id']['$oid']
        about_reporter = all_data['about_reporter']
        bottom_tagline = all_data['bottom_tagline']
        if bottom_tagline:
            bottom_tagline = bottom_tagline.replace("‘", "").replace("’", "").replace("“", "\"").replace("”", "\"").replace("–", "-").replace(';', '')
        breadcrumb = all_data['breadcrumb']
        category = all_data['category']
        content = all_data['content']
        if content:
            content = content.replace("‘", "").replace("’", "").replace("“", "\"").replace("”", "\"").replace("–", "-").replace(';', '')
        date_published = all_data['date_published']['$date']
        generated_keywords = all_data['generated_keywords']
        generated_summary = all_data['generated_summary']
        id = all_data['id']
        image_captions = all_data['image_captions']
        ml_tags = all_data['ml_tags']
        ner_unique_location = all_data['ner_unique_location']
        ner_unique_money = all_data['ner_unique_money']
        ner_unique_organization = all_data['ner_unique_organization']
        ner_unique_percent = all_data['ner_unique_percent']
        ner_unique_person = all_data['ner_unique_person']
        ner_unique_time = all_data['ner_unique_time']
        news_url = all_data['news_url']
        section = all_data['section']
        sentiment = all_data['sentiment']
        title = all_data['title']
        top_tagline = all_data['top_tagline']

        with open('./Scraped data/DailyStar2.csv', 'a') as outfile:
            writer = csv.writer(outfile)
            writer.writerow([oid, about_reporter, bottom_tagline, breadcrumb, category, content, date_published, generated_keywords,
                generated_summary, id, image_captions, ml_tags, ner_unique_location, ner_unique_money, ner_unique_organization, ner_unique_percent,
                ner_unique_person, ner_unique_time, news_url, section, sentiment, title, top_tagline])
