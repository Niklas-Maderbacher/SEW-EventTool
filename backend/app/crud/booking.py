from sqlalchemy.orm import Session
from datetime import datetime

from app.models.booking import Booking
from app.schemas.booking import BookingBase, BookingCreate, BookingUpdate

def get_bookings(*, db: Session):
    return db.query(Booking).all()

def get_booking_by_id(*, db: Session, id: int):
    return db.query(Booking).filter(Booking.id == id).first()

def get_booking_by_user(*, db: Session, user_id: int):
    return db.query(Booking).filter(Booking.user_id == user_id).all()

def get_booking_by_ticket(*, db: Session, ticket_id: int):
    return db.query(Booking).filter(Booking.ticket_id == ticket_id).all()

def get_booking_by_date(*, db: Session, date: datetime):
    return db.query(Booking).filter(Booking.date == date).all()

def create_booking(*, db: Session, booking: BookingCreate):
    booking_db = Booking(
        user_id=booking.user_id,
        ticket_id=booking.ticket_id,
        date=booking.date,
    )

    db.add(booking_db)
    db.commit()
    db.refresh(booking_db)

    return booking_db

def update_booking(*, db: Session, id: int, booking: BookingUpdate):
    booking_db = db.query(Booking).filter(Booking.id == id).first()

    booking_db.user_id=booking.user_id
    booking_db.ticket_id=booking.ticket_id
    booking_db.date=booking.date

    db.commit()
    db.refresh(booking_db)

    return booking_db

def delete_booking(*, db: Session, id: int):
    booking_db = db.query(Booking).filter(Booking.id == id).first()
    db.query(Booking).filter(Booking.id == id).delete()

    db.commit()
    
    return booking_db