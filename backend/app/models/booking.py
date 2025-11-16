from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Float
from sqlalchemy import Enum as SQL_ENUM
from datetime import datetime

from app.database.session import Base

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"))
    ticket_id = Column(Integer, ForeignKey("tickets.id", ondelete="SET NULL"))
    date = Column(DateTime, default=datetime.utcnow)
