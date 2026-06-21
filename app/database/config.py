import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# If the URL starts with standard postgresql://, inject +asyncpg for SQLAlchemy's async engine
if DATABASE_URL and DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://", 1)

# Quick sanity check to make sure it looks right (it should now show postgresql+asyncpg://...)
print(f"Connecting to: {DATABASE_URL}")

engine = create_async_engine(
    DATABASE_URL, 
    echo=True, 
    pool_pre_ping=True, 
    pool_size=10, 
    max_overflow=20,
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine, 
    expire_on_commit=False, 
    class_=AsyncSession,
)

Base = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session