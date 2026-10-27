from sqlalchemy.orm import Session

from city import models
from city import schemas


def get_city_list(db: Session, commons: dict):
    return db.query(models.DBCity).limit(commons["limit"]).offset(commons["skip"]).all()


def create_city(db: Session, city: schemas.CityCreate):
    db_city = models.DBCity(**city.model_dump())

    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city


def delete_city(db: Session, city_id: int):
    db_city = db.query(models.DBCity).filter(models.DBCity.id == city_id).first()

    if not db_city:
        return None

    db.delete(db_city)
    db.commit()

    return db_city


def get_city_detail(db: Session, city_id: int):
    return db.query(models.DBCity).filter(models.DBCity.id == city_id).first()
