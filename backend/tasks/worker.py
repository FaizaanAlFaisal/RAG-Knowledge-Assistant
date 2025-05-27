from celery import Celery

celery_app = Celery(
    "celery_worker",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
)

# sample task
@celery_app.task
def add(x, y):
    """Simple task to add two numbers."""
    return x + y