# Use the official Python image as the base image
FROM python:3.12.3

# Create a user and group 'appuser'
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the working directory
COPY . /app

# Change the ownership of the files to the non-root user
RUN chown -R appuser:appuser /app

# Switch to the non-root user
USER appuser

# Upgrade pip to the latest version
RUN pip install --user --upgrade pip

# Install the application dependencies
RUN pip install --user -r /app/requirements.txt

# Define the entry point for the container, updating the path to manage.py
CMD ["python", "My_blog/manage.py", "runserver", "0.0.0.0:8000"]
