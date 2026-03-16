from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database configuration for AI Code Review Platform
DATABASE_URL = "postgresql://postgres:postgres123@localhost:5432/ai_code_review"

# SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,  # ensures stale connections are recycled
)

# Session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)
# Session factory
SessionLocal = sessionmaker(
    autocommit=True,
    autoflush=True,
    bind=engine,
)

# Base class for ORM models
Base = declarative_base()
