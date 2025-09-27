from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config

DB_USERNAME = config("DB_USERNAME", cast=str)
DB_PASSWORD = config("DB_PASSWORD", cast=str)
DB_SERVER = config("DB_SERVER", cast=str)
DB_PORT = config("DB_PORT", cast=int)
DB_NAME = config("DB_NAME", cast=str)

SQLALCHEMY_DATABASE_URL = (
    f"mssql+pyodbc://{DB_USERNAME}:{DB_PASSWORD}"
    f"@{DB_SERVER}:{DB_PORT}/{DB_NAME}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=3600,
    echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
