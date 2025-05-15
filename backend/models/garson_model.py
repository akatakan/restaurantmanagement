from .personel_model import Personel
from .masa_model import Masa
from typing import TYPE_CHECKING, List
from sqlmodel import Relationship, Field

if TYPE_CHECKING:
    from .siparis_model import Siparis


class Garson(Personel, table=True):
    sorumluMasalar: List["Masa"] = Relationship(back_populates="garson")

    siparisID: int | None = Field(default=None, foreign_key="siparis.siparisID")
    Siparis: "Siparis" = Relationship(back_populates="garson")
