from PyQt5.QtWidgets import QLabel, QMainWindow

class GUI(QMainWindow):
    def __init__(self, label_text='Listening...'):
        super().__init__()
        self.label = QLabel(label_text)
        self.setWindowTitle("Voice Assistant")

    def display(self):
        self.show()

    def update_text(self, text):
         self.label.setText(text)  # Update text of the existing label