from uuid import UUID
from sqlmodel import SQLModel, Field, Relationship
from .garson_model import Garson


class Masa(SQLModel, table=True):
    masa_numarasi: int | None = Field(default=None, primary_key=True)
    kapasite: int
    konum: str
    garson_id: UUID = Field(default=None, foreign_key="garson.id")
    garson: Garson = Relationship(back_populates="masa")
