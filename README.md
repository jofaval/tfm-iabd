# Master's Final Degree Project #

Artificial Intelligence and Big Data

The motivation behind the project is to work as a team with the idea of joining everthing we've seen, in other words:

Being able to design, research, develop and deploy a Data Science idea designing a Big Data Architecture from which to train a model with a conclusion in mind while being ethical and not breaking any EU laws

## Table of content

1. [Title](#title)
1. [Description](#description)
1. [Objectives](#objectives)
1. [Ethics](#ethics)
1. [Design](#design)
    1. [Flow of the Data](#flow-of-the-data)
    1. [Data Structure](#data-structure)
1. [Methodology](#methodology)
    1. [Product Owner](#product-owner)
    1. [Scrum Muster](#scrum-muster)
    1. [Software](#software)
    1. [Programming Language](#programming-language)
1. [Tech Stack](#tech-stack)
    1. [ETL](#etl)
    1. [Database](#database)
    1. [Cloud computing](#cloud-computing)
1. [Usage](#usage)
    1. [Requirements](#requirements)
    1. [Install the project](#install-the-project)
    1. [How to boot it](#how-to-boot-it)
    1. [Stop the execution](#stop-the-execution)
    1. [Deployment](#deployment)
1. [Team](#team)
    1. [Infrastructure (Big Data Architecture)](#infrastructure-big-data-architecture)
    1. [Data Extraction/Mining](#data-extractionmining)
    1. [Data Normalization](#data-normalization)
    1. [Data Storage/Loading](#data-storageloading)
    1. [Data Cleansing](#data-cleansing)
    1. [Data Science/Modeling (AI Engineering, sort of)](#data-sciencemodeling-ai-engineering-sort-of)
    1. [Data Visualization](#data-visualization)
    1. [Deploy (CI/CD integration)](#deploy-cicd-integration)
1. [License](#license)
1. [Legal Notice](#license)
1. [Credits](#credits)

## Title

Unkown

## Description

TODO

## Documentation

For the official documentation visit the [/docs](/docs/README.md) folder

## Objectives

- 

## Ethics

TODO

## Design

### Flow of the Data

1. Node-RED recibe los datos y se los chuta a
1. Kafka, que los distribuye a
1. Spark para que sean transformados y almacenados en
1. MongoDB y posteriormente extraídos con
1. Google Colab/Python
1. Entrenados con Spark y guardando las predicciones en
1. MongoDB para leerlas posteriormente desde
1. PowerBI/Tableau y mostrarlas en
1. Azure Web Service con un Front sencillo de interacción básica

### Data Structure

All the data will have an origin tag/field as to better identify it's properties

Queda decidir si tener una Data Warehouse (los datos guardados están estructurados, limpiados y siguen un orden) o un Data Lake (todo guardado a lo burro y ya se limpiará cuando se necesite, si es que se acaba necesitando)

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
  - > Engine Version 20.10
  - > Compose Version 1.29.2
- Python
  - > \>= 3.6.x

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

I (Pepe) will be supervising each task, but we're all out here to help each other.

### Infrastructure (Big Data Architecture)

#### Description

Defined as Preparation of docker images, ready and interjoined to support the architecture.

#### Software

Docker (Docker-compose), Linux, if cloud computing were to be required (AWS, Azure or Google Cloud)

#### Elements

The information regarding the infrastructure it's in the [**Infrastructure**](#tech-stack) section.

#### Asignees

- Nerea
- Juan
- Pepe (only if cloud computing is required)

### Data Extraction/Mining

#### Description

Defined as Retrieving all the necessary data for it's work. (JUST retrieving data)

#### Software

Node-RED

#### Asignees

- Nerea
- Pepe
- Everyone to search for Data Sources

#### Data Sources

- Twitter Developer API

### Data Normalization

#### Description

Defined as After the data has being retrieved, create a middleground with the common data that may be needed so that all sources end up with the same Data Model, in other words, standarizing the sources.

#### Software

Node-RED

#### Asignees

- Diego
- Nerea
- Juan
- Pepe

### Data Storage/Loading

#### Description

Defined as Storing the normalized data into the NoSQL DB (MongoDB most likely).

#### Software

Node-RED

#### Asignees

- Nerea

### Data Cleansing

#### Description

Defined as At this point, the data has been normalized, but not cleaned, the data should be ready for the Model to train with.

#### Software

Python (Google Colab?)

#### Asignees

- Diego
- Juan
- Pepe

### Data Science/Modeling (AI Engineering, sort of)

#### Description

Defined as Developing and implement the required model(s) for the desired performance and outcome.

Artificial Intelligence and/or Machine Learning.

#### Software

Python (Google Colab?)

#### Asignees

- Diego
- Pepe

### Data Visualization

#### Description

Defined as Designing and developing the story (StoryTelling) and all the required/desired visualizations for whaterever the outcome(s) are that we want.

#### Software

PowerBI or Tableau, up to taste.

#### Asignees

- Juan
- Nerea
- Diego

### Deploy (CI/CD integration)

#### Description

Defined as Prepare the connections, and proper usage of the model via endpoints and utilities.

#### Software

Cloud Platform (if used), Git (Github)

#### Asignees

- Diego
- Pepe

## License

The license used can be seen [here](./LICENSE) or downloading the LICENSE file

## Legal Notice

TODO

## Credits

- 