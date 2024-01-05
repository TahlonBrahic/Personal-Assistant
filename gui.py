from PyQt5.QtWidgets import QLabel, QMainWindow

class GUI(QMainWindow):
    def __init__(self, label_text='Listening...', height=400):
        super().__init__()
        self.setWindowTitle("Voice Assistant")
        self.setFixedHeight(height)

        # Label information
        self.label = QLabel(label_text)
        self.label.resize(120, 80)

    def display(self):
        self.show()

    def update_text(self, text):
         self.label.setText(text)  # Update text of the existing label