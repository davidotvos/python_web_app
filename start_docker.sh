#!/bin/bash

# Start Docker container
docker run -d -p 5000:5000 --name web_app_container web_app_image
