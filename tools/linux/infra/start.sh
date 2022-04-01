#!/bin/bash

# Moves to the proper directory
/bin/bash ./infrastructure.sh

echo Boot theorchestrator
docker-compose up -d