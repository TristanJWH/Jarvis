##########################################################
###############     Jarvis Python Code     ###############
##########################################################

# Imports
import re
import os
import time

# My own modules
# Volume
from modules.volume import relative_volume
from modules.volume import absolute_volume

# Time date
from modules.time_date import time_date
from modules.time_date import current_time
from modules.time_date import current_date

# Leaving and back
from modules.left_back import left
from modules.left_back import back

# Weather
from modules.weather import hourly_weather
from modules.weather import daily_weather
from modules.weather import current_weather

# Internet
from modules.internet import web
from modules.internet import search
from modules.internet import show_me_search
from modules.internet import wiki
from modules.internet import show_me_wiki

# Speak and listen
from modules.speak_listen import speak
from modules.speak_listen import listen

# Misc
from modules.misc import poweroff
from modules.misc import go_to_sleep
from modules.misc import os_command
from modules.misc import play_sound

# Remote Commands
from modules.remote_commands import remote_command_write

# Variables
## User variables
open_weather_map_api_key = ""
wolframalpha_api_key = ""
audio_device = 1  # Get the audio device by running "pactl list short sinks" and check which devices are running to rule them out
home = {"lat":"",
        "lon":""}
wake_word = ""  # The wake phrase for the program (leave blank for no wake word) wake word can be used at any point in the phrase.
# for example 'Hey {wake_word} what is the time' would work the same as 'what's the time {wake_word}
output_file = "current-jarvis-output.mp3"  # The cache file for the output
alarm_sound = "wake_up.mp3"
language = "en"  # Language in which you want to convert
## System Variables
response = ""  # The answer that is generated
last_response = ""  # The last answer
querry = ""  # The question asked
last_querry = ""  # The last question asked
random = 0

# Set volume to 70%
os.system(f"pactl set-sink-volume 1 70%")

while True:
    # Listen
    querry = listen()
    print(querry)
    # Matching the speech to a command

    if re.search(wake_word, querry) != None:
        # Wikipedia
        if (
            re.search("wiki", querry) != None and re.search("show", querry) != None
        ):  # Match wiki (will also match wikipedia) and show me
            url = show_me_wiki(querry)
            web(url[0])
            response = url[1]
        elif (
            re.search("wiki", querry) != None
        ):  # Match wiki (will also match wikipedia)
            response = wiki(querry, "for")
        # Wolframalpha
        elif (
            re.search("search", querry) != None and re.search("show", querry) == None
        ):  # Match search and not show
            response = "searching"
            response = search(querry, "search", wolframalpha_api_key)
        elif (
            re.search("search", querry) != None and re.search("show", querry) != None
        ):  # Match search and show
            response = show_me_search(querry)
        ## Open website
        ## Brilliant
        elif re.search("challenge", querry) != None:  # Match challenge
            response = web("https://brilliant.org/daily-problems/")
        ## Open weather map
        elif (
            re.search("weather", querry) != None and re.search("show", querry) != None
        ):  # Match weather and show
            response = web("https://openweathermap.org/")
        ## Email
        elif re.search("email", querry) != None:  # Match email
            response = web("https://mail.zoho.eu/zm/#mail/folder/inbox")
        # Open program
        ## Newsboat
        elif re.search("news", querry) != None:  # Match news
            response = os_command(
                "nohup alacritty -e newsboat -r > /dev/null 2>&1 &", 0
            )
        # Power off
        elif (
            re.search("power off", querry) != None
            and re.search("server", querry) != None
        ):  # Match power and all
            remote_command_write("poweroff", "fileserver")
            response = poweroff()
        elif re.search("power off", querry) != None:  # Match power and all
            os.system("poweroff")
        # Sleep
        elif re.search("sleep", querry) != None:  # Match sleep
            response = go_to_sleep()
        elif re.search("nap", querry) != None:  # Match nap
            response = go_to_sleep()
        # Time and date
        elif (
            re.search("time", querry) != None
            and re.search("lunch", querry) == None
            and re.search("tea", querry) == None
        ):  # Match time and not tea or lunch
            response = current_time()
        elif re.search("date", querry) != None:  # Match date
            response = current_date()
        # Weather
        ## Current Weather
        elif (
            re.search("weather", querry) != None
            and re.search("current", querry) != None
        ):  # Match weather and current
            weather = current_weather(
                home["lat"], home["lon"], open_weather_map_api_key, "metric"
            )
            response = f"Currently {weather[2]} and {weather[0]} degrees and feeling like {weather[1]}. The wind speed is {weather[3]} metres per second coming from the {weather[4]}."
        ## Weather for tommorow
        elif (
            re.search("weather", querry) != None
            and re.search("tomorrow", querry) != None
        ):  # Match weather and tomorrow
            weather = daily_weather(
                home["lat"], home["lon"], open_weather_map_api_key, "metric", 1
            )
            response = f"Tommorow {weather[2]} with a {weather[5]} percent chance of rain. It will be {weather[0]} degrees and feel like {weather[1]}. The wind speed will be {weather[3]} metres per second coming from the {weather[4]}."
        ## Weather on a specific day
        elif (
            re.search("weather", querry) != None
            and re.search("monday", querry) != None
            or re.search("tuesday", querry) != None
            or re.search("wednesday", querry) != None
            or re.search("thursday", querry) != None
            or re.search("friday", querry) != None
            or re.search("saturday", querry) != None
            or re.search("sunday", querry) != None
        ):  # Match weather
            day_to_number = {
                "monday": 0,
                "tuesday": 1,
                "wednesday": 2,
                "thursday": 3,
                "friday": 4,
                "saturday": 5,
                "sunday": 6,
            }
            day_to_match = querry.split("on ")[-1]
            day_to_match = day_to_number[day_to_match]
            if day_to_match <= 0:
                day_to_match = day_to_match + 6
            days = day_to_match - time_date()[4]
            weather = daily_weather(
                home["lat"],
                home["lon"],
                open_weather_map_api_key,
                "metric",
                days,
            )
            response = f"{weather[2]} and a {weather[5]} percent chance of rain. It will be {weather[0]} degrees and feel like {weather[1]}. The wind speed will be {weather[3]} metres per second coming from the {weather[4]}."
        ## Daily weather
        elif (
            re.search("weather", querry) != None
            and re.search(" day", querry) != None
            or re.search("-day", querry) != None
        ):  # Match weather and tomorrow
            days = querry.split("in")[-1]
            days = days.split(" day")[0]
            days = days.split("-day")[0]
            days = int(days)
            weather = daily_weather(
                home["lat"],
                home["lon"],
                open_weather_map_api_key,
                "metric",
                days,
            )
            response = f"{weather[2]} with a {weather[5]} percent chance of rain. It will be {weather[0]} degrees and feel like {weather[1]}. The wind speed will be {weather[3]} metres per second coming from the {weather[4]}."
        ## Todays weather
        elif re.search("weather", querry) != None:  # Match weather
            weather = daily_weather(
                home["lat"], home["lon"], open_weather_map_api_key, "metric", 0
            )
            response = f"Today {weather[2]} and a {weather[5]} percent chance of rain. It will be {weather[0]} degrees and feel like {weather[1]}. The wind speed will be {weather[3]} metres per second coming from the {weather[4]}."
        ## Hourly weather
        elif (
            re.search("weather", querry) != None and re.search("hour", querry) != None
        ):  # Match weather and hour
            hour = querry.split("in ")[-1]
            hour = hour.split(" hour")[0]
            hour = int(hour)
            weather = hourly_weather(
                home["lat"],
                home["lon"],
                open_weather_map_api_key,
                "metric",
                hour,
            )
            response = f"{weather[2]} with a {weather[5]} percent chance of rain. It will be {weather[0]} degrees and feel like {weather[1]}. The wind speed will be {weather[3]} metres per second coming from the {weather[4]}."
        # Repeat last command
        elif re.search("repeat", querry) != None:  # Match repeat
            response = last_response
        # Volume
        elif (
            re.search("volume", querry) != None
            and re.search("set", querry) != None
            or re.search("change", querry) != None
        ):  # Match volume and set
            response = absolute_volume(querry, audio_device)
        elif (
            re.search("volume", querry) != None
            and re.search("up", querry) != None
            or re.search("down", querry) != None
        ):  # Match volume and up or down
            response = relative_volume(querry, audio_device)
        else:
            pass

    # Speak
    if response != "":
        print(
            f"""

        {response}
        """
        )
        speak(response, language, output_file)
        last_response = response
        response = ""
        last_querry = querry
        querry = ""
