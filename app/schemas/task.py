from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

class TaskBase(BaseModel):
    description: str | None = Field(default=None, max_length=2000)

class TaskCreate(TaskBase):
    title: str = Field(..., min_length=1, max_length=200)


class TaskUpdate(TaskBase):
    title: str | None = Field(default=None, min_length=1, max_length=200)
    completed: bool | None = None

class TaskResponse(TaskBase):
    id: int
    title: str
    completed: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)