from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.db.dependencies import get_db

from app.schemas.task import TaskCreate
from app.schemas.task import TaskUpdate
from app.schemas.task import TaskResponse

from app.services.task_service import TaskService

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.get(
    "/",
    response_model=list[TaskResponse]
)
def get_tasks(
    db: Session = Depends(get_db)
):
    return TaskService.get_all(db)


@router.post(
    "/",
    response_model=TaskResponse,
    status_code=201
)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db)
):
    return TaskService.create(db, task)



@router.put(
    "/{task_id}",
    response_model=TaskResponse
)
def update_task(
    task_id: int,
    task: TaskUpdate,
    db: Session = Depends(get_db)
):

    db_task = TaskService.get_by_id(db, task_id)

    if not db_task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return TaskService.update(
        db,
        db_task,
        task
    )


@router.delete(
    "/{task_id}"
)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):

    db_task = TaskService.get_by_id(
        db,
        task_id
    )

    if not db_task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    TaskService.delete(
        db,
        db_task
    )

    return {
        "message": "Task deleted successfully"
    }