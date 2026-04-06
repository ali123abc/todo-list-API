from fastapi import FastAPI
from app.routes.task import router as task_router
from app.db.session import engine
from app.db.base import Base
from app.models.task import Task
from contextlib import asynccontextmanager
import logging

logging.basicConfig(level=logging.INFO)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code: create tables if they don't exist
    Base.metadata.create_all(bind=engine)
    yield
    # Shutdown code (if needed)

app = FastAPI(lifespan=lifespan)

@app.get("/health")
def health_check():
    return {"status": "healthy"}

app.include_router(task_router)