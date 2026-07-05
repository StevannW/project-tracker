from sqlalchemy.orm import Session

from app.models.notification import Notification


class NotificationService:

    @staticmethod
    def get_all(db: Session):

        return db.query(Notification)\
                 .order_by(Notification.created_at.desc())\
                 .all()

    @staticmethod
    def mark_as_read(
        db: Session,
        notification_id: int
    ):

        notification = db.query(Notification).filter(
            Notification.id == notification_id
        ).first()

        if not notification:
            return None

        notification.is_read = True

        db.commit()

        db.refresh(notification)

        return notification

        
    @staticmethod
    def clear_all(db: Session):

        db.query(Notification).delete()

        db.commit()