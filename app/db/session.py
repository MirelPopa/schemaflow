from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import NullPool
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/schemaflow")

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping = True,
    poolclass = NullPool
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db_session() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
