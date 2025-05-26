from base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from pgvector.sqlalchemy import Vector

class Document(Base):
    __tablename__ = 'documents'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    embedding = Column(Vector(1536))
    owner_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship("User", back_populates="documents")