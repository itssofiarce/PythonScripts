import requests
from twilio.rest import Client
api_key = "your api key"
account_sid = "ypur account id"
auth_token = "auth token"
twilio_num = "+your num"
parameters = {
    "lat": -24.858379,
    "lon": -54.335899,
    "appid": api_key,
    "exclude": "currently,minutely,daily"
}

response = requests.get(
    "https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()

# .get("weather")[0].get("id")
weather_id = weather_data["hourly"][:12]

weather_condition = [dic.get("weather")[0].get("id") for dic in weather_id]

will_rain = False
for cond in weather_condition:
    if cond < 700:
        will_rain = True
    else:
        print("No rain today. Have a Nice Day")
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="Oh no today is going to rain",
            from_=twilio_num,
            to='+your phone number'
        )
    print(message.status)
