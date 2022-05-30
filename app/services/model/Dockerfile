# https://docs.docker.com/engine/reference/builder/
# Official doc: https://hub.docker.com/r/tensorflow/tensorflow/

# Pull base image.
FROM jupyter/tensorflow-notebook:latest

#Copy files and requirements
COPY ./files/"MoviesModel_v1_5_(ML).ipynb" /home/jovyan/work
COPY ./files/requirements.txt .
#Install requirements
RUN pip install --no-cache-dir --upgrade pip && \
pip install --no-cache-dir -r requirements.txt
USER root
RUN chmod 777 "/home/jovyan/work/MoviesModel_v1_5_(ML).ipynb"

#Expose port
EXPOSE 8888