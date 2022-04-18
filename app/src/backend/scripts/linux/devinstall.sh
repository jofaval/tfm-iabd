#!/bin/bash

./root.sh

echo Install all the necessary packages for the dev environment
pip3 install -r requirements.txt dev-requirements.txt