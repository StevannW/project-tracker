from datetime import datetime

from pydantic import BaseModel, Field

from app.core.enums import TaskStatus


class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: str | None = None
    status: TaskStatus
    remind_at: datetime | None = None


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: str | None = Field(None, min_length=1, max_length=255)
    description: str | None = None
    status: TaskStatus | None = None
    remind_at: datetime | None = None


class TaskResponse(TaskBase):
    id: int
    reminder_sent: bool
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }