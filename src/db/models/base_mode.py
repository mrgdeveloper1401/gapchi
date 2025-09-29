from sqlalchemy import Column, DateTime, Boolean
from sqlalchemy.sql import func
from src.db.base import Base


class BaseModel(Base):
    __abstract__ = True

    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), onupdate=func.now())
    is_active = Column(Boolean, default=True)
