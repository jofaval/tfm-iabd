# Master's Final Degree Project #

Artificial Intelligence and Big Data

## Table of content

1. [Title](#title)
1. [Description](#description)
1. [Objectives](#objectives)
1. [Methodology](#methodology)
1. [Tech Stack](#tech-stack)
1. [Usage](#usage)
1. [Team](#team)
1. [License](#license)
1. [Credits](#credits)

## Title

Unkown

## Description

TODO

The motivation behind the project is to work as a team with the idea of joining everthing we've seen, in other words:

Being able to design, research, develop and deploy a Data Science idea designing a Big Data Architecture from which to train a model with a conclusion in mind while being ethical and not breaking any EU laws

## Documentation

For the official documentation visit the [/docs](/docs/README.md) folder

## Objectives

- 

## Methodology

SCRUM

- Kanban Board
- Planning Poker

### Product Owner

To be chosen

### Scrum Muster

Our teachers

### Software

- Trello

## Tech Stack

### Programming Language

- Python

### ETL

1. Node-RED
1. Kafka
1. Spark

### Database

- MongoDB

### Cloud computing

- AWS (Canvas) or Azure
- Terraform

## Usage

### Requirements

- Docker
  - Engine Version 20.10
  - Compose Version 1.29.2
- Python
  - \>= 3.6.x

_All the images versions will be provided on each Dockerfile with the exact version, avoid the `latest` for security reasons, upgrades will be manual._

### Install the project

Execute the following command on the folder you want to store the project in

```bash
git clone https://github.com/jofaval/tfm-ia-big-data.git
cd tfm-ia-big-data
```

### How to boot it

Execute the `tools/start.bat` file

or execute the following commands on the shell

```bash
cd infraestructure
docker-compose up -d
```

### Stop the execution

Execute the `tools/stop.bat` file

or execute the following commands on the shell

```bash
cd infraestructure
docker-compose down
```

### Deployment

Handled by the Github Actions workflow

## Team

|                  Name                  |                       Role                      |
|:--------------------------------------:|:-----------------------------------------------:|
|  [Diego](https://github.com/ddelcano)  |          Data Scientist / Data Analyst          |
| [Juan](https://github.com/juancrespin) |             Data Analyst / SysAdmin             |
|      [Nerea](https://github.com/)      |             Data Engineer / SysAdmin            |
|   [Pepe](https://github.com/jofaval)   | Data Architect / Data Engineer / Data Scientist |

_Table generated with: [https://www.tablesgenerator.com/markdown_tables](https://www.tablesgenerator.com/markdown_tables)_

## License

The license used can be seen [here](./LICENSE) or downloading the LICENSE file

## Credits

- 