from PyQt5.QtWidgets import QApplication, QLabel

class GUI:
    def __init__(self, label_text='Listening...'):
        self.app = QApplication([])
        self.label = QLabel(label_text)

    def display(self):
        self.label.show()
        self.app.exec()

    def update_text(self, text):
        self.label = QLabel(text)

