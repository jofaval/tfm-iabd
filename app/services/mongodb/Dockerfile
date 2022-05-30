# https://docs.docker.com/engine/reference/builder/
# Official doc: https://hub.docker.com/_/mongo
# TODO: configure

# Pull base image.
FROM mongo:latest


# Install Dependencies
RUN apt-get update && \
apt-get install -y dirmngr gnupg apt-transport-https ca-certificates curl  && \
apt-get update && \
apt-get install -y openssh-server sudo nano iputils-ping && \
useradd -ms /bin/bash admin && \
passwd -d admin && \
usermod -aG sudo admin

# Define default command.
CMD ["mongod"]

# Expose ports.
#   - 27017: process
#   - 28017: http
EXPOSE 27017
EXPOSE 28017