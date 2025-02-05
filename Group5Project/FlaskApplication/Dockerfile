# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the entire current directory contents into the container at /app
COPY . .

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# If you have other requirements in subdirectories, install them too
# Uncomment the following line if you have a requirements.txt in other_subdirectory
# RUN pip install --no-cache-dir -r other_subdirectory/requirements.txt

# Command to run your application
CMD ["python", "app.py"]  # Change this if you want to run a different script
