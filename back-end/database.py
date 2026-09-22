from __future__ import annotations

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./Viagem.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


def init_db() -> None:
    """Create database tables."""
    # Import models so SQLAlchemy registers them on Base.
    # (Assumes your models are declared using Base from this module.)
    try:
        import models  # noqa: F401
    except Exception:
        # If models package can't be imported here, let Base metadata handle it.
        pass

    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()