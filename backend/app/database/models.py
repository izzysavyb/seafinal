from sqlalchemy import String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[str] = mapped_column(String(10), default="user") 

    assets: Mapped[list["Asset"]] = relationship(
    back_populates="owner"
)


class Asset(Base):
    __tablename__ = "assets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    category: Mapped[str] = mapped_column(String(50), nullable=False)
    serial_number: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    owner: Mapped["User"] = relationship(
    back_populates="assets"
)