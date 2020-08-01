# Voice-Assistant

A voice assistant that I programmed in python.
Articles are available detailing more information about [how it works](https://www.tristanhodgson.com/articles/building-jarvis-part-2) and the [goals](https://www.tristanhodgson.com/articles/building-jarvis-part-1) (they changed a lot though) of the project.

# Before First Use:

## Dependencies

### What should already be installed:

* pulseaudio
* python3

### What should not already be installed:

* ```sudo apt install python3-pip python3-pyaudio sox libsox-fmt-all```
* ```pip3 install speech_recognition gtts wikipedia wolframalpha```

## API Keys

Get an API key from Wolframalpha at [https://products.wolframalpha.com/api/](https://products.wolframalpha.com/api/).

Get an Open Weather Map API Key at [https://openweathermap.org/price](https://openweathermap.org/price).

Store both in their variables in the app.py file in that variables section.

# How this Program Works

This program is detailed more thoroughly in the articles listed above but I will provide a brief description:

## How this program works in plain speak

1. Listen to what I say
2. Turn that speech to text using google speech recognition
3. Match the text to an action
4. Check the module (this returns some text)
5. Use gtts to convert the text to an mp3 file
6. Play this sound using sox
