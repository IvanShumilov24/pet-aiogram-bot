import uuid

from sqlalchemy import ForeignKey, String, Float, UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database.models.base import Base


class Project(Base):
    __tablename__ = 'projects'

    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, index=True, default=uuid.uuid4)
    seller_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(1000))
    cost: Mapped[float] = mapped_column(Float)
