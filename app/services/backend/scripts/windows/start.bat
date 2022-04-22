call root.bat

cd app

:: For development
:: uvicorn main:app --reload

REM Starts the FastAPI server
uvicorn main:app