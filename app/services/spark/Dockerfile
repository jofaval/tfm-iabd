# https://docs.docker.com/engine/reference/builder/
# Official doc: https://hub.docker.com/r/bitnami/spark

# Pull base image.
FROM bitnami/spark:3-debian-10

USER root

# Install the common utilities.
COPY commons.sh .
RUN ./commons.sh

# Define working directory.
WORKDIR /home/admin
