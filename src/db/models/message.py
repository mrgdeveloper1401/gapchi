# from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, DECIMAL, Text, BigInteger
# from sqlalchemy.orm import relationship
# from sqlalchemy.sql import func
# from src.db.models.base_mode import BaseModel

# from src.db.models.users import Users
# from src.db.models.core import File


# class Message(Base):
#     __tablename__ = "message"
    
#     id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
#     sender_user_id = Column(BigInteger, ForeignKey(Users.id, ondelete="CASCADE"))
#     receiver_user_id = Column(BigInteger, ForeignKey(Users.id, ondelete="CASCADE"))
#     content = Column(Text)
#     message_type = Column(String(50), default='text')  # text, image, file, etc.
#     is_active = Column(Boolean, default=True)
#     is_read = Column(Boolean, default=False)
#     is_delivered = Column(Boolean, default=False)
#     created = Column(DateTime(timezone=True), server_default=func.now())
#     updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
#     # Relationships
#     sender = relationship(Users, foreign_keys=[sender_user_id], back_populates="sent_messages")
#     receiver = relationship(Users, foreign_keys=[receiver_user_id], back_populates="received_messages")
#     files = relationship("MessageFile", back_populates="message")


# class MessageFile(Base):
#     __tablename__ = "message_file"
    
#     id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
#     message_id = Column(BigInteger, ForeignKey("message.id", ondelete="CASCADE"))
#     file_id = Column(BigInteger, ForeignKey("upload_file.id", ondelete="CASCADE"))
#     created = Column(DateTime(timezone=True), server_default=func.now())
    
#     # Relationships
#     message = relationship("Message", back_populates="files")
#     file = relationship("File", back_populates="messages")