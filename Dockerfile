# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Add only requirements first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

# The `--no-cache-dir` option will prevent the caching of pip's packages, 
# which will reduce the overall size of the image.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the codebase into the container
COPY . /app

# This exposes port 5555 on the container
EXPOSE 5555

# Define the command that should be executed when the container is run.
CMD [ "python", "app.py" ]

