from sqlalchemy.orm import Session

from app.models.ticket import Ticket
from app.models.ticket_status import TICKET_STATUS
from app.models.event import Event
from app.schemas.ticket import TicketBase, TicketCreate, TicketUpdate
from app.schemas.user import UserInDB
from app.models.user_roles import USER_ROLE
from app.crud.exeptions.not_authorised import UserNotAuthorised

def get_tickets(*, db: Session, user: UserInDB):
    if user.role == USER_ROLE.ADMIN:
        return db.query(Ticket).all()
    else:
        return db.query(Ticket).filter(Ticket.owner == user.id).all()

def get_ticket_by_id(*, db: Session, id: int):
    return db.query(Ticket).filter(Ticket.id == id).first()

def get_ticket_by_event(*, db: Session, event_id: int, user: UserInDB):
    if user.role == USER_ROLE.ADMIN or user.role == USER_ROLE.ORGANIZER:
        return db.query(Ticket).filter(Ticket.event_id == event_id).all()
    else:
        raise UserNotAuthorised()

def get_ticket_by_user(*, db: Session, user_id: int):
    return db.query(Ticket).filter(Ticket.owner == user_id).all()

def create_ticket(*, db: Session, ticket: TicketCreate, user: UserInDB):
    ticket_db = Ticket(
        owner=user.id,
        seat_number=ticket.seat_number,
        price=ticket.price,
        event_id=ticket.event_id,
        status=ticket.status,
    )

    db.add(ticket_db)
    db.commit()
    db.refresh(ticket_db)

    return ticket_db

def update_ticket(*, db: Session, id: int, ticket: TicketUpdate, user: UserInDB):
    ticket_db = db.query(Ticket).filter(Ticket.id == id).first()

    if user.id != ticket_db.owner or user.role != USER_ROLE.ADMIN:
        raise UserNotAuthorised()

    ticket_db.owner=ticket.owner
    ticket_db.seat_number=ticket.seat_number
    ticket_db.price=ticket.price
    ticket_db.event_id=ticket.event_id
    ticket_db.status=ticket.status

    db.commit()
    db.refresh(ticket_db)

    return ticket_db

def delete_ticket(*, db: Session, id: int, user: UserInDB):
    ticket_db = db.query(Ticket).filter(Ticket.id == id).first()

    if user.id != ticket_db.owner or user.role != USER_ROLE.ADMIN:
        raise UserNotAuthorised()

    db.query(Ticket).filter(Ticket.id == id).delete()
    db.commit()

    return ticket_db