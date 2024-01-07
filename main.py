import sys

import speech_recognition as sr
from PyQt5.QtWidgets import QApplication



# Local file imports
sys.path.append('C:/Users/tahlo/Documents/Programming/Personal-Assistant')
from speech_recognizer import SpeechRecognizer
from personal_assistant import PersonalAssitant

if __name__ == '__main__':
    app = QApplication(sys.argv) # Create instance of a QApplication
    assistant = PersonalAssistant() # Create instance of a PersonalAssistant
    assistant.start() # Start the voice assistant
    sys.exit(app.exec_())  # Start the voice assistant GUI