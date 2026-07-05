from enum import Enum
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Enum as SqlEnum
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.sql import func
from app.core.enums import TaskStatus
from app.db.database import Base
from sqlalchemy import Boolean
from sqlalchemy.orm import relationship


class Task(Base):
    __tablename__ = "tasks"

    notifications = relationship(
        "Notification",
        back_populates="task",
        cascade="all, delete-orphan"
    )

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(255), nullable=False)

    description = Column(String)

    status = Column(
    SqlEnum(TaskStatus),
    nullable=False,
    default=TaskStatus.TODO,
    index=True
)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    remind_at = Column(
    DateTime(timezone=True),
    nullable=True
)
    reminder_sent = Column(
        Boolean,
        nullable=False,
        default=False
    )

    def __repr__(self):
        return f"<Task(id={self.id}, title='{self.title}')>"