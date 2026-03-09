# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables to optimize Python operations
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container at /usr/src/app
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ARG CACHE_BUSTER=default-value
# Copy the rest of the application source code into the container
COPY ./app/ /usr/src/app/app

# Define the command to run the application
EXPOSE 80

CMD ["fastapi", "run", "app/main.py", "--port", "80"]
