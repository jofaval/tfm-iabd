call root.bat

REM Starts all of the services

REM Start the Frontend service
cd frontend/src/scripts/windows
start start.bat
cd ../../../

REM Start the Backend service
cd backend/src/scripts/windows
start start.bat
cd ../../../

REM Start the Node-RED service
cd node-red/scripts/windows
start start.bat
cd ../../../