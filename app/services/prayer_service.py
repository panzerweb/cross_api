from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.prayer_model import Prayer
from app.schemas.prayer_schema import PrayerDTO, PrayerUpdateDTO

class PrayerService:
    @staticmethod
    async def create_prayer(db: AsyncSession, prayer: PrayerDTO) -> Prayer:
        db_prayer = Prayer(title=prayer.title, content=prayer.content, category_id = prayer.category_id)
        db.add(db_prayer)

        await db.commit()
        await db.refresh(db_prayer)

        return db_prayer

    @staticmethod
    async def get_prayers(db: AsyncSession) -> list[Prayer]:

        result = await db.execute(select(Prayer))

        prayers = result.scalars().all()

        return prayers
    
    # This method will act as the primary function to get the id so that it can be used
    # by other services.
    @staticmethod
    async def get_prayer_by_id(db: AsyncSession, prayer_id: int) -> Prayer | None:
        query = await db.execute(select(Prayer).where(Prayer.id == prayer_id))

        prayer: Prayer | None = query.scalar_one_or_none()

        return prayer
    
    @staticmethod
    async def delete_prayer(db:AsyncSession, prayer_id: int) -> bool:
        target_prayer: Prayer | None = await PrayerService.get_prayer_by_id(db=db, prayer_id=prayer_id)

        if not target_prayer:
            return False
        
        await db.delete(target_prayer)
        await db.commit()

        return True
    
    @staticmethod
    async def update_prayer(db: AsyncSession, prayer_id: int, prayer_payload: PrayerUpdateDTO) -> Prayer | None:
        target_prayer: Prayer | None = await PrayerService.get_prayer_by_id(db=db, prayer_id=prayer_id)

        # Validation for prayers
        if not target_prayer:
            return None
        
        if prayer_payload.title is not None:
            target_prayer.title = prayer_payload.title
        
        if prayer_payload.content is not None:
            target_prayer.content = prayer_payload.content

        if prayer_payload.category_id is not None:
            target_prayer.category_id = prayer_payload.category_id

        await db.commit()
        await db.refresh(target_prayer)
        
        return target_prayer
        
        
