from datetime import datetime, timedelta
from app.db import SessionLocal
from app.models import APILog
from .celery_app import celery

@celery.task
def delete_old_logs():
    db = SessionLocal()
    try:
        cutoff = datetime.utcnow() - timedelta(days=30)

        deleted_count = db.query(APILog).filter(APILog.created_at < cutoff).delete()
        db.commit()
        return f"Deleted {deleted_count} old logs"
    finally:
        db.close()