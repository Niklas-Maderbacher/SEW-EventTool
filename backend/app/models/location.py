from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy import Enum as SQL_ENUM
from datetime import datetime

from app.database.session import Base

class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    address = Column(String(100), nullable=False)
    capacity = Column(Integer, nullable=False)
