from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, DECIMAL, Text, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.db.mssql import Base

from src.schema.users import Users, Profile
from src.schema.message import MessageFile


class Country(Base):
    __tablename__ = "Country"
    
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    country_name = Column(String(100), nullable=False)
    is_active = Column(Boolean, default=True)
    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    states = relationship("State", back_populates="country")


class State(Base):
    __tablename__ = "State"
    
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    state_name = Column(String(100), nullable=False)
    country_id = Column(BigInteger, ForeignKey("Country.id"))
    is_active = Column(Boolean, default=True)
    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    country = relationship("Country", back_populates="states")
    profiles = relationship(Profile, back_populates="state")


class File(Base):
    __tablename__ = "File"
    
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey(Users.id))
    file_path = Column(String(500), nullable=False)
    is_active = Column(Boolean, default=True)
    size = Column(BigInteger)
    name = Column(String(255))
    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    user = relationship(Users, back_populates="files")


class Core(Base):
    __tablename__ = "Core"
    
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("Users.id", ondelete="CASCADE"), unique=True)
    language = Column(String(10), default='fa')
    theme = Column(String(20), default='light')
    notifications_enabled = Column(Boolean, default=True)
    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    # Relationships
    user = relationship(Users, back_populates="core_settings")


class IpBlock(Base):
    __tablename__ = "IpBlock"
    
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    ip = Column(String(45), nullable=False, unique=True)
    reason = Column(Text)
    is_active = Column(Boolean, default=True)
    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())


class CoreApp(Base):
    __tablename__ = "CoreApp"
    
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    color = Column(String(50))
    default_language = Column(String(10), default='fa')
    background_color = Column(String(50))
    banner_image_id = Column(BigInteger, ForeignKey("upload_file.id"))
    cover_image_id = Column(BigInteger, ForeignKey("upload_file.id"))
    logo_image_id = Column(BigInteger, ForeignKey("upload_file.id"))
    app_name = Column(String(100), default='Gapchi')
    app_version = Column(String(20), default='1.0.0')
    is_maintenance = Column(Boolean, default=False)
    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    # Relationships
    banner_image = relationship("File", foreign_keys=[banner_image_id], back_populates="core_app_banner")
    cover_image = relationship("File", foreign_keys=[cover_image_id], back_populates="core_app_cover")
    logo_image = relationship("File", foreign_keys=[logo_image_id], back_populates="core_app_logo")