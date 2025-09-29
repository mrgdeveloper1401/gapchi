# from src.db.models.base_mode import BaseModel
# from .users import Users


# class PublicNotification(BaseModel):
#     __tablename__ = "PublicNotification"
    
#     id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
#     title = Column(String(255), nullable=False)
#     body = Column(Text)
#     redirect_url = Column(String(500))
#     notification_type = Column(String(50), default='info')


# class Country(BaseModel):
#     __tablename__ = "Country"
    
#     id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
#     country_name = Column(String(100), nullable=False)
    
#     # Relationships
#     states = relationship("State", back_populates="country")


# class State(BaseModel):
#     __tablename__ = "State"
    
#     id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
#     state_name = Column(String(100), nullable=False)
#     country_id = Column(BigInteger, ForeignKey("Country.id"))
    
#     # Relationships
#     country = relationship("Country", back_populates="states")
#     profiles = relationship(Profile, back_populates="state")



# class File(BaseModel):
#     __tablename__ = "File"
    
#     id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
#     user_id = Column(BigInteger, ForeignKey(Users.id))
#     file_path = Column(String(500), nullable=False)
#     size = Column(BigInteger)
#     name = Column(String(255))
    
#     # Relationships
#     user = relationship(Users, back_populates="files")


# class Core(BaseModel):
#     __tablename__ = "Core"

#     id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
#     user_id = Column(BigInteger, ForeignKey("Users.id", ondelete="CASCADE"), unique=True)
#     language = Column(String(10), default='fa')
#     theme = Column(String(20), default='light')
#     notifications_enabled = Column(Boolean, default=True)

#     # Relationships
#     user = relationship(Users, back_populates="core_settings")


# class IpBlock(BaseModel):
#     __tablename__ = "IpBlock"
    
#     id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
#     ip = Column(String(45), nullable=False, unique=True)
#     reason = Column(Text)


# class CoreApp(BaseModel):
#     __tablename__ = "CoreApp"
    
#     id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
#     color = Column(String(50))
#     default_language = Column(String(10), default='fa')
#     background_color = Column(String(50))
#     banner_image_id = Column(BigInteger, ForeignKey("upload_file.id"))
#     cover_image_id = Column(BigInteger, ForeignKey("upload_file.id"))
#     logo_image_id = Column(BigInteger, ForeignKey("upload_file.id"))
#     app_name = Column(String(100), default='Gapchi')
#     app_version = Column(String(20), default='1.0.0')
#     is_maintenance = Column(Boolean, default=False)
    
#     # Relationships
#     banner_image = relationship("File", foreign_keys=[banner_image_id], back_populates="core_app_banner")
#     cover_image = relationship("File", foreign_keys=[cover_image_id], back_populates="core_app_cover")
#     logo_image = relationship("File", foreign_keys=[logo_image_id], back_populates="core_app_logo")