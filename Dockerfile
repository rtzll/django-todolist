# Use the Python 3.9 base image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy all files and folders from the root of the project into /app
COPY . /app

# Install Python dependencies from requirements.txt
RUN pip install -r /app/requirements.txt

# Run database migrations
RUN python manage.py migrate

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
