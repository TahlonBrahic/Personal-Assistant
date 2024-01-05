import os
import sys
import time
import pathlib
import platform

import webbrowser
import whisper
import speech_recognition as sr

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication

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

class SpeechRecognizer(QThread):
    recognized_signal = pyqtSignal(str)  # Signal to emit recognized text

    def __init__(self, model):
        super().__init__()
        self.model = model
        self.speech = sr.Recognizer()

    def run(self):
        # Implement listening logic using self.model
        listening = True
        while listening:
            print('Listening...')
        
            with sr.Microphone() as source:
                self.speech.adjust_for_ambient_noise(source)
                audio = self.speech.listen(source)
                
                try:
                    recognized_text = self.speech.recognize_whisper(audio)
                    self.recognized_signal.emit(recognized_text)
                    print(f'You just said: {recognized_text}')

                    parsed_text = self.parse_text(recognized_text)
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
        self.gui = gui.GUI()
        self.recognizer.recognized_signal.connect(self.on_recognized)

    def on_recognized(self, text):
        # Update GUI with recognized text
        self.gui.update_text(text)  # Ensure GUI has a method to update text

    def start(self):
        self.gui.display()
        self.recognizer.start()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    assistant = PersonalAssistant()
    assistant.start()
    sys.exit(app.exec_())  # Start the event loop