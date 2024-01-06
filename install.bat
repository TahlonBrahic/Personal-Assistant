@echo off

echo Creating application directory...
mkdir "%LOCALAPPDATA%\TellTruVirtualAssistant" || exit /b


echo Setting up Python virtual environment...
python -m venv "%LOCALAPPDATA%\TellTruVirtualAssistant\venv" || exit /b

echo Copying necessary files...
python -m venv "%LOCALAPPDATA%\TellTruVirtualAssistant\venv" || exit /b

echo Installing dependencies...
"%LOCALAPPDATA%\TellTruVirtualAssistant\venv\Scripts\pip.exe" install -r requirements.txt || exit /b

echo Setup completed successfully.

pause