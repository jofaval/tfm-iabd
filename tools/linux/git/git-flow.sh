#!/bin/bash

echo Initializes git flow on the repo
git flow init

echo Creates the Research branch
git checkout -b research

echo Switches to the Develop branch
git checkout develop