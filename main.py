import sys
from PyQt5.QtWidgets import QApplication
LOCAL_PATH = 'C:/Users/tahlo/Documents/Programming/Personal-Assistant'
sys.path.append(LOCAL_PATH)
from personal_assistant import PersonalAssistant

def main():
    """Main function to start the voice assistant application."""
    try:
        app = QApplication(sys.argv)  # Create instance of a QApplication
        assistant = PersonalAssistant()  # Create instance of a PersonalAssistant
        assistant.start()  # Start the voice assistant
        sys.exit(app.exec_())  # Start the event loop of the application
    except Exception as e:
        print(f"Error occurred: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()