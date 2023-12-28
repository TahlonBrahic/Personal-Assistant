import os
import pathlib
import platform
import speech_recognition as sr

# local path 'C:\Users\tahlo\Documents\Programming\Personal-Assistant'
# virtual env path 'C:\Users\tahlo\Documents\Programming\Personal-Assistant\virtual-assistant-virtualenv\Scripts'
# venv interpreter C:\Users\tahlo\Documents\Programming\Personal-Assistant\pavenv\Scripts\python.exe
speech = sr.Recognizer()
print('Listening')

with sr.Microphone() as source:
    speech.adjust_for_ambient_noise(source)
    audio = speech.listen(source)

    try:
        spoken_text = speech.recognize_sphinx(audio)
        print(f'You just said: {spoken_text}')
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
