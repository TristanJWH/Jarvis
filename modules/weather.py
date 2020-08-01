import requests
from pprint import pprint


# Matching the id codes to a description (based on the descriptions at https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2)
verb = "will be"
match_cloud_id = {
    200: f"it {verb} thunderstorming with light rain",
    201: f"it {verb} thunderstorming with rain",
    202: f"it {verb} thunderstorming with heavy rain",
    210: f"there {verb} a light thunderstorm",
    211: f"it {verb} thunderstorming",
    212: f"there {verb} a heavy thunderstorm",
    221: f"there {verb} a ragged thunderstorm",
    230: f"it {verb} thunderstorming with light drizzle",
    231: f"it {verb} thunderstorming with drizzle",
    232: f"it {verb} thunderstorming with heavy drizzle",
    300: f"there {verb} a light drizzle",
    301: f"it {verb} drizzling",
    302: f"there {verb} a heavy drizzle",
    310: f"there {verb} a light drizzle",
    311: f"it {verb} drizzling",
    312: f"there {verb} a heavy drizzle",
    313: f"there {verb} a light shower",
    314: f"it {verb} showering",
    321: f"there {verb} a heavy shower",
    500: f"there {verb} some light rain",
    501: f"there {verb} some moderate rain",
    502: f"there {verb} some heavy rain",
    503: f"there {verb} some very heavy rain",
    504: f"there {verb} some extremely heavy rain",
    511: f"there {verb} some hail",
    520: f"there {verb} a light shower",
    521: f"there {verb} a shower",
    522: f"there {verb} a heavy shower",
    531: f"there {verb} a ragged shower",
    600: f"there {verb} light snow",
    601: f"there {verb} snow",
    602: f"there {verb} heavy snow",
    611: f"there {verb} some sleet",
    612: f"there {verb} some light sleet",
    613: f"there {verb} a shower of sleet",
    615: f"there {verb} some light rain and snow",
    616: f"there {verb} some rain and snow",
    620: f"there {verb} a light shower of snow",
    621: f"there {verb} a shower of snow",
    622: f"there {verb} a heavy shower of snow",
    701: f"it {verb} misty",
    711: f"there {verb} lots of smoke",
    721: f"it {verb} hazy",
    731: f"it {verb} dusty",
    741: f"it {verb} foggy",
    751: f"it {verb} sandy",
    761: f"it {verb} dusty",
    771: f"there {verb} lots of ash",
    771: f"there {verb} squalls",
    771: f"there {verb} a tornado",
    800: f"there {verb} clear skies",
    801: f"there {verb} few clouds",
    802: f"there {verb} scattered clouds",
    803: f"there {verb} broken clouds",
    804: f"it {verb} overcast",
}
past_verb = "is"
past_match_cloud_id = {
    200: f"it {past_verb} thunderstorming with light rain",
    201: f"it {past_verb} thunderstorming with rain",
    202: f"it {past_verb} thunderstorming with heavy rain",
    210: f"there {past_verb} a light thunderstorm",
    211: f"it {past_verb} thunderstorming",
    212: f"there {past_verb} a heavy thunderstorm",
    221: f"there {past_verb} a ragged thunderstorm",
    230: f"it {past_verb} thunderstorming with light drizzle",
    231: f"it {past_verb} thunderstorming with drizzle",
    232: f"it {past_verb} thunderstorming with heavy drizzle",
    300: f"there {past_verb} a light drizzle",
    301: f"it {past_verb} drizzling",
    302: f"there {past_verb} a heavy drizzle",
    310: f"there {past_verb} a light drizzle",
    311: f"it {past_verb} drizzling",
    312: f"there {past_verb} a heavy drizzle",
    313: f"there {past_verb} a light shower",
    314: f"it {past_verb} showering",
    321: f"there {past_verb} a heavy shower",
    500: f"there {past_verb} some light rain",
    501: f"there {past_verb} some moderate rain",
    502: f"there {past_verb} some heavy rain",
    503: f"there {past_verb} some very heavy rain",
    504: f"there {past_verb} some extremely heavy rain",
    511: f"there {past_verb} some hail",
    520: f"there {past_verb} a light shower",
    521: f"there {past_verb} a shower",
    522: f"there {past_verb} a heavy shower",
    531: f"there {past_verb} a ragged shower",
    600: f"there {past_verb} light snow",
    601: f"there {past_verb} snow",
    602: f"there {past_verb} heavy snow",
    611: f"there {past_verb} some sleet",
    612: f"there {past_verb} some light sleet",
    613: f"there {past_verb} a shower of sleet",
    615: f"there {past_verb} some light rain and snow",
    616: f"there {past_verb} some rain and snow",
    620: f"there {past_verb} a light shower of snow",
    621: f"there {past_verb} a shower of snow",
    622: f"there {past_verb} a heavy shower of snow",
    701: f"it {past_verb} misty",
    711: f"there {past_verb} lots of smoke",
    721: f"it {past_verb} hazy",
    731: f"it {past_verb} dusty",
    741: f"it {past_verb} foggy",
    751: f"it {past_verb} sandy",
    761: f"it {past_verb} dusty",
    771: f"there {past_verb} lots of ash",
    771: f"there {past_verb} squalls",
    771: f"there {past_verb} a tornado",
    800: f"there {past_verb} clear skies",
    801: f"there {past_verb} few clouds",
    802: f"there {past_verb} scattered clouds",
    803: f"there {past_verb} broken clouds",
    804: f"it {past_verb} overcast",
}


def daily_weather(lat, lon, API, units, day):
    Final_url = f"http://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units={units}&appid={API}&exclude=current,minutely,hourly"
    # this variable contain the JSON data which the API returns
    weather_data = requests.get(Final_url).json()
    weather_data = weather_data["daily"][day]
    temp = round(weather_data["temp"]["day"])
    feels_like = round(weather_data["feels_like"]["day"])
    cloud = weather_data["weather"][0]["id"]
    cloud = match_cloud_id[cloud]
    wind = weather_data["wind_speed"]
    wind_direction = weather_data["wind_deg"]
    rain = round(weather_data["pop"] * 100)
    if 338 <= wind_direction:
        wind_direction = "North"
    elif wind_direction <= 22:
        wind_direction = "North"
    elif 23 <= wind_direction <= 67:
        wind_direction = "North East"
    elif 68 <= wind_direction <= 112:
        wind_direction = "East"
    elif 113 <= wind_direction <= 157:
        wind_direction = "South East"
    elif 158 <= wind_direction <= 202:
        wind_direction = "South"
    elif 203 <= wind_direction <= 247:
        wind_direction = "South West"
    elif 248 <= wind_direction <= 292:
        wind_direction = "West"
    elif 293 <= wind_direction <= 337:
        wind_direction = "North West"
    return [temp, feels_like, cloud, wind, wind_direction, rain]


def current_weather(lat, lon, API, units):
    Final_url = f"http://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units={units}&appid={API}&exclude=daily,minutely,hourly"
    # this variable contain the JSON data which the API returns
    weather_data = requests.get(Final_url).json()
    # Matching the id codes to a description (based on the descriptions at https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2)
    weather_data = weather_data["current"]
    # Matching the id codes to a description (based on the descriptions at https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2)
    temp = round(weather_data["temp"])
    feels_like = round(weather_data["feels_like"])
    cloud = weather_data["weather"][0]["id"]
    cloud = past_match_cloud_id[cloud]
    wind = weather_data["wind_speed"]
    wind_direction = weather_data["wind_deg"]
    if 338 <= wind_direction:
        wind_direction = "North"
    elif wind_direction <= 22:
        wind_direction = "North"
    elif 23 <= wind_direction <= 67:
        wind_direction = "North East"
    elif 68 <= wind_direction <= 112:
        wind_direction = "East"
    elif 113 <= wind_direction <= 157:
        wind_direction = "South East"
    elif 158 <= wind_direction <= 202:
        wind_direction = "South"
    elif 203 <= wind_direction <= 247:
        wind_direction = "South West"
    elif 248 <= wind_direction <= 292:
        wind_direction = "West"
    elif 293 <= wind_direction <= 337:
        wind_direction = "North West"
    return [temp, feels_like, cloud, wind, wind_direction]


def hourly_weather(lat, lon, API, units, hour):
    Final_url = f"http://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units={units}&appid={API}&exclude=current,minutely,daily"
    # this variable contain the JSON data which the API returns
    weather_data = requests.get(Final_url).json()
    # Matching the id codes to a description (based on the descriptions at https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2)
    weather_data = weather_data["hourly"][hour]
    cloud = weather_data["weather"][0]["id"]
    cloud = match_cloud_id[cloud]
    temp = round(weather_data["temp"])
    feels_like = round(weather_data["feels_like"])
    wind = weather_data["wind_speed"]
    wind_direction = weather_data["wind_deg"]
    rain = round(weather_data["pop"] * 100)
    if 338 <= wind_direction:
        wind_direction = "North"
    elif wind_direction <= 22:
        wind_direction = "North"
    elif 23 <= wind_direction <= 67:
        wind_direction = "North East"
    elif 68 <= wind_direction <= 112:
        wind_direction = "East"
    elif 113 <= wind_direction <= 157:
        wind_direction = "South East"
    elif 158 <= wind_direction <= 202:
        wind_direction = "South"
    elif 203 <= wind_direction <= 247:
        wind_direction = "South West"
    elif 248 <= wind_direction <= 292:
        wind_direction = "West"
    elif 293 <= wind_direction <= 337:
        wind_direction = "North West"
    return [temp, feels_like, cloud, wind, wind_direction, rain]
