from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.services.task_service import (create_task as create_task_service, 
                                        get_task as get_task_service,
                                        list_tasks as list_tasks_service,
                                        update_task as update_task_service,
                                        delete_task as delete_task_service)

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", response_model=TaskResponse, status_code=201)
def create_task_endpoint(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task_service(db, task)

@router.get("/{task_id}", response_model=TaskResponse)
def get_task_endpoint(task_id: int, db: Session = Depends(get_db)):
    task = get_task_service(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.get("/", response_model=list[TaskResponse])
def list_tasks_endpoint(skip: int= Query(0, ge=0),
                        limit: int= Query(10, ge=1, le=100),
                        db: Session = Depends(get_db)):
    return list_tasks_service(db, skip=skip, limit=limit)

@router.put("/{task_id}", response_model=TaskResponse)
def update_task_endpoint(task_id: int, task_data: TaskUpdate, db: Session = Depends(get_db)):
    task = update_task_service(db, task_id, task_data)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/{task_id}", status_code=204)
def delete_task_endpoint(task_id: int, db: Session = Depends(get_db)):
    task = delete_task_service(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task