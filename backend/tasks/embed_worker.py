from celery import Celery
from core.config import settings

embed_worker_app = Celery(
    "embed_worker",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,
)
