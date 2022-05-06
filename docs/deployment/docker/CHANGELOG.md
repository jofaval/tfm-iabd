# CHANGELOG #
All the log of changes on the Docker infrastrucure

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
and this CHANGELOG adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 0.x.x

### Major - 0.16.0 (2022-05-04)

#### Features

- Implemented the base Keras Dockerfile, which uses GPU.

### Major - 0.15.0 (2022-05-03)

#### Features

- Implemented the base MongoDB Dockerfile.

### Major - 0.14.0 (2022-04-22)

#### Features

- Implemented the base ELK stack, which includes:
  - Elasticsearch
  - Logstash
  - Kibana

### Patch - 0.13.0 (2022-04-22)

#### Fixes

- The base build path is now services
- The images' context now uses the `BUILD_GLOBAL_PATH` constant

### Minor - 0.12.6 (2022-04-17)

#### Features

- Changed the order of the docker compose services arguments

### Major - 0.12.5 (2022-04-17)

#### Features

- Added built image name and version configuration

### Minor - 0.12.4 (2022-04-17)

#### Features

- Changed `ports` to `expose` so that some services are private
- Fix incorrect `spark-master` container name dependency on `mongo-db`
- Standarize the formatting

### Major - 0.12.0 (2022-04-17)

#### Features

- Added frontend container (node/vue image)

### Major - 0.11.0 (2022-04-17)

#### Features

- Added backend container (FastAPI image)

### Major - 0.10.0 (2022-04-17)

#### Features

- The deployment, wether with Docker Swarm, AWS ECS or Azure Container Instances, is now configure for scalability and the use of self load balancing

### Minor - 0.9.0 (2022-04-16)

#### Features

- The order of the services parameters has been standarized so they're the same

### Major - 0.8.0 (2022-04-16)

#### Features

- ZooKeeper and Spark are now properly configured
- Some new `.env` variables are now in use
- The environment section's formatting of each service has been changed. This may be breaking
- Kafka now has a configured boot shell script (`boot.sh`)

### Minor - 0.7.5 (2022-04-04)

#### Features

- Now the docker services have a forced name

### Major - 0.7.0 (2022-04-03)

#### Features

- The containers will always remian up, if there was a crash, they will get up in motion again.

### Major - 0.6.0 (2022-04-03)

#### Features

- The environment variables and boot-up commands are now set.

### Major - 0.5.0 (2022-04-03)

#### Features

- The ports are set up so that they won't crash with one another.

### Major - 0.4.0 (2022-04-03)

#### Features

- The dependencies are now properly set up so that whenever an images is built, it will go up at the right time.

### Major - 0.3.0 (2022-04-03)

#### Features

- The network is now fully implemented.

### Major - 0.2.0 (2022-04-03)

#### Features

- The volumes have now been configured.

### Major - 0.1.0 (2022-04-03)

#### Features

- The building images are referenced.

### Major - 0.0.0 (2022-03-23)

#### Features

- Base Docker-Compose created from the official documentation.