from watson_developer_cloud import AlchemyLanguageV1 as AlchemyLanguage
import csv


def get_text_sentiment(text):
    alchemy_api_key = "9cf7c5bba53e2811cbd53a2b6f3c0aadff9e3a03"

    alchemy_language = AlchemyLanguage(api_key=alchemy_api_key)
    result = alchemy_language.emotion(text=text)

    emotions = result['docEmotions']

    max_emo_val = max(emotions.values())
    max_emo_key = list(emotions.keys())[list(emotions.values()).index(max_emo_val)]
    # print(text)
    return emotions['anger'], emotions['disgust'], emotions['fear'], emotions['joy'], emotions['sadness'], max_emo_key


with open("/home/shoumik/Documents/Kolpokoushol/Scraped data/quotations and speeches v2.0.1.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    with open("/home/shoumik/Documents/Kolpokoushol/Scraped data/quotations and speeches with sentiment v2.1.csv", "a") as out:
        writer = csv.writer(out)
        writer.writerow(["original_id", "timestamp", "text", "locations", "organizations", "persons", "original_tag", "naive_tag", "keywords", "anger", "disgust", "fear", "joy", "sadness", "maximum_emotion"])

    for row in reader:
        anger, disgust, fear, joy, sadness, max_emo_key = get_text_sentiment(row[2])
        with open("/home/shoumik/Documents/Kolpokoushol/Scraped data/quotations and speeches with sentiment v2.1.csv", "a") as out:
            writer = csv.writer(out)
            writer.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], anger, disgust, fear, joy, sadness, max_emo_key])
