from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .db import Base

class APILog(Base):
    __tablename__ = "api_logs"

    id = Column(Integer, primary_key=True, index=True)
    endpoint = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)