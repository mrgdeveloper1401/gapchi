from sqlalchemy import Column, BigInteger, String, Boolean, DateTime
from src.db.models.base_mode import BaseModel

class Users(BaseModel):
    __tablename__ = "Users"
    
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    phone = Column(String(20), nullable=True)
    password = Column(String(128), nullable=False)
    is_staff = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)
    is_freeze = Column(Boolean, default=False)
    is_block = Column(Boolean, default=False)



# class Profile(BaseModel):
#     __tablename__ = "Profile"
    
#     id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
#     user_id = Column(BigInteger, ForeignKey("Users.id"), unique=True)
#     first_name = Column(String(100), nullable=True)
#     last_name = Column(String(100), nullable=True)
#     birth_date = Column(DateTime, nullable=True)
#     banner_image_id = Column(BigInteger, ForeignKey("File.id"), nullable=True)
#     profile_image_id = Column(BigInteger, ForeignKey("File.id"), nullable=True)
#     state_id = Column(BigInteger, ForeignKey("State.id"), nullable=True)
#     country_id = Column(BigInteger, ForeignKey("Country.id"), nullable=True)
#     is_block = Column(Boolean, default=False)
#     bio = Column(Text, nullable=True)
#     latitude = Column(DECIMAL(10, 8), nullable=True)
#     longitude = Column(DECIMAL(11, 8), nullable=True)
    
#     # Relationships
#     user = relationship("Users", back_populates="profile")
#     state = relationship(State, back_populates="profiles")
#     country = relationship(Country)
#     banner_image = relationship(File, foreign_keys=[banner_image_id])
#     profile_image = relationship(File, foreign_keys=[profile_image_id])


# class UserLocation(BaseModel):
#     __tablename__ = "UserLocation"
    
#     id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
#     user_id = Column(BigInteger, ForeignKey("Users.id"))
#     latitude = Column(DECIMAL(10, 8), nullable=False)
#     longitude = Column(DECIMAL(11, 8), nullable=False)


# class Relation(BaseModel):
#     __tablename__ = "Relation"
    
#     id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
#     from_user_id = Column(BigInteger, ForeignKey("Users.id", ondelete="CASCADE"))
#     to_user_id = Column(BigInteger, ForeignKey("Users.id", ondelete="CASCADE"))
#     relation_type = Column(String(50), default='friend')  # friend, follow, etc.
    
#     # Relationships
#     sender = relationship("Users", foreign_keys=[from_user_id], back_populates="sent_relations")
#     receiver = relationship("Users", foreign_keys=[to_user_id], back_populates="received_relations")
    
#     __table_args__ = (
#         UniqueConstraint('from_user_id', 'to_user_id', name='uq_relation_users'),
#     )


# class FavoritUser(BaseModel):
#     __tablename__ = "FavoritUser"
    
#     id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
#     from_user_id = Column(BigInteger, ForeignKey("Users.id", ondelete="CASCADE"))
#     to_user_id = Column(BigInteger, ForeignKey("Users.id", ondelete="CASCADE"))
    
#     # Relationships
#     favoriter = relationship("Users", foreign_keys=[from_user_id], back_populates="favorites")
#     favorite_user = relationship("Users", foreign_keys=[to_user_id], back_populates="favorited_by")
    
#     __table_args__ = (
#         UniqueConstraint('from_user_id', 'to_user_id', name='uq_favorite_users'),
#     )


# class BlockUser(BaseModel):
#     __tablename__ = "BlockUser"
    
#     id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
#     from_user_id = Column(BigInteger, ForeignKey("Users.id", ondelete="CASCADE"))
#     to_user_id = Column(BigInteger, ForeignKey("Users.id", ondelete="CASCADE"))
    
#     # Relationships
#     blocker = relationship("Users", foreign_keys=[from_user_id], back_populates="blocked_users")
#     blocked_user = relationship("Users", foreign_keys=[to_user_id], back_populates="blocked_by")
    
#     __table_args__ = (
#         UniqueConstraint('from_user_id', 'to_user_id', name='uq_block_users'),
#     )



# class Like(BaseModel):
#     __tablename__ = "Like"
    
#     id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
#     from_user_id = Column(BigInteger, ForeignKey("Users.id", ondelete="CASCADE"))
#     to_user_id = Column(BigInteger, ForeignKey("Users.id", ondelete="CASCADE"))
#     like_type = Column(String(50), default='profile')  # profile, post, comment, etc.
    
#     # Relationships
#     sender = relationship("Users", foreign_keys=[from_user_id], back_populates="sent_likes")
#     receiver = relationship("Users", foreign_keys=[to_user_id], back_populates="received_likes")
    
#     __table_args__ = (
#         UniqueConstraint('from_user_id', 'to_user_id', 'like_type', name='uq_like_unique'),
#     )


# class UserNotification(BaseModel):
#     __tablename__ = "UserNotification"
    
#     id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
#     user_id = Column(BigInteger, ForeignKey("Users.id", ondelete="CASCADE"))
#     title = Column(String(255), nullable=False)
#     body = Column(Text)
#     redirect_url = Column(String(500))
#     notification_type = Column(String(50), default='info')  # info, warning, success, error
#     is_read = Column(Boolean, default=False)
    
#     # Relationships
#     user = relationship("Users", back_populates="notifications")


# class LoginAttempts(BaseModel):
#     __tablename__ = "LoginAttempts"
    
#     id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
#     user_id = Column(BigInteger, ForeignKey("Users.id", ondelete="CASCADE"))
#     max_request_number = Column(Integer, default=5)
#     user_request_number = Column(Integer, default=0)
#     is_active = Column(Boolean, default=True)
#     ip = Column(String(45), nullable=True)
#     device_info = Column(String(500), nullable=True)
#     user_agent = Column(String(500), nullable=True)
#     attempt_status = Column(String(20), default='failed')  # success, failed
    
#     # Relationships
#     user = relationship("Users", back_populates="login_attempts")


# class UserLog(BaseModel):
#     __tablename__ = "UserLog"
    
#     id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
#     user_id = Column(BigInteger, ForeignKey("Users.id", ondelete="CASCADE"))
#     request_path = Column(String(500))
#     method = Column(String(10))
#     ip = Column(String(45))
#     device_info = Column(String(500))
#     user_agent = Column(String(500))
#     status_code = Column(Integer)
#     response_time = Column(DECIMAL(8, 3))  # in milliseconds
    
#     # Relationships
#     user = relationship("Users")


# class UserTokenBlock(BaseModel):
#     __tablename__ = "UserTokenBlock"
    
#     id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
#     user_id = Column(BigInteger, ForeignKey("Users.id", ondelete="CASCADE"))
#     refresh_token = Column(Text, nullable=False)
#     expires_at = Column(DateTime(timezone=True))
    
#     # Relationships
#     user = relationship("Users", back_populates="tokens")