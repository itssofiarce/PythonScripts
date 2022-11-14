import requests
from twilio.rest import Client
api_key = "819e709a5deef0464eabb2155c85c4af"
account_sid = "AC4f4def930902a396f5e665fb6b94980f"
auth_token = "97ecf1949f64a84e46e7f9e8d55b9836"
twilio_num = "+19124556430"
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
