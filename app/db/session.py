import os
from collections.abc import Generator
from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

# Use SQLite by default; can be overridden via environment variable.
DATABASE_URL = settings.DATABASE_URL

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency that provides a DB session per request
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
