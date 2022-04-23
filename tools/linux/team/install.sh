#!/bin/bash

./root.sh

echo Install the python module
cd module/scripts/linux/
./install.sh
cd ../../../

echo Install the backend
cd backend/scripts/linux/
./devinstall.sh
cd ../../../

echo Install the frontend
cd frontend/scripts/linux/
./install.sh
cd ../../../

echo Install the Node-RED packages
cd node-red/scripts/linux/
./install.sh
cd ../../../