from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.scheduler.reminder_scheduler import check_reminders
from app.schemas.notification import NotificationResponse
from app.services.notification_service import NotificationService

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)


@router.get(
    "",
    response_model=list[NotificationResponse]
)
def get_notifications(
    db: Session = Depends(get_db)
):
    return NotificationService.get_all(db)


@router.post("/run")
def run_scheduler():

    check_reminders()

    return {
        "message": "Scheduler executed"
    }
    
@router.patch("/{notification_id}/read",
              response_model=NotificationResponse)
def mark_as_read(

    notification_id: int,

    db: Session = Depends(get_db)

):

    notification = NotificationService.mark_as_read(

        db,

        notification_id

    )

    if notification is None:

        raise HTTPException(

            status_code=404,

            detail="Notification not found"

        )

    return notification


@router.delete("/clear")
def clear_notifications(
    db: Session = Depends(get_db)
):
    NotificationService.clear_all(db)
    return {
        "message": "Notifications cleared"
    }