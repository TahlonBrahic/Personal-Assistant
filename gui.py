from PyQt5.QtWidgets import QApplication, QLabel

class GUI:
    def __init__(self, label_text='Listening...'):
        self.label = QLabel(label_text)

    def display(self):
        self.label.show()

    def update_text(self, text):
         self.label.setText(text)  # Update text of the existing label