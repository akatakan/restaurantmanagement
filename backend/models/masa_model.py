from uuid import UUID
from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING
from backend.enums.masa_durumu_enum import MasaDurumu

if TYPE_CHECKING:
    from .garson_model import Garson
    from .siparis_model import Siparis


class Masa(SQLModel, table=True):
    masa_numarasi: int | None = Field(default=None, primary_key=True)
    kapasite: int
    konum: str
    durum: MasaDurumu

    garson_id: UUID = Field(default=None, foreign_key="garson.id")
    garson: "Garson" = Relationship(back_populates="sorumluMasalar")

    Siparis: "Siparis" = Relationship(back_populates="Masa")
