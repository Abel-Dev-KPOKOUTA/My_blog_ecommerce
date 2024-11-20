# Use the official Python image as the base image
FROM python:3.12.3

# Create a user and group 'appuser'
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the working directory
COPY . /app

# Change the ownership of the necessary directories
RUN chown -R appuser:appuser /app /home/appuser

# Switch to the non-root user
USER appuser

# Upgrade pip without using cache
RUN pip install --no-cache-dir --upgrade pip

# Install the application dependencies without using cache
RUN pip install --no-cache-dir -r /app/requirements.txt

# Define the entry point for the container
CMD ["python", "My_blog/manage.py", "runserver", "0.0.0.0:8000"]
