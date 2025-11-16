from sqlalchemy import Column, Integer, String, DateTime, Boolean
from enum import Enum

from app.database.session import Base

class USER_ROLE(Enum):
    ADMIN = "admin"
    ORGANIZER = "organizer"
    VISITOR = "visitor"
