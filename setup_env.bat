@echo off
    echo Creating Python virtual environment...
    python -m venv venv
    echo Activating environment and installing dependencies...
    call venv\Scripts\activate
    pip install --upgrade pip
    pip install flask requests stockfish
    echo Setup complete!
    pause
    