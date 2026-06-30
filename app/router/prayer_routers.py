from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.prayer_service import PrayerService
from app.schemas.prayer_schema import PrayerDTO, PrayerSchema, PrayerUpdateDTO
from app.database.config import get_db
from app.models.prayer_model import Prayer, Category

router = APIRouter(prefix="/prayers", tags=["prayers"])

@router.post("/", response_model=PrayerDTO, status_code=201)
async def create_prayers(prayer: PrayerDTO, db: AsyncSession = Depends(get_db)):
    response: Prayer =  await PrayerService.create_prayer(db, prayer)

    if not response:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail=f"Unable to process the fields"
        )
    
    return response

@router.get("/", response_model=list[PrayerSchema], status_code=200)
async def get_prayers(db: AsyncSession = Depends(get_db)) -> list[PrayerSchema]:
    prayers: list[Prayer] = await PrayerService.get_prayers(db=db)

    if not prayers:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unable to fetch prayers data"
        )
    return prayers

@router.get("/{prayer_id}", response_model=PrayerSchema, status_code=200)
async def get_prayer(prayer_id: int, db: AsyncSession = Depends(get_db)) -> PrayerSchema:
    prayer: Prayer = await PrayerService.get_prayer_by_id(db=db, prayer_id=prayer_id)

    if prayer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Prayer not found"
        )
    
    return prayer

@router.patch("/{prayer_id}", response_model=PrayerSchema, status_code=200)
async def update_prayer(prayer_id: int, prayer: PrayerUpdateDTO, db: AsyncSession = Depends(get_db)):
    response: Prayer = await PrayerService.update_prayer(db=db, prayer_id=prayer_id, prayer_payload=prayer)

    if response is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Prayer not found in the database"
        )
    
    return response