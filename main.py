from fastapi import FastAPI
from src.db.postgre import settings
from src.db.connect_db import engine
from src.db.base import Base
from src.db.models import Users
from src.db.connect_db import engine

app = FastAPI()

def create_tables():
    Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
    create_tables()
    return app


app = start_application()

@app.get("/")
async def home():
    return {"msg":"Hello FastAPI🚀"}


@app.get("/check_db")
async def check_db():
    try:
        with engine.connect() as conn:
            return {
                "conn": "connection successfly",
                "url": conn.engine.url
            }
    except Exception as e:
        return {
            "conn": "connection unsucceful",
            "error": str(e)
        }
