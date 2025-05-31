# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements/ /app/requirements

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r /app/requirements/production.txt

# Copy the rest of the application code into the container
COPY . /app

# Set environment variables
# Copy the entrypoint script
COPY entrypoint.sh /app/entrypoint.sh

# Make entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Set the entrypoint script
ENTRYPOINT ["/app/entrypoint.sh"]