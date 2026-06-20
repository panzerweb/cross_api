from pydantic import BaseModel
from datetime import datetime

class PrayerDTO(BaseModel):
    title: str
    content: str
    category_id: int

class PrayerSchema(BaseModel):
    id: int
    title: str
    content: str
    category_id: int
    is_favorite: bool
    created_at: datetime

class CategorySchema(BaseModel):
    id: int
    name: str
    created_at: datetime

