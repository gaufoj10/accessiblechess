@echo off
    echo Checking for Python installation...
    python --version >nul 2>&1
    if %errorlevel% neq 0 (
        echo Python is not installed. Downloading...
        powershell -Command "& {Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe' -OutFile 'python_installer.exe'}"
        start /wait python_installer.exe /quiet InstallAllUsers=1 PrependPath=1
        del python_installer.exe
    )
    echo Python is installed!
    pause
    