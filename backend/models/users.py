from .base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_admin = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

    documents = relationship("Document", back_populates="owner")