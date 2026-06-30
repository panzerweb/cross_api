from pydantic import BaseModel, ConfigDict
from datetime import datetime

class PrayerDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str
    content: str
    category_id: int

class PrayerUpdateDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str
    content: str
    category_id: int

class PrayerSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    content: str
    category_id: int
    is_favorite: bool
    created_at: datetime

class CategorySchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    created_at: datetime

