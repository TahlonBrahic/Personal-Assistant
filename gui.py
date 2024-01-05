from PyQt5.QtWidgets import QApplication, QLabel

class GUI:
    def __init__(self):
        self.app = QApplication([])
        self.label = QLabel('Listening...')

    def display(self):
        self.label.show()
        self.app.exec()

    def update_text(self, text):
        self.label.setText(text)

