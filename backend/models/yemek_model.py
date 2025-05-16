from typing import TYPE_CHECKING, List
from sqlmodel import Relationship, Field, SQLModel

if TYPE_CHECKING:
    from .siparis_model import Siparis


class Yemek(SQLModel, table=True):
    yemekID: int | None = Field(default=None, primary_key=True)
    ad: str
    aciklama: str
    fiyat: float
    hazirlanmaSüresi: int

    siparis_id: int | None = Field(default=None, foreign_key="siparis.siparisID")
    Siparis: "Siparis" = Relationship(back_populates="yemekler")
