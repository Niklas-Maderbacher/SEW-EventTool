from sqlalchemy.orm import Session

from app.models.ticket import Ticket
from app.models.ticket_status import TICKET_STATUS
from app.models.event import Event
from app.schemas.ticket import TicketBase, TicketCreate, TicketUpdate

def get_tickets(*, db: Session):
    return db.query(Ticket).all()

def get_ticket_by_id(*, db: Session, id: int):
    return db.query(Ticket).filter(Ticket.id == id).first()

def get_ticket_by_event(*, db: Session, event_id: int):
    return db.query(Ticket).filter(Ticket.event_id == event_id).all()

def get_ticket_by_user(*, db: Session, user_id: int):
    return db.query(Ticket).filter(Ticket.owner == user_id).all()

def create_ticket(*, db: Session, ticket: TicketCreate):
    ticket_db = Ticket(
        owner=ticket.owner,
        seat_number=ticket.seat_number,
        price=ticket.price,
        event_id=ticket.event_id,
        status=ticket.status,
    )

    db.add(ticket_db)
    db.commit()
    db.refresh(ticket_db)

    return ticket_db

def update_ticket(*, db: Session, id: int, ticket: TicketUpdate):
    ticket_db = db.query(Ticket).filter(Ticket.id == id).first()

    ticket_db.owner=ticket.owner
    ticket_db.seat_number=ticket.seat_number
    ticket_db.price=ticket.price
    ticket_db.event_id=ticket.event_id
    ticket_db.status=ticket.status

    db.commit()
    db.refresh(ticket_db)

    return ticket_db

def delete_ticket(*, db: Session, id: int):
    ticket_db = db.query(Ticket).filter(Ticket.id == id).first()
    db.query(Ticket).filter(Ticket.id == id).delete()

    db.commit()

    return ticket_db