from sqlalchemy import Column, Integer, String, DateTime, Boolean
from enum import Enum

from app.database.session import Base

class TICKET_STATUS(Enum):
    AVAILABLE = "available"
    SOLD = "seld"
    CANCELLED = "cancelled"
