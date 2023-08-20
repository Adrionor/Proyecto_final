# Use the Python 3.11 slim base image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy the API code into the container
COPY api.py .

# Install dependencies
RUN pip install fastapi numpy

# Expose port 8000
EXPOSE 8000

# Set the entry point command to run the API
CMD ["python", "api.py"]