# Use an official Python runtime as a parent image
FROM python:3.12.1-slim-bookworm

# Define environment variables
ENV NAME wikiwikiwrap
ENV FLASK_ENV production

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in pyproject.toml
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME wikiwikiwrap

# Run app.py when the container launches
CMD ["gunicorn", "-b", ":5000", "--access-logfile", "-", "--error-logfile", "-", "wikiwikiwrap:create_app()"]
