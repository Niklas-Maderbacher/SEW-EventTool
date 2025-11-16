from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy import Enum as SQL_ENUM
from datetime import datetime

from app.database.session import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    date = Column(DateTime, nullable=False)
    description = Column(String(500), nullable=True)
    location_id = Column(Integer, ForeignKey("locations.id", ondelete="SET NULL"))
    organizer_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"))
