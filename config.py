# '''
# The following section provides information for me on important locations to run the application from source code.

# local path 'C:\Users\\tahlo\Documents\Programming\Personal-Assistant'
# virtual env path 'C:\Users\\tahlo\Documents\Programming\Personal-Assistant\pavenv\Scripts'
# start virtual environemnt: source activate
# venv interpreter C:\Users\\tahlo\Documents\Programming\Personal-Assistant\pavenv\Scripts\python.exe

# INCLUDE ENVIRONMENT VARIABLE: 'C:\Program Files (x86)\Microsoft Visual Studio\\2022\BuildTools\VC\Tools\MSVC\\14.38.33130\include'
# LIB ENVIRONMENT VARIABLE: 'C:\Program Files (x86)\Microsoft Visual Studio\\2022\BuildTools\VC\Tools\MSVC\\14.38.33130\lib\\x64'
# PATH ENVIRONMENT VARIABLE: 'C:\Program Files (x86)\Microsoft Visual Studio\\2022\BuildTools\VC\Tools\MSVC\\14.38.33130\\bin\Hostx64\\x64'
# '''

import sys, os

LOCAL_PATH = 'C:/Users/tahlo/Documents/Programming/Personal-Assistant'

class SystemPath():
    def __init__(self) -> None:
        self.application_path = self.find_application_path
        self.resource_file_path =

    def find_application_path(self):
        if getattr(sys, 'frozen', False):
            # If the application is compiled and run as a bundle
            application_path = os.path.dirname(sys.executable)
            return application_path
        else:
            # If the application is run as a script
            application_path = os.path.dirname(os.path.abspath(__file__))
            return application_path

    def find_resource_file_path(self):
        # Example of using application_path to access a resource file
        resource_file_path = os.path.join(self.application_path, 'resources', 'file.txt')
        return resource_file_path
    
    def append(self):
        sys.path.append(LOCAL_PATH)
