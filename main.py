import os
import sys
import time
import pathlib
import platform
import webbrowser
import whisper
import speech_recognition as sr

# Local file imports
sys.path.append('C:/Users/tahlo/Documents/Programming/Personal-Assistant')
import lists

# local path 'C:\Users\tahlo\Documents\Programming\Personal-Assistant'
# virtual env path 'C:\Users\tahlo\Documents\Programming\Personal-Assistant\pavenv\Scripts'
# start virtual environemnt: source activate
# venv interpreter C:\Users\tahlo\Documents\Programming\Personal-Assistant\pavenv\Scripts\python.exe

# INCLUDE ENVIRONMENT VARIABLE: 'C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.38.33130\include'
# LIB ENVIRONMENT VARIABLE: 'C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.38.33130\lib\x64'
# PATH ENVIRONMENT VARIABLE: 'C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.38.33130\bin\Hostx64\x64'

# This function listens to one audio input with the sphinx model. 
def listen_with_sphinx():
    speech = sr.Recognizer()
    listening = True
    print('Listening')
    
    while listening:
        with sr.Microphone() as source:
            speech.adjust_for_ambient_noise(source)
            audio = speech.listen(source)

            try:
                spoken_text = speech.recognize_sphinx(audio)
                print(f'You just said: {spoken_text}')

                if spoken_text == 'stop':
                    break
            except sr.UnknownValueError:
                print("Sorry, I did not understand that.")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")

# This function listens to one audio inputs with open ai's whisper model which has much better performance.
def listen_with_whisper():
    speech = sr.Recognizer()
    listening = True
    print('Listening')

    while listening:
        with sr.Microphone() as source:
            speech.adjust_for_ambient_noise(source)
            audio = speech.listen(source)
            model = whisper.load_model('base.en') # Right now the model uses the base training set, I do not understand the API well enough to implement the others just yet

            try:
                spoken_text = speech.recognize_whisper(audio)
                print(f'You just said: {spoken_text}')

                parsed_text = parse_text(spoken_text)
                listening = control_flow(parsed_text)

            except sr.UnknownValueError:
                print("Sorry, I did not understand that.")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")

# Control Flow
def parse_text(text: str) -> list:

    # I am going to divide the text into an array and parse each substring for keywords.

    text_to_array = text.split(' ')
    return text_to_array

def control_flow(parsed_array: list):

    # This function parses the parsed text and searches for keywords. If it detects keywords then it runs a function
    for word in parsed_array:
        
        if word in lists.stop_list:
            print('Exiting program')
            return False # Stop listening
            
        # For example if it detects time in the parsed array it could prompt a time control flow function
        if word == 'time':
            print(time.time())

        if word == lists.web_list:
            print('Opening the following website:')
            webbrowser.open('https://' + 'youtube' + '.com')
    
    return True

if __name__ == '__main__':
    print(lists.web_list)