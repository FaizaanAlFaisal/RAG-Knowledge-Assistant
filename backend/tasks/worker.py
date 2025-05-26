from celery import Celery

celery_app = Celery(
    "backend",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
    include=["backend.tasks.embedding_tasks", "backend.tasks.query_tasks"]
)

# sample task
@celery_app.task
def add(x, y):
    """Simple task to add two numbers."""
    return x + y