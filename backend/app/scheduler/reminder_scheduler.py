from datetime import datetime, timezone

from app.db.database import SessionLocal
from app.models.notification import Notification
from app.models.task import Task


def check_reminders():

    # print("Checking reminders...")

    db = SessionLocal()

    try:

        now = datetime.now(timezone.utc)

        tasks = (
            db.query(Task)
            .filter(
                Task.status == "Todo",
                Task.remind_at.is_not(None),
                Task.reminder_sent == False,
                Task.remind_at <= now,
            )
            .all()
        )

        # print(f"Found {len(tasks)} reminder(s).")

        for task in tasks:

            print(f"Create notification -> {task.title}")

            desc = task.description or ""
            message = desc

            notification = Notification(
                task_id=task.id,
                title=task.title,
                message=message,
            )

            db.add(notification)

            task.reminder_sent = True

        db.commit()

    finally:

        db.close()