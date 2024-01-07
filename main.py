import os
import sys
import time
import pathlib

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
    app = QApplication(sys.argv) # Create instance of a QApplication
    assistant = PersonalAssistant() # Create instance of a PersonalAssistant
    assistant.start() # Start the voice assistant
    sys.exit(app.exec_())  # Start the voice assistant GUI