import os
import sys
import time
import pathlib

import speech_recognition as sr
from PyQt5.QtWidgets import QApplication



# Local file imports
sys.path.append('C:/Users/tahlo/Documents/Programming/Personal-Assistant')
import lists
import gui
from speech_recognizer import SpeechRecognizer

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