from datetime import datetime
from typing import Optional

from sqlalchemy import String, Text, Enum, func
from sqlalchemy.orm import Mapped, mapped_column

from db.base import Base
from schemas.enums import TaskPriority
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Task(Base):

    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    title: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )

    description: Mapped[str] = mapped_column(
        Text
    )

    priority: Mapped[TaskPriority] = mapped_column(
        Enum(TaskPriority),
        nullable=False
    )

    owner_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )

    owner: Mapped["User"] = relationship(
        back_populates="tasks",
    )

    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )
