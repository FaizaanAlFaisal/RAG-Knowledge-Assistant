from .base import Base
from pgvector.sqlalchemy import Vector
from datetime import datetime, timezone
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

class QueryLog(Base):
    __tablename__ = 'query_logs'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    query_text = Column(String, nullable=False)
    embedding = Column(Vector(1536))
    timestamp = Column(DateTime, default=datetime.now(timezone.utc))

    user = relationship("User", backref="query_logs")
