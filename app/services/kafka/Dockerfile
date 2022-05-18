# https://docs.docker.com/engine/reference/builder/
# Official doc: https://hub.docker.com/r/bitnami/kafka/

FROM bitnami/kafka:2.8-debian-10

# Copy all the utilities scripts
COPY ./scripts/linux/boot.sh /scripts/linux/boot.sh
COPY ./scripts/linux/consumers.sh /scripts/linux/consumers.sh
COPY ./scripts/linux/producers.sh /scripts/linux/producers.sh
COPY ./scripts/linux/topics.sh /scripts/linux/topics.sh
COPY ./scripts/linux/data/topics.txt /scripts/data/topics.txt

# Execute all the commands needed when booted up
#RUN boot.sh