from PyQt5.QtWidgets import QApplication, QLabel

def display():
    app = QApplication([])
    label = QLabel('Listening...')
    label.show()
    app.exec()

