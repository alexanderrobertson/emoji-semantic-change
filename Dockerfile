# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Ensures Python output is sent straight to the terminal without buffering
ENV PYTHONUNBUFFERED 1
# Set the port the app will run on
ENV PORT 8080

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Command to run the application
# Gunicorn will look for the 'server' variable in the 'app.py' file.
# The :$PORT binding is required by Cloud Run.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:server
