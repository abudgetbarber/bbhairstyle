@echo off
echo Installing Budget Barber dependencies...
pip install -r requirements.txt
echo.
echo Starting Budget Barber server...
echo Open http://localhost:5000 in your browser
echo.
python server.py
pause
