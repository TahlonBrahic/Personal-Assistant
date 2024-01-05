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
import gui

# The following section provides information for me on important locations to run the application from source code.

# local path 'C:\Users\tahlo\Documents\Programming\Personal-Assistant'
# virtual env path 'C:\Users\tahlo\Documents\Programming\Personal-Assistant\pavenv\Scripts'
# start virtual environemnt: source activate
# venv interpreter C:\Users\tahlo\Documents\Programming\Personal-Assistant\pavenv\Scripts\python.exe

# INCLUDE ENVIRONMENT VARIABLE: 'C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.38.33130\include'
# LIB ENVIRONMENT VARIABLE: 'C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.38.33130\lib\x64'
# PATH ENVIRONMENT VARIABLE: 'C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.38.33130\bin\Hostx64\x64'

class SpeechRecognizer:
    def __init__(self, model):
        self.model = model
        self.speech = sr.Recognizer()

    def listen(self):
        # Implement listening logic using self.model
        listening = True
        while listening:
            with sr.Microphone() as source:
                self.speech.adjust_for_ambient_noise(source)
                audio = self.speech.listen(source)
                model = whisper.load_model('base.en') # Right now the model uses the base training set, I do not understand the API well enough to implement the others just yet

                try:
                    spoken_text = self.speech.recognize_whisper(audio)
                    print(f'You just said: {spoken_text}')

                    parsed_text = self.parse_text(spoken_text)
                    listening = self.recognize(parsed_text)

                except sr.UnknownValueError:
                    print("Sorry, I did not understand that.")
                except sr.RequestError as e:
                    print(f"Could not request results; {e}")

    def parse_text(self, text: str) -> list:

        # I am going to divide the text into an array and parse each substring for keywords.

        text_to_array = text.split(' ')
        return text_to_array

    def recognize(self, parsed_array: list):
        # Implement recognition logic based on self.model
        # This function parses the parsed text and searches for keywords. If it detects keywords then it runs a function
        for word in parsed_array:
            if word in lists.stop_list:
                print('Exiting program')
                return False # Stop listening
                
            # For example if it detects time in the parsed array it could prompt a time control flow function
            if word == 'time':
                print(time.time())
                gui_input = f'Your time is {time.localtime()}.'

            if word in lists.web_list:
                print('Opening the following website:')
                webbrowser.open('https://' + 'youtube' + '.com')

        return True # This keeps the listen method running

class PersonalAssistant:
    def __init__(self, model='whisper'):
        self.recognizer = SpeechRecognizer(model=model)

    def start(self):
        self.recognizer.listen()
        

if __name__ == '__main__':
    assistant = PersonalAssistant()
    assistant.start()