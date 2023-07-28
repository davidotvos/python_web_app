# Python Web Application


## Overview

This is a simple Python web application that accepts POST requests with a parameter named 'string' and returns the same string with swapped case in the response body.


## Requirements

- Python 3.8 or higher
- Docker
- Ubuntu 20.04 (for shell scripts)


## Installation and Setup

1. Clone this repository to your local machine:

```
git clone https://github.com/davidotvos/python_web_app.git
cd python_web_app
```

2. Install the required Python dependencies:

```
pip install -r requirements.txt
```


## Testing

To run the test cases for the application, execute the following command:
```
pytest tests/
```


## Running the Application Locally

To run the application locally, use the following command:

```
python app.py
```

The application will be available at http://127.0.0.1:5000/.


## Docker Usage

Before using Docker, make sure it's installed on your system.


### Build Docker Image

To build the Docker image containing the application, run the following script:

```
bash build_docker.sh
```


### Start Docker Container

To start the Docker container, run the following script:

```
bash start_docker.sh
```


The application will be accessible at http://localhost:5000/.


### Stop Docker Container

To stop and remove the Docker container, run the following script:

```
bash stop_docker.sh
```


## Deployment

To deploy the application to a production environment, you can use any Docker-compatible hosting service like AWS, GCP, or Azure.


