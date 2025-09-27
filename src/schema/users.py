from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, DECIMAL, Text, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database.connection import Base


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
    
    profile = relationship("Profile", back_populates="user", uselist=False)
    posts = relationship("Post", back_populates="user")
    files = relationship("File", back_populates="user")


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
    
    user = relationship("Users", back_populates="profile")
    state = relationship("State", back_populates="profiles")
    country = relationship("Country")
    banner_image = relationship("File", foreign_keys=[banner_image_id])
    profile_image = relationship("File", foreign_keys=[profile_image_id])


class UserLocation(Base):
    __tablename__ = "UserLocation"
    
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("Users.id"))
    latitude = Column(DECIMAL(10, 8), nullable=False)
    longitude = Column(DECIMAL(11, 8), nullable=False)


