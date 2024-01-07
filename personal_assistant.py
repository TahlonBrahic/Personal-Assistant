from gui import GUI
from speech_recognizer import SpeechRecognizer

class PersonalAssistant:
    def __init__(self, model='whisper'):
        self.recognizer = SpeechRecognizer(model=model)
        self.gui = GUI()
        self.recognizer.recognized_signal.connect(self.on_recognized)

    def on_recognized(self, text):
        # Update GUI with recognized text
        self.gui.update_text(text)  # Ensure GUI has a method to update text

    def start(self):
        self.gui.display()
        self.recognizer.start()