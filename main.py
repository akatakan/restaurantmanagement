from sqlmodel import create_engine, Session
from backend.models.garson_model import Garson
from backend.models.masa_model import Masa
from datetime import datetime


def main():
    engine = create_engine("sqlite:///restaurant.db")
    with Session(engine) as session:
        garson = Garson(
            "Atakan",
            "Ak",
            "kıdemli",
            "5442131231",
            datetime.now().strftime("%d/%m/%y"),
        )
        session.add(garson)
        session.commit()

        masa1 = Masa(5, "Bahçe", garson_id=garson.id)
        session.add(masa1)
        session.commit()


if __name__ == "__main__":
    main()
