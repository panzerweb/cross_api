from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.prayer_service import create_prayer
from app.schemas.prayer_schema import PrayerDTO, PrayerSchema
from app.database.config import get_db

router = APIRouter(prefix="/prayers", tags=["prayers"])

@router.post("/prayers/", response_model=PrayerDTO, status_code=201)
async def create_prayers(prayer: PrayerDTO, db: Session = Depends(get_db)):
    return await create_prayer(db, prayer)

# @router.get("/prayers", response_model=PrayerSchema, status_code=200)
# def get_prayers() -> list[PrayerSchema]:
#     return [
#         PrayerSchema()
#     ]