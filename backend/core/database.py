from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

SQLALCHEMY_DATABASE_URL = settings.DB_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

from models import Base
Base.metadata.create_all(bind=engine)
logger.info("✅ Database tables created successfully. ✅")

def test_db():
    try:
        db = SessionLocal()
        db.execute("SELECT 1")
        logger.info("Database connection successful.")
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
    finally:
        db.close()
