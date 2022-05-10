#!/bin/bash

# Creates a Kafka producer
# 
# Example:
# create_producer "tweets" "localhost:9092" "Hello World!"
# Creates a producer for the topic tweets bootstrapped at localhost:9092 with the message Hello World!
# 
# Doesn't return something
create_producer () {
    # The name of the producer
    topic=${1:-default_producer}

    # The bootstrap server address
    server=${2:-localhost:9092}

    # The message to produce
    message=${3:-Default}

    echo It will create a Kafka producer for the topic "$topic" bootstrapped at "$server", with the message "$message"

    /opt/kafka/bin/kafka-console-producer.sh --topic "$topic" --bootstrap-server $server
    $message

    echo Kafka producer successfully created!
}

# Usage Example
create_producer "tweets" "localhost:9092" "Hello World!"