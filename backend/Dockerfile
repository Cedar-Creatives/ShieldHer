# Backend Dockerfile
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements/production.txt requirements/production.txt
COPY requirements/base.txt requirements/base.txt
RUN pip install --upgrade pip && \
    pip install -r requirements/production.txt

# Copy project
COPY . .

# Create necessary directories
RUN mkdir -p staticfiles media

# Collect static files
RUN python manage.py collectstatic --noinput --settings=config.settings.production || true

# Copy entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Expose port
EXPOSE 8000

# Run entrypoint script
ENTRYPOINT ["/entrypoint.sh"]
