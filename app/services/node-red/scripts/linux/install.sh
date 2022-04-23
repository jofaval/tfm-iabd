#!/bin/bash

./root.sh

echo Install Node-RED
npm i -g --unsafe-perm  node-red

echo Install all the necessary packages
cd data
npm install
cd ..