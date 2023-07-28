#!/bin/bash

# Set the container name
CONTAINER_NAME="python_web_app_container"

# Stop and remove Docker container
docker stop "${CONTAINER_NAME}"
