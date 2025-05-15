from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4
from datetime import datetime


class Personel(SQLModel, table=False):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    ad: str
    soyad: str
    pozisyon: str
    telefon: str
    iseGirisTarihi: datetime
