# Use the official Python image as the base image
FROM python:3.12.3

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the working directory
COPY . /app

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Install the application dependencies
RUN pip install -r requirements.txt

# Define the entry point for the container
CMD ["python", "My_blog/manage.py", "runserver", "0.0.0.0:8000"]
