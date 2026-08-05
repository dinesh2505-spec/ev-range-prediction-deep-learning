
# Use official Python image
FROM python:3.11-slim


# Set working directory inside container
WORKDIR /app


# Copy dependency file
COPY requirements-docker.txt .


# Install Python dependencies
RUN pip install --no-cache-dir -r requirements-docker.txt


# Copy project files
COPY app ./app
COPY src ./src
COPY models ./models


# Expose FastAPI port
EXPOSE 8000


# Start FastAPI application
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]