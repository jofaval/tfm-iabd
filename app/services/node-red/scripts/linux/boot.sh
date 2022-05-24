#!/bin/bash

echo Install the necessary Node-RED packages
./install.sh
cd ./scripts/linux

echo Boots Node-RED
./start.sh
cd ./scripts/linux