# https://docs.docker.com/engine/reference/builder/
# Official doc: https://hub.docker.com/_/mongo
# TODO: configure

# Pull base image.
FROM debian:latest

# Install MongoDB.
RUN \
  apt-get update && \
  apt-get install -y dirmngr gnupg apt-transport-https software-properties-common ca-certificates curl && \
  curl -fsSL https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add - && \
  add-apt-repository 'deb https://repo.mongodb.org/apt/debian buster/mongodb-org/4.2 main' && \
  apt-get update && \
  apt-get install -y mongodb-org openssh-server sudo && \
  useradd -ms /bin/bash admin && \
  passwd -d admin && \
  mkdir -p /data/db && \
  chmod 777 /data/db
  
# User without pass  
USER admin 


# Start mongo and ssh services when docker starts  
CMD service mongod start && service ssh start

# Define working directory.
WORKDIR /home/admin

# Define default command.
CMD ["mongod"]

# Expose ports.
#   - 27017: process
#   - 28017: http
EXPOSE 27017
EXPOSE 28017
