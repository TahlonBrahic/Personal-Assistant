from datetime import datetime
import platform
import webbrowser
import os
import pathlib
import whisper

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication

import tts
import lists
import speech_recognition as sr

class SpeechRecognizer(QThread):
    recognized_signal = pyqtSignal(str)  # Signal to emit recognized text

    def __init__(self, model):
        super().__init__()
        self.model = model
        self.speech = sr.Recognizer()
        self.os = platform.system()
        self.tts = tts.Speaker()

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
            if word in lists.time_list:
                print(datetime.now().strftime("%H:%M:%S"))
                self.tts.say(f'Your time is {datetime.now().strftime("%H:%M:%S")}.')

            if word in lists.web_list:
                if word in lists.youtube_list:
                    print('Opening the following website:')
                    self.tts.say('I am opening youtube.com for you.')
                    webbrowser.open('https://' + 'youtube' + '.com')

        return True # This keeps the listen method running