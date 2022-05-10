REM Moves to the infraestructure folder
call infraestructure.bat

REM Boots all the containers on detach mode
docker-compose up -d