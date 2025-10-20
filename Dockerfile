FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DOCKER_ENV=true

# Install system dependencies (if needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app/app

# Create non-root user for security
RUN useradd -m -u 1000 appuser

# Create logs directory and set permissions BEFORE switching user
RUN mkdir -p /app/logs && chown -R appuser:appuser /app

USER appuser

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]