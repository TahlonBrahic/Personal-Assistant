import os
import pathlib
import platform
import whisper
import speech_recognition

# local path 'C:\Users\tahlo\Documents\Programming\Personal-Assistant'
# virtual env path 'C:\Users\tahlo\Documents\Programming\Personal-Assistant\virtual-assistant-virtualenv\Scripts'

# Load model
whisper = whisper.load_model('medium.en')

speech = speech_recognition.Recognizer()
print('Listening')

with speech_recognition.Microphone() as source:
    speech.adjust_for_ambient_noise(source)
    audio = speech.listen(source)
    input = speech.recognize_whisper(audio, model=whisper)
    print(f'You just said {input}')