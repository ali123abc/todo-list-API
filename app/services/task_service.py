
from app.models.task import Task
from sqlalchemy.orm import Session
from app.schemas.task import TaskCreate, TaskUpdate
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_task(db: Session, task_data: TaskCreate) -> Task:
    new_task = Task(**task_data.model_dump())
    logger.info(f"Creating task with Title: {new_task.title}")
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task 

def get_task(db: Session, task_id: int) -> Task | None:
    logger.info(f"Retrieving task with ID: {task_id}")
    return db.query(Task).filter(Task.id == task_id).first()

def list_tasks(db: Session, skip: int = 0, limit: int = 10) -> list[Task]:
    logger.info(f"Listing tasks with skip: {skip} and limit: {limit}")
    return db.query(Task).offset(skip).limit(limit).all()

def update_task(db: Session, task_id: int, task_data: TaskUpdate) -> Task | None:
    logger.info(f"Updating task with ID: {task_id}")
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        logger.warning(f"Task with ID: {task_id} not found for update")
        return None
    for key, value in task_data.model_dump(exclude_unset=True).items():
        setattr(task, key, value)
    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task_id: int) -> bool:
    logger.info(f"Deleting task with ID: {task_id}")
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        logger.warning(f"Task with ID: {task_id} not found for deletion")
        return False
    db.delete(task)
    db.commit()
    return True