FROM python:3.11-slim

WORKDIR /app

# Install system dependencies required for Selenium / browser automation
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    curl \
    unzip \
    libglib2.0-0 \
    libnss3 \
    libfontconfig1 \
    libxi6 \
    libxrender1 \
    libxext6 \
    libx11-6 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (better caching)
COPY requirements.txt .

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Default command to run tests
CMD ["pytest", "tests", "-v"]