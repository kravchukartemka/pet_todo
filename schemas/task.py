from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field, ConfigDict
from schemas.enums import TaskPriority


model_config = ConfigDict(
    from_attributes=True
)


class TaskCreate(BaseModel):
    title: str = Field(
        min_length=1,
        max_length=255,
        description="Task title"
    )

    description: str | None = Field(
        default=None,
        max_length=2000,
        description="Task description"
    )

    priority: TaskPriority = Field(
        default=TaskPriority.MEDIUM,
        description="Task priority"
    )


class TaskUpdate(BaseModel):
    title: str | None = Field(
        default=None,
        min_length=1,
        max_length=255,
        description="Task title"
    )

    description: str | None = Field(
        default=None,
        max_length=2000,
        description="Task description"
    )

    priority: TaskPriority | None = Field(
        default=None,
        description="Task priority"
    )


class TaskResponse(BaseModel):
    id: int
    title: str = Field(
        min_length=1,
        max_length=255,
        description="Task title"
    )

    description: str | None = Field(
        default=None,
        max_length=2000,
        description="Task description"
    )

    priority: TaskPriority = Field(
        description="Task priority"
    )
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TaskFilter(BaseModel):
    limit: int = 20
    offset: int = 0
    sort_by: str | None = None
    order_by: Literal["asc", "desc"] = "desc"
    priority: TaskPriority | None = None
    search: str | None = None
