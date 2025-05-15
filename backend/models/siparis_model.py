from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from backend.enums.odeme_durumu_enum import OdemeDurumu
from backend.enums.siparis_durumu_enum import SiparisDurumu
from uuid import UUID
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .garson_model import Garson
    from .masa_model import Masa


class Siparis(SQLModel, table=True):
    siparisID: int | None = Field(default=None, primary_key=True)
    siparisZamani: datetime
    toplamTutar: float
    odemeDurumu: OdemeDurumu
    siparisDurumu: SiparisDurumu

    garson_id: UUID = Field(default=None, foreign_key="garson.id")
    Garson: "Garson" = Relationship(back_populates="siparis")

    masa_id: int | None = Field(default=None, foreign_key="masa.masa_numarasi")
    Masa: "Masa" = Relationship(back_populates="siparis")
