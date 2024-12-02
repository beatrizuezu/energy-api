# Use the official slim Python image for a smaller base
FROM python:3.11-slim

# Install system dependencies required for psycopg2
RUN apt-get update && apt-get install -y \
    libpq-dev gcc && apt-get clean

# Set the working directory inside the container
WORKDIR /app

# Copy the lock file to the container
COPY requirements.lock ./

# Install dependencies using pip from the lock file
RUN PYTHONDONTWRITEBYTECODE=1 pip install --no-cache-dir psycopg2-binary -r requirements.lock

# Copy the rest of the project files into the container
COPY src /app/src

# Command to run your Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
