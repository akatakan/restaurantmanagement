from sqlmodel import SQLModel, Field
from uuid import uuid4
from .personel_model import Personel


class Asci(Personel, table=True):
    uzmanlikAlani: str
