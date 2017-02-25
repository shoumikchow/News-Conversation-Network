import indicoio
import csv

indicoio.config.api_key = "my_api_key"


def get_text_sentiment(text):
    sentiment_value = indicoio.sentiment_hq(text)
    sentiment = ""
    if sentiment_value > 0.5:
        sentiment = "positive"
    elif sentiment_value == 0.5:
        sentiment = "neutral"
    else:
        sentiment = "negative"
    return sentiment, sentiment_value


with open("./Scraped data/quotations_and_speeches_v2.0.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        # print(row)
        # break
        sentiment, sentiment_value = get_text_sentiment(row[2])
        with open("./Scraped data/quotations_and_speeches_with_sentiment_v2.1.csv", "a") as out:
            writer = csv.writer(out)
            writer.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], sentiment, sentiment_value])
            print(count)
            count += 1
