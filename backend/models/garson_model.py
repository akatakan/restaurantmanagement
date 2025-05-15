from .personel_model import Personel
from .masa_model import Masa
from typing import List
from sqlmodel import Relationship


class Garson(Personel, table=True):
    sorumluMasalar: List["Masa"] = Relationship(back_populates="garson")
