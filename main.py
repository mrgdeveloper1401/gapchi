from fastapi import FastAPI
from src.db.mssql import engine, Base
from src.schema import (
    # BlockUser,
    # Comment,
    # CommentLike,
    # Core,
    # CoreApp,
    # Country,
    # FavoritUser,
    # File,
    # IpBlock,
    # Like,
    # LoginAttempts,
    # Message,
    # MessageFile,
    # UserTokenBlock,
    Users,
    # UserNotification,
    # UserLog,
    # UserLocation,
    # State,
    # Post,
    # PostFile,
    # PostLike,
    # Relation,
    # PublicNotification,
    # Profile
)

app = FastAPI()

def create_tables():
    Base.metadata.create_all(bind=engine)

create_tables()

if __name__ == "__main__":
    import uvicorn
    create_tables()
    print("All tables created successfully!")
    uvicorn.run(app, host="0.0.0.0", port=8000)
