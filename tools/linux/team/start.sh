#!/bin/bash

./root.sh

echo Starts all of the services

echo Start the Frontend service
cd frontend/src/scripts/windows
./start.sh
cd ../../../

echo Start the Backend service
cd backend/src/scripts/windows
./start.sh
cd ../../../

echo Start the Node-RED service
cd node-red/scripts/linux
./start.sh
cd ../../../