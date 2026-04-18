# eHealth4everyone-test-project

## Overview

This project is a backend application built with FastAPI that demonstrates:

* Scheduled background tasks using Celery
* API response caching using Redis
* Logging and cleanup of API request data

---

## Features

### 1. API Logging

All incoming API requests are logged into a database with timestamps.

### 2. Scheduled Task

A background worker (Celery) runs periodically to delete logs older than 30 days.

### 3. Caching

External API responses are cached using Redis with a TTL (Time-To-Live) of 1 hour to improve performance.

### 4. API Endpoint

* `GET /data` → Returns cached external API data

---

## Tech Stack

* FastAPI
* Redis
* Celery
* SQLAlchemy
* Alembic (Database Migrations)
* PostgreSQL

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/DekunleJr/eHealth4everyone-test-project.git
cd eHealth4everyone-test-project
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Environment Variables

Copy the example environment variables file and update it with your PostgreSQL credentials and Redis host:

```bash
cp .env.example .env
```

*Note: The app uses Alembic to manage the database schema. When you start the FastAPI server, it will automatically run the migrations and create the `api_logs` table for you!*

### 4. Start Redis

```bash
redis-server
```

### 5. Run FastAPI Server

```bash
uvicorn app.main:app --reload
```

### 6. Start Celery Worker

```bash
celery -A worker.celery_app.celery worker --loglevel=info --pool=solo
```

### 7. Start Celery Beat Scheduler

```bash
celery -A worker.celery_app.celery beat --loglevel=info
```

---

## How It Works

* When `/data` is called:

  * The system checks Redis cache
  * If cached → returns instantly
  * If not → fetches from external API and caches it

* Celery runs daily to:

  * Delete logs older than 30 days

---

## Notes

* Cache expires automatically every 1 hour using Redis TTL
* Logging ensures traceability of API usage
* Background tasks ensure database stays clean

---