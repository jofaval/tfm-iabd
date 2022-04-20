call root.bat

REM Starts testing everything there is to test

REM Tests Spark
cd spark/scripts/windows
start test.bat
cd ../../../

REM Tests the Frontend
cd frontend/scripts/windows
start test.bat
cd ../../../

REM Tests the Backend
cd backend/scripts/windows
start test.bat
cd ../../../