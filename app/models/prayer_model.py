from sqlalchemy import Integer, String, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.config import Base
from datetime import datetime

class Prayer(Base):
    __tablename__ = "prayer"
    id:Mapped[int] = mapped_column(
        Integer, primary_key=True, unique=True, autoincrement=True
    )

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    title: Mapped[str] = mapped_column(String, nullable=True)

    content: Mapped[str] = mapped_column(Text, nullable=True)

    category_id: Mapped[int] = mapped_column(
        ForeignKey("category.id"),
        nullable=True
    )

    is_favorite: Mapped[bool] = mapped_column(
        Boolean, default=False
    )

    category = relationship("Category", back_populates="prayer")

class Category(Base):
    __tablename__ = "category"

    id:Mapped[int] = mapped_column(
        Integer, primary_key=True, unique=True, autoincrement=True
    )

    name: Mapped[str] = mapped_column(String, nullable=True)

    created_at:Mapped[datetime] = mapped_column(DateTime(timezone=True))

    prayer = relationship("Prayer", back_populates="category")