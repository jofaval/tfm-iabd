# CHANGELOG #
All the log of changes on the project/repository

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

For the Docker's CHANGELOG please [click here](./docs/deployment/docker/CHANGELOG.md).

## 2022-04-27

### Added

- Uploaded the Node-RED main flow to Github

### Modified

- Remove old unusable Node-RED subflows

## 2022-04-25

### Modified

- Slightly improve the README
- Adjust and improve the package.json scripts and cycle

## 2022-04-23

### Added

- Configured the Node-RED service with some basic scripts and the base dependency file (package.json)

### Modified

- Keep on improving the base Node-RED flow.
  - Created, as an example, the base Twitter flow, with room for improvement. It still needs some tweaks here and there.

### Fixed

- The team scritps for the installation were incomplete, the script paths were.

## 2022-04-22

### Added

- Creating the Node-RED initial flow(s) configuration.
  - Created the basic tabs and overall environment configuration.

### Modified

- Renamed `app/src` to `app/services` for a better semantic. And adjuested the necessary components.
  - Due to this change, history is lost, but ONLY on Github, the history still remains on the git

## 2022-04-20

### Added

- Heaviliy configured the frontend package.json
  - Vue-CLI is now used
  - Added some scripts for utilities
  - Add the package-required config files
- Added the last team scripts, it now provides:
  - Booting up part of the system
  - Testing part of the system
  - Installing part of the system

### Modified

- Polished the team scripts with some utilities
  - Added missing dependencies

### Fixed

- Fixed some of the team scripts with incorrect path configuration

## 2022-04-19

### Added

- Keep on adding more team scripts

## 2022-04-18

### Added

- Implemented the base Spark Transformer class logic
- Added spark basic utilities to the `module` package
- The `pyspark` package to the spark folder
- Create basic Example Transformer test
- Added team scripts utilities for an easier usage of the application

### Modified

- Reestructure the scripts into folders
- Added the Vue-CLI scripts to the package.json in the frontend

## 2022-04-17

### Added

- Created Kafka shell scripts for an easier control and usage
- Infrastructure is now explained and added to the Tech Stack section
- Expanded the topics shell scripts
  - It now can list all the topics
  - It can create topics from a file
- The python module is now correctly setup and ready for packaging and installation

### Modified

- Explained almost all of the TODO sections at the README, but changes will surely be made

### Modified

- The Docker-Compose file, more details at the [CHANGELOG](./docs/deployment/docker/CHANGELOG.md)

## 2022-04-16

### Modified

- Adjusted the Docker-Compose, more details at the [CHANGELOG](./docs/deployment/docker/CHANGELOG.md)

## 2022-04-15

### Added

- Jupyter Notebooks will now be ignored for the linguistic statistics
- Added the project's description

### Modified

- Improving some minor (and not so minor) details in the README for a clearer explanation of the project, it's technologies choices, the design

## 2022-04-13

### Added

- The base Google Colab Jupyter Notebook for the model

## 2022-04-06

### Fixed

- Fixed the `topic.sh` incorrect kafka script path call
- Changed the docker compose container name from `name` to `container_name`

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