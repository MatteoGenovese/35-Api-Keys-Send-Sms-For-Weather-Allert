import requests
import password
from twilio.rest import Client

OWMEndPoint = "https://api.openweathermap.org/data/3.0/onecall"
account_sid = password.account_sid
auth_token = password.auth_token

params = {
    "lat": "46.00",
    "lon": "8.74",
    "appid": password.personalApiKey,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWMEndPoint, params=params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_=password.twillioNumber,
        to=password.myNumber
    )
    print(message.status)
