from gtts import gTTS
import speech_recognition as sr
import os


def listen():
    # Speech to text
    r = sr.Recognizer()  # initialize recognizer
    with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.
        print("Speak: ")
        audio = r.listen(source)  # listen to the source
    try:
        querry = r.recognize_google(
            audio
        )  # use recognizer to convert our audio into text part.
        return querry.lower()
    except:
        response = "I don't understand"
        return response


def speak(response, language, output_file):
    # Passing the text and language to the engine
    text = gTTS(text=response, lang=language, slow=False)
    # Saving the converted audio in a mp3 file in .cache
    text.save(output_file)
    # Playing the converted file
    os.system(f"play {output_file}")
