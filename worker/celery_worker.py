from celery import Celery
import os

celery_app = Celery(
    "schemaflow_worker",
    broker=os.getenv("REDIS_BROKER_URL", "redis://localhost:6379/0"),
    backend=os.getenv("REDIS_BROKER_URL", "redis://localhost:6379/0"),
)

celery_app.conf.task_routes = {"worker.tasks.*": {"queue": "validation"}}

import worker.tasks.validate_submission  # noqa: F401
