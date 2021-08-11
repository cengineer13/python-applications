import requests
import os
from twilio.rest import Client
#API key from https://openweathermap.org/
MY_API = "a0dcd893489051a250fab51574e77371"
account_sid ='ACff4886a215b405fa93eab01b9bf200a0'
auth_token = '4e2cfbf94c3192e1ef074f6a962bd2eb'

parametres = {
    "lat" : 35.294472,
    "lon" : 128.728058,
    "appid": MY_API,
    "exclude":"current,minutely,daily"
}


response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parametres)
response.raise_for_status()
weather_data = response.json()

weather_ids = []

weather_slice = weather_data['hourly'][:12]
#print(weather_slice)

is_rain = False
for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        is_rain = True

if is_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Today the weather is expected to be rainy. Please bring an umbrella!☔",
        from_='+14243535185',
        to='+821047406606'
    )
    print(message.status )




