@echo off
echo Starting legacy Streamlit UI...
if not exist .venv (
    echo Virtual environment not found. Please run initialization first.
    pause
    exit /b
)
call .venv\Scripts\activate
streamlit run ui\app.py
pause
