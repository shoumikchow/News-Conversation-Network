import json
import csv

with open('./Scraped data/bd_news_dt.json', 'r+') as infile:
    data = json.load(infile)


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

for i in range(3):
    fj = (flattenjson(data[i], "__"))
    # print (fj)

    oid = fj["_id__$oid"]  # column 0
    is_negative = fj["is_negative"]  # column 1
    news_crawled_date = fj["news_crawled_date__$date"]  # column 2
    news_headline = fj["news_headline"]  # column 3
    news_image_urls = fj["news_image_urls"]  # column 4
    news_keywords = fj["news_keywords"]  # column 5
    news_location = fj["news_location"]  # column 6
    news_ml_tags = fj["news_ml_tags"]  # column 7
    news_naive_tags = fj["news_naive_tags"]  # column 8
    news_ner_tags__dates = fj["news_ner_tags__dates"]  # column 9
    news_ner_tags__dates_unique = fj["news_ner_tags__dates_unique"]  # column 10
    news_ner_tags__locations = fj["news_ner_tags__locations"]  # column 11
    news_ner_tags__locations_unique = fj["news_ner_tags__locations_unique"]  # column 12
    news_ner_tags__moneys = fj["news_ner_tags__moneys"]  # column 13
    news_ner_tags__moneys_unique = fj["news_ner_tags__moneys_unique"]  # column 14
    news_ner_tags__organizations = fj["news_ner_tags__organizations"]  # column 15
    news_ner_tags__organizations_unique = fj["news_ner_tags__organizations_unique"]  # column 16
    news_ner_tags__percents = fj["news_ner_tags__percents"]  # column 17
    news_ner_tags__percents_unique = fj["news_ner_tags__percents_unique"]  # column 18
    news_ner_tags__persons = fj["news_ner_tags__persons"]  # column 19
    news_ner_tags__persons_unique = fj["news_ner_tags__persons_unique"]  # column 20
    news_ner_tags__times = fj["news_ner_tags__times"]  # column 21
    news_ner_tags__times_unique = fj["news_ner_tags__times_unique"]  # column 22
    news_original_tags = fj["news_original_tags"]  # column 23
    news_publish_date = fj["news_publish_date__$date"]  # column 24
    news_reporters = fj["news_reporters"]  # column 25
    news_text = fj["news_text"]  # column 26
    news_url = fj["news_url"]  # column 27
    newspaper_name = fj["newspaper_name"]  # column 28
    newspaper_url = fj["newspaper_url"]  # column 29

    # replace("‚Äė", "").replace("‚Äô","").replace(",Äú","\"").replace("‚ÄĚ","\"").replace("‚Äô","'")

    f = csv.writer(open("./Scraped data/new_scraped.csv", "a"))
    """
    f.writerow(["_id__$oid", "is_negative", "news_crawled_date__$date", "news_headline", "news_image_urls",
                "news_keywords", "news_location", "news_ml_tags", "news_naive_tags", "news_ner_tags__dates",
                "news_ner_tags__dates_unique", "news_ner_tags__locations", "news_ner_tags__locations_unique",
                "news_ner_tags__moneys", "news_ner_tags__moneys_unique", "news_ner_tags__organizations",
                "news_ner_tags__organizations_unique", "news_ner_tags__percents", "news_ner_tags__percents_unique",
                "news_ner_tags__persons", "news_ner_tags__persons_unique", "news_ner_tags__times", "news_ner_tags__times_unique",
                "news_original_tags", "news_publish_date__$date", "news_reporters", "news_text", "news_url", "newspaper_name",
                "newspaper_url"])
    """
    f.writerow([oid, is_negative, news_crawled_date, news_headline,
                news_image_urls, news_keywords, news_location, news_ml_tags, news_naive_tags,
                news_ner_tags__dates, news_ner_tags__dates_unique, news_ner_tags__locations,
                news_ner_tags__locations_unique, news_ner_tags__moneys, news_ner_tags__moneys_unique,
                news_ner_tags__organizations, news_ner_tags__organizations_unique,
                news_ner_tags__percents, news_ner_tags__percents_unique, news_ner_tags__persons,
                news_ner_tags__persons_unique, news_ner_tags__times, news_ner_tags__times_unique,
                news_original_tags, news_publish_date, news_reporters, news_text, news_url,
                newspaper_name, newspaper_url])
