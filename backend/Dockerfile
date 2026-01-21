# Base image: Python 3.12.4 slim version to match your dev environment
FROM python:3.12.4-slim

# Set the working directory inside the container
WORKDIR /app

# Set environment variables
# PYTHONDONTWRITEBYTECODE: Prevents Python from writing pyc files to disc
# PYTHONUNBUFFERED: Prevents Python from buffering stdout and stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy requirements file first to leverage Docker layer caching
COPY requirements.txt .

# Install dependencies
# --no-cache-dir reduces image size by not storing the cache
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the application source code and model
# Based on your image, these are all in the root of 'backend'
# 
COPY main.py featureEngineering.py modelWithPipeline.joblib ./

# Expose the port Uvicorn will run on
EXPOSE 8000

# Command to run the application
# Assumes your FastAPI instance in main.py is named 'app'
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]