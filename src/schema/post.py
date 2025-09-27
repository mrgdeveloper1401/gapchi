from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, DECIMAL, Text, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database.connection import Base


class Post(Base):
    __tablename__ = "Post"
    
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("Users.id"))
    content = Column(Text)
    location = Column(BigInteger, ForeignKey("UserLocation.id"))
    is_active = Column(Boolean, default=True)
    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), onupdate=func.now())
    
    user = relationship("Users", back_populates="posts")
    user_location = relationship("UserLocation")
    comments = relationship("Comment", back_populates="post")
    likes = relationship("PostLike", back_populates="post")