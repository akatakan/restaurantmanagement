from sqlmodel import create_engine, Session, SQLModel, select
from backend.models.garson_model import Garson
from backend.models.masa_model import Masa
from datetime import datetime
from uuid import UUID

from backend.enums.masa_durumu_enum import MasaDurumu
from backend.models.siparis_model import Siparis
from backend.models.yemek_model import Yemek
from backend.enums.odeme_durumu_enum import OdemeDurumu
from backend.enums.siparis_durumu_enum import SiparisDurumu


engine = create_engine("sqlite:///restaurant.db")


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

#Kaya are the king
def create_models():
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

        masa1 = Masa(
            kapasite=2, konum="Salon 1", durum=MasaDurumu.BOS, garson_id=garson1.id
        )

        session.add(masa1)
        session.commit()

        siparis = Siparis(
            siparisZamani=datetime.now(),
            toplamTutar=25.0,
            odemeDurumu=OdemeDurumu.ODENMEDI,
            siparisDurumu=SiparisDurumu.ALINDI,
            garson_id=garson1.id,
            masa_id=masa1.masa_numarasi,
        )

        session.add(siparis)
        session.commit()

        yemek1 = Yemek(
            ad="Tantuni",
            aciklama="Et",
            fiyat=200.0,
            hazirlanmaSüresi=5,
        )

        session.add(yemek1)
        session.commit()

        yemek2 = Yemek(
            ad="Tantuni",
            aciklama="Tavuk",
            fiyat=200.0,
            hazirlanmaSüresi=5,
        )

        session.add(yemek2)
        session.commit()

        yemek3 = Yemek(
            ad="Döner",
            aciklama="Et",
            fiyat=5100.0,
            hazirlanmaSüresi=3,
        )

        session.add(yemek3)
        session.commit()

        siparis.yemekler.append(yemek1)
        siparis.yemekler.append(yemek2)
        siparis.yemekler.append(yemek3)
        toplam = 0
        for yemek in siparis.yemekler:
            toplam += yemek.fiyat
        siparis.toplamTutar = toplam

        session.add(siparis)
        session.commit()

        print(siparis.toplamTutar)


def main():
    create_db_and_tables()
    create_models()
    # with Session(engine) as session:
    #     statement = select(Garson).where(
    #         Garson.id == UUID("146300cba4634d73b44ed2453dbe9c10")
    #     )
    #     garson1 = session.exec(statement).first()

    #     statement = select(Siparis).where(Siparis.garson_id == garson1.id)
    #     siparis1 = session.exec(statement).first()
    #     print(siparis1)


if __name__ == "__main__":
    main()
