# https://docs.docker.com/engine/reference/builder/
# Official doc: https://hub.docker.com/_/mongo

# TODO: configure

# Pull base image.
FROM debian:latest

# Install MongoDB.
RUN \
  apt-get install gnupg2 wget -y && \
  wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | apt-key add - echo "deb http://repo.mongodb.org/apt/debian buster/mongodb-org/4.4 main" | tee /etc/apt/sources.list.d/mongodb-org-4.4.list && \
  apt-get update && \
  apt-get install -y mongodb-org openssh-server && \
  rm -rf /var/lib/apt/lists/* && \
  systemctl enable ssh && \
  systemctl restart mongod


# Define working directory.
WORKDIR /data

# Define default command.
CMD ["mongod"]

# Expose ports.
#   - 27017: process
#   - 28017: http
EXPOSE 27017
EXPOSE 28017
