from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.schemas.task import TaskCreate, TaskUpdate
from app.models.task import Task
import logging

logger = logging.getLogger(__name__)

def create_task(db: Session, task_data: TaskCreate) -> Task:
    '''Creates a new task in the database.
        Args:        
            db: Database session
            task_data: TaskCreate schema with task details
        Returns:
            The created Task object if successful, otherwise raises an exception.
    '''
    new_task = Task(**task_data.model_dump())
    logger.info("Creating task with title: %s", new_task.title)
    try:
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        logger.info("Task created with id: %s", new_task.id)
    except SQLAlchemyError:
        logger.exception("Error creating task with title: %s", new_task.title)
        db.rollback()
        raise
    return new_task

def get_task(db: Session, task_id: int) -> Task | None:
    '''Retrieves a task by its ID.
        Args:
            db: Database session
            task_id: ID of the task to retrieve
        Returns:
            The Task object if found, otherwise None.
    '''
    logger.info("Retrieving task with id: %s", task_id)
    return db.query(Task).filter(Task.id == task_id).first()

def list_tasks(db: Session, skip: int = 0, limit: int = 10) -> list[Task]:
    '''Lists tasks with pagination.
        Args:
            db: Database session
            skip: Number of tasks to skip
            limit: Maximum number of tasks to return
        Returns:
            A list of Task objects
    '''
    logger.info("Listing tasks with skip: %s and limit: %s", skip, limit)
    return db.query(Task).offset(skip).limit(limit).all()

def update_task(db: Session, task_id: int, task_data: TaskUpdate) -> Task | None:
    '''Updates an existing task.
        Args:
            db: Database session
            task_id: ID of the task to update
            task_data: TaskUpdate schema with updated task details
        Returns:
            The updated Task object if successful, otherwise None.
    '''
    logger.info("Updating task with id: %s", task_id)
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        logger.warning("Task with id: %s not found for update", task_id)
        return None
    logger.info("Task with id: %s retrieved", task_id)
    for key, value in task_data.model_dump(exclude_unset=True).items():
        setattr(task, key, value)
    try:
        db.commit()
        db.refresh(task)
        logger.info("Task with id: %s updated successfully", task_id)
    except SQLAlchemyError:
        logger.exception("Error updating task with id: %s", task_id)
        db.rollback()
        raise
    return task

def delete_task(db: Session, task_id: int) -> bool:
    '''Deletes a task by its ID.
        Args:
            db: Database session
            task_id: ID of the task to delete
        Returns:
            True if the task was deleted successfully, otherwise False.
    '''
    logger.info("Deleting task with id: %s", task_id)
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        logger.warning("Task with id: %s not found for deletion", task_id)
        return False
    try:
        db.delete(task)
        db.commit()
        logger.info("Task with id: %s deleted successfully", task_id)
    except SQLAlchemyError:
        logger.exception("Error deleting task with id: %s", task_id)
        db.rollback()
        raise
    return True