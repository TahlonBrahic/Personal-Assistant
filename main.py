import os
import pathlib
import platform
import speech_recognition 

speech = speech_recognition.Recognizer()
print('Listening')

with speech_recognition.Microphone() as source:
    speech.adjust_for_ambient_noise(source)
    audio = speech.listen(source)
    input = speech.recognize_sphinx(audio)
    print(f'You just said {input}')