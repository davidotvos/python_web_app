#!/bin/bash

# Set the Docker image name and tag
DOCKER_IMAGE="davidotvos/python_web_app"
DOCKER_TAG="latest"

# Build the Docker image
docker build -t "${DOCKER_IMAGE}:${DOCKER_TAG}" .