#!/bin/bash

./root.sh

echo Starts testing everything there is to test

echo Tests Spark
cd spark/scripts/windows
./test.sh
cd ../../../

echo Tests the Frontend
cd frontend/scripts/windows
./test.sh
cd ../../../

echo Tests the Backend
cd backend/scripts/windows
./test.sh
cd ../../../