import os  
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
SUPABASE_URL = os.getenv("SUPABASE_URL")
print("DATABASE_URL =", DATABASE_URL)

engine = create_async_engine(DATABASE_URL, echo=True, pool_pre_ping=True, pool_size=10, max_overflow=20,)

async def test():
    async with engine.connect() as conn:
        print("Connected!")

asyncio.run(test())