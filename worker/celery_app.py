from celery import Celery
from app.config import REDIS_URL

celery = Celery(
    "worker",
    broker=REDIS_URL,
    backend=REDIS_URL
)

celery.conf.beat_schedule = {
    "delete-old-logs-daily": {
        "task": "worker.tasks.delete_old_logs",
        "schedule": 86400.0,
    },
}