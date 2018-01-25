# Define an os and a python
FROM python:3.5.2-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Make port 9000 available to the world outside this container
EXPOSE 9000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "Main.py"]