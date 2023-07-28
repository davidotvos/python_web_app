FROM python:3.8-slim-buster

# Set working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port
EXPOSE 5000

# Command to run the application
CMD gunicorn -b localhost:5000 app:app
