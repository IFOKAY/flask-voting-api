# Use the official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt /app/

# Install dependencies
RUN pip install -r requirements.txt

# Copy all files
COPY . /app/

# Expose the port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
