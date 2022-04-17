#!/bin/bash

# Creates a Kafka consumer
# 
# Example:
# create_consumer "tweets" "localhost:9092"
# Creates a consumer for the topic tweets bootstrapped at localhost:9092
# 
# Doesn't return something
create_consumer () {
    # The name of the consumer
    topic=${1:-default_consumer}

    # The bootstrap server address
    server=${2:-localhost:9092}

    echo It will create a Kafka consumer for the topic "$topic" bootstrapped at "$server"

    /opt/kafka/bin/kafka-console-consumer.sh --topic "$topic" --from-beginning --bootstrap-server $server
    $message

    echo Kafka consumer successfully created!
}

# Usage Example
create_consumer "tweets" "localhost:9092"