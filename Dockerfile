# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install system-level dependencies required for building Python packages
# - gcc and build-essential are compilers
# - default-libmysqlclient-dev provides the MySQL development files
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    pkg-config \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*
# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY app/requirements.txt .

# Install any needed packages specified in requirements.txt
# This will now succeed because the build tools are present.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's source code from the 'app' directory
COPY app/ .

# Expose port 5000 to allow traffic to the Flask application
EXPOSE 5000

# Define the command to run your app
CMD ["python", "app.py"]
