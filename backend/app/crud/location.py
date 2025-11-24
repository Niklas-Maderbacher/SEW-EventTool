from sqlalchemy.orm import Session
from app.models.location import Location
from app.schemas.location import LocationCreate, LocationBase, LocationUpdate
from app.schemas.user import UserInDB
from app.models.user_roles import USER_ROLE
from app.crud.exeptions.not_authorised import UserNotAuthorised

def get_all_locations(*, db: Session, user: UserInDB):
    return db.query(Location).all()

def get_location_by_id(*, db: Session, id: int):
    return db.query(Location).filter(Location.id == id).first()

def get_location_by_name(*, db: Session, name: str):
    return db.query(Location).filter(Location.name == name).first()

def get_location_by_address(*, db: Session, address: str):
    return db.query(Location).filter(Location.address == address).first()

def get_location_by_capacity(*, db: Session, min: int, max: int):
    return db.query(Location).filter(Location.capacity > min).filter(Location.capacity < max).all()

def create_location(*, db: Session, location: LocationCreate):
    location_db = Location(
        name=location.name,
        address=location.address,
        capacity=location.capacity
    )

    db.add(location_db)
    db.commit()
    db.refresh(location_db)

    return location_db

def update_location(*, db: Session, id: int, location: LocationUpdate):
    location_db = db.query(Location).filter(Location.id == id).first()

    location_db.name = location.name
    location_db.address = location.address
    location_db.capacity = location.capacity

    db.commit()
    db.refresh(location_db)

    return location_db

def delete_location(*, db: Session, id: int):
    location_db = db.query(Location).filter(Location.id == id).first()
    db.query(Location).filter(Location.id == id).delete()

    db.commit()

    return location_db