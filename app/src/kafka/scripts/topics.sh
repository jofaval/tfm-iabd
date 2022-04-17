#!/bin/bash

# Creates a Kafka topic
# 
# Example:
# create_topic "tweets" 1 1 "localhost:9092"
# Creates a topic named tweets with 1 partition and 1 replica per partition, bootstrapped at localhost:9092
# 
# Doesn't return something
create_topic () {
    # The name of the topic
    topic_name=${1:-default_topic}

    # The number of partitions
    partitions=${2:-1}

    # The number of replicas per partitions
    replicas=${3:-1}

    # The bootstrap server address
    server=${4:-localhost:9092}

    echo It will create a Kafka topic named "$topic_name" with $partitions partition(s) and $replicas replica(s) per partition, bootstrap at "$server"

    /opt/kafka/bin/kafka-topics.sh --create --bootstrap-server $server --replication-factor $replicas --partitions $partitions --topic "$topic_name"

    echo Kafka topic successfully created!
}

# Usage Example
create_topic "tweets" 1 1 "localhost:9092"