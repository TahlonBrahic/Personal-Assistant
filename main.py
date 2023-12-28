import os
import pathlib
import platform
import speech_recognition

# local path 'C:\Users\tahlo\Documents\Programming\Personal-Assistant'
# virtual env path 'C:\Users\tahlo\Documents\Programming\Personal-Assistant\virtual-assistant-virtualenv\Scripts'
# venv interpreter C:\Users\tahlo\Documents\Programming\Personal-Assistant\pavenv\Scripts\python.exe

speech = speech_recognition.Recognizer()
print('Listening')

with speech_recognition.Microphone() as source:
    speech.adjust_for_ambient_noise(source)
    audio = speech.listen(source)
    input = speech.recognize_sphinx(audio)
    print(f'You just said {input}')