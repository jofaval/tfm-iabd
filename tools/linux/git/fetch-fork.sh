#!/bin/bash

# Retrieves, Updates and Merge with the fork origin
git fetch upstream
git checkout master
git merge upstream/master