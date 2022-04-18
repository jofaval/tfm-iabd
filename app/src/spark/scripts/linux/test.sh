#!/bin/bash

./root.sh
cd src/tests

echo Install the necessary packages
pip3 install -r test-requirements.txt

echo Execute all the tests
python3 -m unittest -v