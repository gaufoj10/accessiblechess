@echo off
    echo Searching for Stockfish executable...
    for /r %%x in (stockfish.exe) do (
        echo Found: %%x
    )
    pause
    