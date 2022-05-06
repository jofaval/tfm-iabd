# https://docs.docker.com/engine/reference/builder/
# Official doc: https://hub.docker.com/r/bitnami/spark

# Pull base image.
FROM bitnami/spark:3-debian-10

USER root

# Install packages.
RUN \
 apt-get update && \
 apt-get install -y openssh-server sudo nano iputils-ping && \
 useradd -ms /bin/bash  admin && \
 passwd -d admin && \
 usermod -aG sudo admin
 

# Define working directory.
WORKDIR /home/admin
