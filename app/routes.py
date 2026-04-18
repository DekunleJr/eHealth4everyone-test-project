from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .cache import get_external_data
from .db import SessionLocal
from .models import APILog

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def log_request(db: Session, endpoint: str):
    log = APILog(endpoint=endpoint)
    db.add(log)
    db.commit()

@router.get("/data")
def fetch_data(db: Session = Depends(get_db)):
    data = get_external_data()
    log_request(db, "/data")
    return data