# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and app code
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Make sure logs and uploads dirs exist
RUN mkdir -p /app/logs /app/uploads

# Declare /app/logs as a Docker volume
VOLUME ["/app/logs"]

# Expose port 8000
EXPOSE 8000

# Start FastAPI application using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
