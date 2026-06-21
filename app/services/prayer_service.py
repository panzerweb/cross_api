from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.prayer_model import Prayer
from app.schemas.prayer_schema import PrayerDTO, PrayerSchema

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