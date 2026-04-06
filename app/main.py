from fastapi import FastAPI
from app.routes.task import router as task_router
import logging

logging.basicConfig(level=logging.INFO)


app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "healthy"}

app.include_router(task_router)