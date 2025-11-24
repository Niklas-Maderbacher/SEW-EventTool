from sqlalchemy.orm import Session
from datetime import datetime

from app.models.booking import Booking
from app.schemas.booking import BookingBase, BookingCreate, BookingUpdate
from app.schemas.user import UserInDB
from app.models.user_roles import USER_ROLE
from app.crud.exeptions.not_authorised import UserNotAuthorised

def get_bookings(*, db: Session, user: UserInDB):
    if user.role == USER_ROLE.ADMIN:
        return db.query(Booking).all()
    else:
        return db.query(Booking).filter(Booking.user_id == user.id).all()


def get_booking_by_id(*, db: Session, id: int):
    return db.query(Booking).filter(Booking.id == id).first()

def get_booking_by_ticket(*, db: Session, ticket_id: int):
    return db.query(Booking).filter(Booking.ticket_id == ticket_id).all()

def get_booking_by_date(*, db: Session, date: datetime, user: UserInDB):
    if user.role == USER_ROLE.ADMIN:
        return db.query(Booking).filter(Booking.date == date).all()
    else:
        return db.query(Booking).filter(Booking.date == date).filter(Booking.user_id == user.id).all()

def create_booking(*, db: Session, booking: BookingCreate, user: UserInDB):
    booking_db = Booking(
        user_id=user.id,
        ticket_id=booking.ticket_id,
        date=booking.date,
    )

    db.add(booking_db)
    db.commit()
    db.refresh(booking_db)

    return booking_db

def update_booking(*, db: Session, id: int, booking: BookingUpdate, user: UserInDB):
    booking_db = db.query(Booking).filter(Booking.id == id).first()

    if user.id != booking_db.user_id and user.role != USER_ROLE.ADMIN:
        raise UserNotAuthorised()

    booking_db.user_id=booking.user_id
    booking_db.ticket_id=booking.ticket_id
    booking_db.date=booking.date

    db.commit()
    db.refresh(booking_db)

    return booking_db

def delete_booking(*, db: Session, id: int, user: UserInDB):
    booking_db = db.query(Booking).filter(Booking.id == id).first()

    if user.id != booking_db.user_id and user.role != USER_ROLE.ADMIN:
        raise UserNotAuthorised()

    db.query(Booking).filter(Booking.id == id).delete()

    db.commit()
    
    return booking_db