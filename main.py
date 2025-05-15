from sqlmodel import create_engine, Session, SQLModel, select
from backend.models.garson_model import Garson
from backend.models.masa_model import Masa
from datetime import datetime
from uuid import UUID

from backend.enums.masa_durumu_enum import MasaDurumu
from backend.models.siparis_model import Siparis
from backend.enums.odeme_durumu_enum import OdemeDurumu
from backend.enums.siparis_durumu_enum import SiparisDurumu


engine = create_engine("sqlite:///restaurant.db")


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def main():
    create_db_and_tables()
    with Session(engine) as session:
        garson1 = Garson(
            ad="Mustafa",
            soyad="Kaya",
            pozisyon="Doggy",
            telefon="234523534534",
            iseGirisTarihi=datetime.now(),
        )

        session.add(garson1)
        session.commit()

        masa1 = Masa(kapasite=2, durum=MasaDurumu.BOS, garson_id=garson1.id)

        session.add(masa1)
        session.commit()

        siparis = Siparis(
            siparisZamani=datetime.now(),
            toplamTutar=25.0,
            odemeDurumu=OdemeDurumu.ODENMEDI,
            siparisDurumu=SiparisDurumu.ALINDI,
            garson_id=garson1.id,
            masa_id=masa1.id,
        )

        session.add(siparis)
        session.commit()


if __name__ == "__main__":
    main()
