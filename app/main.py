from fastapi import FastAPI
from contextlib import asynccontextmanager
from alembic.config import Config
from alembic import command
from .routes import router
import os
import logging

logger = logging.getLogger("uvicorn.error")

def run_migrations():
    if os.path.exists("alembic.ini"):
        alembic_cfg = Config("alembic.ini")
        command.upgrade(alembic_cfg, "head")

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        logger.info("Attempting to connect to the database and run migrations...")
        run_migrations()
        logger.info("✅ Database connected and initialized successfully!")
    except Exception as e:
        logger.error(f"❌ Database connection or migration failed: {e}")
        raise e
        
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(router)