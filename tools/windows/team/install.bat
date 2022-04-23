call root.bat

REM Install the python module
cd module/scripts/windows/
call install.bat
cd ../../../

REM Install the backend
cd backend/scripts/windows/
call devinstall.bat
cd ../../../

REM Install the frontend
cd frontend/scripts/windows/
call install.bat
cd ../../../

REM Install the Node-RED packages
cd node-red/scripts/windows/
call install.bat
cd ../../../