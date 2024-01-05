from PyQt5.QtWidgets import QLabel, QMainWindow, QDesktopWidget, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt

class GUI(QMainWindow):
    def __init__(self, label_text='Listening...', height=400):
        super().__init__()
        self.label = label_text

        self.setWindowTitle("Voice Assistant")
        self.setGeometry(100, 100, 800, 600)
        self.centerWindow()

        self.createCentralWidget()

    # This creates the central widget and adds the label that reads the input text.
    def createCentralWidget(self):

        # Create the central widget
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        # Create a Layout and Label, centers the label
        layout = QVBoxLayout()
        label = QLabel(self.label, centralWidget)
        label.setAlignment(Qt.AlignCenter)

        # Add widget to label and set layout of central widget
        layout.addWidget(label)
        centralWidget.setLayout(layout)

    def centerWindow(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def inputSpeechWidget(self):
        self.label = QLabel(self)
        self.label.resize(120, 80)

    def display(self):
        self.show()

    def update_text(self, text: str):
         self.label.setText(text)  # Update text of the existing label