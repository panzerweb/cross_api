import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession,  async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

print(DATABASE_URL)
print(SUPABASE_URL)

engine = create_async_engine(DATABASE_URL, echo=True, pool_pre_ping=True, pool_size=10, max_overflow=20,)
AsyncSessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession,)
Base = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session