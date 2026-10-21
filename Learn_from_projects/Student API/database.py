
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL"
)

# Async database engine
engine = create_async_engine(
    DATABASE_URL,
    echo=True,          # SQL queries terminal mein show hongi
    pool_pre_ping=True,
)

# Async session factory
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)



# Dependency for FastAPI routes
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


# Create tables during development
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# Close database connections
async def close_db():
    await engine.dispose()



# =========== Models =======================
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column

from sqlalchemy.sql import func




# Base class for ORM models
class Base(DeclarativeBase):
    pass


class Student(Base): 
    __tablename__ = "students"
    id: Mapped[int]  = mapped_column(Integer, primary_key=True)
    age: Mapped[int]  = mapped_column(Integer, nullable=False)
    mark: Mapped[int]  = mapped_column(Integer, nullable=False)
    