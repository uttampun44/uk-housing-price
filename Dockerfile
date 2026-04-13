# Use Python 3.10+ base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies (if needed for matplotlib, etc.)
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project (but volumes will override this at runtime)
COPY . .

# Create outputs directory if it doesn't exist
RUN mkdir -p outputs/charts

# Default command: run the analysis
CMD ["python", "main.py"]
