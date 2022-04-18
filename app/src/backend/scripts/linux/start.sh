#!/bin/bash

./root.sh

cd app

# For development
# uvicorn main:app --reload

echo Starts the FastAPI server
uvicorn main:app