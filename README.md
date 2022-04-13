# Master's Final Degree Project #

Artificial Intelligence and Big Data

The motivation behind the project is to work as a team with the idea of joining everthing we've seen, in other words:

Being able to design, research, develop and deploy a Data Science idea designing a Big Data Architecture from which to train a model with a conclusion in mind while being ethical and not breaking any EU laws

### <p align="right">Grade</p>
<p align="right">
To be graded
</p>

## Table of Contents

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
[↑ Back to top](#table-of-contents)

"Hype" is all you need

## Description
[↑ Back to top](#table-of-contents)

TODO

## Documentation
[↑ Back to top](#table-of-contents)

For the official documentation visit the [/docs](/docs/README.md) folder

## Objectives
[↑ Back to top](#table-of-contents)

- 

## Ethics
[↑ Back to top](#table-of-contents)

TODO

## Design
[↑ Back to top](#table-of-contents)

### Flow of the Data
[↑ To the section](#design)

1. Node-RED sniffs the data and sends them to
1. Kafka, which itself distributes it to
1. Spark for them to be transformed and stored in
1. MongoDB to be later retrieved with
1. Google Colab/Python
1. To be trained with Spark saving the predictions in
1. MongoDB so they can be accessed from
1. PowerBI/Tableau and display them in
1. Azure Web Service with a simple Front with an even simpler interaction

### Data Structure
[↑ To the section](#design)

All the data will have an origin tag/field as to better identify it's properties

Queda decidir si tener una Data Warehouse (los datos guardados están estructurados, limpiados y siguen un orden) o un Data Lake (todo guardado a lo burro y ya se limpiará cuando se necesite, si es que se acaba necesitando)

## Methodology
[↑ Back to top](#table-of-contents)

SCRUM

- Kanban Board
- Planning Poker

### Product Owner
[↑ To the section](#methodology)

Diego

### Tech/Team Lead
[↑ To the section](#methodology)

Pepe

### Scrum Muster
[↑ To the section](#methodology)

Our teachers

### Software
[↑ To the section](#methodology)

- Trello

## Tech Stack
[↑ Back to top](#table-of-contents)

### Programming Language
[↑ To the section](#tech-stack)

- Python

### ETL
[↑ To the section](#tech-stack)

1. Node-RED
1. Kafka
1. Spark

### Database
[↑ To the section](#tech-stack)

- MongoDB

### Cloud computing
[↑ To the section](#tech-stack)

- AWS (Canvas) or Azure
- Terraform

## Usage
[↑ Back to top](#table-of-contents)

### Requirements
[↑ To the section](#usage)

- Docker
  - > Engine Version 20.10
  - > Compose Version 1.29.2
- Python
  - > \>= 3.6.x

_All the images versions will be provided on each Dockerfile with the exact version, avoid the `latest` for security reasons, upgrades will be manual._

### Install the project
[↑ To the section](#usage)

Execute the following command on the folder you want to store the project in

```bash
git clone https://github.com/jofaval/tfm-iabd.git
cd tfm-iabd
```

### How to boot it
[↑ To the section](#usage)

Execute the `tools/windows/infra/stop.bat` or the `tools/linux/infra/stop.sh` file

or execute the following commands on the shell

```bash
cd app/infra
docker-compose up -d
```

### Stop the execution
[↑ To the section](#usage)

Execute the `tools/windows/infra/stop.bat` or the `tools/linux/infra/stop.sh` file

or execute the following commands on the shell

```bash
cd app/infra
docker-compose down
```

### Deployment
[↑ To the section](#usage)

Handled by the Github Actions workflow

## Team
[↑ Back to top](#table-of-contents)

|                          Name                          |                       Role                      |
|:------------------------------------------------------:|:-----------------------------------------------:|
| [Diego del Caño](https://github.com/ddelcanonavarrete) |          Data Scientist / Data Analyst          |
|  [Juan Crespin Valero](https://github.com/juancrespin) |             Data Analyst / SysAdmin             |
|      [Nerea Gluskova](https://github.com/Rubirea)      |             Data Engineer / SysAdmin            |
|    [Pepe Fabra Valverde](https://github.com/jofaval)   | Data Architect / Data Engineer / Data Scientist |

_Table generated with: [https://www.tablesgenerator.com/markdown_tables](https://www.tablesgenerator.com/markdown_tables)_

I (Pepe) will be supervising each task, but we're all out here to help each other.

### Infrastructure (Big Data Architecture)
[↑ To the section](#team)

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
[↑ To the section](#team)

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
[↑ To the section](#team)

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
[↑ To the section](#team)

#### Description

Defined as Storing the normalized data into the NoSQL DB (MongoDB most likely).

#### Software

Node-RED

#### Asignees

- Nerea

### Data Cleansing
[↑ To the section](#team)

#### Description

Defined as At this point, the data has been normalized, but not cleaned, the data should be ready for the Model to train with.

#### Software

Python (Google Colab?)

#### Asignees

- Diego
- Juan
- Pepe

### Data Science/Modeling (AI Engineering, sort of)
[↑ To the section](#team)

#### Description

Defined as Developing and implement the required model(s) for the desired performance and outcome.

Artificial Intelligence and/or Machine Learning.

#### Software

Python (Google Colab?)

#### Asignees

- Diego
- Pepe

### Data Visualization
[↑ To the section](#team)

#### Description

Defined as Designing and developing the story (StoryTelling) and all the required/desired visualizations for whaterever the outcome(s) are that we want.

#### Software

PowerBI or Tableau, up to taste.

#### Asignees

- Juan
- Nerea
- Diego

### Deploy (CI/CD integration)
[↑ To the section](#team)

#### Description

Defined as Prepare the connections, and proper usage of the model via endpoints and utilities.

#### Software

Cloud Platform (if used), Git (Github)

#### Asignees

- Diego
- Pepe

## License
[↑ Back to top](#table-of-contents)

The license used can be seen [here](./LICENSE) or downloading the LICENSE file

## Legal Notice
[↑ Back to top](#table-of-contents)

TODO

## Credits
[↑ Back to top](#table-of-contents)

- Ismael, for the idea