# https://docs.docker.com/engine/reference/builder/
# Official doc: https://hub.docker.com/r/tensorflow/tensorflow/

# Pull base image.
FROM tensorflow/tensorflow:latest

# Install packages.
RUN \
  apt-get update && \
  apt-get update && \
  apt-get install -y openssh-server sudo et-tools nano iputils-ping && \
  useradd -ms /bin/bash  admin && \
  passwd -d admin

  
# User without pass  
USER admin 

# Define working directory.
WORKDIR /home/admin
