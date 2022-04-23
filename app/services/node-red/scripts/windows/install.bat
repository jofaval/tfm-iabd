call root.bat

REM Install Node-RED
npm i -g --unsafe-perm  node-red

REM Install all the necessary packages
cd data
npm install
cd ..