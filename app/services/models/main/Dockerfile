# https://docs.docker.com/engine/reference/builder/
# Official doc: https://hub.docker.com/r/tensorflow/tensorflow/

# Pull base image.
FROM tensorflow/tensorflow:2.9.0rc2-gpu

# Install the common utilities.
COPY commons.sh .
RUN ./commons.sh  

# User without pass  
USER admin 

# Define working directory.
WORKDIR /home/admin
