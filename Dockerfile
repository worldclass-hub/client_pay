FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV WEB_CONCURRENCY=2

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# ✅ Render automatically sets $PORT environment variable
CMD gunicorn worldbank.wsgi:application \
    --bind 0.0.0.0:$PORT \
    --timeout 120 \
    --workers $WEB_CONCURRENCY \
    --preload