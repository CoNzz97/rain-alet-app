import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv("B:/Coding/Python/EnviromentVariables/.env")
# OpenWeatherMap API endpoint and key
OWM_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"
API_KEY = os.getenv("ra_OWM_API_KEY")

# Twilio account SID and authentication token
account_sid = os.getenv("ra_twillio_account_sid")
auth_token = os.getenv("ra_twillio_auth_token")

# Latitude and longitude coordinates of your location
MY_LAT = "00.000" # Input your Latitude here
MY_LNG = "-00.000" # Input your Longitude here

# Parameters for the weather API request
weather_params = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

# Send a GET request to the OpenWeatherMap API with the specified parameters
with requests.get(OWM_Endpoint, params=weather_params) as connection:
    connection.raise_for_status()
    weather_data = connection.json()
    hourly_12 = weather_data["hourly"][:12]

# Check if it will rain within the next 12 hours
will_rain = False

for hour in weather_data["hourly"]:
    weather_id = hour["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True

if will_rain:
    # Initialize Twilio client
    client = Client(account_sid, auth_token)

    # Send a message using Twilio
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an Umbrella.",
        from_='+447481337984',
        to='+447876203324'
    )
    print(message.status)


