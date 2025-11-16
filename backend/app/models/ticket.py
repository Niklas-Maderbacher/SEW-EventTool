from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Float
from sqlalchemy import Enum as SQL_ENUM
from datetime import datetime

from app.database.session import Base
from app.models.ticket_status import TICKET_STATUS

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, autoincrement=True, primary_key=True)
    owner = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    seat_number = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    event_id = Column(Integer, ForeignKey("events.id", ondelete="SET NULL"))
    status = Column(SQL_ENUM(TICKET_STATUS), nullable=False)
