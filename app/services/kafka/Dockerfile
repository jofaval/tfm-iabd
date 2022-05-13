# https://docs.docker.com/engine/reference/builder/
# Official doc: https://hub.docker.com/r/bitnami/kafka/

FROM bitnami/kafka:2.8-debian-10

# Copy all the utilities scripts
COPY ./kafka/scripts/linux/boot.sh /scripts/linux/boot.sh
COPY ./kafka/scripts/linux/consumers.sh /scripts/linux/consumers.sh
COPY ./kafka/scripts/linux/producers.sh /scripts/linux/producers.sh
COPY ./kafka/scripts/linux/topics.sh /scripts/linux/topics.sh
COPY ./kafka/scripts/data/topics.txt /scripts/data/topics.txt

# Execute all the commands needed when booted up
RUN boot.sh