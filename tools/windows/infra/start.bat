REM Moves to the infraestructure folder
call infrastructure.bat

REM Boots all the containers on detach mode
docker-compose up -d
pause