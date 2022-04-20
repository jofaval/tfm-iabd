#!/bin/bash

./root.sh

echo Install the python module
cd module
call install.sh

echo Install the backend
cd ../backend
call devinstall.sh

echo Install the frontend
cd ../frontend
call install.sh