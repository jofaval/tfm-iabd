# CHANGELOG #
All the log of changes on the project/repository

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

For the Docker's CHANGELOG please [click here](./docs/deployment/docker/CHANGELOG.md).

## 2022-04-04

### Modified

- Added missing names to the docker services

## 2022-04-03

### Added

- `.env` file created for the Docker-Compose and an easier configuration
- Add the ZooKeeper Dockerfile for Kafka cluster management
- Configure the Docker Compose file with the basic requirements
- Documented the Deployment and Docker implementations, and add a Docker's infrastructure CHANGELOG

### Modified

- Reorganize types folder into models folder with a package `__init__` file for bundling

## 2022-04-02

### Added

- Backend container, there's a chance it may be moved to another repository, just for the website
 - FastAPI and uvicorn
- Create a Kafka topic shell script for easier usage

### Modified

- Extended the spark transformer example with custom typing and folder reestrcutring

### Fixed

- Update the usage section in the README with the correct execution scripts

## 2022-04-01

### Added

- Add git utilities to tools
 - Created the documentation
- Create Frontend folder
 - Install some basic necessary packages (vue.js with element, flow and eslint)
 - Configured basic eslint file

### Modified

- Moved files to an app folder structure for clearer organization
 - Renamed `src/app` to `app/src/module`
- Reestructure the tools folder
 - Adding support to windows and linux

### Fixed

- Replaced incorrect Dockerfile doca and add missing one (MongoDB)

## 2022-03-27

### Achieved

- Product Owner and Tech/Team Lead role have been chosen
- Title has been decided (by Diego)

## 2022-03-24

### Added

- Improve navigation in the READMEs by providing links

## 2022-03-23

### Achieved

- Repository Initialized

### Added

- Github Actions CI/CD basic integration (template only)
- Basic Docker folder structure distribution
- Utility Docker tools
- Basic README structure with some minor, provisional data
- Basic folder structure
- Basic app folder with global utilities and more to come
- Basic Spark structure, and semi-flow
- Use the MIT License
- Official docker image docs

### Modified

- Changed repository name

## 2022-02-25

### Achieved

- Project Started