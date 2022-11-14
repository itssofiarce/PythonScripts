import requests
from datetime import datetime, timedelta
import os
from twilio.rest import Client
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
MY_API = "C8LMDJHZUK46PV66"

MY_NEWS_API = "971beb6994704d83b6df84dcf8c286fd"

TWILIO_SID = "AC4f4def930902a396f5e665fb6b94980f"
TWILIO_AUTH_TOKEN = "97ecf1949f64a84e46e7f9e8d55b9836"
TWILIO_NUM = "+19124556430"

# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": MY_API,
}

url = 'https://www.alphavantage.co/query'
stocks = requests.get(url, params=parameters)
data = stocks.json().get("Time Series (Daily)")

yesterday = (datetime.today() - timedelta(days=1)).isoformat().split("T")[0]
yesterday_stock_price = data.get(yesterday).get("4. close")

# TODO 2. - Get the day before yesterday's closing stock price
before_yest = (datetime.today() - timedelta(days=2)).isoformat().split("T")[0]
before_yest_stock_price = data.get(before_yest).get("4. close")


# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

dif = float(before_yest_stock_price)-float(yesterday_stock_price)
# print(abs(round(dif)))

# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

percentage_dif = round(abs(round(dif)) / float(before_yest_stock_price) * 100)
# print(f"{percentage_dif}%")

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

if percentage_dif > 5:
    print("Get News")

# STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

news_params = {
    "q": "tesla",
    "from": (datetime.today() - timedelta(days=1)).isoformat().split("T")[0],
    "apiKey": MY_NEWS_API,
}


response = requests.get(NEWS_ENDPOINT, params=news_params)
get_news = response.json()["articles"]


# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

three_articles = get_news[:3]

print(three_articles)

# STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
formated_article = [
    f"Title: {article['title']} \n {article['url']}" for article in three_articles]

# TODO 9. - Send each article as a separate message via Twilio.


# Find your Account SID and Auth Token at twilio.com/console
# and set the enviroenment variables. Se http://twil.io/secure

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
for article in formated_article:
    message = client.messages \
                    .create(
                        body=article,
                        from_=TWILIO_NUM,
                        to='+543415930261'
                    )

print(message.sid)

# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
