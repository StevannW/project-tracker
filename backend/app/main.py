from contextlib import asynccontextmanager

from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from app.api.notifications import router as notification_router
from app.api.tasks import router as task_router
from app.core.config import settings
from app.db.database import Base
from app.db.database import engine
from app.models.notification import Notification
from app.models.task import Task
from app.scheduler.reminder_scheduler import check_reminders

# ======================================================
# Scheduler
# ======================================================

scheduler = BackgroundScheduler()


@asynccontextmanager
async def lifespan(app: FastAPI):

    Base.metadata.create_all(bind=engine)

    scheduler.add_job(
        check_reminders,
        trigger="interval",
        seconds=10,
        id="task-reminder",
        replace_existing=True,
    )

    scheduler.start()

    print("========== Scheduler Started ==========")

    yield

    scheduler.shutdown()

    print("========== Scheduler Stopped ==========")


# ======================================================
# FastAPI
# ======================================================

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan,
)

app.include_router(task_router)
app.include_router(notification_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost",
        "http://127.0.0.1",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "API is running",
        "database": settings.DATABASE_NAME,
    }


@app.get("/db-test")
def db_test():

    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))

    return {
        "message": "Database connected successfully",
    }