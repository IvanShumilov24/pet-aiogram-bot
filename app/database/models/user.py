import enum
from typing import Optional

from sqlalchemy import Integer, String, Enum, BigInteger
from sqlalchemy.orm import mapped_column, Mapped

from app.database.models.base import Base


class UserType(str, enum.Enum):
    SELLER = "seller"
    BUYER = "buyer"


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    username: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    first_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    last_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    user_type: Mapped[Enum] = mapped_column(Enum(UserType), nullable=True)