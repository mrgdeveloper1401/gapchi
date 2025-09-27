from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, DECIMAL, Text, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.db.mssql import Base

from src.schema.post import Post
from src.schema.core import File, State, Country

class Users(Base):
    __tablename__ = "Users"
    
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    phone = Column(String(20))
    is_active = Column(Boolean, default=True)
    is_staff = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)
    is_freeze = Column(Boolean, default=False)
    is_block = Column(Boolean, default=False)
    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    profile = relationship("Profile", back_populates="user", uselist=False)
    posts = relationship(Post, back_populates="user")
    files = relationship(File, back_populates="user")


class Profile(Base):
    __tablename__ = "Profile"
    
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("Users.id"), unique=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    birth_date = Column(DateTime)
    banner_image_id = Column(BigInteger, ForeignKey("File.id"))
    profile_image_id = Column(BigInteger, ForeignKey("File.id"))
    state_id = Column(BigInteger, ForeignKey("State.id"))
    country_id = Column(BigInteger, ForeignKey("Country.id"))
    is_block = Column(Boolean, default=False)
    bio = Column(Text)
    latitude = Column(DECIMAL(10, 8))
    longitude = Column(DECIMAL(11, 8))
    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    user = relationship("Users", back_populates="profile")
    state = relationship(State, back_populates="profiles")
    country = relationship(Country)
    banner_image = relationship(File, foreign_keys=[banner_image_id])
    profile_image = relationship(File, foreign_keys=[profile_image_id])


class UserLocation(Base):
    __tablename__ = "UserLocation"
    
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("Users.id"))
    latitude = Column(DECIMAL(10, 8), nullable=False)
    longitude = Column(DECIMAL(11, 8), nullable=False)


class Relation(Base):
    __tablename__ = "Relation"
    
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    from_user_id = Column(BigInteger, ForeignKey("Users.id", ondelete="CASCADE"))
    to_user_id = Column(BigInteger, ForeignKey("Users.id", ondelete="CASCADE"))
    relation_type = Column(String(50), default='friend')  # friend, follow, etc.
    is_active = Column(Boolean, default=True)
    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    # Relationships
    sender = relationship("Users", foreign_keys=[from_user_id], back_populates="sent_relations")
    receiver = relationship("Users", foreign_keys=[to_user_id], back_populates="received_relations")
    
    __table_args__ = (
        UniqueConstraint('from_user_id', 'to_user_id', name='uq_relation_users'),
    )


class FavoritUser(Base):
    __tablename__ = "FavoritUser"
    
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    from_user_id = Column(BigInteger, ForeignKey("Users.id", ondelete="CASCADE"))
    to_user_id = Column(BigInteger, ForeignKey("Users.id", ondelete="CASCADE"))
    is_active = Column(Boolean, default=True)
    created = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    favoriter = relationship("Users", foreign_keys=[from_user_id], back_populates="favorites")
    favorite_user = relationship("Users", foreign_keys=[to_user_id], back_populates="favorited_by")
    
    __table_args__ = (
        UniqueConstraint('from_user_id', 'to_user_id', name='uq_favorite_users'),
    )


class BlockUser(Base):
    __tablename__ = "BlockUser"
    
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    from_user_id = Column(BigInteger, ForeignKey("Users.id", ondelete="CASCADE"))
    to_user_id = Column(BigInteger, ForeignKey("Users.id", ondelete="CASCADE"))
    is_active = Column(Boolean, default=True)
    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    # Relationships
    blocker = relationship("Users", foreign_keys=[from_user_id], back_populates="blocked_users")
    blocked_user = relationship("Users", foreign_keys=[to_user_id], back_populates="blocked_by")
    
    __table_args__ = (
        UniqueConstraint('from_user_id', 'to_user_id', name='uq_block_users'),
    )



class Like(Base):
    __tablename__ = "Like"
    
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    from_user_id = Column(BigInteger, ForeignKey("Users.id", ondelete="CASCADE"))
    to_user_id = Column(BigInteger, ForeignKey("Users.id", ondelete="CASCADE"))
    like_type = Column(String(50), default='profile')  # profile, post, comment, etc.
    is_active = Column(Boolean, default=True)
    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    # Relationships
    sender = relationship("Users", foreign_keys=[from_user_id], back_populates="sent_likes")
    receiver = relationship("Users", foreign_keys=[to_user_id], back_populates="received_likes")
    
    __table_args__ = (
        UniqueConstraint('from_user_id', 'to_user_id', 'like_type', name='uq_like_unique'),
    )


class UserNotification(Base):
    __tablename__ = "UserNotification"
    
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("Users.id", ondelete="CASCADE"))
    title = Column(String(255), nullable=False)
    body = Column(Text)
    redirect_url = Column(String(500))
    notification_type = Column(String(50), default='info')  # info, warning, success, error
    is_read = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    # Relationships
    user = relationship("Users", back_populates="notifications")


class PublicNotification(Base):
    __tablename__ = "PublicNotification"
    
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    body = Column(Text)
    redirect_url = Column(String(500))
    notification_type = Column(String(50), default='info')
    is_active = Column(Boolean, default=True)
    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())


class LoginAttempts(Base):
    __tablename__ = "LoginAttempts"
    
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("Users.id", ondelete="CASCADE"))
    max_request_number = Column(Integer, default=5)
    user_request_number = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
    ip = Column(String(45))
    device_info = Column(String(500))
    user_agent = Column(String(500))
    attempt_status = Column(String(20), default='failed')  # success, failed
    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    # Relationships
    user = relationship("Users", back_populates="login_attempts")


class UserLog(Base):
    __tablename__ = "UserLog"
    
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("Users.id", ondelete="CASCADE"))
    request_path = Column(String(500))
    method = Column(String(10))
    ip = Column(String(45))
    device_info = Column(String(500))
    user_agent = Column(String(500))
    status_code = Column(Integer)
    response_time = Column(DECIMAL(8, 3))  # in milliseconds
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    user = relationship("Users")


class UserTokenBlock(Base):
    __tablename__ = "UserTokenBlock"
    
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("Users.id", ondelete="CASCADE"))
    refresh_token = Column(Text, nullable=False)
    is_active = Column(Boolean, default=True)
    expires_at = Column(DateTime(timezone=True))
    created = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    user = relationship("Users", back_populates="tokens")