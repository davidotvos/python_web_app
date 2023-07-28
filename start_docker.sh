#!/bin/bash

# Set the Docker image name and tag
DOCKER_IMAGE="davidotvos/python_web_app"
DOCKER_TAG="latest"

# Set the container name
CONTAINER_NAME="python_web_app_container"

# Start Docker container
docker run -d -p 5000:5000 --name "${CONTAINER_NAME}" "${DOCKER_IMAGE}:${DOCKER_TAG}"
