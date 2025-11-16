from sqlalchemy.orm import Session
from datetime import datetime

from app.models.event import Event
from app.schemas.event import EventBase, EventCreate, EventUpdate


def get_all_events(*, db: Session):
    return db.query(Event).all()

def get_event_by_id(*, db: Session, id: int):
    return db.query(Event).filter(Event.id == id).first()

def get_event_by_name(*, db: Session, name: str):
    return db.query(Event).filter(Event.name == name).first()

def get_event_by_date(*, db: Session, date: datetime):
    return db.query(Event).filter(Event.date == date).first()

def get_event_by_range(*, db: Session, start_date: datetime, end_date: datetime):
    return db.query(Event).filter(Event.date > start_date).filter(Event.date < end_date).all()

def get_event_by_location(*, db: Session, location_id: int):
    return db.query(Event).filter(Event.location_id == location_id).first()

def get_event_by_organizer(*, db: Session, organizer_id: int):
    return db.query(Event).filter(Event.organizer_id == organizer_id).first()

def create_event(*, db: Session, event: EventCreate):
    event_db = Event(
        name=event.name,
        date = event.date,
        description = event.description,
        location_id = event.location_id,
        organizer_id = event.organizer_id
    )

    db.add(event_db)
    db.commit()
    db.refresh(event_db)

    return event_db

def update_event(*, db: Session, id: int, event: EventUpdate):
    event_db = db.query(Event).filter(Event.id == id).first()

    event_db.name = event.name
    event_db.date = event.date
    event_db.description = event.description
    event_db.location_id = event.location_id
    event_db.organizer_id = event.organizer_id

    db.commit()
    db.refresh(event_db)

    return event_db

def delete_event(*, db: Session, id: int):
    event_db = db.query(Event).filter(Event.id == id).first()
    db.query(Event).filter(Event.id == id).delete()

    db.commit()

    return event_db