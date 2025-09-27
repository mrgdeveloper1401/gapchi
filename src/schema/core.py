from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, DECIMAL, Text, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database.connection import Base


class Country(Base):
    __tablename__ = "Country"
    
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    country_name = Column(String(100), nullable=False)
    is_active = Column(Boolean, default=True)
    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), onupdate=func.now())
    
    states = relationship("State", back_populates="country")

class State(Base):
    __tablename__ = "State"
    
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    state_name = Column(String(100), nullable=False)
    country_id = Column(BigInteger, ForeignKey("Country.id"))
    is_active = Column(Boolean, default=True)
    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), onupdate=func.now())
    
    country = relationship("Country", back_populates="states")
    profiles = relationship("Profile", back_populates="state")


class File(Base):
    __tablename__ = "File"
    
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("Users.id"))
    file_path = Column(String(500), nullable=False)
    is_active = Column(Boolean, default=True)
    size = Column(BigInteger)
    name = Column(String(255))
    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), onupdate=func.now())
    
    user = relationship("Users", back_populates="files")