from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.prayer_service import create_prayer, get_prayers
from app.schemas.prayer_schema import PrayerDTO, PrayerSchema
from app.database.config import get_db

router = APIRouter(prefix="/prayers", tags=["prayers"])

@router.post("/", response_model=PrayerDTO, status_code=201)
async def create_prayers(prayer: PrayerDTO, db: AsyncSession = Depends(get_db)):
    return await create_prayer(db, prayer)

@router.get("/prayers", response_model=PrayerSchema, status_code=200)
async def get_prayers(db: AsyncSession = Depends(get_db)) -> list[PrayerSchema]:
    return await get_prayers(db=db)