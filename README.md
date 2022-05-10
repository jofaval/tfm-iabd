# Master's Final Degree Project #

Artificial Intelligence and Big Data

The motivation behind the project is to work as a team with the idea of joining everthing we've seen, in other words:

Being able to design, research, develop and deploy a Data Science idea designing a Big Data Architecture from which to train a model with a conclusion in mind while being ethical and not breaking any EU laws.

For reference about the changes, please, check out our [CHANGELOG](./CHANGELOG.md).

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
    1. [Data Sources](#data-sources)
1. [Product](#product)
    1. [Product Roadmap](#product-roadmap)
    1. [How is the Product managed?](#how-is-the-product-managed)
1. [Methodology](#methodology)
    1. [Product Owner](#product-owner)
    1. [Scrum Muster](#scrum-muster)
    1. [Software](#software)
1. [Tech Stack](#tech-stack)
    1. [Programming Language](#programming-language)
    1. [ETL](#etl)
    1. [Database](#database)
    1. [Cloud computing](#cloud-computing)
    1. [Infrastructure](#infrastructure)
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
1. [Legal Notice](#legal-notice)
1. [Credits](#credits)
1. [Gratitude](#gratitude)

## Title
[↑ Back to top](#table-of-contents)

"Hype" is all you need

## Description
[↑ Back to top](#table-of-contents)

This is research into what defines the success of films, and whether success can be predicted (proportionally) based on the hype (expectation) generated around a film; to be able to be expandable with both series and anime, video games or any other type of multimedia content or not.

It is intended, as possible definitions of the success of a film, to be able to predict:

- The benefits generated of a film based on its initial investment and how good will it be received
- The acceptance/acclamation of a film with respect to the initial "hype"
- Predict the note on IMDB a week after release, and whoever says IMDB can say other platforms (Rotten Tomatoes, Metacritic)
- Predict your success (previously defined) one week after your release

For this, various data sources will be used, such as: Twitter, Reddit, YouTube, IMDB, and those that we can discover as the investigation progresses. One of the main and central components of the application is sentiment analysis, which would become the main focus of the prediction.

## Documentation
[↑ Back to top](#table-of-contents)

For the official documentation visit the [/docs](/docs/README.md) folder

## Objectives
[↑ Back to top](#table-of-contents)

_Not in a specific order._

- Teamwork as a team of Data Sciencist with (almost) no experience in the data field.
- Use knowledge from every subject seen in the degree.
- Develop all the required elements components and integrate them.
- Design a Data Infrastructure.
- Research about the movie's hype and it's success, and it's total box-office.
- Manage and develop an E2E (end-to-end) Big Data project, from idea to analysis/visualizations.
- Apply AI Engineering techniques to deliver a product that showcases our conclusion.
- Develop the (A.I. and machine learning) models required for the desired outcome.
- Use Cloud Computing Services where needed and learn to work with them.
- Fullfill a Data Science Project requirements with a Data Team.
- Trying to understand and predict the box office of blockbuster (mainly) movies, wether independent or from a franchise.

## Ethics
[↑ Back to top](#table-of-contents)

Our idea is to have a non-biased model that does not get influenced by people's opinion, rather, can know the difference between the general sentiment and how well will it reflect the movie's success.

Regarding the ethics, our goal woudln't be to forcefeed certain movies, nor to dictate whatpeople should do/watch, it'd be to have, just another tool to decide what you may want to see.

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

#### Data Lake

Instead of following the classic paradigm of ETL, first extract the data, then transform it BEFORE loading it. Data Lakes strives for the ELT, extract the data, load it FIRST then transform it when you need to use it.

And we'll be using it to store all the (raw) data, that we collect in the span of the project. We'll be having Diogenes syndrome towards the data. We'd rather delete data than not having enough.

#### Data Warehouse

From this point forward we should have quality data, data that is "clean". Following the aforementioned ELT paradigm, a Data Warehouse is where the information will be loaded ONCE Transformed.

It will serve us as the main storage for our models, all the data that comes to this point, should and must be: clean, standarized, normalized and regularized. It should be as ready as possible for the model.

### Data Sources
[↑ To the section](#design)

- IMDB
- Twitter
- YouTube
- Reddit
- Google Trends

## Product
[↑ Back to top](#table-of-contents)

We're not going to sell anyting, but, our Product idea is to have a model that retrains with differente sources of information to display the outcome on the web and with some storytelling with the conclusion.

### Product Roadmap
[↑ To the section](#product)

#### Original estimation
[↑ To the section](#product)

The initial estimation, it should be updated with the real roadmap at the end.

![Roadmap](/pages/screenshots/home/Product%20Roadmap%2017-04-2022.png)
<p align="center">Initial product roadmap</p>

#### Real
[↑ To the section](#product)

**_The project has not yet been finished_**

### How is the Product managed?
[↑ To the section](#product)

We've splitted the product in different phases. The traditiona Product phases, and expanded the Data Science development ones:

#### Traditional
[↑ To the section](#product)

- Product Identification
- Product Planification
- Product Development
- Product Control
- Product Closure

#### Product Development
[↑ To the section](#product)

- Infrastructure
- Data Extraction
- Data Normalization
- Data Storage/Loading
- Data Cleansing
- Data Science/Modeling
- Data Visualization
- Deploy
- Documentation Draft
- Validation

## Methodology
[↑ Back to top](#table-of-contents)

SCRUM

- Kanban Board
- Planning Poker

### Product Owner
[↑ To the section](#methodology)

Pepe

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

- **Python**\
An easy-to-learn language chosen, mainly, because it's what the team's most comfortable with related to Big Data and A.I. technologies and it's usage. There were alternatives such as Scala, C++ or Java.

### ETL
[↑ To the section](#tech-stack)

1. **Node-RED**\
A light weight graph/node based npm package for flow development to connect services, such as, APIs, and IoT.
1. **Kafka**\
A data broker, one of the most used ones, if not the most used, meant to be used with Java or Scala, but can be interacted with through plugins, add-ons, and shell scripts
1. **Spark**\
A highly efficient cluster computation and paralelization. It's API allows for Python (PySpark), Java, Scala, R and SQL, which makes it a perfect fit for our team. It is in high demand nowadays.

### Database
[↑ To the section](#tech-stack)

- **MongoDB**\
An opensource NoSQL document based Database, it has a great community and multiple implementations and integrations.

### Cloud computing
[↑ To the section](#tech-stack)

- **AWS or Azure**\
Both great cloud computing services that offer similar services, each with their own pros and cons, but both are top notch in the world of cloud computing, data science and DaaS (Data as a Service)
- **Terraform (and maybe AWS CloudFormation)**\
IaC (Infrastructure as Code) is the way to go, cloudformation forces/restricts us to one service, but it is important that, however it is that we develop and deploy our cloud infrastructure, if ever, it is, cloud agnostic if possible, but easily replicable, and highly reliable, it should always produce the some output, the same outcome, without (as much) human mistake.

### Infrastructure
[↑ To the section](#tech-stack)

- **Docker**\
An open-source software container service that adds and extra layer of abstraction for packing software solutions
- **Compose**\
A cloud-agnostic standard for container orchestration maintained by Docker that is supported by: Docker Swarm, AWS ECS, Azure Container Instances, and many more.

## Usage
[↑ Back to top](#table-of-contents)

### Requirements
[↑ To the section](#usage)

- Docker
  - > Engine Version 20.10
  - > Compose Version 1.29.2
- Python
  - > \>= 3.6.x
- Node
  - > \>= v15.14.0

_All the images versions will be provided on each Dockerfile with the exact version, avoid the `latest` for security reasons, upgrades will be manual._

### Install the project
[↑ To the section](#usage)

Execute the following command on the folder you want to store the project in

```bash
git clone https://github.com/jofaval/tfm-iabd.git
cd tfm-iabd
```

And now configure the project's branches with Git flow

For Windows
```bash
cd tools/windows/git/
git-flow.bat
```

For Linux
```bash
cd tools/linux/git/
./git-flow.sh
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
- IMDB API
- YouTube API
- Reddit API
- Google Trends

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

The license used (MIT License) can be seen [here](./LICENSE) or you can read it locally by downloading the LICENSE file

## Legal Notice
[↑ Back to top](#table-of-contents)

All the data used is being used and stored up-to-date with the European Union's legislation, more precisely, to Span's laws which comply with E.U.'s law [GDPR (General Data Protection Regulation)](https://gdpr-info.eu/) and following the standards described at the [Charter of European Digital Rights (EDRi, EDR initiative)](https://edri.org/), surrounding the usage A.I. towards sentiment analysis and overall in the possible bias it may provide to the user. As to be ethical and prepare the model for the coming years.

For more information about the ethics of our model, please refer to the [Ethics' section](#ethics).

## Use of the Data
[↑ Back to top](#table-of-contents)

We plan to use the extracted data and it's provided data to better analyze the sentiments of users all around the world about the hype generated by a movie, wether is it's announcement, a trailer, some celeb talking about it.

By analyzing the general feeling, whether positive, negative, or neutral, we could determine if one user at a time, had a good or bad experience, they were hyped, or not.
So we can later influence our model towards the idea people have/had of the movie.

We'll collect the raw text data, if it's a thread, the more information we'll collect, so we can tokenize, lemmatize, preprocess and prepare the text.
Our methodology is to preprocess, and clean the data, tokenized it into a word embedding, and using Transformers, maybe Siamese Neural Networks, but surely mT5 HuggingFace BERT to make a Logic Consequence with NLI so that we can “classify the data”.

Maybe even reviews or the general feeling, in case of adaptations we'd have even more information.

And to display the conclusion obtained thanks to the insight of the data extracted. We’ll use personal websites, github of course, a medium article. We’d like to develop and research a paper so that we could more clearly provide, document and explain the results obtained and it’s conclusions.

As for the tools, Tableau, but maybe we could get PowerBI through studentship, it’s unclear at the moment.

## Credits
[↑ Back to top](#table-of-contents)

- Ismael, for the idea

## Gratitude
[↑ Back to top](#table-of-contents)

TODO