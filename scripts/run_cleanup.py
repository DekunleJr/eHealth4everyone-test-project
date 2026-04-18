import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from worker.tasks import delete_old_logs

if __name__ == "__main__":
    result = delete_old_logs.delay()
    print(f"Cleanup task dispatched to Celery. Task ID: {result.id}")