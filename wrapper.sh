#!/bin/bash
# Container name
container_name="di2020_clint"
# Stop contianer
docker stop $container_name
# Delete contianer
docker rm -f $container_name
# Delete image
docker rmi -f $container_name
# Build container
docker image build -t $container_name .
# Run container
docker run --rm -ti --name $container_name $container_name 
