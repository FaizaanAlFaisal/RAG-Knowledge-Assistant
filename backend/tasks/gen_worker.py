from celery import Celery
from core.config import settings

gen_worker_app = Celery(
    "gen_worker",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,
)
