from celery import Celery

celery_app = Celery(
    "schemaflow_worker",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
)

celery_app.conf.task_routes = {"worker.tasks.*": {"queue": "validation"}}
