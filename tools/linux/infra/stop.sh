#!/bin/bash

# Moves to the proper directory
/bin/bash ./infrastructure.sh

echo Shuts down the orchestrator
docker-compose down