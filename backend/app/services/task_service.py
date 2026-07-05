from sqlalchemy.orm import Session

from app.models.task import Task
from app.schemas.task import TaskCreate
from app.schemas.task import TaskUpdate


class TaskService:

    @staticmethod
    def get_all(db: Session):
        return db.query(Task).all()

    @staticmethod
    def get_by_id(db: Session, task_id: int):
        return db.query(Task).filter(Task.id == task_id).first()

    @staticmethod
    def create(db: Session, task: TaskCreate):

        db_task = Task(**task.model_dump())
        db.add(db_task)
        db.commit()
        db.refresh(db_task)

        return db_task

    @staticmethod
    def _to_timestamp(dt):
        """Convert a datetime to a UTC timestamp for safe comparison,
        handling both timezone-aware and timezone-naive datetimes."""
        if dt is None:
            return None
        return dt.timestamp()

    @staticmethod
    def update(
        db: Session,
        db_task: Task,
        task: TaskUpdate
    ):

        data = task.model_dump(exclude_unset=True)

        old_remind_ts = TaskService._to_timestamp(db_task.remind_at)

        for key, value in data.items():
            setattr(db_task, key, value)

        if "remind_at" in data:
            new_remind_ts = TaskService._to_timestamp(db_task.remind_at)
            if old_remind_ts != new_remind_ts:
                db_task.reminder_sent = False

        db.commit()
        db.refresh(db_task)

        return db_task

    @staticmethod
    def delete(
        db: Session,
        db_task: Task
    ):

        db.delete(db_task)
        db.commit()