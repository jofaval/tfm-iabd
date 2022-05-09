# https://docs.docker.com/engine/reference/builder/
# Official doc: https://hub.docker.com/_/mongo
# TODO: configure

# Pull base image.
FROM debian:latest


# Install MongoDB.
COPY ./mongodb/scripts/linux/install.sh .
RUN ./install.sh

# Install the common utilities.
COPY commons.sh .
RUN ./commons.sh

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