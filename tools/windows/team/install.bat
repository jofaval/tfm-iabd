call root.bat

REM Install the python module
cd module
call install.bat

REM Install the backend
cd ../backend
call devinstall.bat

REM Install the frontend
cd ../frontend
call install.bat